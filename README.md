# Agentic Hello API

First AI agent, served as an inference API.

## What Changed From the Agentic AI Hub - 01 Hello Agent?

| Before (agent.py)           | After (FastAPI API)              |
|-----------------------------|----------------------------------|
| Runs in terminal            | Runs as a web server             |
| One-shot execution          | Stays alive, handles many users  |
| Only you can use it         | Any app can call it via HTTP     |
| No input validation         | Auto-validates with Pydantic     |

## Quick Start

```bash
# 1. Install FastAPI (includes CLI + Uvicorn + everything)
uv add "fastapi[standard]"

# 2. Install OpenAI Agents SDK
uv add openai-agents

# 3. Start the dev server (from project root, NOT inside /app)
fastapi dev app/main.py

# That's it! FastAPI CLI auto-finds main.py and the app object.
# Auto-reload is ON by default in dev mode.
```

Open **http://localhost:8000/docs** - you get a free interactive test UI!

## The Two Commands You Need to Know

| Command        | Mode        | Auto-reload | Listens on             |
|----------------|-------------|-------------|------------------------|
| `fastapi dev`  | Development | Yes         | 127.0.0.1 (local only) |
| `fastapi run`  | Production  | No          | 0.0.0.0 (public)       |

## Test Your API

### Option A: Swagger UI (easiest)
Open `http://localhost:8000/docs` -> click POST `/chat` -> Try it out ->
paste `{"message": "Hi! My name is Ahmad."}` -> Execute

### Option B: cURL
```bash
curl -X POST http://localhost:8000/chat \
  -H "Content-Type: application/json" \
  -d '{"message": "Hi! My name is Ahmad."}'
```

### Option C: Python
```python
import requests

response = requests.post(
    "http://localhost:8000/chat",
    json={"message": "Hi! My name is Ahmad."}
)
print(response.json())
# -> {"reply": "Hello, Ahmad! Welcome to Agentic AI Hub!"}
```

## Project Structure

```
agentic-hello-api/
├── app/
│   ├── __init__.py        # makes it a Python package
│   ├── main.py            # FastAPI app + endpoints
│   ├── agent_setup.py     # agent config + runner helper
│   └── schemas.py         # request/response data shapes
├── shared/                # shared folder
└── requirements.txt
```

## What's Next?

1. Add a `/chat/multi-turn` endpoint with conversation history
2. Add streaming responses (Server-Sent Events)
3. Add API key authentication
4. Deploy with `fastapi run` behind a reverse proxy
