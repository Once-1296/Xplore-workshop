"""Terminal chatbot exercise.

This module provides a small CLI chatbot skeleton. It is intentionally
network-free by default. If students want to connect a real API, they can
export an environment variable `CHATBOT_API_KEY` and implement the
`call_external_api` function.

Files and assets: none required. The module supports a simulated reply
mode when no API key is present.
"""

import os
import sys
from typing import Optional


def call_external_api(api_key: str, prompt: str) -> str:
    """Placeholder for calling a real LLM API.

    Students: implement API call here (requests/httpx or official SDK).
    Keep this function separate so tests can monkeypatch it.
    """
    raise NotImplementedError("Implement call_external_api if you want to call a real service")


class Chatbot:
    def __init__(self, api_key: Optional[str] = None):
        self.api_key = api_key or os.environ.get("CHATBOT_API_KEY")

    def reply(self, prompt: str) -> str:
        """Return a reply for the given prompt.

        If no API key is configured, return a deterministic simulated reply
        so students can still run and test the CLI.
        """
        if self.api_key:
            return call_external_api(self.api_key, prompt)
        # simple simulated reply: echo and add guidance
        return f"[simulated reply] You said: {prompt}"


def run_cli():
    print("Starting terminal chatbot (type 'quit' to exit)")
    bot = Chatbot()
    try:
        while True:
            prompt = input("You: ")
            if prompt.strip().lower() in ("quit", "exit"):
                print("Goodbye!")
                break
            print("Bot:", bot.reply(prompt))
    except (KeyboardInterrupt, EOFError):
        print("\nExiting.")


if __name__ == "__main__":
    run_cli()