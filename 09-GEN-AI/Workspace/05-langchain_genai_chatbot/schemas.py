from typing import Literal
from pydantic import BaseModel, Field


class ChatRequest(BaseModel):
    question: str = Field(min_length=2, max_length=2000)
    student_id: int | None = Field(
        default=None,
        description="Optional student ID used to retrieve one student record.",
    )


class ChatAnswer(BaseModel):
    answer: str = Field(description="Clear final answer to the user")
    sources_used: list[
        Literal["database", "external_api", "rag", "general_reasoning"]
    ] = Field(description="Sources actually used in the answer")
    confidence: Literal["high", "medium", "low"]
    follow_up_question: str | None = None


class HealthResponse(BaseModel):
    status: str
    llm_model: str
    embedding_model: str
