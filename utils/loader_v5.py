"""
Masini Barokɛla
V5.0 Knowledge Base Loader

Loads the structured V5.0 knowledge base.
"""

import json
from pathlib import Path


# --------------------------------------------------
# Project root
# --------------------------------------------------

PROJECT_ROOT = Path(__file__).resolve().parent.parent


# --------------------------------------------------
# V5.0 knowledge base
# --------------------------------------------------

JSON_FILE = (
    PROJECT_ROOT
    / "data"
    / "knowledge_base_v5.json"
)


def load_knowledge_base_v5():
    """
    Load the V5.0 knowledge base.

    Returns:
        list: Structured V5.0 knowledge records.
    """

    if not JSON_FILE.exists():

        raise FileNotFoundError(
            f"V5.0 knowledge base not found:\n{JSON_FILE}"
        )

    with open(
        JSON_FILE,
        "r",
        encoding="utf-8",
    ) as file:

        knowledge = json.load(file)

    if not isinstance(knowledge, list):

        raise ValueError(
            "V5.0 knowledge base must contain a list of records."
        )

    return knowledge