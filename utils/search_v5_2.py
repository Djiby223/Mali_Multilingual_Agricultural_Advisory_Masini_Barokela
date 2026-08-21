"""
Masini Barokɛla
V5.2 Controlled Search Engine

Pipeline:

    User Question
        ↓
    Intent Detection
        ↓
    Domain / Crop Filtering
        ↓
    RapidFuzz Similarity
        ↓
    Confidence Check
        ↓
    Record OR None

This module does not modify the V5.1 search engine.
"""

import re

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
    "Français": "french",
    "FranÃ§ais": "french",
    "Bambara": "bambara",
    "Bamanankan": "bambara",
}


# --------------------------------------------------
# Intent → Knowledge Base category
# --------------------------------------------------

INTENT_TO_CATEGORY = {

    # Planting
    "PLANTING_TIME": "Planting",
    "PLANTING_DEPTH": "Planting",
    "PLANTING_SPACING": "Planting",
    "PLANTING_IMPORTANCE": "Planting",

    # Irrigation
    "WATER_CONSERVATION": "Irrigation",
    "IRRIGATION_FREQUENCY": "Irrigation",
    "IRRIGATION_TIMING": "Irrigation",
    "WATER_STRESS": "Irrigation",
    "EXCESSIVE_IRRIGATION": "Irrigation",

    # Fertilization
    "FERTILIZER_TIMING": "Fertilizer",
    "FERTILIZER_TYPE": "Fertilizer",
    "FERTILIZER_IMPORTANCE": "Fertilizer",
    "COMPOST": "Fertilizer",
    "NUTRIENT_DEFICIENCY": "Fertilizer",

    # Pests
    "INTEGRATED_PEST_MANAGEMENT": "Pests",
    "PEST_CONTROL": "Pests",
    "PEST_SYMPTOMS": "Pests",
    "PEST_MONITORING": "Pests",
    "PEST_ROTATION": "Pests",

    # Diseases
    "DISEASE_PREVENTION": "Diseases",
    "DISEASE_SYMPTOMS": "Diseases",

    # Soil
    "SOIL_MANAGEMENT": "Soil Management",

    # Harvest
    "HARVEST": "Harvest",

    # Storage
    "STORAGE": "Storage",

    # Seeds
    "SEED_SELECTION": "Seed Selection",

    # Land preparation
    "LAND_PREPARATION": "Land Preparation",

    # Weeds
    "WEED_MANAGEMENT": "Weed Management",

    # Climate-smart agriculture
    "CLIMATE_SMART_AGRICULTURE": "Climate-Smart Agriculture",

    # Sustainable agriculture
    "SUSTAINABLE_AGRICULTURE": "Sustainable Agriculture",

    # Post-harvest
    "POST_HARVEST_HANDLING": "Post-Harvest Handling",

    # Livestock
    "LIVESTOCK_INTEGRATION": "Livestock Integration",

    # Agricultural extension
    "AGRICULTURAL_EXTENSION": "Agricultural Extension",

    # Soil conservation
    "SOIL_CONSERVATION": "Soil and Water Conservation",

    # Pest and disease diagnosis
    "PEST_DISEASE_DIAGNOSIS": "Pest and Disease Diagnosis",
}
# --------------------------------------------------
# Intent cues for candidate-question alignment
# --------------------------------------------------

INTENT_CUES = {

    "PLANTING_TIME": {
        "when",
        "time",
        "season",
        "start",
        "begin",
        "beginning",
        "planting time",
    },

    "PLANTING_DEPTH": {
        "deep",
        "depth",
        "centimeter",
        "centimeters",
        "cm",
    },

    "PLANTING_SPACING": {
        "spacing",
        "apart",
        "distance",
        "between",
        "rows",
    },

}

# --------------------------------------------------
# Stopwords
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

    text = text.lower().strip()

    text = re.sub(r"[^\w\s]", " ", text)

    text = re.sub(r"\s+", " ", text).strip()

    return text


# --------------------------------------------------
# Word normalization
# --------------------------------------------------

def normalize_word(word, language_key):

    word = word.lower().strip()

    if language_key == "english":

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

    text = normalize_text(text)

    words = text.split()

    stopwords = STOPWORDS.get(language_key, set())

    tokens = []

    for word in words:

        if word in stopwords:
            continue

        normalized = normalize_word(
            word,
            language_key,
        )

        if normalized:
            tokens.append(normalized)

    return set(tokens)


# --------------------------------------------------
# Candidate filtering
# --------------------------------------------------

def filter_candidates(records, category, crop):

    candidates = records

    # --------------------------------------------------
    # Category filtering
    # --------------------------------------------------

    if category:

        category_matches = [
            record
            for record in candidates
            if record.get("category") == category
        ]

        if category_matches:
            candidates = category_matches

    # --------------------------------------------------
    # Crop filtering
    # --------------------------------------------------
    # If a specific crop is detected, keep both:
    #   1. records specifically for that crop
    #   2. General records that may apply across crops
    #
    # This prevents relevant General records from being
    # eliminated before similarity scoring.
    # --------------------------------------------------

    if crop:

        crop_matches = [
            record
            for record in candidates
            if record.get("crop") in (crop, "General")
        ]

        if crop_matches:
            candidates = crop_matches

    return candidates


# --------------------------------------------------
# Candidate intent detection
# --------------------------------------------------

def detect_candidate_intent(question):

    if not question:
        return None

    intent_result = detect_intent_v5(
        question
    )

    return intent_result.get(
        "sub_intent"
    )

# --------------------------------------------------
# Search
# --------------------------------------------------

def search_question_v5_2(
    user_question,
    language="English",
):

    data = load_knowledge_base_v5()

    if not user_question or not user_question.strip():

        return None, 0

    # --------------------------------------------------
    # Detect intent
    # --------------------------------------------------

    intent_result = detect_intent_v5(
        user_question
    )

    domain = intent_result["domain"]

    sub_intent = intent_result["sub_intent"]

    crop = intent_result["crop"]

    # --------------------------------------------------
    # Determine KB category
    # --------------------------------------------------

    category = INTENT_TO_CATEGORY.get(
        sub_intent
    )

    # --------------------------------------------------
    # Filter candidates
    # --------------------------------------------------

    candidates = filter_candidates(
        data,
        category,
        crop,
    )

    # --------------------------------------------------
    # Language
    # --------------------------------------------------

    language_key = LANGUAGE_KEYS.get(
        language,
        "english",
    )

    # --------------------------------------------------
    # Normalize query
    # --------------------------------------------------

    user_question_normalized = normalize_text(
        user_question
    )

    if len(user_question_normalized.split()) < 2:

        return None, 0

    user_tokens = meaningful_tokens(
        user_question_normalized,
        language_key,
    )

    # --------------------------------------------------
    # Score candidates
    # --------------------------------------------------

    best_record = None

    best_score = 0

    for record in candidates:

        language_data = record.get(
            language_key,
            {},
        )

        question = language_data.get(
            "question"
        )

        if not question:
            continue

        question_normalized = normalize_text(
            question
        )

        # Fuzzy similarity
        wratio = fuzz.WRatio(
            user_question_normalized,
            question_normalized,
        )

        token_similarity = fuzz.token_set_ratio(
            user_question_normalized,
            question_normalized,
        )

        # Meaningful-word coverage
        question_tokens = meaningful_tokens(
            question_normalized,
            language_key,
        )

        if user_tokens:

            overlap = (
                user_tokens
                & question_tokens
            )

            coverage = (
                len(overlap)
                / len(user_tokens)
            ) * 100

        else:

            coverage = 0

        # Combined score
        score = (
            (wratio * 0.45)
            + (token_similarity * 0.25)
            + (coverage * 0.30)
        )
                # --------------------------------------------------
        # Intent alignment
        # --------------------------------------------------

        candidate_intent = detect_candidate_intent(
            question
        )

        # For a specific detected intent, reject candidates
        # belonging to a different intent.
        #
        # GENERAL is treated as a fallback because it does not
        # identify a specific agricultural task.

        if (
            sub_intent
            and sub_intent != "GENERAL"
            and candidate_intent
            and candidate_intent != sub_intent
        ):
            continue

        # Reward candidates matching the detected intent.

        if (
            sub_intent
            and sub_intent != "GENERAL"
            and candidate_intent == sub_intent
        ):
            score += 10

        # Exact meaningful-token bonus

        if (
            user_tokens
            and user_tokens == question_tokens
        ):

            score += 20

        score = min(
            round(score, 1),
            100,
        )

        if score > best_score:

            best_score = score

            best_record = record

        # --------------------------------------------------
        # Confidence check
        # --------------------------------------------------

        if sub_intent == "GENERAL":

            # General queries require stronger textual similarity
            # because no specific intent/category filter was available.
            if best_score >= 85:

                return best_record, best_score

            else:

                return None, best_score

        else:

            if best_score >= MIN_SCORE:

                return best_record, best_score

            else:

                return None, best_score