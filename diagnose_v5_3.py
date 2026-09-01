from utils.intent_v5 import detect_intent_v5
from utils.search_v5_2 import search_question_v5_2


tests = [
    (
        "EN",
        "How much distance should there be between maize plants?",
        "English",
    ),
    (
        "FR",
        "Quand faut-il planter le mil ?",
        "Français",
    ),
    (
        "FR",
        "Quelle est la période recommandée pour planter le maïs ?",
        "Français",
    ),
]


print("=" * 75)
print("V5.3 TARGETED DIAGNOSTIC — MB-V53-001")
print("=" * 75)


for lang, question, language in tests:

    print()
    print("-" * 75)
    print(f"{lang} | {language}")
    print(f"QUESTION: {question}")
    print("-" * 75)

    intent = detect_intent_v5(question)

    print("INTENT:", intent)

    record, score = search_question_v5_2(
        question,
        language=language,
    )

    if record:
        print("SEARCH RECORD:", record.get("id"))
        print("SEARCH CROP:", record.get("crop"))
        print("SEARCH CATEGORY:", record.get("category"))
    else:
        print("SEARCH RECORD: None")

    print("SEARCH SCORE:", score)


print()
print("=" * 75)
print("END DIAGNOSTIC")
print("=" * 75)