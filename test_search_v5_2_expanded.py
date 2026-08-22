from utils.search_v5_2 import search_question_v5_2


TESTS = [
    # English
    ("EN-P1", "When should I plant millet?", "English", "1"),
    ("EN-P2", "When is the right time to sow maize?", "English", "2"),
    ("EN-P3", "How deep should millet seeds be planted?", "English", "3"),
    ("EN-P4", "How far apart should maize plants be?", "English", "4"),
    ("EN-P5", "How much spacing should I leave between maize plants?", "English", "4"),
    ("EN-P6", "How deep should I sow millet seeds?", "English", "3"),

    # French
    ("FR-1", "Quelle est la meilleure période pour planter le mil ?", "Français", "1"),
    ("FR-2", "Quelle est la meilleure période pour planter le maïs ?", "Français", "2"),
    ("FR-3", "Quelle est la profondeur recommandée pour semer les graines de mil ?", "Français", "3"),
    ("FR-4", "Quel espacement faut-il entre les plants de maïs ?", "Français", "4"),

    # Bambara
    ("BM-1", "Ɲɔ ka kan ka dan tuma jumɛn?", "Bambara", "1"),
    ("BM-2", "Kaba ka kan ka dan tuma jumɛn?", "Bambara", "2"),
    ("BM-3", "Ɲɔ danni dingɛ jate ye jumɛn ye?", "Bambara", "3"),
    ("BM-4", "Jate jumɛn ka kan ka kɛ kaba siraw ani kaba danni dingɛw ni nɔgɔn cɛ?", "Bambara", "4"),

    # Negative tests
    ("NEG-1", "How do I repair a tractor?", "English", None),
    ("NEG-2", "What is the price of a tractor?", "English", None),
    ("NEG-3", "How does a car engine work?", "English", None),
    ("NEG-4", "What is the capital of Mali?", "English", None),
]


passed = 0
failed = 0

print("=" * 70)
print("Masini Barokɛla V5.2 Expanded Search Test")
print("=" * 70)

for test_id, question, language, expected_id in TESTS:

    result, score = search_question_v5_2(
        question,
        language=language,
    )

    actual_id = result.get("id") if result else None

    ok = actual_id == expected_id

    if ok:
        passed += 1
        status = "PASS"
    else:
        failed += 1
        status = "FAIL"

    print(
        f"{status} | {test_id} | "
        f"{language} | "
        f"Expected={expected_id} | "
        f"Actual={actual_id} | "
        f"Score={score} | "
        f"{question}"
    )

print()
print("=" * 70)
print("SUMMARY")
print("=" * 70)
print(f"Passed: {passed}/{len(TESTS)}")
print(f"Failed: {failed}/{len(TESTS)}")
print(f"Accuracy: {(passed / len(TESTS)) * 100:.1f}%")
print("=" * 70)
