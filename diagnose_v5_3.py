from utils.intent_v5 import detect_intent_v5
from utils.search_v5_2 import (
    load_knowledge_base_v5,
    search_question_v5_2,
)


tests = [
    (
        "EN",
        "English",
        "How much distance should there be between maize plants?",
    ),
    (
        "FR",
        "Français",
        "Quand faut-il planter le mil ?",
    ),
    (
        "FR",
        "Français",
        "Quelle est la période recommandée pour planter le maïs ?",
    ),
]


print("=" * 75)
print("V5.3 DIAGNOSTIC")
print("=" * 75)

d = load_knowledge_base_v5()

for code, language, question in tests:

    print()
    print("-" * 75)
    print(code, "|", language)
    print("QUESTION:", question)
    print("-" * 75)

    intent = detect_intent_v5(question)

    print("INTENT:", intent)

    record, score = search_question_v5_2(
        question,
        language=language,
    )

    print("SEARCH RECORD:", record)
    print("SEARCH SCORE:", score)

print()
print("=" * 75)
print("END DIAGNOSTIC")
print("=" * 75)