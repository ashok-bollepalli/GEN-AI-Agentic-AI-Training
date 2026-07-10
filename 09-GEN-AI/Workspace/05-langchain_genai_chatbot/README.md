# LangChain Multi-Source GenAI Chatbot

## Pipeline

```text
                         +--> SQLite database -------+
User -> FastAPI -> Input +--> External HTTP API ----+--> Prompt -> Ollama LLM
                         +--> FAISS RAG retriever ---+              |
                                                                  v
                                                         JSON output parser
                                                                  |
                                                                  v
                                                        Validated API response
```

## 1. Prerequisites

- Python 3.11 or 3.12
- Ollama installed and running

Pull the models:

```bash
ollama pull llama3.2
ollama pull nomic-embed-text
```

## 2. Create and activate a virtual environment

Windows:

```bash
python -m venv venv
venv\Scripts\activate
```

macOS/Linux:

```bash
python3 -m venv venv
source venv/bin/activate
```

## 3. Install packages

```bash
pip install -r requirements.txt
```

Optional environment variables:

Windows PowerShell:

```powershell
$env:OLLAMA_BASE_URL="http://localhost:11434"
$env:OLLAMA_CHAT_MODEL="llama3.2"
$env:OLLAMA_EMBEDDING_MODEL="nomic-embed-text"
```

macOS/Linux:

```bash
export OLLAMA_BASE_URL=http://localhost:11434
export OLLAMA_CHAT_MODEL=llama3.2
export OLLAMA_EMBEDDING_MODEL=nomic-embed-text
```

## 4. Start the application

```bash
uvicorn main:app --reload --port 8000
```

Open Swagger UI:

```text
http://localhost:8000/docs
```

## 5. Test the chat endpoint

```bash
curl -X POST "http://localhost:8000/chat" \
  -H "Content-Type: application/json" \
  -d "{\"question\":\"I am student 101. What course am I enrolled in, how much fee is due, and what topics are covered?\",\"student_id\":101}"
```

Or run:

```bash
python test_pipeline.py
```

## 6. Add RAG documents

Put `.txt` files inside `knowledge/`, then rebuild the index:

```bash
curl -X POST "http://localhost:8000/admin/rebuild-index"
```

## 7. Replace the demo API

Edit `external_api.py`:

1. Change `API_URL`.
2. Add required authentication headers.
3. Map the real JSON response to a compact text context.
4. Keep timeout and exception handling.

## 8. Replace SQLite with MySQL/PostgreSQL

Keep `fetch_student_context(payload)` as the boundary function. Replace its
SQLite query with SQLAlchemy or your own repository call. The LangChain
pipeline does not need to change as long as the function returns a string.

## Important security notes

- Never let the LLM directly generate and execute unrestricted SQL.
- Authorize the current user before retrieving private database records.
- Store API keys in environment variables or a secret manager.
- Add authentication to `/admin/rebuild-index`.
- Log failures, but do not log private student data or secrets.
