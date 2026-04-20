"""
agent_setup.py - AI Agent configuration (separated from API code).

The API layer imports from here — clean separation of concerns.
"""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from agents import Agent, Runner, function_tool

# -----------------------------------------------------------------
# If you're using Ollama locally, keep this import.
# If you want to use OpenAI / Anthropic, swap the model line below.
# -----------------------------------------------------------------
from shared.models.ollama_provider import get_model


# --- Tools ---
@function_tool
def greet(name: str) -> str:
    """Greet a person by name."""
    return f"Hello, {name}! Welcome to Agentic AI Hub!"


# --- Agent ---
agent = Agent(
    name="Hello Agent",
    instructions=(
        "You are a friendly greeter. "
        "Use the greet tool when someone tells you their name. "
        "Be warm and concise."
    ),
    model=get_model(),
    tools=[greet],
)


# --- Helper function the API will call ---
async def run_agent(history: list[dict], new_message: str) -> str:
    """
    This is the one function FastAPI API endpoint needs.
    """
    input_list = history + [{"role": "user", "content": new_message}]
    result = await Runner.run(agent, input_list)
    
    return result.final_output
