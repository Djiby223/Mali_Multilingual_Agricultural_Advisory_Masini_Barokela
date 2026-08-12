"""
Masini Barokɛla
V5.1 Search Engine

Stage 2:
    Improved RapidFuzz retrieval against the structured V5.0
    knowledge base.

Improvements over V5.0:
    - Removes common question words from overlap scoring
    - Normalizes simple word variants
    - Combines fuzzy similarity with meaningful-word coverage
    - Prevents generic words such as "what", "when", and "should"
      from dominating the score
"""

import re

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
    "Français": "french",
    "Bambara": "bambara",
    "Bamanankan": "bambara",
}


# --------------------------------------------------
# Common words to ignore during keyword matching
# --------------------------------------------------

STOPWORDS = {
    "english": {
        "what", "when", "where", "why", "how",
        "which", "who", "whom",
        "is", "are", "was", "were",
        "the", "a", "an",
        "to", "of", "for", "in", "on", "at",
        "and", "or",
        "should", "can", "could", "would",
        "do", "does", "did",
        "i", "we", "you", "they", "he", "she",
        "my", "our", "your", "their",
    },

    "french": {
        "quelle", "quelles", "quel", "quels",
        "quand", "où", "ou", "pourquoi", "comment",
        "qui", "que", "quoi",
        "est", "sont", "était", "étaient",
        "le", "la", "les", "un", "une", "des",
        "du", "de", "dans", "sur", "à", "au", "aux",
        "et", "ou",
        "doit", "doivent", "peut", "peuvent",
        "je", "nous", "vous", "ils", "elles",
        "mon", "notre", "votre", "leur",
    },

    "bambara": set(),
}


# --------------------------------------------------
# Text normalization
# --------------------------------------------------

def normalize_text(text):
    """
    Normalize text for comparison.
    """

    text = text.lower().strip()

    # Remove punctuation while preserving letters/numbers.
    text = re.sub(r"[^\w\s]", " ", text)

    # Normalize repeated spaces.
    text = re.sub(r"\s+", " ", text).strip()

    return text


# --------------------------------------------------
# Simple word normalization
# --------------------------------------------------

def normalize_word(word, language_key):
    """
    Normalize simple English/French word variants.

    This is intentionally conservative.
    """

    word = word.lower().strip()

    if language_key == "english":

        # Common English endings.
        replacements = [
            ("ies", "y"),
            ("ing", ""),
            ("ed", ""),
            ("es", ""),
            ("s", ""),
        ]

        for suffix, replacement in replacements:

            if len(word) > len(suffix) + 2 and word.endswith(suffix):

                word = word[:-len(suffix)] + replacement
                break

    elif language_key == "french":

        # Conservative French normalization.
        replacements = [
            ("ées", "ée"),
            ("és", "é"),
            ("es", "e"),
            ("s", ""),
        ]

        for suffix, replacement in replacements:

            if len(word) > len(suffix) + 2 and word.endswith(suffix):

                word = word[:-len(suffix)] + replacement
                break

    return word


# --------------------------------------------------
# Meaningful tokens
# --------------------------------------------------

def meaningful_tokens(text, language_key):
    """
    Return normalized content words while ignoring
    generic question words.
    """

    text = normalize_text(text)

    words = text.split()

    stopwords = STOPWORDS.get(language_key, set())

    tokens = []

    for word in words:

        if word in stopwords:
            continue

        normalized = normalize_word(word, language_key)

        if normalized:
            tokens.append(normalized)

    return set(tokens)


# --------------------------------------------------
# Search
# --------------------------------------------------

def search_question_v5(user_question, language="English"):
    """
    Search the V5.0 knowledge base using improved RapidFuzz retrieval.

    Returns:
        tuple:
            (best_record, best_score)
    """

    data = load_knowledge_base_v5()

    user_question = normalize_text(user_question)

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

    user_tokens = meaningful_tokens(
        user_question,
        language_key,
    )

    for record in data:

        language_data = record.get(language_key, {})

        question = language_data.get("question")

        if not question:
            continue

        question = normalize_text(question)

        # --------------------------------------------------
        # Fuzzy similarity
        # --------------------------------------------------

        wratio = fuzz.WRatio(
            user_question,
            question,
        )

        token_similarity = fuzz.token_set_ratio(
            user_question,
            question,
        )

        # --------------------------------------------------
        # Meaningful-word overlap
        # --------------------------------------------------

        question_tokens = meaningful_tokens(
            question,
            language_key,
        )

        if user_tokens:

            overlap = user_tokens & question_tokens

            coverage = (
                len(overlap) / len(user_tokens)
            ) * 100

        else:

            coverage = 0

        # --------------------------------------------------
        # Combined score
        # --------------------------------------------------

        score = (
            (wratio * 0.45)
            + (token_similarity * 0.25)
            + (coverage * 0.30)
        )

        # Exact meaningful-token match bonus.
        if (
            user_tokens
            and user_tokens == question_tokens
        ):
            score += 5

        # Never allow score above 100.
        score = min(round(score, 1), 100)

        # --------------------------------------------------
        # Best result
        # --------------------------------------------------

        if score > best_score:

            best_score = score
            best_record = record

    # --------------------------------------------------
    # Minimum confidence threshold
    # --------------------------------------------------

    if best_score >= MIN_SCORE:
        return best_record, best_score

    return None, best_score