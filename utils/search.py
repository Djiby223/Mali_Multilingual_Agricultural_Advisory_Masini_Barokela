"""
Masini Barokɛla
Multilingual Search Engine
Version 4.1
"""

from rapidfuzz import fuzz

from utils.loader import load_knowledge_base


MIN_SCORE = 70


def search_question(user_question, language):

    data = load_knowledge_base()

    user_question = user_question.lower().strip()

    best_record = None
    best_score = 0

    for record in data:

        if language == "English":
            question = record["english"]["question"]

        elif language == "Français":
            question = record["french"]["question"]

        else:
            question = record["bambara"]["question"]

        score = fuzz.WRatio(
            user_question,
            question.lower()
        )

        if score > best_score:
            best_score = score
            best_record = record

    if best_score >= MIN_SCORE:
        return best_record, best_score

    return None, best_score