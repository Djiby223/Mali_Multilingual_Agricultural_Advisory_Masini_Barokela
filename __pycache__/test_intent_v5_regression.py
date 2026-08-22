from utils.intent_v5 import detect_intent_v5


# ============================================================
# Masini Barokɛla V5.2 Intent Regression Test
# ============================================================

TESTS = [

    # --------------------------------------------------------
    # PLANTING
    # --------------------------------------------------------
    ("PLANTING_TIME", "When should I plant millet?"),
    ("PLANTING_TIME", "When is the right time to sow maize?"),
    ("PLANTING_DEPTH", "How deep should millet seeds be planted?"),
    ("PLANTING_DEPTH", "How deep should I sow millet seeds?"),
    ("PLANTING_SPACING", "How far apart should maize plants be?"),
    ("PLANTING_SPACING", "How much spacing should I leave between maize plants?"),
    ("PLANTING_IMPORTANCE", "Why is timely planting important?"),

    # --------------------------------------------------------
    # FERTILIZER
    # --------------------------------------------------------
    ("FERTILIZER_TIMING", "When should I apply fertilizer?"),
    ("FERTILIZER_TYPE", "Which fertilizer should I use?"),
    ("FERTILIZER_IMPORTANCE", "Why is fertilizer important?"),
    ("COMPOST", "What is compost?"),
    ("NUTRIENT_DEFICIENCY", "What are the signs of nutrient deficiency?"),

    # --------------------------------------------------------
    # IRRIGATION
    # --------------------------------------------------------
    ("WATER_CONSERVATION", "How can I conserve irrigation water?"),
    ("IRRIGATION_FREQUENCY", "How often should I irrigate crops?"),
    ("IRRIGATION_TIMING", "When should I irrigate my crops?"),
    ("WATER_STRESS", "What are signs that crops need water?"),
    ("EXCESSIVE_IRRIGATION", "What happens with too much irrigation?"),

    # --------------------------------------------------------
    # PESTS
    # --------------------------------------------------------
    ("INTEGRATED_PEST_MANAGEMENT", "What is integrated pest management?"),
    ("PEST_CONTROL", "How can I control pests?"),
    ("PEST_SYMPTOMS", "What are signs of pest infestation?"),
    ("PEST_MONITORING", "How should I monitor pests?"),
    ("PEST_ROTATION", "Can crop rotation reduce pests?"),

    # --------------------------------------------------------
    # DISEASES
    # --------------------------------------------------------
    ("DISEASE_PREVENTION", "How can I prevent crop diseases?"),
    ("DISEASE_SYMPTOMS", "What are the symptoms of crop disease?"),
    ("PEST_DISEASE_DIAGNOSIS", "How can I diagnose crop pests and diseases?"),

    # --------------------------------------------------------
    # SOIL
    # --------------------------------------------------------
    ("SOIL_MANAGEMENT", "How can I improve soil fertility?"),
    ("SOIL_CONSERVATION", "How can I reduce soil erosion?"),

    # --------------------------------------------------------
    # OTHER AGRICULTURAL INTENTS
    # --------------------------------------------------------
    ("HARVEST", "When should I harvest my crops?"),
    ("STORAGE", "How should I store crops?"),
    ("SEED_SELECTION", "How should I select quality seeds?"),
    ("LAND_PREPARATION", "How should I prepare the land before planting?"),
    ("WEED_MANAGEMENT", "How can I control weeds?"),
    ("CLIMATE_SMART_AGRICULTURE", "What is climate-smart agriculture?"),
    ("SUSTAINABLE_AGRICULTURE", "What is sustainable agriculture?"),
    ("POST_HARVEST_HANDLING", "What is post-harvest handling?"),
    ("LIVESTOCK_INTEGRATION", "How can livestock be integrated with crop farming?"),
    ("AGRICULTURAL_EXTENSION", "What are agricultural extension services?"),
]


def main():

    print("=" * 70)
    print("Masini Barokɛla V5.2 Intent Regression Test")
    print("=" * 70)

    passed = 0
    failed = 0

    for expected, question in TESTS:

        result = detect_intent_v5(question)

        actual = result.get("sub_intent")

        status = "PASS" if actual == expected else "FAIL"

        if status == "PASS":
            passed += 1
        else:
            failed += 1

        print(
            f"{status} | "
            f"Expected={expected:<28} | "
            f"Actual={str(actual):<28} | "
            f"{question}"
        )

    total = len(TESTS)
    accuracy = (passed / total * 100) if total else 0

    print()
    print("=" * 70)
    print("SUMMARY")
    print("=" * 70)
    print(f"Passed:   {passed}/{total}")
    print(f"Failed:   {failed}/{total}")
    print(f"Accuracy: {accuracy:.1f}%")
    print("=" * 70)

    if failed > 0:
        raise SystemExit(1)


if __name__ == "__main__":
    main()