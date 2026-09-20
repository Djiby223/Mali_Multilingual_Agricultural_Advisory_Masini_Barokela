"""
Masini Barokɛla
N’Ko Challenge — NKO-10

Controlled KB Retrieval

Purpose:
    Retrieve actual Masini Barokɛla knowledge-base records
    for validated N’Ko Concept_ID mappings.

This module is experimental.

It does NOT:
    - accept arbitrary N’Ko text
    - perform linguistic interpretation
    - perform fuzzy matching
    - call the production V5.3/V5.4 search engine
    - modify search_question_v5_2
    - modify app.py
    - change production retrieval logic
"""

import csv
from pathlib import Path

from utils.nko_v5_concept_mapper import map_concept_ids


KB_FILE = (
    Path(__file__).resolve().parent.parent
    / "data"
    / "Masini_Barokela_Master_Knowledge_Base.tsv"
)


def load_knowledge_base():
    """Load the complete Masini Barokɛla knowledge base."""

    with KB_FILE.open(
        "r",
        encoding="utf-8",
        newline="",
    ) as handle:

        reader = csv.DictReader(handle, delimiter="\t")

        required_columns = {
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
        }

        if not required_columns.issubset(reader.fieldnames or []):
            raise ValueError(
                "Invalid Masini Barokɛla knowledge-base columns"
            )

        return list(reader)


def retrieve_concept_records(concept_ids):
    """
    Retrieve complete knowledge-base records for validated
    N’Ko Concept_ID values.
    """

    mapping_result = map_concept_ids(concept_ids)

    if mapping_result["status"] != "MAPPED":
        return {
            "status": "NO_RETRIEVAL",
            "record_count": 0,
            "records": [],
        }

    kb_records = load_knowledge_base()
    records = []

    for mapping in mapping_result["mappings"]:

        category = mapping["kb_category"]

        matching_records = [
            row
            for row in kb_records
            if row["Category"] == category
        ]

        records.extend(matching_records)

    return {
        "status": "RETRIEVED" if records else "NO_RETRIEVAL",
        "record_count": len(records),
        "records": records,
    }


if __name__ == "__main__":

    examples = [
        ["AGRI-WATER"],
        ["AGRI-SOIL-EARTH"],
        ["AGRI-SEED"],
        ["UNKNOWN-CONCEPT"],
        [],
    ]

    for concept_ids in examples:
        print("=" * 60)
        print(f"Concept IDs: {concept_ids}")
        print(retrieve_concept_records(concept_ids))
