"""
Masini Barokɛla
V5.2 Intent-Aware Search Engine

Architecture:

    Intent first
        ↓
    Crop second
        ↓
    Similarity third

The search engine first identifies the user's intent and crop.
Only records matching BOTH are allowed to compete.

If no knowledge-base record exists for the requested
intent + crop combination, the engine returns None.

This prevents semantically different questions from
competing with each other.
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
    "Français": "french",
    "Bambara": "bambara",
    "Bamanankan": "bambara",
}


# --------------------------------------------------
# Knowledge-base record → sub-intent
# --------------------------------------------------

RECORD_INTENTS = {

    # Planting
    1: "PLANTING_TIME",
    2: "PLANTING_TIME",
    3: "PLANTING_DEPTH",
    4: "PLANTING_SPACING",
    5: "PLANTING_IMPORTANCE",

    # Irrigation
    6: "IRRIGATION_FREQUENCY",
    7: "IRRIGATION_TIMING",
    8: "WATER_CONSERVATION",
    9: "WATER_STRESS",
    10: "EXCESSIVE_IRRIGATION",

    # Fertilizer
    11: "FERTILIZER_TYPE",
    12: "FERTILIZER_IMPORTANCE",
    13: "FERTILIZER_TIMING",
    14: "COMPOST",
    15: "NUTRIENT_DEFICIENCY",

    # Pests
    16: "PEST_CONTROL",
    17: "PEST_SYMPTOMS",
    18: "PEST_MONITORING",
    19: "INTEGRATED_PEST_MANAGEMENT",
    20: "PEST_ROTATION",

    # Diseases
    21: "DISEASE_PREVENTION",
    22: "DISEASE_REMOVAL",
    23: "FUNGAL_DISEASES",
    24: "SEED_TREATMENT",
    25: "CROP_SANITATION",

    # Weather
    26: "RAINFALL_EFFECT",
    27: "WEATHER_FORECAST",
    28: "HEAVY_RAINFALL",
    29: "STRONG_WINDS",
    30: "RAINFALL_ANOMALY",

    # Drought
    31: "DROUGHT_DEFINITION",
    32: "DROUGHT_SIGNS",
    33: "DROUGHT_MANAGEMENT",
    34: "DROUGHT_TOLERANT_CROPS",
    35: "DROUGHT_MULCHING",

    # Soil Management
    36: "SOIL_FERTILITY",
    37: "SOIL_EROSION",
    38: "CROP_ROTATION",
    39: "CROP_ROTATION_BENEFITS",
    40: "MULCHING",

    # Harvest
    41: "HARVEST_READINESS",
    42: "HARVEST_TIMING",
    43: "EARLY_HARVEST",
    44: "LATE_HARVEST",
    45: "HARVEST_HANDLING",

    # Storage
    46: "STORAGE_IMPORTANCE",
    47: "GRAIN_DRYING",
    48: "STORAGE_PESTS",
    49: "STORAGE_PEST_CONTROL",
    50: "STORAGE_CLEANLINESS",

    # Seed Selection
    51: "CERTIFIED_SEEDS",
    52: "SEED_SELECTION",
    53: "SEED_GERMINATION",
    54: "GERMINATION_TEST",
    55: "DAMAGED_SEEDS",

    # Land Preparation
    56: "LAND_PREPARATION_IMPORTANCE",
    57: "LAND_PREPARATION_TIMING",
    58: "LAND_PREPARATION_METHODS",
    59: "MINIMUM_TILLAGE",
    60: "LAND_PREPARATION_EROSION",

    # Weed Management
    61: "WEED_IMPORTANCE",
    62: "WEED_CONTROL",
    63: "WEED_TIMING",
    64: "MULCHING_WEEDS",
    65: "HERBICIDE_USE",

    # Climate-Smart Agriculture
    66: "CLIMATE_SMART_AGRICULTURE",
    67: "CLIMATE_SMART_PRACTICES",
    68: "AGROFORESTRY",
    69: "WATER_HARVESTING",
    70: "CROP_DIVERSIFICATION",

    # Sustainable Agriculture
    71: "SUSTAINABLE_AGRICULTURE",
    72: "AGRICULTURAL_BIODIVERSITY",
    73: "SOIL_ORGANIC_MATTER",
    74: "CROP_RESIDUES",
    75: "CHEMICAL_INPUT_REDUCTION",

    # Post-Harvest Handling
    76: "POST_HARVEST_HANDLING",
    77: "PRODUCE_SORTING",
    78: "SUNLIGHT_PROTECTION",
    79: "POST_HARVEST_LOSSES",
    80: "PACKAGING",

    # Livestock Integration
    81: "LIVESTOCK_CROP_INTEGRATION",
    82: "ANIMAL_MANURE",
    83: "LIVESTOCK_WATER",
    84: "CROP_RESIDUES_LIVESTOCK",
    85: "LIVESTOCK_VACCINATION",

    # Agricultural Extension
    86: "AGRICULTURAL_EXTENSION",
    87: "EXTENSION_AGENTS",
    88: "AGRICULTURAL_INFORMATION",
    89: "FARMER_ORGANIZATIONS",
    90: "FARMER_TRAINING",

    # Soil and Water Conservation
    91: "SOIL_CONSERVATION",
    92: "WATER_CONSERVATION",
    93: "CONTOUR_RIDGES",
    94: "FARM_TREES",
    95: "COVER_CROPS",

    # Pest and Disease Diagnosis
    96: "DISEASE_IDENTIFICATION",
    97: "EARLY_DISEASE_DETECTION",
    98: "UNUSUAL_CROP_SYMPTOMS",
    99: "MOBILE_DIAGNOSIS",
    100: "FARM_RECORDS",
}


# --------------------------------------------------
# Crop terms
# --------------------------------------------------

CROP_TERMS = {

    "Millet": [
        "millet"
    ],

    "Maize": [
        "maize",
        "corn"
    ],

    "Rice": [
        "rice"
    ],

    "Sorghum": [
        "sorghum"
    ],

    "Cotton": [
        "cotton"
    ],

    "Groundnut": [
        "groundnut",
        "peanut"
    ],

    "Cowpea": [
        "cowpea"
    ],

    "Sesame": [
        "sesame"
    ],

    "Tomato": [
        "tomato",
        "tomatoes"
    ],
}


# --------------------------------------------------
# Detect crop in a knowledge-base question
# --------------------------------------------------

def question_contains_crop(question, crop):

    if not crop:
        return True

    terms = CROP_TERMS.get(crop, [])

    question = question.lower()

    return any(
        term in question
        for term in terms
    )


# --------------------------------------------------
# Search
# --------------------------------------------------

def search_question_v5_2(
    user_question,
    language="English"
):

    data = load_knowledge_base_v5()

    user_question = user_question.lower().strip()

    if not user_question:
        return None, 0

    if len(user_question.split()) < 2:
        return None, 0

    # --------------------------------------------------
    # STEP 1 — INTENT
    # --------------------------------------------------

    intent = detect_intent_v5(user_question)

    domain = intent.get("domain")
    sub_intent = intent.get("sub_intent")
    crop = intent.get("crop")

    print("V5.2 Intent:", intent)

    # --------------------------------------------------
    # Language
    # --------------------------------------------------

    language_key = LANGUAGE_KEYS.get(language, "english")

    # --------------------------------------------------
    # STEP 2 — FILTER BY INTENT
    # --------------------------------------------------

    intent_candidates = []

    for record in data:

        record_id = record.get("id")

        record_intent = RECORD_INTENTS.get(record_id)

        if record_intent == sub_intent:

            intent_candidates.append(record)

    print(
        "Intent candidates:",
        [r.get("id") for r in intent_candidates]
    )

    # --------------------------------------------------
    # No records for this intent
    # --------------------------------------------------

    if not intent_candidates:

        print("No records found for intent:", sub_intent)

        return None, 0

    # --------------------------------------------------
    # STEP 3 — FILTER BY CROP
    # --------------------------------------------------

    if crop:

        crop_candidates = []

        for record in intent_candidates:

            question_data = record.get(
                language_key,
                {}
            )

            kb_question = question_data.get(
                "question",
                ""
            )

            if question_contains_crop(
                kb_question,
                crop
            ):

                crop_candidates.append(record)

    else:

        crop_candidates = intent_candidates

    print(
        "Crop candidates:",
        [r.get("id") for r in crop_candidates]
    )

    # --------------------------------------------------
    # CRITICAL V5.2 RULE
    #
    # If the user explicitly identifies a crop but
    # the KB contains no record for that crop + intent,
    # DO NOT fall back to another crop.
    # --------------------------------------------------

    if crop and not crop_candidates:

        print(
            "No KB record for:",
            sub_intent,
            "+",
            crop
        )

        return None, 0

    # --------------------------------------------------
    # STEP 4 — SIMILARITY
    # --------------------------------------------------

    best_record = None
    best_score = 0

    for record in crop_candidates:

        question_data = record.get(
            language_key,
            {}
        )

        kb_question = question_data.get(
            "question",
            ""
        )

        if not kb_question:
            continue

        kb_question = kb_question.lower().strip()

        # RapidFuzz similarity
        wratio = fuzz.WRatio(
            user_question,
            kb_question
        )

        # Word overlap
        user_words = set(
            user_question.split()
        )

        kb_words = set(
            kb_question.split()
        )

        overlap = len(
            user_words & kb_words
        )

        score = wratio + (
            overlap * 5
        )

        score = min(
            score,
            100
        )

        print(
            "Candidate:",
            record.get("id"),
            "|",
            kb_question,
            "| score:",
            score
        )

        if score > best_score:

            best_score = score
            best_record = record

    # --------------------------------------------------
    # STEP 5 — CONFIDENCE THRESHOLD
    # --------------------------------------------------

    if best_score >= MIN_SCORE:

        return best_record, best_score

    return None, best_score