"""
Masini Barokɛla V5.0
Knowledge Base Audit

Purpose:
    Audit the current master TSV knowledge base
    without modifying the source data.
"""

from pathlib import Path
import pandas as pd


# --------------------------------------------------
# Project paths
# --------------------------------------------------

PROJECT_ROOT = Path(__file__).resolve().parent.parent

INPUT_FILE = (
    PROJECT_ROOT
    / "data"
    / "Masini_Barokela_Master_Knowledge_Base.tsv"
)


# --------------------------------------------------
# Expected schema
# --------------------------------------------------

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


# --------------------------------------------------
# Load data
# --------------------------------------------------

print("=" * 70)
print("Masini Barokɛla V5.0 — Knowledge Base Audit")
print("=" * 70)

print(f"\nReading:\n{INPUT_FILE}")

df = pd.read_csv(
    INPUT_FILE,
    sep="\t",
    encoding="utf-8",
)


# --------------------------------------------------
# Basic information
# --------------------------------------------------

print("\n" + "-" * 70)
print("1. BASIC INFORMATION")
print("-" * 70)

print(f"Rows:    {len(df)}")
print(f"Columns: {len(df.columns)}")


# --------------------------------------------------
# Schema validation
# --------------------------------------------------

print("\n" + "-" * 70)
print("2. SCHEMA CHECK")
print("-" * 70)

missing_columns = [
    col for col in EXPECTED_COLUMNS
    if col not in df.columns
]

unexpected_columns = [
    col for col in df.columns
    if col not in EXPECTED_COLUMNS
]

if not missing_columns and not unexpected_columns:
    print("✓ Schema is correct.")

else:
    if missing_columns:
        print("Missing columns:")
        for col in missing_columns:
            print(f"  - {col}")

    if unexpected_columns:
        print("Unexpected columns:")
        for col in unexpected_columns:
            print(f"  - {col}")


# --------------------------------------------------
# ID check
# --------------------------------------------------

print("\n" + "-" * 70)
print("3. ID CHECK")
print("-" * 70)

duplicate_ids = df[df["ID"].duplicated(keep=False)]

if duplicate_ids.empty:
    print("✓ No duplicate IDs.")

else:
    print("⚠ Duplicate IDs found:")
    print(duplicate_ids["ID"].tolist())


# --------------------------------------------------
# Required text fields
# --------------------------------------------------

required_text_fields = [
    "English Question",
    "English Answer",
    "French Question",
    "French Answer",
    "Bambara Question",
    "Bambara Answer",
]


print("\n" + "-" * 70)
print("4. REQUIRED TEXT FIELDS")
print("-" * 70)

for column in required_text_fields:

    missing = df[column].isna().sum()

    empty = (
        df[column]
        .fillna("")
        .astype(str)
        .str.strip()
        .eq("")
        .sum()
    )

    print(
        f"{column}: "
        f"missing={missing}, "
        f"empty={empty}"
    )


# --------------------------------------------------
# Metadata coverage
# --------------------------------------------------

print("\n" + "-" * 70)
print("5. METADATA COVERAGE")
print("-" * 70)

metadata_fields = [
    "Crop",
    "Region",
    "Season",
]

for column in metadata_fields:

    populated = df[column].notna().sum()
    missing = df[column].isna().sum()

    print(
        f"{column}: "
        f"populated={populated}, "
        f"missing={missing}"
    )


# --------------------------------------------------
# Categories
# --------------------------------------------------

print("\n" + "-" * 70)
print("6. CATEGORIES")
print("-" * 70)

print(
    df["Category"]
    .value_counts(dropna=False)
    .to_string()
)


# --------------------------------------------------
# Crops
# --------------------------------------------------

print("\n" + "-" * 70)
print("7. CROPS")
print("-" * 70)

print(
    df["Crop"]
    .value_counts(dropna=False)
    .to_string()
)


# --------------------------------------------------
# Duplicate questions
# --------------------------------------------------

print("\n" + "-" * 70)
print("8. DUPLICATE QUESTIONS")
print("-" * 70)

for column in [
    "English Question",
    "French Question",
    "Bambara Question",
]:

    duplicates = df[df[column].duplicated(keep=False)]

    if duplicates.empty:
        print(f"✓ No duplicates: {column}")

    else:
        print(
            f"⚠ Duplicate questions in {column}: "
            f"{len(duplicates)} rows"
        )


# --------------------------------------------------
# Final summary
# --------------------------------------------------

print("\n" + "=" * 70)
print("AUDIT COMPLETE")
print("=" * 70)