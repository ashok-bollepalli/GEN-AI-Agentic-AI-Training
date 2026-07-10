import os
from contextlib import asynccontextmanager

from fastapi import FastAPI, HTTPException

from database import initialize_database
from pipeline import ask_chatbot
from rag import build_or_load_vector_store, rebuild_vector_store
from schemas import ChatAnswer, ChatRequest, HealthResponse


@asynccontextmanager
async def lifespan(_: FastAPI):
    initialize_database()
    # Build/load once at startup so the first chat request is faster.
    build_or_load_vector_store()
    yield


app = FastAPI(
    title="LangChain Multi-Source GenAI Chatbot",
    version="1.0.0",
    description="Pipeline: DB + API + RAG -> Prompt -> LLM -> Parser",
    lifespan=lifespan,
)


@app.get("/health", response_model=HealthResponse)
def health() -> HealthResponse:
    return HealthResponse(
        status="UP",
        llm_model=os.getenv("OLLAMA_CHAT_MODEL", "llama3.2"),
        embedding_model=os.getenv(
            "OLLAMA_EMBEDDING_MODEL", "nomic-embed-text"
        ),
    )


@app.post("/chat", response_model=ChatAnswer)
def chat(request: ChatRequest) -> ChatAnswer:
    try:
        result = ask_chatbot(request.model_dump())
        return ChatAnswer.model_validate(result)
    except Exception as exc:
        raise HTTPException(
            status_code=500,
            detail=f"Chat pipeline failed: {type(exc).__name__}: {exc}",
        ) from exc


@app.post("/admin/rebuild-index")
def rebuild_index() -> dict[str, int | str]:
    try:
        chunk_count = rebuild_vector_store()
        return {
            "message": "FAISS index rebuilt successfully",
            "indexed_vectors": chunk_count,
        }
    except Exception as exc:
        raise HTTPException(
            status_code=500,
            detail=f"Index rebuild failed: {type(exc).__name__}: {exc}",
        ) from exc
