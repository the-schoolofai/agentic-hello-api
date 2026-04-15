"""
schemas.py - Define what data goes IN and OUT of our API.

Pydantic models validate incoming data automatically.
If someone sends bad data, FastAPI returns a clear error.
"""

from pydantic import BaseModel


# What the client sends TO our API
class ChatRequest(BaseModel):
    message: str    # The user's message, e.g. "Hi, my name is Ahmad"


# What our API sends BACK
class ChatResponse(BaseModel):
    reply: str      # The agent's response
