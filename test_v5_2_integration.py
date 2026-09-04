from utils.intent_v5 import detect_intent_v5
from utils.search_v5_2 import search_question_v5_2


# ============================================================
# Masini Barokɛla V5.2 End-to-End Integration Test
# ============================================================

TESTS = [

    # --------------------------------------------------------
    # English
    # --------------------------------------------------------
    {
        "id": "EN-01",
        "language": "English",
        "question": "When should I plant millet?",
        "expected_id": "1",
        "expected_intent": "PLANTING_TIME",
        "expected_crop": "Millet",
    },
    {
        "id": "EN-02",
        "language": "English",
        "question": "When is the right time to sow maize?",
        "expected_id": "2",
        "expected_intent": "PLANTING_TIME",
        "expected_crop": "Maize",
    },
    {
        "id": "EN-03",
        "language": "English",
        "question": "How deep should millet seeds be planted?",
        "expected_id": "3",
        "expected_intent": "PLANTING_DEPTH",
        "expected_crop": "Millet",
    },
    {
        "id": "EN-04",
        "language": "English",
        "question": "How far apart should maize plants be?",
        "expected_id": "4",
        "expected_intent": "PLANTING_SPACING",
        "expected_crop": "Maize",
    },
    {
        "id": "EN-05",
        "language": "English",
        "question": "Why is timely planting important?",
        "expected_id": "5",
        "expected_intent": "PLANTING_IMPORTANCE",
        "expected_crop": None,
    },
    {
       "id": "EN-06",
       "language": "English",
       "question": "When should I apply fertilizer?",
       "expected_id": "13",
       "expected_intent": "FERTILIZER_TIMING",
       "expected_crop": None,
    },
    {
        "id": "EN-07",
        "language": "English",
        "question": "How can I control pests?",
        "expected_id": None,
        "expected_intent": "PEST_CONTROL",
        "expected_crop": None,
    },
    {
        "id": "EN-08",
        "language": "English",
        "question": "How can I improve soil fertility?",
        "expected_id": "36",
        "expected_intent": "SOIL_MANAGEMENT",
        "expected_crop": None,
    },

    # --------------------------------------------------------
    # French
    # --------------------------------------------------------
    {
        "id": "FR-01",
        "language": "Français",
        "question": "Quelle est la meilleure période pour planter le mil ?",
        "expected_id": "1",
        "expected_intent": "PLANTING_TIME",
        "expected_crop": "Millet",
    },
    {
        "id": "FR-02",
        "language": "Français",
        "question": "Quelle est la meilleure période pour planter le maïs ?",
        "expected_id": "2",
        "expected_intent": "PLANTING_TIME",
        "expected_crop": "Maize",
    },
    {
        "id": "FR-03",
        "language": "Français",
        "question": "Quelle est la profondeur recommandée pour semer les graines de mil ?",
        "expected_id": "3",
        "expected_intent": "PLANTING_DEPTH",
        "expected_crop": "Millet",
    },
    {
        "id": "FR-04",
        "language": "Français",
        "question": "Quel espacement faut-il entre les plants de maïs ?",
        "expected_id": "4",
        "expected_intent": "PLANTING_SPACING",
        "expected_crop": "Maize",
    },

    # --------------------------------------------------------
    # Bambara
    # --------------------------------------------------------
    {
        "id": "BM-01",
        "language": "Bambara",
        "question": "Ɲɔ ka kan ka dan tuma jumɛn?",
        "expected_id": "1",
        "expected_intent": "GENERAL",
        "expected_crop": "Millet",
    },
    {
        "id": "BM-02",
        "language": "Bambara",
        "question": "Kaba ka kan ka dan tuma jumɛn?",
        "expected_id": "2",
        "expected_intent": "GENERAL",
        "expected_crop": "Maize",
    },
    {
        "id": "BM-03",
        "language": "Bambara",
        "question": "Ɲɔ danni dingɛ jate ye jumɛn ye?",
        "expected_id": "3",
        "expected_intent": "GENERAL",
        "expected_crop": "Millet",
    },
    {
        "id": "BM-04",
        "language": "Bambara",
        "question": "Jate jumɛn ka kan ka kɛ kaba siraw ani kaba danni dingɛw ni nɔgɔn cɛ?",
        "expected_id": "4",
        "expected_intent": "GENERAL",
        "expected_crop": "Maize",
    },

    # --------------------------------------------------------
    # Negative / off-domain
    # --------------------------------------------------------
    {
        "id": "NEG-01",
        "language": "English",
        "question": "How do I repair a tractor?",
        "expected_id": None,
        "expected_intent": None,
        "expected_crop": None,
    },
    {
        "id": "NEG-02",
        "language": "English",
        "question": "What is the capital of Mali?",
        "expected_id": None,
        "expected_intent": None,
        "expected_crop": None,
    },
]


def main():

    print("=" * 75)
    print("Masini Barokɛla V5.2 End-to-End Integration Test")
    print("=" * 75)

    passed = 0
    failed = 0

    for test in TESTS:

        question = test["question"]
        language = test["language"]

        # ----------------------------------------------------
        # Intent
        # ----------------------------------------------------

        intent_result = detect_intent_v5(question)

        actual_intent = intent_result.get("sub_intent")
        actual_crop = intent_result.get("crop")

        # ----------------------------------------------------
        # Search
        # ----------------------------------------------------

        record, score = search_question_v5_2(
            question,
            language=language,
        )

        actual_id = record.get("id") if record else None

        # ----------------------------------------------------
        # Validate
        # ----------------------------------------------------

        intent_ok = (
    	      test["expected_intent"] is None
              or actual_intent == test["expected_intent"]
        )

        crop_ok = (
            test["expected_crop"] is None
            or actual_crop == test["expected_crop"]
        )

        id_ok = actual_id == test["expected_id"]

        success = intent_ok and crop_ok and id_ok

        if success:
            passed += 1
            status = "PASS"
        else:
            failed += 1
            status = "FAIL"

        print(
            f"{status} | "
            f"{test['id']} | "
            f"{language:<9} | "
            f"Intent={actual_intent:<28} | "
            f"Crop={str(actual_crop):<8} | "
            f"Expected ID={str(test['expected_id']):<4} | "
            f"Actual ID={str(actual_id):<4} | "
            f"Score={score:<5} | "
            f"{question}"
        )

    total = len(TESTS)
    accuracy = (passed / total * 100) if total else 0

    print()
    print("=" * 75)
    print("SUMMARY")
    print("=" * 75)
    print(f"Passed:   {passed}/{total}")
    print(f"Failed:   {failed}/{total}")
    print(f"Accuracy: {accuracy:.1f}%")
    print("=" * 75)

    if failed:
        raise SystemExit(1)


if __name__ == "__main__":
    main()