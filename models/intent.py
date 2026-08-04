INTENTS = {

    "Planting": [
        "plant",
        "sow",
        "seed",
        "spacing"
    ],

    "Fertilizer": [
        "fertilizer",
        "urea",
        "npk",
        "compost",
        "manure"
    ],

    "Irrigation": [
        "water",
        "irrigation"
    ],

    "Pests": [
        "pest",
        "insect",
        "worm",
        "aphid",
        "locust"
    ],

    "Disease": [
        "disease",
        "fungus",
        "rot",
        "blight",
        "yellow"
    ],

    "Harvest": [
        "harvest",
        "storage"
    ]
}

def detect_intent(question):

    q = question.lower()

    for intent, keywords in INTENTS.items():

        for word in keywords:

            if word in q:

                return intent

    return "General Advice"