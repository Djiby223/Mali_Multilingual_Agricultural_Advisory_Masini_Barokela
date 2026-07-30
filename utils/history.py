import json
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent

LOGS_DIR = PROJECT_ROOT / "logs"

HISTORY_FILE = LOGS_DIR / "conversations.json"


def save_conversation(chat):

    LOGS_DIR.mkdir(exist_ok=True)

    history = []

    if HISTORY_FILE.exists():

        with open(HISTORY_FILE, "r", encoding="utf-8") as f:
            history = json.load(f)

    history.append(chat)

    with open(HISTORY_FILE, "w", encoding="utf-8") as f:
        json.dump(
            history,
            f,
            indent=4,
            ensure_ascii=False
        )