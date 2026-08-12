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


# --------------------------------------------------
# Specific intent patterns
# --------------------------------------------------

INTENT_PATTERNS = {

    # ------------------------------
    # Planting
    # ------------------------------

    "PLANTING_TIME": [
        "when should",
        "when do i plant",
        "when to plant",
        "best time",
        "best period",
        "planting time",
        "planting season",
        "time to plant",
        "period to plant",
    ],

    "PLANTING_DEPTH": [
        "how deep",
        "depth",
        "planting depth",
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


    # ------------------------------
    # Irrigation
    # ------------------------------

    "IRRIGATION_FREQUENCY": [
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

    "WATER_CONSERVATION": [
        "conserve water",
        "save water",
        "save irrigation water",
        "reduce water use",
        "water conservation",
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
    # Fertilizer
    # ------------------------------

    "FERTILIZER_TYPE": [
        "which fertilizer",
        "what fertilizer",
        "fertilizer to use",
        "fertiliser to use",
    ],

    "FERTILIZER_IMPORTANCE": [
        "why is fertilizer",
        "why use fertilizer",
        "importance of fertilizer",
        "organic manure important",
    ],

    "FERTILIZER_TIMING": [
        "when should fertilizer",
        "when to apply fertilizer",
        "when apply fertilizer",
        "fertilizer timing",
        "fertiliser timing",
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
    # Pests
    # ------------------------------

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

    "INTEGRATED_PEST_MANAGEMENT": [
        "integrated pest management",
        "integrated pest control",
    ],

    "PEST_ROTATION": [
        "crop rotation reduce pests",
        "rotation reduce pests",
        "crop rotation pests",
    ],
}


# --------------------------------------------------
# Main detector
# --------------------------------------------------

def detect_intent_v5(question):
    """
    Detect the agricultural domain, specific intent,
    and crop/entity.

    Returns:
        {
            "domain": str,
            "sub_intent": str,
            "crop": str or None
        }
    """

    text = question.lower().strip()

    # ------------------------------
    # Crop detection
    # ------------------------------

    crop = None

    for keyword, crop_name in CROPS.items():

        if keyword in text:

            crop = crop_name
            break

    # ------------------------------
    # Specific intent detection
    # ------------------------------

    detected_intent = "GENERAL"

    for intent, patterns in INTENT_PATTERNS.items():

        for pattern in patterns:

            if pattern in text:

                detected_intent = intent
                break

        if detected_intent != "GENERAL":
            break

    # ------------------------------
    # Domain
    # ------------------------------

    if detected_intent.startswith("PLANTING"):

        domain = "PLANTING"

    elif detected_intent.startswith("IRRIGATION"):

        domain = "IRRIGATION"

    elif detected_intent.startswith("WATER"):

        domain = "IRRIGATION"

    elif (
        detected_intent.startswith("FERTILIZER")
        or detected_intent == "COMPOST"
        or detected_intent == "NUTRIENT_DEFICIENCY"
    ):

        domain = "FERTILIZATION"

    elif detected_intent.startswith("PEST"):

        domain = "PESTS"

    elif detected_intent == "INTEGRATED_PEST_MANAGEMENT":

        domain = "PESTS"

    else:

        domain = "GENERAL"

    return {
        "domain": domain,
        "sub_intent": detected_intent,
        "crop": crop,
    }