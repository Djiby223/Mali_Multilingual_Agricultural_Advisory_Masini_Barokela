"""
Masini Barokɛla
Multilingual Search Engine
"""

from utils.loader import load_knowledge_base


def search_question(user_question, language):
    """
    Search the knowledge base using the selected language.

    Parameters
    ----------
    user_question : str
        Question entered by the user.

    language : str
        English, Français or Bamanankan

    Returns
    -------
    dict | None
    """

    data = load_knowledge_base()

    user_question = user_question.lower().strip()

    for record in data:

        if language == "English":
            question = record["english"]["question"].lower()

        elif language == "Français":
            question = record["french"]["question"].lower()

        else:
            question = record["bambara"]["question"].lower()

        if user_question in question:
            return record

    return None