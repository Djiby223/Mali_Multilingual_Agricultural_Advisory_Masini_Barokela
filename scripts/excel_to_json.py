import json
from pathlib import Path

import pandas as pd

# --------------------------------------------------
# Project paths
# --------------------------------------------------

PROJECT_ROOT = Path(__file__).resolve().parent.parent

EXCEL_FILE = PROJECT_ROOT / "data" / "Masini_Barokela_Master_Knowledge_Base.xlsx"

JSON_FILE = PROJECT_ROOT / "data" / "masini_barokela.json"

print("=" * 60)
print("Masini Barokɛla Excel → JSON Converter")
print("=" * 60)

print(f"Workbook: {EXCEL_FILE}")

# --------------------------------------------------
# Read workbook
# --------------------------------------------------

df = pd.read_excel(
    EXCEL_FILE,
    engine="openpyxl"
)

print(f"Rows loaded: {len(df)}")
print()

knowledge = []

# --------------------------------------------------
# Convert rows
# --------------------------------------------------

for _, row in df.iterrows():

    record = {
        "id": int(row["ID"]),
        "category": str(row["Category"]),

        "english": {
            "question": str(row["English Question"]),
            "answer": str(row["English Answer"])
        },

        "french": {
            "question": str(row["French Question"]),
            "answer": str(row["French Answer"])
        },

        "bambara": {
            "question": str(row["Bambara Question"]),
            "answer": str(row["Bambara Answer"])
        },

        "crop": str(row["Crop"]),
        "region": str(row["Region"]),
        "season": str(row["Season"])
    }

    knowledge.append(record)

# --------------------------------------------------
# Save JSON
# --------------------------------------------------

with open(JSON_FILE, "w", encoding="utf-8") as f:

    json.dump(
        knowledge,
        f,
        indent=4,
        ensure_ascii=False
    )

print()
print("SUCCESS!")
print(f"{len(knowledge)} records exported.")
print()
print("JSON created:")
print(JSON_FILE)