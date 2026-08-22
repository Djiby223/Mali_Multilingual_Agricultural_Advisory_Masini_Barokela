from utils.intent_v5 import detect_intent_v5


TESTS = [

    # ==========================================================
    # FERTILIZATION
    # ==========================================================

    ("FERT-1", "When should I apply fertilizer to maize?", "FERTILIZER_TIMING", "Fertilization", "Maize"),
    ("FERT-2", "What fertilizer should I use for millet?", "FERTILIZER_TYPE", "Fertilization", "Millet"),
    ("FERT-3", "Why is fertilizer important for crops?", "FERTILIZER_IMPORTANCE", "Fertilization", None),
    ("FERT-4", "What is compost?", "COMPOST", "Fertilization", None),
    ("FERT-5", "What should I do if the soil lacks nutrients?", "NUTRIENT_DEFICIENCY", "Fertilization", None),

    # ==========================================================
    # IRRIGATION / WATER
    # ==========================================================

    ("WAT-1", "How can I conserve irrigation water?", "WATER_CONSERVATION", "IRRIGATION", None),
    ("WAT-2", "How often should I irrigate maize?", "IRRIGATION_FREQUENCY", "IRRIGATION", "Maize"),
    ("WAT-3", "When should I irrigate millet?", "IRRIGATION_TIMING", "IRRIGATION", "Millet"),
    ("WAT-4", "What are the signs that crops need water?", "WATER_STRESS", "IRRIGATION", None),
    ("WAT-5", "What happens with too much irrigation?", "EXCESSIVE_IRRIGATION", "IRRIGATION", None),

    # ==========================================================
    # PLANTING
    # ==========================================================

    ("PLANT-1", "When should I plant millet?", "PLANTING_TIME", "PLANTING", "Millet"),
    ("PLANT-2", "How deep should millet seeds be planted?", "PLANTING_DEPTH", "PLANTING", "Millet"),
    ("PLANT-3", "How far apart should maize plants be?", "PLANTING_SPACING", "PLANTING", "Maize"),
    ("PLANT-4", "Why is timely planting important?", "PLANTING_IMPORTANCE", "PLANTING", None),

    # ==========================================================
    # PESTS
    # ==========================================================

    ("PEST-1", "What is integrated pest management?", "INTEGRATED_PEST_MANAGEMENT", "PESTS", None),
    ("PEST-2", "How can I control pests in maize?", "PEST_CONTROL", "PESTS", "Maize"),
    ("PEST-3", "What are the signs of pest infestation?", "PEST_SYMPTOMS", "PESTS", None),
    ("PEST-4", "How should I monitor pests in the field?", "PEST_MONITORING", "PESTS", None),
    ("PEST-5", "Can crop rotation reduce pests?", "PEST_ROTATION", "PESTS", None),

    # ==========================================================
    # DISEASES
    # ==========================================================

    ("DIS-1", "How can I prevent crop diseases?", "DISEASE_PREVENTION", "DISEASES", None),
    ("DIS-2", "What are the symptoms of crop disease?", "DISEASE_SYMPTOMS", "DISEASES", None),

    # ==========================================================
    # SOIL
    # ==========================================================

    ("SOIL-1", "How can I improve soil fertility?", "SOIL_MANAGEMENT", "SOIL_MANAGEMENT", None),
    ("SOIL-2", "How can I prevent soil erosion?", "SOIL_CONSERVATION", "SOIL_CONSERVATION", None),

    # ==========================================================
    # HARVEST / STORAGE
    # ==========================================================

    ("HARV-1", "When should I harvest maize?", "HARVEST", "HARVEST", "Maize"),
    ("STOR-1", "How should I store grain?", "STORAGE", "STORAGE", None),

    # ==========================================================
    # SEEDS / LAND / WEEDS
    # ==========================================================

    ("SEED-1", "How should I select good seeds?", "SEED_SELECTION", "SEED_SELECTION", None),
    ("LAND-1", "How should I prepare the land before planting?", "LAND_PREPARATION", "LAND_PREPARATION", None),
    ("WEED-1", "How can I control weeds in maize?", "WEED_MANAGEMENT", "WEED_MANAGEMENT", "Maize"),

    # ==========================================================
    # CLIMATE / SUSTAINABILITY
    # ==========================================================

    ("CLIM-1", "What is climate-smart agriculture?", "CLIMATE_SMART_AGRICULTURE", "CLIMATE_SMART_AGRICULTURE", None),
    ("SUST-1", "What are sustainable farming practices?", "SUSTAINABLE_AGRICULTURE", "SUSTAINABLE_AGRICULTURE", None),

    # ==========================================================
    # POST-HARVEST / LIVESTOCK / EXTENSION
    # ==========================================================

    ("POST-1", "What is post-harvest handling?", "POST_HARVEST_HANDLING", "POST_HARVEST_HANDLING", None),
    ("LIVE-1", "How can I integrate livestock with crop farming?", "LIVESTOCK_INTEGRATION", "LIVESTOCK_INTEGRATION", None),
    ("EXT-1", "What are agricultural extension services?", "AGRICULTURAL_EXTENSION", "AGRICULTURAL_EXTENSION", None),

    # ==========================================================
    # PEST / DISEASE DIAGNOSIS
    # ==========================================================

    ("DIAG-1", "How can I diagnose crop pests and diseases?", "PEST_DISEASE_DIAGNOSIS", "PEST_DISEASE_DIAGNOSIS", None),
]


def run_tests():

    passed = 0
    failed = 0

    print("=" * 70)
    print("Masini Barokɛla V5 Intent Regression Test")
    print("=" * 70)

    for test_id, question, expected_intent, expected_domain, expected_crop in TESTS:

        result = detect_intent_v5(question)

        actual_intent = result["sub_intent"]
        actual_domain = result["domain"]
        actual_crop = result["crop"]

        intent_ok = actual_intent == expected_intent
        domain_ok = actual_domain == expected_domain
        crop_ok = actual_crop == expected_crop

        if intent_ok and domain_ok and crop_ok:

            passed += 1

            print(
                f"PASS | {test_id} | "
                f"Intent={actual_intent} | "
                f"Domain={actual_domain} | "
                f"Crop={actual_crop} | "
                f"{question}"
            )

        else:

            failed += 1

            print(
                f"FAIL | {test_id} | "
                f"Expected=({expected_intent}, {expected_domain}, {expected_crop}) | "
                f"Actual=({actual_intent}, {actual_domain}, {actual_crop}) | "
                f"{question}"
            )

    total = len(TESTS)
    accuracy = (passed / total) * 100

    print()
    print("=" * 70)
    print("SUMMARY")
    print("=" * 70)
    print(f"Passed:   {passed}/{total}")
    print(f"Failed:   {failed}/{total}")
    print(f"Accuracy: {accuracy:.1f}%")
    print("=" * 70)


if __name__ == "__main__":
    run_tests()