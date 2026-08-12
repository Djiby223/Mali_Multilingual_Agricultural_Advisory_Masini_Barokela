"""
Masini Barokɛla
V5.2 Intent-Aware Search Engine

Search strategy:

1. Detect domain, sub-intent, and crop.
2. Filter knowledge-base records using intent.
3. Rank remaining candidates with RapidFuzz.
4. Return the best matching record and confidence score.

This module does NOT replace the V4 search engine.
"""

from rapidfuzz import fuzz

from utils.loader_v5 import load_knowledge_base_v5
from utils.intent_v5 import detect_intent_v5


# --------------------------------------------------
# Configuration
# --------------------------------------------------

MIN_SCORE = 70


# --------------------------------------------------
# Language mapping
# --------------------------------------------------

LANGUAGE_KEYS = {
    "English": "english",
    "FranÃ§ais": "french",
    "Bambara": "bambara",
}


# --------------------------------------------------
# Knowledge-base intent mapping
# --------------------------------------------------

CATEGORY_TO_INTENTS = {

    "Planting": {
        "PLANTING_TIME",
        "PLANTING_DEPTH",
        "PLANTING_SPACING",
        "PLANTING_IMPORTANCE",
    },

    "Fertilizer": {
        "FERTILIZER_TIMING",
        "FERTILIZER_TYPE",
        "FERTILIZER_IMPORTANCE",
        "COMPOST",
        "NUTRIENT_DEFICIENCY",
    },

    "Irrigation": {
        "IRRIGATION_FREQUENCY",
        "IRRIGATION_TIMING",
        "WATER_CONSERVATION",
        "WATER_STRESS",
        "EXCESSIVE_IRRIGATION",
    },

    "Pests": {
        "PEST_CONTROL",
        "PEST_SYMPTOMS",
        "PEST_MONITORING",
        "INTEGRATED_PEST_MANAGEMENT",
        "PEST_ROTATION",
    },
}


# --------------------------------------------------
# Find compatible category
# --------------------------------------------------

def get_target_categories(sub_intent):

    categories = []

    for category, intents in CATEGORY_TO_INTENTS.items():

        if sub_intent in intents:
            categories.append(category)

    return categories


# --------------------------------------------------
# Search
# --------------------------------------------------

def search_question_v5_2(user_question, language="English"):

    data = load_knowledge_base_v5()

    user_question = user_question.lower().strip()

    if not user_question:
        return None, 0

    # --------------------------------------------------
    # Very short questions
    # --------------------------------------------------

    if len(user_question.split()) < 2:
        return None, 0

    # --------------------------------------------------
    # Detect intent
    # --------------------------------------------------

    intent = detect_intent_v5(user_question)

    domain = intent["domain"]
    sub_intent = intent["sub_intent"]
    crop = intent["crop"]

    print("V5.2 Intent:", intent)

    # --------------------------------------------------
    # Language
    # --------------------------------------------------

    language_key = LANGUAGE_KEYS.get(language)

    if language_key is None:
        language_key = "english"

    # --------------------------------------------------
    # Determine target categories
    # --------------------------------------------------

    target_categories = get_target_categories(sub_intent)

    # --------------------------------------------------
    # Candidate filtering
    # --------------------------------------------------

    candidates = []

    for record in data:

        category = record.get("category")

        # If we know the correct category, use it.
        if target_categories:

            if category not in target_categories:
                continue

        candidates.append(record)

    # --------------------------------------------------
    # Crop filtering
    #
    # IMPORTANT:
    # The V5 knowledge base does not currently contain
    # a crop field for every record, so crop filtering
    # is based on the question text.
    # --------------------------------------------------

    if crop:

        crop_candidates = []

        crop_terms = {
            "Millet": ["millet"],
            "Maize": ["maize", "corn"],
            "Rice": ["rice"],
            "Sorghum": ["sorghum"],
            "Cotton": ["cotton"],
            "Groundnut": ["groundnut", "peanut"],
            "Cowpea": ["cowpea"],
            "Sesame": ["sesame"],
            "Tomato": ["tomato", "tomatoes"],
        }

        terms = crop_terms.get(crop, [])

        for record in candidates:

            question_data = record.get(language_key, {})
            kb_question = question_data.get("question", "").lower()

            if any(term in kb_question for term in terms):

                crop_candidates.append(record)

        # Only use crop filtering if it found candidates.
        if crop_candidates:
            candidates = crop_candidates

    # --------------------------------------------------
    # If intent filtering produced nothing,
    # fall back to the full knowledge base.
    # --------------------------------------------------

    if not candidates:

        candidates = data

    # --------------------------------------------------
    # RapidFuzz ranking
    # --------------------------------------------------

    best_record = None
    best_score = 0

    for record in candidates:

        question_data = record.get(language_key, {})

        kb_question = question_data.get("question")

        if not kb_question:
            continue

        kb_question = kb_question.lower().strip()

        # ----------------------------------------------
        # Base similarity
        # ----------------------------------------------

        wratio = fuzz.WRatio(
            user_question,
            kb_question,
        )

        # ----------------------------------------------
        # Word overlap
        # ----------------------------------------------

        user_words = set(user_question.split())
        kb_words = set(kb_question.split())

        overlap = len(user_words & kb_words)

        score = wratio + (overlap * 5)

        # ----------------------------------------------
        # Intent-aware bonus
        # ----------------------------------------------

        intent_bonus = 0

        if target_categories:

            if record.get("category") in target_categories:
                intent_bonus += 10

        score += intent_bonus

        # ----------------------------------------------
        # Crop bonus
        # ----------------------------------------------

        if crop:

            crop_terms = {
                "Millet": ["millet"],
                "Maize": ["maize", "corn"],
                "Rice": ["rice"],
                "Sorghum": ["sorghum"],
                "Cotton": ["cotton"],
                "Groundnut": ["groundnut", "peanut"],
                "Cowpea": ["cowpea"],
                "Sesame": ["sesame"],
                "Tomato": ["tomato", "tomatoes"],
            }

            terms = crop_terms.get(crop, [])

            if any(term in kb_question for term in terms):

                score += 10

        # Never exceed 100.

        score = min(score, 100)

        # ----------------------------------------------
        # Keep best result
        # ----------------------------------------------

        if score > best_score:

            best_score = score
            best_record = record

    # --------------------------------------------------
    # Minimum confidence
    # --------------------------------------------------

    if best_score >= MIN_SCORE:

        return best_record, best_score

    return None, best_score