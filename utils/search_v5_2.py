"""
Masini Barokɛla
V5.2 Intent Detection

Architecture:
    1. Detect crop/entity
    2. Detect specific agricultural intent
    3. Determine agricultural domain

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

    # ==================================================
    # PLANTING
    # ==================================================

    "PLANTING_TIME": [
        "when should i plant",
        "when should i sow",
        "when do i plant",
        "when to plant",
        "best time to plant",
        "best period to plant",
        "planting time",
        "planting season",
        "time to plant",
        "period to plant",
        "when should farmers plant",
    ],

    "PLANTING_DEPTH": [
        "how deep should i plant",
        "how deep should i sow",
        "how deep to plant",
        "how deep to sow",
        "planting depth",
        "sowing depth",
        "depth should",
    ],

    "PLANTING_SPACING": [
        "how far apart",
        "how much spacing",
        "spacing between",
        "distance between plants",
        "distance between",
        "space between plants",
        "space between",
    ],

    "PLANTING_IMPORTANCE": [
        "why is timely planting",
        "why is planting important",
        "importance of planting",
        "why plant on time",
        "why timely planting",
    ],


    # ==================================================
    # IRRIGATION
    # ==================================================

    "IRRIGATION_FREQUENCY": [
        "how often should i water",
        "how often should crops be watered",
        "how often to water",
        "how frequently should i water",
        "how frequently to water",
        "watering frequency",
        "irrigation frequency",
    ],

    "IRRIGATION_TIMING": [
        "best time of day to irrigate",
        "best time to irrigate",
        "when should i irrigate",
        "when to irrigate",
        "time to irrigate",
    ],

    "WATER_CONSERVATION": [
        "conserve irrigation water",
        "conserve water",
        "save irrigation water",
        "save water",
        "reduce water use",
        "water conservation",
        "conserving water",
    ],

    "WATER_STRESS": [
        "signs that crops need water",
        "signs of water stress",
        "signs crops need water",
        "crops need water",
        "need water",
        "lack of water",
        "water stress",
    ],

    "EXCESSIVE_IRRIGATION": [
        "excessive irrigation",
        "too much irrigation",
        "too much water",
        "over irrigation",
        "over-irrigation",
        "overwatering",
    ],


    # ==================================================
    # FERTILIZATION
    # ==================================================

    "FERTILIZER_TYPE": [
        "which fertilizer",
        "what fertilizer",
        "fertilizer to use",
        "which fertiliser",
        "what fertiliser",
        "fertiliser to use",
    ],

    "FERTILIZER_TIMING": [
        "when should fertilizer",
        "when should i apply fertilizer",
        "when to apply fertilizer",
        "when apply fertilizer",
        "fertilizer timing",
        "when should fertiliser",
        "when to apply fertiliser",
        "fertiliser timing",
    ],

    "FERTILIZER_IMPORTANCE": [
        "why is fertilizer",
        "why use fertilizer",
        "importance of fertilizer",
        "why use fertiliser",
        "importance of fertiliser",
        "organic manure important",
        "why is organic manure",
    ],

    "COMPOST": [
        "what is compost",
        "what does compost mean",
    ],

    "NUTRIENT_DEFICIENCY": [
        "soil lacks nutrients",
        "lack nutrients",
        "lacks nutrients",
        "nutrient deficiency",
        "soil deficiency",
        "deficiency in nutrients",
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
        "signs of pest infestation",
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
        "prevent crop disease",
        "disease prevention",
        "prevent plant diseases",
    ],

    "DISEASED_PLANT_REMOVAL": [
        "diseased plants removed",
        "remove diseased plants",
        "why should diseased plants",
        "remove diseased",
    ],

    "FUNGAL_DISEASES": [
        "fungal diseases",
        "fungal disease",
        "what causes fungal",
        "causes of fungal diseases",
    ],

    "SEED_TREATMENT": [
        "what is seed treatment",
        "seed treatment",
        "treat seeds",
    ],

    "CROP_SANITATION": [
        "crop sanitation",
        "field sanitation",
        "why is crop sanitation",
    ],


    # ==================================================
    # WEATHER
    # ==================================================

    "RAINFALL_EFFECT": [
        "how does rainfall affect",
        "rainfall affect crop",
        "rainfall affect crops",
        "effect of rainfall",
    ],

    "WEATHER_FORECAST": [
        "follow weather forecasts",
        "weather forecast",
        "weather forecasts",
        "why follow weather",
    ],

    "HEAVY_RAINFALL": [
        "before heavy rainfall",
        "before heavy rain",
        "heavy rainfall",
        "heavy rain",
    ],

    "STRONG_WINDS": [
        "strong winds affect",
        "strong winds",
        "wind damage crops",
    ],

    "RAINFALL_ANOMALY": [
        "rainfall anomaly",
        "what is a rainfall anomaly",
    ],


    # ==================================================
    # DROUGHT
    # ==================================================

    "DROUGHT_DEFINITION": [
        "what is drought",
        "define drought",
    ],

    "DROUGHT_SIGNS": [
        "early signs of drought",
        "signs of drought",
        "drought signs",
    ],

    "DROUGHT_IMPACT_REDUCTION": [
        "reduce the impact of drought",
        "reduce drought impact",
        "cope with drought",
        "manage drought",
    ],

    "DROUGHT_TOLERANT_CROPS": [
        "drought-tolerant crops",
        "drought tolerant crops",
        "crops tolerant to drought",
    ],

    "DROUGHT_MULCHING": [
        "mulching during drought",
        "mulching important during drought",
        "mulch during drought",
    ],


    # ==================================================
    # SOIL MANAGEMENT
    # ==================================================

    "SOIL_FERTILITY": [
        "why is soil fertility",
        "soil fertility important",
        "importance of soil fertility",
    ],

    "SOIL_EROSION_CONTROL": [
        "reduce soil erosion",
        "soil erosion control",
        "prevent soil erosion",
        "control soil erosion",
    ],

    "CROP_ROTATION": [
        "what is crop rotation",
        "crop rotation",
    ],

    "CROP_ROTATION_BENEFITS": [
        "why is crop rotation beneficial",
        "benefits of crop rotation",
        "crop rotation beneficial",
    ],

    "MULCHING": [
        "what is mulching",
        "mulching",
    ],


    # ==================================================
    # HARVEST
    # ==================================================

    "HARVEST_READINESS": [
        "ready for harvest",
        "ready to harvest",
        "when crops are ready",
        "know when crops are ready",
        "know when to harvest",
        "harvest readiness",
    ],

    "HARVEST_TIMING": [
        "timely harvesting",
        "why harvest on time",
        "importance of timely harvesting",
    ],

    "EARLY_HARVEST": [
        "harvested too early",
        "harvest too early",
        "harvest too soon",
    ],

    "LATE_HARVEST": [
        "harvested too late",
        "harvest too late",
        "harvest too late",
    ],

    "HARVEST_HANDLING": [
        "harvested produce handled",
        "handle harvested produce",
        "handling harvested produce",
    ],


    # ==================================================
    # STORAGE
    # ==================================================

    "STORAGE_IMPORTANCE": [
        "why is proper storage",
        "proper storage important",
        "importance of storage",
    ],

    "GRAIN_DRYING": [
        "how should grains be dried",
        "dry grains before storage",
        "grains dried before storage",
    ],

    "STORAGE_PESTS": [
        "storage pests",
        "common storage pests",
    ],

    "STORAGE_PEST_CONTROL": [
        "protect stored grains from pests",
        "stored grains from pests",
        "storage pest control",
    ],

    "STORAGE_CLEANLINESS": [
        "storage facilities kept clean",
        "keep storage facilities clean",
        "storage facilities clean",
    ],


    # ==================================================
    # SEED SELECTION
    # ==================================================

    "CERTIFIED_SEEDS": [
        "certified seeds",
        "why use certified seeds",
        "importance of certified seeds",
    ],

    "SEED_QUALITY": [
        "select good quality seeds",
        "good quality seeds",
        "quality seeds",
    ],

    "SEED_GERMINATION": [
        "what is seed germination",
        "seed germination",
    ],

    "GERMINATION_TEST": [
        "test seed germination",
        "germination test",
        "test germination before planting",
    ],

    "DAMAGED_SEEDS": [
        "damaged seeds",
        "why should damaged seeds",
    ],


    # ==================================================
    # LAND PREPARATION
    # ==================================================

    "LAND_PREPARATION_IMPORTANCE": [
        "why is land preparation",
        "land preparation important",
    ],

    "LAND_PREPARATION_TIMING": [
        "when should land preparation",
        "when should farmers prepare land",
        "land preparation begin",
    ],

    "LAND_PREPARATION_METHODS": [
        "methods of land preparation",
        "methods for land preparation",
        "land preparation methods",
    ],

    "MINIMUM_TILLAGE": [
        "what is minimum tillage",
        "minimum tillage",
    ],

    "EROSION_LAND_PREPARATION": [
        "reduce soil erosion during land preparation",
        "soil erosion during land preparation",
    ],


    # ==================================================
    # WEED MANAGEMENT
    # ==================================================

    "WEED_IMPORTANCE": [
        "why is weed control",
        "why is weed control important",
        "importance of weed control",
    ],

    "WEED_CONTROL_METHODS": [
        "methods of weed control",
        "methods for weed control",
        "how to control weeds",
    ],

    "WEED_CONTROL_TIMING": [
        "when should farmers remove weeds",
        "when should farmers weed",
        "when to remove weeds",
        "when to weed",
        "when should weeds be removed",
    ],

    "WEED_MULCHING": [
        "mulching help control weeds",
        "mulch control weeds",
        "mulching control weeds",
    ],

    "HERBICIDE_USE": [
        "excessive herbicide use",
        "avoid excessive herbicide",
        "too much herbicide",
    ],


    # ==================================================
    # CLIMATE-SMART AGRICULTURE
    # ==================================================

    "CLIMATE_SMART_AGRICULTURE": [
        "what is climate-smart agriculture",
        "what is climate smart agriculture",
        "climate-smart agriculture",
    ],

    "CLIMATE_SMART_PRACTICES": [
        "examples of climate-smart",
        "examples of climate smart",
        "climate-smart agricultural practices",
    ],

    "AGROFORESTRY": [
        "how can agroforestry",
        "agroforestry benefit",
        "benefits of agroforestry",
    ],

    "WATER_HARVESTING": [
        "what is water harvesting",
        "water harvesting",
    ],

    "CROP_DIVERSIFICATION": [
        "crop diversification",
        "why is crop diversification",
        "benefits of crop diversification",
    ],


    # ==================================================
    # SUSTAINABLE AGRICULTURE
    # ==================================================

    "SUSTAINABLE_AGRICULTURE": [
        "what is sustainable agriculture",
        "sustainable agriculture",
    ],

    "AGRICULTURAL_BIODIVERSITY": [
        "why is biodiversity important",
        "biodiversity important in agriculture",
        "agricultural biodiversity",
    ],

    "SOIL_ORGANIC_MATTER": [
        "improve soil organic matter",
        "soil organic matter",
        "increase organic matter",
    ],

    "CROP_RESIDUES": [
        "crop residues retained",
        "retain crop residues",
        "crop residues on the field",
    ],

    "REDUCE_CHEMICAL_INPUTS": [
        "reduce the use of chemical inputs",
        "reduce chemical inputs",
        "reduce chemical use",
    ],


    # ==================================================
    # POST-HARVEST
    # ==================================================

    "POST_HARVEST_HANDLING": [
        "what is post-harvest handling",
        "post-harvest handling",
    ],

    "PRODUCE_SORTING": [
        "why should harvested produce be sorted",
        "sort harvested produce",
        "sorting harvested produce",
    ],

    "SUNLIGHT_PROTECTION": [
        "protected from direct sunlight",
        "direct sunlight after harvest",
        "protect harvested produce from sunlight",
    ],

    "POST_HARVEST_LOSSES": [
        "reduce post-harvest losses",
        "post-harvest losses",
        "reduce post harvest losses",
    ],

    "PACKAGING": [
        "why is proper packaging",
        "proper packaging important",
        "packaging important",
    ],


    # ==================================================
    # LIVESTOCK INTEGRATION
    # ==================================================

    "LIVESTOCK_CROP_INTEGRATION": [
        "integrating livestock with crop farming",
        "livestock with crop farming",
        "integrate livestock and crops",
    ],

    "ANIMAL_MANURE": [
        "animal manure benefit",
        "animal manure",
        "manure benefit crop production",
    ],

    "LIVESTOCK_WATER": [
        "livestock clean water",
        "animals clean water",
        "livestock have access to clean water",
    ],

    "CROP_RESIDUES_LIVESTOCK": [
        "crop residues livestock",
        "crop residues be used in livestock",
        "use crop residues for livestock",
    ],

    "LIVESTOCK_VACCINATION": [
        "livestock vaccination",
        "why is livestock vaccination",
        "vaccination important for livestock",
    ],


    # ==================================================
    # AGRICULTURAL EXTENSION
    # ==================================================

    "AGRICULTURAL_EXTENSION": [
        "what is agricultural extension",
        "agricultural extension",
    ],

    "EXTENSION_AGENTS": [
        "consult extension agents",
        "extension agents",
        "agricultural specialists",
    ],

    "AGRICULTURAL_INFORMATION": [
        "access agricultural information",
        "agricultural information",
    ],

    "FARMER_ORGANIZATIONS": [
        "farmer organizations",
        "role do farmer organizations",
    ],

    "FARMER_TRAINING": [
        "farmer training",
        "why is farmer training",
        "importance of farmer training",
    ],


    # ==================================================
    # SOIL AND WATER CONSERVATION
    # ==================================================

    "SOIL_CONSERVATION": [
        "what is soil conservation",
        "soil conservation",
    ],

    "WATER_CONSERVATION_AGRICULTURE": [
        "water conservation in agriculture",
        "water conservation agriculture",
    ],

    "CONTOUR_RIDGES": [
        "contour ridges",
        "how do contour ridges",
    ],

    "FARM_TREES": [
        "trees important on farms",
        "trees on farms",
        "benefits of trees on farms",
    ],

    "COVER_CROPS": [
        "benefits of cover crops",
        "cover crops",
    ],


    # ==================================================
    # PEST AND DISEASE DIAGNOSIS
    # ==================================================

    "DISEASE_IDENTIFICATION": [
        "identify crop diseases",
        "identify crop disease",
        "how can farmers identify diseases",
        "identify plant diseases",
    ],

    "EARLY_DISEASE_DETECTION": [
        "early disease detection",
        "early detection of disease",
        "why is early disease detection",
    ],

    "CROP_SYMPTOMS": [
        "unusual crop symptoms",
        "unusual symptoms",
        "crop symptoms",
    ],

    "MOBILE_DIAGNOSIS": [
        "mobile technologies",
        "mobile technology diagnose",
        "mobile technologies help diagnose",
    ],

    "FARM_RECORDS": [
        "farm records",
        "keep farm records",
        "why should farmers keep farm records",
    ],
}


# --------------------------------------------------
# Domain mapping
# --------------------------------------------------

DOMAIN_MAP = {

    "PLANTING": "PLANTING",

    "IRRIGATION": "IRRIGATION",
    "WATER_CONSERVATION": "IRRIGATION",
    "WATER_STRESS": "IRRIGATION",
    "EXCESSIVE_IRRIGATION": "IRRIGATION",

    "FERTILIZER_TIMING": "FERTILIZATION",
    "FERTILIZER_TYPE": "FERTILIZATION",
    "FERTILIZER_IMPORTANCE": "FERTILIZATION",
    "COMPOST": "FERTILIZATION",
    "NUTRIENT_DEFICIENCY": "FERTILIZATION",

    "PEST_CONTROL": "PESTS",
    "PEST_SYMPTOMS": "PESTS",
    "PEST_MONITORING": "PESTS",
    "PEST_ROTATION": "PESTS",
    "INTEGRATED_PEST_MANAGEMENT": "PESTS",

    "DISEASE_PREVENTION": "DISEASES",
    "DISEASED_PLANT_REMOVAL": "DISEASES",
    "FUNGAL_DISEASES": "DISEASES",
    "SEED_TREATMENT": "DISEASES",
    "CROP_SANITATION": "DISEASES",

    "RAINFALL_EFFECT": "WEATHER",
    "WEATHER_FORECAST": "WEATHER",
    "HEAVY_RAINFALL": "WEATHER",
    "STRONG_WINDS": "WEATHER",
    "RAINFALL_ANOMALY": "WEATHER",

    "DROUGHT_DEFINITION": "DROUGHT",
    "DROUGHT_SIGNS": "DROUGHT",
    "DROUGHT_IMPACT_REDUCTION": "DROUGHT",
    "DROUGHT_TOLERANT_CROPS": "DROUGHT",
    "DROUGHT_MULCHING": "DROUGHT",

    "SOIL_FERTILITY": "SOIL_MANAGEMENT",
    "SOIL_EROSION_CONTROL": "SOIL_MANAGEMENT",
    "CROP_ROTATION": "SOIL_MANAGEMENT",
    "CROP_ROTATION_BENEFITS": "SOIL_MANAGEMENT",
    "MULCHING": "SOIL_MANAGEMENT",

    "HARVEST_READINESS": "HARVEST",
    "HARVEST_TIMING": "HARVEST",
    "EARLY_HARVEST": "HARVEST",
    "LATE_HARVEST": "HARVEST",
    "HARVEST_HANDLING": "HARVEST",

    "STORAGE_IMPORTANCE": "STORAGE",
    "GRAIN_DRYING": "STORAGE",
    "STORAGE_PESTS": "STORAGE",
    "STORAGE_PEST_CONTROL": "STORAGE",
    "STORAGE_CLEANLINESS": "STORAGE",

    "CERTIFIED_SEEDS": "SEED_SELECTION",
    "SEED_QUALITY": "SEED_SELECTION",
    "SEED_GERMINATION": "SEED_SELECTION",
    "GERMINATION_TEST": "SEED_SELECTION",
    "DAMAGED_SEEDS": "SEED_SELECTION",

    "LAND_PREPARATION_IMPORTANCE": "LAND_PREPARATION",
    "LAND_PREPARATION_TIMING": "LAND_PREPARATION",
    "LAND_PREPARATION_METHODS": "LAND_PREPARATION",
    "MINIMUM_TILLAGE": "LAND_PREPARATION",
    "EROSION_LAND_PREPARATION": "LAND_PREPARATION",

    "WEED_IMPORTANCE": "WEED_MANAGEMENT",
    "WEED_CONTROL_METHODS": "WEED_MANAGEMENT",
    "WEED_CONTROL_TIMING": "WEED_MANAGEMENT",
    "WEED_MULCHING": "WEED_MANAGEMENT",
    "HERBICIDE_USE": "WEED_MANAGEMENT",

    "CLIMATE_SMART_AGRICULTURE": "CLIMATE_SMART_AGRICULTURE",
    "CLIMATE_SMART_PRACTICES": "CLIMATE_SMART_AGRICULTURE",
    "AGROFORESTRY": "CLIMATE_SMART_AGRICULTURE",
    "WATER_HARVESTING": "CLIMATE_SMART_AGRICULTURE",
    "CROP_DIVERSIFICATION": "CLIMATE_SMART_AGRICULTURE",

    "SUSTAINABLE_AGRICULTURE": "SUSTAINABLE_AGRICULTURE",
    "AGRICULTURAL_BIODIVERSITY": "SUSTAINABLE_AGRICULTURE",
    "SOIL_ORGANIC_MATTER": "SUSTAINABLE_AGRICULTURE",
    "CROP_RESIDUES": "SUSTAINABLE_AGRICULTURE",
    "REDUCE_CHEMICAL_INPUTS": "SUSTAINABLE_AGRICULTURE",

    "POST_HARVEST_HANDLING": "POST_HARVEST_HANDLING",
    "PRODUCE_SORTING": "POST_HARVEST_HANDLING",
    "SUNLIGHT_PROTECTION": "POST_HARVEST_HANDLING",
    "POST_HARVEST_LOSSES": "POST_HARVEST_HANDLING",
    "PACKAGING": "POST_HARVEST_HANDLING",

    "LIVESTOCK_CROP_INTEGRATION": "LIVESTOCK_INTEGRATION",
    "ANIMAL_MANURE": "LIVESTOCK_INTEGRATION",
    "LIVESTOCK_WATER": "LIVESTOCK_INTEGRATION",
    "CROP_RESIDUES_LIVESTOCK": "LIVESTOCK_INTEGRATION",
    "LIVESTOCK_VACCINATION": "LIVESTOCK_INTEGRATION",

    "AGRICULTURAL_EXTENSION": "AGRICULTURAL_EXTENSION",
    "EXTENSION_AGENTS": "AGRICULTURAL_EXTENSION",
    "AGRICULTURAL_INFORMATION": "AGRICULTURAL_EXTENSION",
    "FARMER_ORGANIZATIONS": "AGRICULTURAL_EXTENSION",
    "FARMER_TRAINING": "AGRICULTURAL_EXTENSION",

    "SOIL_CONSERVATION": "SOIL_AND_WATER_CONSERVATION",
    "WATER_CONSERVATION_AGRICULTURE": "SOIL_AND_WATER_CONSERVATION",
    "CONTOUR_RIDGES": "SOIL_AND_WATER_CONSERVATION",
    "FARM_TREES": "SOIL_AND_WATER_CONSERVATION",
    "COVER_CROPS": "SOIL_AND_WATER_CONSERVATION",

    "DISEASE_IDENTIFICATION": "PEST_AND_DISEASE_DIAGNOSIS",
    "EARLY_DISEASE_DETECTION": "PEST_AND_DISEASE_DIAGNOSIS",
    "CROP_SYMPTOMS": "PEST_AND_DISEASE_DIAGNOSIS",
    "MOBILE_DIAGNOSIS": "PEST_AND_DISEASE_DIAGNOSIS",
    "FARM_RECORDS": "PEST_AND_DISEASE_DIAGNOSIS",
}


# --------------------------------------------------
# Main detector
# --------------------------------------------------

def detect_intent_v5(question):
    """
    Detect:

        1. Agricultural domain
        2. Specific sub-intent
        3. Crop/entity

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

    for intent, patterns in INTENT_PATTERNS.items():

        for pattern in patterns:

            if pattern in text:
                detected_intent = intent
                break

        if detected_intent != "GENERAL":
            break

    # --------------------------------------------------
    # Domain detection
    # --------------------------------------------------

    domain = DOMAIN_MAP.get(
        detected_intent,
        "GENERAL"
    )

    return {
        "domain": domain,
        "sub_intent": detected_intent,
        "crop": crop,
    }