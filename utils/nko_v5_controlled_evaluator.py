"""
Masini Barokɛla
N’Ko Challenge — NKO-09

Controlled KB Support Evaluator

Purpose:
    Verify that validated N’Ko Concept_ID mappings are supported
    by real records in the Masini Barokɛla knowledge base.

This module is experimental.

It does NOT:
    - retrieve answers
    - call the production V5.3/V5.4 search engine
    - modify search_question_v5_2
    - modify app.py
    - perform fuzzy matching
    - perform linguistic interpretation
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
    """Load the Masini Barokɛla knowledge base."""

    with KB_FILE.open(
        "r",
        encoding="utf-8",
        newline="",
    ) as handle:

        reader = csv.DictReader(handle, delimiter="\t")

        required_columns = {
            "ID",
            "Category",
        }

        if not required_columns.issubset(reader.fieldnames or []):
            raise ValueError(
                "Invalid Masini Barokɛla knowledge-base columns"
            )

        return list(reader)


def evaluate_concept_ids(concept_ids):
    """
    Evaluate whether mapped N’Ko Concept_ID values are supported
    by real knowledge-base records.
    """

    mapping_result = map_concept_ids(concept_ids)

    if mapping_result["status"] != "MAPPED":
        return {
            "status": "NO_SUPPORT",
            "evaluations": [],
        }

    kb_records = load_knowledge_base()
    evaluations = []

    for mapping in mapping_result["mappings"]:

        category = mapping["kb_category"]

        matching_records = [
            row
            for row in kb_records
            if row["Category"] == category
        ]

        evaluations.append(
            {
                "concept_id": mapping["nko_concept_id"],
                "kb_category": category,
                "kb_crop": mapping["kb_crop"],
                "mapping_status": mapping["status"],
                "evidence": mapping["evidence"],
                "kb_record_count": len(matching_records),
                "kb_record_ids": [
                    row["ID"]
                    for row in matching_records
                ],
                "supported": bool(matching_records),
            }
        )

    overall_status = (
        "SUPPORTED"
        if evaluations
        and all(item["supported"] for item in evaluations)
        else "NO_SUPPORT"
    )

    return {
        "status": overall_status,
        "evaluations": evaluations,
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
        print(evaluate_concept_ids(concept_ids))
