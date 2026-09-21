"""
Masini Barokɛla
N’Ko Challenge — NKO-12

Controlled Answer Assembly

Purpose:
    Assemble already-retrieved Masini Barokɛla knowledge-base
    records into a language-specific, auditable answer package.

This module is experimental.

It does NOT:
    - accept arbitrary N’Ko text
    - perform N’Ko detection
    - perform linguistic interpretation
    - perform fuzzy matching
    - perform knowledge-base retrieval
    - call the production V5.3/V5.4 search engine
    - modify search_question_v5_2
    - modify app.py
    - change production retrieval logic
"""

SUPPORTED_LANGUAGES = {
    "English": {
        "question": "English Question",
        "answer": "English Answer",
    },
    "Français": {
        "question": "French Question",
        "answer": "French Answer",
    },
    "Bamanankan": {
        "question": "Bambara Question",
        "answer": "Bambara Answer",
    },
}


def assemble_answer_package(retrieval_result, language):
    """
    Assemble a language-specific answer package from an
    already-retrieved NKO-10 result.
    """

    if language not in SUPPORTED_LANGUAGES:
        return {
            "status": "NO_ANSWER_PACKAGE",
            "language": language,
            "record_count": 0,
            "answers": [],
        }

    if not isinstance(retrieval_result, dict):
        return {
            "status": "NO_ANSWER_PACKAGE",
            "language": language,
            "record_count": 0,
            "answers": [],
        }

    if retrieval_result.get("status") != "RETRIEVED":
        return {
            "status": "NO_ANSWER_PACKAGE",
            "language": language,
            "record_count": 0,
            "answers": [],
        }

    records = retrieval_result.get("records", [])

    if not records:
        return {
            "status": "NO_ANSWER_PACKAGE",
            "language": language,
            "record_count": 0,
            "answers": [],
        }

    fields = SUPPORTED_LANGUAGES[language]

    answers = []

    for record in records:
        answers.append(
            {
                "ID": record["ID"],
                "question": record[fields["question"]],
                "answer": record[fields["answer"]],
                "Crop": record["Crop"],
                "Region": record["Region"],
                "Season": record["Season"],
            }
        )

    return {
        "status": "ANSWER_PACKAGE_READY",
        "language": language,
        "record_count": len(answers),
        "answers": answers,
    }
