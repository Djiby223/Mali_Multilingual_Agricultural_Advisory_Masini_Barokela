from utils.search_v5_2 import search_question_v5_2

tests = [
    ("EN-P1", "When should I plant millet?", "1"),
    ("EN-P2", "When is the right time to sow maize?", "2"),
    ("EN-P3", "How deep should millet seeds be planted?", "3"),
    ("EN-P4", "How far apart should maize plants be?", "4"),
    ("EN-P5", "What spacing is recommended for maize?", "4"),
    ("EN-P6", "At what depth should I sow millet?", "3"),

    ("FR-1", "Quelle est la meilleure période pour planter le mil ?", "1"),
    ("FR-2", "Quand faut-il planter le maïs ?", "2"),
    ("FR-3", "À quelle profondeur faut-il semer le mil ?", "3"),
    ("FR-4", "Quel espacement faut-il laisser entre les plants de maïs ?", "4"),

    ("BM-1", "Ɲɔ ka kan ka dan tuma jumɛn?", "1"),
    ("BM-2", "Kaba ka kan ka dan tuma jumɛn?", "2"),
    ("BM-3", "Ɲɔ danni dingɛ jate ye jumɛn ye?", "3"),
    ("BM-4", "Jate jumɛn ka kan ka kɛ kaba siraw ni nɔgɔn cɛ?", "4"),

    ("NEG-1", "How do I operate a tractor?", "NONE"),
    ("NEG-2", "What is the price of a tractor?", "NONE"),
    ("NEG-3", "How do I repair a car engine?", "NONE"),
    ("NEG-4", "What is the capital of Mali?", "NONE"),
]

print("=" * 100)
print("MASINI BAROKƐLA V5.2 — EXPANDED CONTROLLED SUITE")
print("=" * 100)

passed = 0
failed = 0

for label, question, expected in tests:
    result, score = search_question_v5_2(question)

    if result:
        actual = result.get("id")
        crop = result.get("crop")
    else:
        actual = "NONE"
        crop = "-"

    status = "PASS" if actual == expected else "FAIL"

    if status == "PASS":
        passed += 1
    else:
        failed += 1

    print(
        f"{label:7} | "
        f"{question:65} | "
        f"ID={actual:4} | "
        f"Crop={str(crop):8} | "
        f"Score={score:5.1f} | "
        f"{status}"
    )

print("=" * 100)
print(f"TOTAL: {len(tests)} | PASSED: {passed} | FAILED: {failed}")
print("=" * 100)
