"""
Masini Barokɛla
Question Classifier
Version 4.4
"""

AGRICULTURE_KEYWORDS = {

    # Crops
    "rice",
    "millet",
    "maize",
    "corn",
    "sorghum",
    "cotton",
    "groundnut",
    "peanut",
    "cowpea",
    "sesame",
    "vegetable",
    "tomato",

    # Soil and inputs
    "soil",
    "fertilizer",
    "fertiliser",
    "compost",
    "manure",

    # Water and irrigation
    "rain",
    "rainfall",
    "water",
    "watering",
    "irrigation",
    "irrigate",

    # Planting and crops
    "seed",
    "seeds",
    "plant",
    "plants",
    "planting",
    "sow",
    "sowing",
    "crop",
    "crops",

    # Farm
    "farm",
    "farmer",
    "farmers",
    "field",
    "fields",
    "agriculture",
    "agricultural",

    # Crop management
    "pest",
    "pests",
    "disease",
    "diseases",
    "weed",
    "weeds",
    "harvest",
    "harvesting",

    # Livestock
    "livestock",
    "animal",
    "animals",
    "cattle",
    "goat",
    "sheep",
    "poultry"
}


GREETINGS = {

    "hello",
    "hi",
    "hey",
    "good morning",
    "good afternoon",
    "good evening"
}


def is_greeting(text):
    """
    Detect simple greetings.
    """

    text = text.lower().strip()

    return text in GREETINGS


def is_agriculture_question(text):
    """
    Determine whether a question is related to agriculture.
    """

    text = text.lower().strip()

    for word in AGRICULTURE_KEYWORDS:

        if word in text:
            return True

    return False