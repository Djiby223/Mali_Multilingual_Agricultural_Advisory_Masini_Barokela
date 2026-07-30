from utils.search import search_question

from utils.classifier import (
    is_greeting,
    is_agriculture_question,
)

from datetime import datetime

from utils.history import save_conversation

import streamlit as st

st.set_page_config(page_title="Masini Barokela", page_icon="🌾")

# ---------------------------
# Language Selection
# ---------------------------
language = st.sidebar.selectbox(
    "Choose language / Choisir la langue / Kan kan",
    ["English", "Français", "Bamanankan"]
)

# ---------------------------
# Conversation History
# ---------------------------

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []
# ---------------------------
# Translations
# ---------------------------
TEXT = {
    "English": {
        "title": "🌾 Masini Barokela",
        "subtitle": "Multilingual Agricultural Advisory Chatbot for Mali",
        "crop": "Select a crop",
        "question": "Ask your agricultural question",
        "button": "Get advice"
    },
    "Français": {
        "title": "🌾 Masini Barokela",
        "subtitle": "Assistant agricole multilingue pour le Mali",
        "crop": "Choisissez une culture",
        "question": "Posez votre question agricole",
        "button": "Obtenir un conseil"
    },
    "Bamanankan": {
        "title": "🌾 Masini Barokela",
        "subtitle": "Mali ka senekɛlaw ka barokɛla",
        "crop": "Bii min sugandi",
        "question": "I ka senekɛlɛla kumakan don",
        "button": "Baro sɔrɔ"
    }
}

t = TEXT[language]

# ---------------------------
# Simple Agricultural Knowledge Base
# ---------------------------
ADVICE = {
    "Millet": {
        "English": "Plant with the onset of reliable rains and keep the field weed-free during the first weeks.",
        "Français": "Semez dès l'installation des pluies régulières et désherbez pendant les premières semaines.",
        "Bamanankan": "Aw ye sumaya siri ni sanji ka kɛɲɛ ye, aw ka foro jɔsi kɛ fɔlɔ dɔw la."
    },
    "Sorghum": {
        "English": "Use drought-tolerant varieties and apply organic manure when available.",
        "Français": "Utilisez des variétés tolérantes à la sécheresse et apportez du fumier organique si possible.",
        "Bamanankan": "Aw ye jiri min bɛ se ka jɛgɛya munu kɛ, ani aw ye nɔgɔman bɔ."
    },
    "Rice": {
        "English": "Maintain good water management and use healthy seed.",
        "Français": "Assurez une bonne gestion de l'eau et utilisez des semences saines.",
        "Bamanankan": "Ji labɛnni kɛ ka ɲɛ, ani aw ye si min ka kɛnɛ ye kɛ."
    },
    "Maize": {
        "English": "Plant early with the rains and fertilize according to local recommendations.",
        "Français": "Semez tôt avec les pluies et fertilisez selon les recommandations locales.",
        "Bamanankan": "Aw ye sumaya siri ni sanji ye, ani aw ye nɔgɔya kɛ i ka duguya fɔli la."
    },
    "Cotton": {
        "English": "Use certified seed and monitor pests regularly.",
        "Français": "Utilisez des semences certifiées et surveillez régulièrement les ravageurs.",
        "Bamanankan": "Aw ye si tɔgɔsɛbɛnna kɛ, ani aw ye nɔgɔjuguya lajɛ waati bɛɛ."
    }
}

# ---------------------------
# Interface
# ---------------------------
st.title(t["title"])
st.write(t["subtitle"])

crop = st.selectbox(t["crop"], list(ADVICE.keys()))
question = st.text_area(t["question"])

if st.button(t["button"]):

    if not question.strip():

        st.warning("Please enter a question.")

    elif is_greeting(question):

        st.success(
            "Hello! 👋\n\nWelcome to Masini Barokɛla.\n\nI answer agricultural questions."
        )

    else:

        result, score = search_question(question, language)

        if result:

            st.success(f"Match confidence: {score:.0f}%")

            if language == "English":
                answer = result["english"]["answer"]

            elif language == "Français":
                answer = result["french"]["answer"]

            else:
                answer = result["bambara"]["answer"]

            st.info(answer)

            chat_entry = {
                "question": question,
                "answer": answer,
                "score": score,
                "language": language,
                "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }

            st.session_state.chat_history.append(chat_entry)

            save_conversation(chat_entry)

    else:

        if language == "English":
            st.error("Sorry, I couldn't find an answer.")

        elif language == "Français":
            st.error("Désolé, je n'ai pas trouvé de réponse.")

        else:
            st.error("A hakɛ to, n ma se ka jaabi sɔrɔ.")
    
    
