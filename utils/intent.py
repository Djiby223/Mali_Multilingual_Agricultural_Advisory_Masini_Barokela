"""
Masini Barokɛla
Intent Detection
Version 4.3
"""

INTENTS = {
    "PLANTING": [
        "plant", "planting", "sow", "seed"
    ],
    "IRRIGATION": [
        "irrigate", "irrigation", "water", "watering"
    ],
    "FERTILIZATION": [
        "fertilizer", "fertilize", "manure", "compost"
    ],
    "WEED_CONTROL": [
        "weed", "weeds", "weeding"
    ],
    "PESTS": [
        "pest", "insect", "worm", "locust"
    ],
    "DISEASES": [
        "disease", "fungus", "blight", "virus"
    ],
    "HARVEST": [
        "harvest", "harvesting"
    ],
    "STORAGE": [
        "store", "storage", "warehouse"
    ],
    "SOIL": [
        "soil", "land", "earth"
    ]
}


def detect_intent(question):
    """
    Detect the agricultural intent of a user's question.
    """

    question = question.lower()

    for intent, keywords in INTENTS.items():

        for keyword in keywords:

            if keyword in question:
                return intent

    return "GENERAL"