"""
Masini Barokɛla
V5.2 Intent Detection

Detects:
    1. Agricultural domain
    2. Specific agricultural intent
    3. Crop/entity when identifiable

This module is intentionally separate from the
older V4 intent.py.
"""


# --------------------------------------------------
# Crop detection
# --------------------------------------------------

CROPS = {
    "millet": "Millet",
    "maize": "Maize",
    "corn": "Maize",
    "rice": "Rice",
    "sorghum": "Sorghum",
    "cotton": "Cotton",
    "groundnut": "Groundnut",
    "peanut": "Groundnut",
    "cowpea": "Cowpea",
    "sesame": "Sesame",
    "tomato": "Tomato",
    "tomatoes": "Tomato",
}


INTENT_PATTERNS = {

    # --------------------------------------------------
    # More specific intents FIRST
    # --------------------------------------------------

    # ------------------------------
    # Fertilizer
    # ------------------------------

    "FERTILIZER_TIMING": [
        "when should fertilizer",
        "when should i apply fertilizer",
        "when to apply fertilizer",
        "when apply fertilizer",
        "fertilizer timing",
        "fertiliser timing",
        "when should fertiliser",
        "when to apply fertiliser",
    ],

    "FERTILIZER_TYPE": [
        "which fertilizer",
        "what fertilizer",
        "fertilizer to use",
        "fertiliser to use",
        "which fertiliser",
        "what fertiliser",
    ],

    "FERTILIZER_IMPORTANCE": [
        "why is fertilizer",
        "why use fertilizer",
        "importance of fertilizer",
        "organic manure important",
        "why use fertiliser",
        "importance of fertiliser",
    ],

    "COMPOST": [
        "what is compost",
        "compost",
    ],

    "NUTRIENT_DEFICIENCY": [
        "soil lacks nutrients",
        "lack nutrients",
        "nutrient deficiency",
        "soil deficiency",
    ],


    # ------------------------------
    # Irrigation / Water
    # ------------------------------

    "WATER_CONSERVATION": [
        "conserve irrigation water",
        "conserve water",
        "save irrigation water",
        "save water",
        "reduce water use",
        "water conservation",
        "conserving water",
    ],

    "IRRIGATION_FREQUENCY": [
        "how often should",
        "how often",
        "how frequently",
        "frequency",
    ],

    "IRRIGATION_TIMING": [
        "best time of day",
        "when should i irrigate",
        "when to irrigate",
        "time to irrigate",
    ],

    "WATER_STRESS": [
        "signs that crops need water",
        "signs of water stress",
        "need water",
        "lack of water",
    ],

    "EXCESSIVE_IRRIGATION": [
        "excessive irrigation",
        "too much water",
        "over irrigation",
        "overwatering",
    ],


    # ------------------------------
    # Planting
    # ------------------------------

    "PLANTING_DEPTH": [
        "how deep",
        "planting depth",
        "depth",
        "deep should",
        "deep to plant",
    ],

    "PLANTING_SPACING": [
        "how far apart",
        "how much spacing",
        "spacing",
        "distance between",
        "space between",
        "apart should",
    ],

    "PLANTING_IMPORTANCE": [
        "why is timely planting",
        "why is planting important",
        "importance of planting",
        "why plant on time",
    ],

    "PLANTING_TIME": [
        "when should i plant",
        "when should i sow",
        "when do i plant",
        "when to plant",
        "best time",
        "best period",
        "planting time",
        "planting season",
        "time to plant",
        "period to plant",
    ],


    # ------------------------------
    # Pests
    # ------------------------------

    "INTEGRATED_PEST_MANAGEMENT": [
        "integrated pest management",
        "integrated pest control",
    ],

    "PEST_CONTROL": [
        "control pests",
        "control pest",
        "fight pests",
        "manage pests",
        "pest control",
    ],

    "PEST_SYMPTOMS": [
        "signs of pest",
        "signs of pests",
        "pest infestation",
        "pest symptoms",
    ],

    "PEST_MONITORING": [
        "monitor pests",
        "monitoring pests",
        "field monitoring",
        "monitor the field",
    ],

    "PEST_ROTATION": [
        "crop rotation reduce pests",
        "rotation reduce pests",
        "crop rotation pests",
    ],
}