import os
from typing import Any

from langchain_core.output_parsers import JsonOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import (
    RunnableLambda,
    RunnableParallel,
    RunnablePassthrough,
)
from langchain_ollama import ChatOllama

from database import fetch_student_context
from external_api import fetch_external_api_context
from rag import retrieve_rag_context
from schemas import ChatAnswer


parser = JsonOutputParser(pydantic_object=ChatAnswer)

prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            """You are a reliable student-support assistant.

Use the supplied contexts according to these rules:
1. Database context is the source of truth for the identified student's
   enrollment, batch, and payment details.
2. External API context contains live operational information.
3. RAG context contains institutional/course knowledge.
4. Never invent a fee, student record, schedule, policy, or API result.
5. When context is missing or unavailable, clearly say so.
6. Do not reveal information about any student except the requested record.
7. Give a direct, concise but useful answer.

Return valid JSON only.
{format_instructions}
""",
        ),
        (
            "human",
            """Question:
{question}

Database context:
{db_context}

External API context:
{api_context}

RAG context:
{rag_context}
""",
        ),
    ]
).partial(format_instructions=parser.get_format_instructions())


def create_pipeline():
    llm = ChatOllama(
        model=os.getenv("OLLAMA_CHAT_MODEL", "llama3.2"),
        base_url=os.getenv("OLLAMA_BASE_URL", "http://localhost:11434"),
        temperature=0,
        format="json",
    )

    # RunnableParallel runs the independent context-producing branches
    # concurrently. Each branch receives the same request dictionary.
    context_pipeline = RunnableParallel(
        question=RunnableLambda(lambda payload: payload["question"]),
        db_context=RunnableLambda(fetch_student_context),
        api_context=RunnableLambda(fetch_external_api_context),
        rag_context=RunnableLambda(retrieve_rag_context),
    )

    # Final LCEL pipeline:
    # input -> DB/API/RAG context -> prompt -> LLM -> JSON parser
    return context_pipeline | prompt | llm | parser


chat_pipeline = create_pipeline()


def ask_chatbot(payload: dict[str, Any]) -> dict[str, Any]:
    result = chat_pipeline.invoke(payload)
    return ChatAnswer.model_validate(result).model_dump()
