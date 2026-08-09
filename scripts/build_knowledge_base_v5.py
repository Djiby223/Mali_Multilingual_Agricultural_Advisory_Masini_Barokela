"""
Masini Barokɛla V5.0
Knowledge Base Builder

Reads the existing master TSV and creates a clean,
structured V5.0 JSON knowledge base.

IMPORTANT:
This script does NOT modify the source TSV.
"""

from pathlib import Path
import json
import pandas as pd


# ============================================================
# PATHS
# ============================================================

PROJECT_ROOT = Path(__file__).resolve().parent.parent

INPUT_FILE = (
    PROJECT_ROOT
    / "data"
    / "Masini_Barokela_Master_Knowledge_Base.tsv"
)

OUTPUT_FILE = (
    PROJECT_ROOT
    / "data"
    / "knowledge_base_v5.json"
)


# ============================================================
# EXPECTED SOURCE COLUMNS
# ============================================================

EXPECTED_COLUMNS = [
    "ID",
    "Category",
    "English Question",
    "English Answer",
    "French Question",
    "French Answer",
    "Bambara Question",
    "Bambara Answer",
    "Crop",
    "Region",
    "Season",
]


# ============================================================
# HELPERS
# ============================================================

def clean_value(value):
    """Convert pandas missing values to Python None."""

    if pd.isna(value):
        return None

    if isinstance(value, str):
        value = value.strip()

        if value == "":
            return None

    return value


# ============================================================
# LOAD SOURCE
# ============================================================

print("=" * 70)
print("Masini Barokɛla V5.0 — Knowledge Base Builder")
print("=" * 70)

print(f"\nInput:")
print(INPUT_FILE)

df = pd.read_csv(
    INPUT_FILE,
    sep="\t",
    encoding="utf-8",
)


# ============================================================
# VALIDATE SCHEMA
# ============================================================

missing_columns = [
    column
    for column in EXPECTED_COLUMNS
    if column not in df.columns
]

if missing_columns:
    raise ValueError(
        f"Missing required columns: {missing_columns}"
    )


# ============================================================
# BUILD RECORDS
# ============================================================

records = []

for _, row in df.iterrows():

    record = {
        "id": str(row["ID"]),
        "category": clean_value(row["Category"]),
        "topic": None,

        "crop": clean_value(row["Crop"]),
        "region": clean_value(row["Region"]),
        "agroecological_zone": None,
        "season": clean_value(row["Season"]),

        "english": {
            "question": clean_value(row["English Question"]),
            "answer": clean_value(row["English Answer"]),
        },

        "french": {
            "question": clean_value(row["French Question"]),
            "answer": clean_value(row["French Answer"]),
        },

        "bambara": {
            "question": clean_value(row["Bambara Question"]),
            "answer": clean_value(row["Bambara Answer"]),
        },

        "intent": None,
        "keywords": [],

        "source": None,
        "source_type": None,

        "status": "review",
        "version": "5.0",
        "last_updated": None,
    }

    # --------------------------------------------------------
    # Known translation-review item
    # --------------------------------------------------------

    if record["id"] == "60":
        record["status"] = "translation_review"

    records.append(record)


# ============================================================
# WRITE JSON
# ============================================================

with open(
    OUTPUT_FILE,
    "w",
    encoding="utf-8",
) as f:

    json.dump(
        records,
        f,
        ensure_ascii=False,
        indent=2,
    )


# ============================================================
# SUMMARY
# ============================================================

print("\n" + "-" * 70)
print("BUILD COMPLETE")
print("-" * 70)

print(f"Records created: {len(records)}")
print(f"Output file:     {OUTPUT_FILE}")

translation_review = [
    record["id"]
    for record in records
    if record["status"] == "translation_review"
]

print(
    f"Translation review records: "
    f"{translation_review}"
)

print("\n✓ Source TSV was not modified.")
print("✓ Unicode preserved.")
print("✓ Missing values converted to null.")
print("✓ V5.0 JSON created.")