"""
schemas.py - Define what data goes IN and OUT of our API.

Pydantic models validate incoming data automatically.
If someone sends bad data, FastAPI returns a clear error.
"""

from pydantic import BaseModel


# What the client sends TO our API
class ChatIn(BaseModel):
    message: str            # The user's message, e.g. "Hi, my name is Rizwan"


# What our API sends BACK
class ChatOut(BaseModel):
    reply: str              # The agent's response
    conversation_id: int
