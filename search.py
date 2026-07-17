crop = st.selectbox(t["crop"], list(ADVICE.keys()))
crop = st.selectbox(
    t["crop"],
    [
        "General",
        "Rice",
        "Maize",
        "Millet",
        "Sorghum",
        "Cotton",
        "Groundnut",
        "Cowpea",
        "Sesame",
        "Vegetables"
    ]
)