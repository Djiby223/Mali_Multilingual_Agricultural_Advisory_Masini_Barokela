"""
Masini Barokɛla
Question Classifier
Version 4.2
"""

AGRICULTURE_KEYWORDS = {

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
    "soil",
    "fertilizer",
    "fertiliser",
    "compost",
    "rain",
    "rainfall",
    "irrigation",
    "seed",
    "plant",
    "planting",
    "harvest",
    "crop",
    "farm",
    "farmer",
    "pest",
    "disease",
    "weed"
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

    text = text.lower().strip()

    return text in GREETINGS


def is_agriculture_question(text):

    text = text.lower()

    for word in AGRICULTURE_KEYWORDS:

        if word in text:
            return True

    return False