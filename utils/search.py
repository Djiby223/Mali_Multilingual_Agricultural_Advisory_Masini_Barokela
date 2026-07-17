import json
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
JSON_FILE = PROJECT_ROOT / "data" / "masini_barokela.json"


def load_knowledge_base():
    with open(JSON_FILE, "r", encoding="utf-8") as f:
        return json.load(f)


def search_question(user_question):

    data = load_knowledge_base()

    user_question = user_question.lower()

    for record in data:

        english = record["english"]["question"].lower()

        if user_question in english:
            return record

    return None