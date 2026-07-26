"""
Masini Barokɛla
Multilingual Search Engine
"""

from utils.loader import load_knowledge_base


def normalize(text):
    """
    Convert text into a set of lowercase words.
    """

    words = text.lower().replace("?", "").replace(",", "").split()

    return set(words)


def search_question(user_question, language):

    data = load_knowledge_base()

    user_words = normalize(user_question)

    best_match = None
    highest_score = 0

    for record in data:

        if language == "English":
            question = record["english"]["question"]

        elif language == "Français":
            question = record["french"]["question"]

        else:
            question = record["bambara"]["question"]

        question_words = normalize(question)

        score = len(user_words & question_words)

        if score > highest_score:

            highest_score = score
            best_match = record

    if highest_score >= 2:
        return best_match

    return None