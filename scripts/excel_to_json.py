"""
Masini Barokɛla
Excel → JSON Converter (Version 1)

Reads the Master Knowledge Base Excel workbook and converts
every row into a JSON object.

The script automatically detects the workbook columns so it
works even if the column names change slightly.

Author: Masini Barokɛla Project
"""

import json
from pathlib import Path

import pandas as pd


# ---------------------------------------------------------
# Project paths
# ---------------------------------------------------------

PROJECT_ROOT = Path(__file__).resolve().parent.parent

EXCEL_FILE = PROJECT_ROOT / "data" / "Masini_Barokela_Master_Knowledge_Base.xlsx"

OUTPUT_FILE = PROJECT_ROOT / "data" / "masini_barokela.json"


# ---------------------------------------------------------
# Read workbook
# ---------------------------------------------------------

print("Reading workbook...")

df = pd.read_excel(EXCEL_FILE, engine="openpyxl") 

print(f"Found {len(df)} records.\n")

print("Workbook columns:")

for i, col in enumerate(df.columns, start=1):
    print(f"{i}. {col}")

print()


# ---------------------------------------------------------
# Helper function
# ---------------------------------------------------------

def find_column(*possible_names):
    """
    Returns the first matching column name.

    Search is case-insensitive.
    """

    lower = {c.lower(): c for c in df.columns}

    for name in possible_names:
        if name.lower() in lower:
            return lower[name.lower()]

    return None


# ---------------------------------------------------------
# Locate workbook columns
# ---------------------------------------------------------

id_col = find_column("ID", "Id", "Number", "No", "No.")

category_col = find_column("Category")

english_question_col = find_column(
    "English Question",
    "Question English",
    "Question_EN",
    "English"
)

english_answer_col = find_column(
    "English Answer",
    "Answer English",
    "Answer_EN"
)

french_question_col = find_column(
    "French Question",
    "Question French",
    "Question_FR"
)

french_answer_col = find_column(
    "French Answer",
    "Answer French",
    "Answer_FR"
)

bambara_question_col = find_column(
    "Bambara Question",
    "Question Bambara",
    "Question_BM",
    "Bamanankan Question"
)

bambara_answer_col = find_column(
    "Bambara Answer",
    "Answer Bambara",
    "Answer_BM",
    "Bamanankan Answer"
)


# ---------------------------------------------------------
# Convert workbook
# ---------------------------------------------------------

records = []

for index, row in df.iterrows():

    record = {

        "id": int(row[id_col]) if id_col else index + 1,

        "category": (
            row[category_col]
            if category_col
            else "Unknown"
        ),

        "english": {
            "question": (
                row[english_question_col]
                if english_question_col
                else ""
            ),
            "answer": (
                row[english_answer_col]
                if english_answer_col
                else ""
            )
        },

        "french": {
            "question": (
                row[french_question_col]
                if french_question_col
                else ""
            ),
            "answer": (
                row[french_answer_col]
                if french_answer_col
                else ""
            )
        },

        "bambara": {
            "question": (
                row[bambara_question_col]
                if bambara_question_col
                else ""
            ),
            "answer": (
                row[bambara_answer_col]
                if bambara_answer_col
                else ""
            )
        }

    }

    records.append(record)


# ---------------------------------------------------------
# Save JSON
# ---------------------------------------------------------

OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)

with open(
    OUTPUT_FILE,
    "w",
    encoding="utf-8"
) as f:

    json.dump(
        records,
        f,
        indent=4,
        ensure_ascii=False
    )

print("----------------------------------------")
print("Conversion completed successfully!")
print(f"Records exported : {len(records)}")
print(f"JSON saved to    : {OUTPUT_FILE}")
print("----------------------------------------")
