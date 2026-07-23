from pathlib import Path
import pandas as pd
import json

PROJECT_ROOT = Path(__file__).resolve().parent.parent

INPUT_FILE = PROJECT_ROOT / "data" / "Masini_Barokela_Master_Knowledge_Base.xlsx"
OUTPUT_FILE = PROJECT_ROOT / "data" / "masini_barokela.json"

print("=" * 60)
print("Masini Barokɛla TSV → JSON Converter")
print("=" * 60)

print("Reading:", INPUT_FILE)

# Read the TSV (tab-separated) file
df = pd.read_csv(INPUT_FILE, sep="\t", dtype=str)

print(f"{len(df)} records found.")

records = []

for _, row in df.iterrows():

    record = {
        "id": row.get("ID", ""),
        "category": row.get("Category", ""),
        "crop": row.get("Crop", ""),

        "english": {
            "question": row.get("English Question", ""),
            "answer": row.get("English Answer", "")
        },

        "french": {
            "question": row.get("French Question", ""),
            "answer": row.get("French Answer", "")
        },

        "bambara": {
            "question": row.get("Bambara Question", ""),
            "answer": row.get("Bambara Answer", "")
        },

        "keywords": row.get("Keywords", ""),
        "source": row.get("Source", ""),
        "status": row.get("Status", ""),
        "version": row.get("Version", ""),
        "last_updated": row.get("Last Updated", "")
    }

    records.append(record)

with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
    json.dump(records, f, ensure_ascii=False, indent=4)

print()
print("SUCCESS!")
print(f"{len(records)} records exported.")
print("Saved to:")
print(OUTPUT_FILE)