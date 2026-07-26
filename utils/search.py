"""
Masini Barokɛla
Multilingual Search Engine
"""

from utils.loader import load_knowledge_base

from utils.loader import load_knowledge_base

# Common words to ignore
STOP_WORDS = {

    # English
    "the", "is", "are", "a", "an", "to", "of",
    "for", "on", "in", "at", "by", "what",
    "when", "where", "how", "why", "can",
    "should", "do", "does", "i", "my",

    # French
    "le", "la", "les", "de", "du", "des",
    "un", "une", "et", "pour", "dans",
    "comment", "quand", "où", "est",
    "je", "mon", "ma", "mes",

    # Bambara
    "ye", "ka", "ni", "la", "be",
    "ani", "i", "aw", "n", "o"
}

def normalize(text):
    """
    Normalize text for better searching.
    """

    text = text.lower()

    for ch in ".,?!:;()[]{}\"'":
        text = text.replace(ch, " ")

    words = []

    for word in text.split():

        if word not in STOP_WORDS:

            words.append(word)

    return set(words)


def search_question(user_question, language):

    data = load_knowledge_base()

    user_words = normalize(user_question)

    best_match = None
    highest_score = 0

  for record in data:

    if language == "English":
        question = record["english"]["question"]

    elif language == "Français":
        question = record["french"]["question"]

    else:
        question = record["bambara"]["question"]

    question_words = normalize(question)

    common_words = user_words & question_words

    score = len(common_words)

    # Bonus if the beginning of the question matches
    if question.lower().startswith(user_question.lower()[:10]):
        score += 2

    # Bonus if both questions contain the same number of important words
    if len(user_words) == len(question_words):
        score += 1

    if score > highest_score:
        highest_score = score
        best_match = record

    if highest_score >= 2:
        return best_match

    return None