from utils.intent_v5 import detect_intent_v5
from utils.search_v5_2 import search_question_v5_2


# ============================================================
# Masini Barokɛla V5.3 Robustness Test
# Phase 1: Natural Query Variations
# ============================================================

TESTS = [

    # --------------------------------------------------------
    # English — Planting Time
    # --------------------------------------------------------
    {
        "id": "EN-RT-01",
        "language": "English",
        "question": "When should I plant millet?",
        "expected_id": "1",
    },
    {
        "id": "EN-RT-02",
        "language": "English",
        "question": "When is the best time to plant millet?",
        "expected_id": "1",
    },
    {
        "id": "EN-RT-03",
        "language": "English",
        "question": "What is the best time for planting millet?",
        "expected_id": "1",
    },
    {
        "id": "EN-RT-04",
        "language": "English",
        "question": "When do I plant millet?",
        "expected_id": "1",
    },
    {
        "id": "EN-RT-05",
        "language": "English",
        "question": "What is the recommended planting time for millet?",
        "expected_id": "1",
    },

    # --------------------------------------------------------
    # English — Planting Depth
    # --------------------------------------------------------
    {
        "id": "EN-RD-01",
        "language": "English",
        "question": "How deep should millet seeds be planted?",
        "expected_id": "3",
    },
    {
        "id": "EN-RD-02",
        "language": "English",
        "question": "What depth should I plant millet seeds?",
        "expected_id": "3",
    },
    {
        "id": "EN-RD-03",
        "language": "English",
        "question": "How deep do I sow millet?",
        "expected_id": "3",
    },
    {
        "id": "EN-RD-04",
        "language": "English",
        "question": "What is the recommended planting depth for millet?",
        "expected_id": "3",
    },

    # --------------------------------------------------------
    # English — Planting Spacing
    # --------------------------------------------------------
    {
        "id": "EN-RS-01",
        "language": "English",
        "question": "How far apart should maize plants be?",
        "expected_id": "4",
    },
    {
        "id": "EN-RS-02",
        "language": "English",
        "question": "What spacing should I use for maize?",
        "expected_id": "4",
    },
    {
        "id": "EN-RS-03",
        "language": "English",
        "question": "How much distance should there be between maize plants?",
        "expected_id": "4",
    },
    {
        "id": "EN-RS-04",
        "language": "English",
        "question": "What is the recommended spacing for maize plants?",
        "expected_id": "4",
    },

    # --------------------------------------------------------
    # French — Planting Time
    # --------------------------------------------------------
    {
        "id": "FR-RT-01",
        "language": "Français",
        "question": "Quand faut-il planter le mil ?",
        "expected_id": "1",
    },
    {
        "id": "FR-RT-02",
        "language": "Français",
        "question": "Quel est le meilleur moment pour planter le mil ?",
        "expected_id": "1",
    },
    {
        "id": "FR-RT-03",
        "language": "Français",
        "question": "À quelle période faut-il semer le maïs ?",
        "expected_id": "2",
    },
    {
        "id": "FR-RT-04",
        "language": "Français",
        "question": "Quelle est la période recommandée pour planter le maïs ?",
        "expected_id": "2",
    },

    # --------------------------------------------------------
    # French — Planting Depth
    # --------------------------------------------------------
    {
        "id": "FR-RD-01",
        "language": "Français",
        "question": "À quelle profondeur faut-il semer le mil ?",
        "expected_id": "3",
    },
    {
        "id": "FR-RD-02",
        "language": "Français",
        "question": "Quelle profondeur faut-il utiliser pour planter les graines de mil ?",
        "expected_id": "3",
    },

    # --------------------------------------------------------
    # French — Planting Spacing
    # --------------------------------------------------------
    {
        "id": "FR-RS-01",
        "language": "Français",
        "question": "À quelle distance faut-il planter les plants de maïs ?",
        "expected_id": "4",
    },
    {
        "id": "FR-RS-02",
        "language": "Français",
        "question": "Quelle distance faut-il laisser entre les plants de maïs ?",
        "expected_id": "4",
    },

    # --------------------------------------------------------
    # Bambara — Planting Time
    # --------------------------------------------------------
    {
        "id": "BM-RT-01",
        "language": "Bambara",
        "question": "Ɲɔ ka kan ka dan tuma jumɛn?",
        "expected_id": "1",
    },
    {
        "id": "BM-RT-02",
        "language": "Bambara",
        "question": "Kaba ka kan ka dan tuma jumɛn?",
        "expected_id": "2",
    },

    # --------------------------------------------------------
    # Bambara — Planting Depth
    # --------------------------------------------------------
    {
        "id": "BM-RD-01",
        "language": "Bambara",
        "question": "Ɲɔ danni dingɛ jate ye jumɛn ye?",
        "expected_id": "3",
    },

    # --------------------------------------------------------
    # Bambara — Planting Spacing
    # --------------------------------------------------------
    {
        "id": "BM-RS-01",
        "language": "Bambara",
        "question": (
            "Jate jumɛn ka kan ka kɛ kaba siraw ani "
            "kaba danni dingɛw ni nɔgɔn cɛ?"
        ),
        "expected_id": "4",
    },

    # --------------------------------------------------------
    # Negative / Out-of-domain
    # --------------------------------------------------------
    {
        "id": "NEG-R-01",
        "language": "English",
        "question": "How do I repair a tractor?",
        "expected_id": None,
    },
    {
        "id": "NEG-R-02",
        "language": "English",
        "question": "What is the price of a tractor?",
        "expected_id": None,
    },
    {
        "id": "NEG-R-03",
        "language": "English",
        "question": "How does a car engine work?",
        "expected_id": None,
    },
    {
        "id": "NEG-R-04",
        "language": "English",
        "question": "What is the capital of Mali?",
        "expected_id": None,
    },
]


# ============================================================
# Test runner
# ============================================================

print("=" * 75)
print("Masini Barokɛla V5.3 Robustness Test")
print("=" * 75)

passed = 0
failed = 0

for test in TESTS:

    question = test["question"]
    language = test["language"]
    expected_id = test["expected_id"]

    intent_result = detect_intent_v5(question)

    actual_intent = intent_result.get("sub_intent")
    actual_crop = intent_result.get("crop")

    record, score = search_question_v5_2(
        question,
        language=language,
    )

    actual_id = record.get("id") if record else None

    if expected_id is None:
        success = actual_id is None
    else:
        success = actual_id == expected_id

    status = "PASS" if success else "FAIL"

    if success:
        passed += 1
    else:
        failed += 1

    print(
        f"{status} | {test['id']} | "
        f"{language:<9} | "
        f"Intent={actual_intent:<28} | "
        f"Crop={str(actual_crop):<8} | "
        f"Expected={str(expected_id):<4} | "
        f"Actual={str(actual_id):<4} | "
        f"Score={score} | "
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