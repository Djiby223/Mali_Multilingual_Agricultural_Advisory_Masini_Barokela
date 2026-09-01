from utils.intent_v5 import detect_intent_v5
from utils.search_v5_2 import (
    load_knowledge_base_v5,
    filter_candidates,
    meaningful_tokens,
    normalize_text,
    LANGUAGE_KEYS,
    INTENT_TO_CATEGORY,
)
from rapidfuzz import fuzz


question = "How much distance should there be between maize plants?"
language = "English"

print("=" * 75)
print("V5.3 MB-V53-001 CANDIDATE DIAGNOSTIC")
print("=" * 75)

intent_result = detect_intent_v5(question)

print("\nQUERY:")
print(question)

print("\nDETECTED INTENT:")
print(intent_result)

sub_intent = intent_result["sub_intent"]
crop = intent_result["crop"]

category = INTENT_TO_CATEGORY.get(sub_intent)

print("\nCATEGORY:", category)
print("CROP:", crop)

data = load_knowledge_base_v5()

candidates = filter_candidates(
    data,
    category,
    crop,
)

print("\nCANDIDATE COUNT:", len(candidates))

language_key = LANGUAGE_KEYS.get(language, "english")

user_normalized = normalize_text(question)
user_tokens = meaningful_tokens(
    user_normalized,
    language_key,
)

print("\nUSER TOKENS:")
print(user_tokens)

print("\n" + "-" * 75)
print("CANDIDATES")
print("-" * 75)

results = []

for record in candidates:

    language_data = record.get(language_key, {})
    candidate_question = language_data.get("question")

    if not candidate_question:
        continue

    candidate_normalized = normalize_text(candidate_question)

    wratio = fuzz.WRatio(
        user_normalized,
        candidate_normalized,
    )

    token_similarity = fuzz.token_set_ratio(
        user_normalized,
        candidate_normalized,
    )

    candidate_tokens = meaningful_tokens(
        candidate_normalized,
        language_key,
    )

    if user_tokens:
        overlap = user_tokens & candidate_tokens
        coverage = (
            len(overlap) / len(user_tokens)
        ) * 100
    else:
        coverage = 0

    score = (
        (wratio * 0.45)
        + (token_similarity * 0.25)
        + (coverage * 0.30)
    )

    candidate_intent = detect_intent_v5(
        candidate_question
    ).get("sub_intent")

    results.append(
        (
            score,
            record.get("id"),
            record.get("crop"),
            record.get("category"),
            candidate_intent,
            candidate_question,
        )
    )


results.sort(reverse=True, key=lambda x: x[0])

for item in results[:10]:

    score, record_id, record_crop, record_category, candidate_intent, candidate_question = item

    print("\nID:", record_id)
    print("Crop:", record_crop)
    print("Category:", record_category)
    print("Candidate Intent:", candidate_intent)
    print("Score:", round(score, 1))
    print("Question:", candidate_question)

print("\n" + "=" * 75)
print("END DIAGNOSTIC")
print("=" * 75)