"""Chat-model configuration for the Quantum Experiment Agent."""

import os
from typing import Any

from beeai_framework.backend import ChatModel, ChatModelError
from dotenv import load_dotenv


load_dotenv()


def model_name(agent: str = "EXPERIMENT") -> str:
    configured = os.getenv(f"{agent.upper()}_MODEL")
    if configured:
        return configured
    fallback = os.getenv("WATSONX_EXPERIMENT_MODEL", "mistralai/mistral-small-3-1-24b-instruct-2503")
    return f"watsonx:{fallback}"


def create_chat_model(agent: str = "EXPERIMENT") -> ChatModel:
    return ChatModel.from_name(model_name(agent))


def explain_error(error: Exception) -> str:
    explain = getattr(error, "explain", None)
    return explain() if callable(explain) else str(error)


async def run_agent_with_retries(agent: Any, prompt: str, *, retries: int = 2) -> Any:
    for attempt in range(1, retries + 2):
        try:
            return await agent.run(prompt)
        except ChatModelError:
            if attempt > retries:
                raise
