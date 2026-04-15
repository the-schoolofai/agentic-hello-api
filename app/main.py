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

from fastapi import FastAPI, HTTPException
from .schemas import ChatRequest, ChatResponse
from .agent_setup import run_agent


# --- Create the FastAPI app ---
app = FastAPI(
    title="Hello Agent API",
    description="A beginner-friendly inference API that wraps an AI agent.",
    version="0.1.0",
)


# --- Endpoint 1: Health Check ---
# GET request - just visit http://localhost:8000/ in a browser
@app.get("/")
async def health_check():
    return {"status": "running", "agent": "Hello AI Agent"}


# --- Endpoint 2: Chat with the AI Agent ---
# POST request - send JSON like {"message": "Hi, my name is Ahmad"}
@app.post("/chat", response_model=ChatResponse)
async def chat(request: ChatRequest):
    """
    Send a message to the AI agent and get a reply.

    Example request body:
        {"message": "Hi! My name is Ahmad."}

    Example response:
        {"reply": "Hello, Ahmad! Welcome to Agentic AI Hub!"}
    """
    try:
        response = await run_agent(request.message)
        return ChatResponse(
            reply=response
        )
    except Exception as err:
        raise HTTPException(
            status_code=500, 
            detail=f"Agent error: {str(err)}"
        )
