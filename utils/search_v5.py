"""
Masini Barokɛla
V5.0 Search Engine

Stage 1:
    RapidFuzz retrieval against the structured V5.0
    knowledge base.

This is an intermediate step before semantic search.
"""

from rapidfuzz import fuzz

from utils.loader_v5 import load_knowledge_base_v5


# --------------------------------------------------
# Configuration
# --------------------------------------------------

MIN_SCORE = 70


# --------------------------------------------------
# Language mapping
# --------------------------------------------------

LANGUAGE_KEYS = {
    "English": "english",
    "Français": "french",
    "Bambara": "bambara",
}


# --------------------------------------------------
# Search
# --------------------------------------------------

def search_question_v5(user_question, language="English"):
    """
    Search the V5.0 knowledge base using RapidFuzz.

    Args:
        user_question: User's question.
        language: English, Français, or Bambara.

    Returns:
        tuple:
            (best_record, best_score)
    """

    data = load_knowledge_base_v5()

    user_question = user_question.lower().strip()

    if not user_question:
        return None, 0

    # Very short queries are unreliable.
    if len(user_question.split()) < 2:
        return None, 0

    language_key = LANGUAGE_KEYS.get(language)

    if language_key is None:
        language_key = "english"

    best_record = None
    best_score = 0

    for record in data:

        language_data = record.get(language_key, {})

        question = language_data.get("question")

        if not question:
            continue

        question = question.lower().strip()

        # --------------------------------------------------
        # RapidFuzz similarity
        # --------------------------------------------------

        wratio = fuzz.WRatio(
            user_question,
            question,
        )

        # --------------------------------------------------
        # Word overlap
        # --------------------------------------------------

        user_words = set(user_question.split())
        question_words = set(question.split())

        overlap = len(
            user_words & question_words
        )

        score = wratio + (overlap * 5)

        # Never allow score above 100.
        score = min(score, 100)

        if score > best_score:

            best_score = score
            best_record = record

    # --------------------------------------------------
    # Minimum confidence threshold
    # --------------------------------------------------

    if best_score >= MIN_SCORE:
        return best_record, best_score

    return None, best_score