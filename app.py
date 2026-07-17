from utils.search import search_question

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

    if question:

        result = search_question(question)

        if result:

            if language == "English":
                st.success(result["english"]["answer"])

            elif language == "Français":
                st.success(result["french"]["answer"])

            else:
                st.success(result["bambara"]["answer"])

        else:
            st.warning("No matching answer found.")

    else:
        st.warning("Please enter a question.")

st.divider()
st.caption("Version 2.0 - Multilingual support and crop-specific recommendations.")