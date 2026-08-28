"""
Masini Barokɛla
V5.2 Intent Detection

Detects:
    1. Agricultural domain
    2. Specific agricultural intent
    3. Crop/entity when identifiable

This module is intentionally separate from
the older V4 intent.py.
"""


# --------------------------------------------------
# Crop detection
# --------------------------------------------------

CROPS = {
    # English
    "millet": "Millet",
    "maize": "Maize",
    "corn": "Maize",
    "rice": "Rice",
    "sorghum": "Sorghum",
    "cotton": "Cotton",
    "groundnut": "Groundnut",
    "peanut": "Groundnut",

    # French
    "mil": "Millet",
    "maïs": "Maize",

    # Bambara
    "ɲɔ": "Millet",
    "kaba": "Maize",
}


# --------------------------------------------------
# Specific intent patterns
# --------------------------------------------------

INTENT_PATTERNS = {

    # ==================================================
    # FERTILIZER
    # ==================================================

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


    # ==================================================
    # IRRIGATION / WATER
    # ==================================================

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
       "too much irrigation",
       "too much water",
       "over irrigation",
       "over-irrigation",
       "overwatering",
       "too much watering",
       "excess water",
       "excessive watering",
   ],

    # ==================================================
    # PLANTING
    # ==================================================

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
        "when do i sow",
        "when to plant",
        "when to sow",
        "best time",
        "right time",
        "best time to plant",
        "best time to sow",
        "right time to plant",
        "right time to sow",
        "when is the best time",
        "when is the right time",
        "planting time",
        "planting season",
        "planting period",
        "when is planting",
        "when is the planting season",
        "when should planting be done",
    ],


    # ==================================================
    # PESTS
    # ==================================================

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


    # ==================================================
    # DISEASES
    # ==================================================

    "DISEASE_PREVENTION": [
        "prevent crop diseases",
        "prevent diseases",
        "prevent disease",
        "disease prevention",
        "avoid crop diseases",
        "how to prevent diseases",
    ],

    "DISEASE_SYMPTOMS": [
       "signs of disease",
       "signs of diseases",
       "signs of crop disease",
       "signs of crop diseases",
       "disease symptoms",
       "crop disease symptoms",
       "symptoms of disease",
       "symptoms of crop disease",
       "symptoms of crop diseases",
       "crop symptoms",
   ],


    # ==================================================
    # SOIL MANAGEMENT
    # ==================================================

    "SOIL_MANAGEMENT": [
        "soil management",
        "manage the soil",
        "manage soil",
        "improve soil",
        "soil fertility",
        "improving soil",
        "crop rotation beneficial",
        "benefits of crop rotation",
    ],


    # ==================================================
    # HARVEST
    # ==================================================

    "HARVEST": [
        "when to harvest",
        "when should farmers harvest",
        "when should i harvest",
        "harvest time",
        "harvesting time",
        "ready for harvest",
        "ready to harvest",
        "harvest crops",
    ],


    # ==================================================
    # STORAGE
    # ==================================================

    "STORAGE": [
        "proper storage",
        "crop storage",
        "grain storage",
        "store crops",
        "how to store",
        "why is storage important",
        "importance of storage",
        "storage important",
    ],


    # ==================================================
    # SEED SELECTION
    # ==================================================

    "SEED_SELECTION": [
        "seed selection",
        "select seeds",
        "selecting seeds",
        "certified seeds",
        "quality seeds",
        "good seeds",
        "why use certified seeds",
        "importance of certified seeds",
    ],


    # ==================================================
    # LAND PREPARATION
    # ==================================================

    "LAND_PREPARATION": [
        "land preparation",
        "prepare the land",
        "prepare land",
        "land before planting",
        "preparing the land",
    ],


    # ==================================================
    # WEED MANAGEMENT
    # ==================================================

    "WEED_MANAGEMENT": [
        "weed management",
        "control weeds",
        "control weed",
        "remove weeds",
        "remove weed",
        "weeding",
        "manage weeds",
        "weed control",
    ],


    # ==================================================
    # CLIMATE-SMART AGRICULTURE
    # ==================================================

    "CLIMATE_SMART_AGRICULTURE": [
        "climate-smart agriculture",
        "climate smart agriculture",
        "climate-smart farming",
        "climate smart farming",
        "smart agriculture",
        "farming under climate change",
    ],


    # ==================================================
    # SUSTAINABLE AGRICULTURE
    # ==================================================

    "SUSTAINABLE_AGRICULTURE": [
        "sustainable agriculture",
        "sustainable farming",
        "sustainable farming practices",
        "sustainable agriculture practices",
    ],


    # ==================================================
    # POST-HARVEST HANDLING
    # ==================================================

    "POST_HARVEST_HANDLING": [
        "post-harvest handling",
        "post harvest handling",
        "postharvest handling",
        "after harvest",
        "after harvesting",
        "handling after harvest",
    ],


    # ==================================================
    # LIVESTOCK INTEGRATION
    # ==================================================

    "LIVESTOCK_INTEGRATION": [
       "livestock integration",
       "integrating livestock",
       "integrate livestock",
       "livestock with crops",
       "livestock and crop farming",
       "crop livestock integration",
       "benefits of integrating livestock",
       "livestock be integrated with crop farming",
       "integrating livestock with crop farming",
       "integrated livestock and crop farming",
       "integrate livestock with crops",
       "combine livestock and crop farming",
       "combine crops and livestock",
   ],


    # ==================================================
    # AGRICULTURAL EXTENSION
    # ==================================================

    "AGRICULTURAL_EXTENSION": [
        "agricultural extension",
        "extension services",
        "extension service",
        "agricultural advisory",
        "farm advisory",
        "extension officer",
    ],


    # ==================================================
    # SOIL AND WATER CONSERVATION
    # ==================================================

    "SOIL_CONSERVATION": [
        "soil conservation",
        "conserve soil",
        "soil erosion",
        "reduce soil erosion",
        "prevent soil erosion",
        "erosion control",
        "water conservation and soil",
    ],


    # ==================================================
    # PEST AND DISEASE DIAGNOSIS
    # ==================================================

    "PEST_DISEASE_DIAGNOSIS": [
       "identify crop diseases",
       "identify diseases",
       "identify crop disease",
       "diagnose crop disease",
       "diagnose diseases",
       "disease diagnosis",
       "identify pests and diseases",
       "identify pest and disease",
       "unusual crop symptoms",
       "diagnose crop pests and diseases",
       "diagnose pests and diseases",
       "diagnose crop pests",
       "identify crop pests and diseases",
       "identify crop pests",
       "how to diagnose crop pests and diseases",
      "how can i diagnose crop pests and diseases",
   ],
}
   # --------------------------------------------------
# V5.3 Multilingual Intent Patterns
# French planting intents
# --------------------------------------------------

MULTILINGUAL_INTENT_PATTERNS = {

    "PLANTING_TIME": [
        # French
        "quand planter",
        "quand faut il planter",
        "quand faut-il planter",
        "quand semer",
        "quand faut il semer",
        "quand faut-il semer",
        "meilleur moment pour planter",
        "meilleur moment pour semer",
        "meilleure période pour planter",
        "meilleure période pour semer",
        "période recommandée pour planter",
        "période recommandée pour semer",
        "moment recommandé pour planter",
        "moment recommandé pour semer",
        "quelle période pour planter",
        "quelle période pour semer",
    ],

    "PLANTING_DEPTH": [
        # French
        "profondeur",
        "à quelle profondeur",
        "a quelle profondeur",
        "profondeur pour semer",
        "profondeur pour planter",
        "profondeur recommandée",
        "profondeur recommandée pour semer",
        "profondeur recommandée pour planter",
        "profondeur des graines",
        "profondeur de semis",
    ],

    "PLANTING_SPACING": [
        # French
        "espacement",
        "quel espacement",
        "distance entre",
        "distance entre les plants",
        "distance entre les plantes",
        "distance pour planter",
        "quelle distance",
        "quelle distance entre",
        "laisser entre les plants",
        "espace entre les plants",
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

    # --------------------------------------------------
    # Crop detection
    # --------------------------------------------------

    crop = None

    for keyword, crop_name in CROPS.items():

        if keyword in text:

            crop = crop_name
            break


    # --------------------------------------------------
    # Specific intent detection
    # --------------------------------------------------
    detected_intent = "GENERAL"

    # --------------------------------------------------
    # V5.3: Existing English intent detection
    # --------------------------------------------------

    for intent, patterns in INTENT_PATTERNS.items():

        for pattern in patterns:

            if pattern in text:

                detected_intent = intent
                break

        if detected_intent != "GENERAL":
            break


    # --------------------------------------------------
    # V5.3: Multilingual intent fallback
    #
    # Existing English patterns remain authoritative.
    # Multilingual patterns are checked only when the
    # English detector returns GENERAL.
    # --------------------------------------------------

    if detected_intent == "GENERAL":

        for intent, patterns in MULTILINGUAL_INTENT_PATTERNS.items():

            for pattern in patterns:

                if pattern in text:

                    detected_intent = intent
                    break

            if detected_intent != "GENERAL":
                break


    # --------------------------------------------------
    # Domain detection
    # --------------------------------------------------

    if detected_intent.startswith("PLANTING"):

        domain = "PLANTING"

    elif (
        detected_intent.startswith("IRRIGATION")
        or detected_intent.startswith("WATER")
        or detected_intent == "EXCESSIVE_IRRIGATION"

    ):

        domain = "IRRIGATION"

    elif (
        detected_intent.startswith("FERTILIZER")
        or detected_intent == "COMPOST"
        or detected_intent == "NUTRIENT_DEFICIENCY"
    ):

        domain = "FERTILIZATION"

    elif detected_intent == "PEST_DISEASE_DIAGNOSIS":
        domain = "PEST_DISEASE_DIAGNOSIS"

    elif (
        detected_intent.startswith("PEST")
        or detected_intent == "INTEGRATED_PEST_MANAGEMENT"
    ):
        domain = "PESTS"

    elif detected_intent.startswith("DISEASE"):

        domain = "DISEASES"

    elif detected_intent == "SOIL_MANAGEMENT":

        domain = "SOIL_MANAGEMENT"

    elif detected_intent == "HARVEST":

        domain = "HARVEST"

    elif detected_intent == "STORAGE":

        domain = "STORAGE"

    elif detected_intent == "SEED_SELECTION":

        domain = "SEED_SELECTION"

    elif detected_intent == "LAND_PREPARATION":

        domain = "LAND_PREPARATION"

    elif detected_intent == "WEED_MANAGEMENT":

        domain = "WEED_MANAGEMENT"

    elif detected_intent == "CLIMATE_SMART_AGRICULTURE":

        domain = "CLIMATE_SMART_AGRICULTURE"

    elif detected_intent == "SUSTAINABLE_AGRICULTURE":

        domain = "SUSTAINABLE_AGRICULTURE"

    elif detected_intent == "POST_HARVEST_HANDLING":

        domain = "POST_HARVEST_HANDLING"

    elif detected_intent == "LIVESTOCK_INTEGRATION":

        domain = "LIVESTOCK_INTEGRATION"

    elif detected_intent == "AGRICULTURAL_EXTENSION":

        domain = "AGRICULTURAL_EXTENSION"

    elif detected_intent == "SOIL_CONSERVATION":

        domain = "SOIL_CONSERVATION"

    else:

        domain = "GENERAL"


    # --------------------------------------------------
    # Return result
    # --------------------------------------------------

    return {
        "domain": domain,
        "sub_intent": detected_intent,
        "crop": crop,
    }