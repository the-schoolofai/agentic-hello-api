"""
main.py - Inference API for AI Agent

Run with FastAPI CLI:
    Development:  fastapi dev
    Production:   fastapi run

Then open:
    http://localhost:8000/docs   <-- interactive Swagger UI to test!
    http://localhost:8000/       <-- health check

Note: FastAPI CLI auto-detects this file (main.py) and the `app` object.
      No need to specify "main:app" - it just works!
"""

from contextlib import asynccontextmanager
from fastapi import FastAPI, HTTPException

from .schemas import ChatIn, ChatOut
from .agent_setup import run_agent
from .db import init_db, SessionDep, Conversation, Message


# --- App ---
@asynccontextmanager
async def lifespan(app: FastAPI):
    init_db()
    yield

app = FastAPI(
    title="Hello Agent API",
    description="A beginner-friendly inference API that wraps an AI agent.",
    version="0.1.0",
    lifespan=lifespan
)


# --- Endpoint 1: Health Check ---
# GET request - just visit http://localhost:8000/ in a browser
@app.get("/")
async def health_check():
    return {"status": "running", "agent": "Hello AI Agent"}


# --- Endpoint 2: ... ---
@app.post("/conversations", response_model=dict)
def create_convo(session: SessionDep):
    """Create a new conversation."""
    c = Conversation()
    session.add(c)
    session.commit()
    session.refresh(c)
    return {"id": c.id, "title": c.title}


# --- Endpoint 3: ... ---
@app.post("/conversations/{cid}/chat", response_model=ChatOut)
async def chat(cid: int, body: ChatIn, session: SessionDep):
    """Send a message, agent replies, both saved."""
    c = session.get(Conversation, cid)
    if not c:
        raise HTTPException(404, "Not found")
 
    # Build history from DB
    history = [{"role": msg.role, "content": msg.content} for msg in c.messages]

    # Run agent
    response = await run_agent(history, body.message)
 
    # Save both messages
    session.add(Message(conversation_id=cid, role="user", content=body.message))
    session.add(Message(conversation_id=cid, role="assistant", content=response))
 
    # # Auto-title from first message
    # if c.title == "New chat":
    #     c.title = body.message[:50]
    # session.add(c)

    session.commit()
 
    return ChatOut(reply=response, conversation_id=cid)




# # --- Endpoint 3: Chat with the AI Agent ---
# # POST request - send JSON like {"message": "Hi, my name is Ahmad"}
# @app.post("/chat", response_model=ChatIn)
# async def chat(request: ChatOut):
#     """
#     Send a message to the AI agent and get a reply.

#     Example request body:
#         {"message": "Hi! My name is Ahmad."}

#     Example response:
#         {"reply": "Hello, Ahmad! Welcome to Agentic AI Hub!"}
#     """
#     try:
#         response = await run_agent(request.message)
#         return ChatOut(
#             reply=response
#         )
#     except Exception as err:
#         raise HTTPException(
#             status_code=500, 
#             detail=f"Agent error: {str(err)}"
#         )
