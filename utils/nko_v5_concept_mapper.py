"""
Masini Barokɛla
N’Ko Challenge — NKO-08

N’Ko V5 Concept Mapper

Purpose:
    Map validated N’Ko Concept_ID values to experimental
    Masini Barokɛla knowledge-base categories.

This module is experimental.
It does NOT perform knowledge-base retrieval.
It does NOT modify the V5.3/V5.4 production search engine.
"""

import csv
from pathlib import Path


MAPPING_FILE = (
    Path(__file__).resolve().parent.parent
    / "data"
    / "nko_v5_concept_map.tsv"
)


def load_concept_map():
    """
    Load the experimental N’Ko → Masini Barokɛla mapping table.

    Returns:
        dict mapping NKO_CONCEPT_ID to mapping information.
    """

    mappings = {}

    with MAPPING_FILE.open(
        "r",
        encoding="utf-8",
        newline="",
    ) as handle:

        reader = csv.DictReader(handle, delimiter="\t")

        required_columns = {
            "NKO_CONCEPT_ID",
            "KB_CATEGORY",
            "KB_CROP",
            "STATUS",
            "EVIDENCE",
        }

        if not required_columns.issubset(reader.fieldnames or []):
            raise ValueError(
                "Invalid NKO-V5 concept map columns"
            )

        for row in reader:
            concept_id = row["NKO_CONCEPT_ID"]

            if not concept_id:
                continue

            mappings[concept_id] = {
                "nko_concept_id": concept_id,
                "kb_category": row["KB_CATEGORY"],
                "kb_crop": row["KB_CROP"],
                "status": row["STATUS"],
                "evidence": row["EVIDENCE"],
            }

    return mappings


def map_concept_ids(concept_ids):
    """
    Map validated N’Ko Concept_ID values to experimental
    Masini Barokɛla KB targets.

    Args:
        concept_ids: iterable of validated Concept_ID strings.

    Returns:
        dict with:
            status
            mappings
    """

    concept_map = load_concept_map()
    mappings = []

    for concept_id in concept_ids or []:

        mapping = concept_map.get(concept_id)

        if mapping and mapping not in mappings:
            mappings.append(mapping)

    status = "MAPPED" if mappings else "NO_MAPPING"

    return {
        "status": status,
        "mappings": mappings,
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
        print(map_concept_ids(concept_ids))