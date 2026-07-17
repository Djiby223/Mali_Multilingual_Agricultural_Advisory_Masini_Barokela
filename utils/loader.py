"""
Masini Barokɛla
Knowledge Base Loader

Loads the JSON knowledge base for the chatbot.
"""

import json
from pathlib import Path

# Project root directory
PROJECT_ROOT = Path(__file__).resolve().parent.parent

# JSON knowledge base
JSON_FILE = PROJECT_ROOT / "data" / "masini_barokela.json"


def load_knowledge_base():
    """
    Load the chatbot knowledge base from JSON.

    Returns:
        list: List of knowledge records.
    """

    if not JSON_FILE.exists():
        raise FileNotFoundError(
            f"Knowledge base not found:\n{JSON_FILE}"
        )

    with open(JSON_FILE, "r", encoding="utf-8") as file:
        knowledge = json.load(file)

    return knowledge