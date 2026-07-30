import json
import os
HISTORY_FILE = "logs/conversations.json"

def save_conversation(chat):

    os.makedirs("logs", exist_ok=True)

    if os.path.exists(HISTORY_FILE):

        with open(HISTORY_FILE, "r", encoding="utf-8") as f:
            history = json.load(f)

    else:

        history = []

    history.append(chat)

    with open(HISTORY_FILE, "w", encoding="utf-8") as f:
        json.dump(history, f, ensure_ascii=False, indent=4)