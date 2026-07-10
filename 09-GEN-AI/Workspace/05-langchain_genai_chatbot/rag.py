import os
from pathlib import Path
from typing import Any

from langchain_community.document_loaders import DirectoryLoader, TextLoader
from langchain_community.vectorstores import FAISS
from langchain_ollama import OllamaEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter

BASE_DIR = Path(__file__).parent
KNOWLEDGE_DIR = BASE_DIR / "knowledge"
INDEX_DIR = BASE_DIR / "data" / "faiss_index"

_embeddings: OllamaEmbeddings | None = None
_vector_store: FAISS | None = None


def get_embeddings() -> OllamaEmbeddings:
    global _embeddings
    if _embeddings is None:
        _embeddings = OllamaEmbeddings(
            model=os.getenv("OLLAMA_EMBEDDING_MODEL", "nomic-embed-text"),
            base_url=os.getenv("OLLAMA_BASE_URL", "http://localhost:11434"),
        )
    return _embeddings


def build_or_load_vector_store() -> FAISS:
    global _vector_store
    if _vector_store is not None:
        return _vector_store

    embeddings = get_embeddings()

    if INDEX_DIR.exists():
        _vector_store = FAISS.load_local(
            str(INDEX_DIR),
            embeddings,
            allow_dangerous_deserialization=True,
        )
        return _vector_store

    loader = DirectoryLoader(
        str(KNOWLEDGE_DIR),
        glob="**/*.txt",
        loader_cls=TextLoader,
        loader_kwargs={"encoding": "utf-8"},
    )
    documents = loader.load()
    if not documents:
        raise RuntimeError(f"No knowledge files found in {KNOWLEDGE_DIR}")

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=80,
    )
    chunks = splitter.split_documents(documents)

    _vector_store = FAISS.from_documents(chunks, embeddings)
    INDEX_DIR.parent.mkdir(parents=True, exist_ok=True)
    _vector_store.save_local(str(INDEX_DIR))
    return _vector_store


def rebuild_vector_store() -> int:
    global _vector_store
    import shutil

    if INDEX_DIR.exists():
        shutil.rmtree(INDEX_DIR)
    _vector_store = None
    store = build_or_load_vector_store()
    return store.index.ntotal


def retrieve_rag_context(payload: dict[str, Any]) -> str:
    question = str(payload.get("question", "")).strip()
    if not question:
        return "No question was supplied for knowledge-base retrieval."

    store = build_or_load_vector_store()
    documents = store.similarity_search(question, k=3)

    if not documents:
        return "No relevant knowledge-base documents were found."

    return "\n\n".join(
        f"[Knowledge chunk {number}]\n{doc.page_content}"
        for number, doc in enumerate(documents, start=1)
    )
