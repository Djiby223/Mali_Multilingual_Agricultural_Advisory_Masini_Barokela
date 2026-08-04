import re

CROPS = {
    "rice": ["rice", "paddy"],
    "maize": ["maize", "corn"],
    "millet": ["millet"],
    "sorghum": ["sorghum"],
    "cotton": ["cotton"],
    "groundnut": ["groundnut", "peanut"],
    "cowpea": ["cowpea"],
    "sesame": ["sesame"],
    "vegetables": [
        "vegetable",
        "tomato",
        "onion",
        "pepper",
        "cabbage",
        "okra"
    ]
}

def detect_crop(question):

    q = question.lower()

    for crop, keywords in CROPS.items():

        for word in keywords:

            if re.search(rf"\b{re.escape(word)}\b", q):

                return crop.title()

    return "General"