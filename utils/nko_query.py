"""
Masini Barokɛla
N’Ko Challenge — NKO-06

N’Ko Query Recognition Prototype

Purpose:
    Detect N’Ko queries and identify known lexical forms.

This module is experimental.
It does NOT modify the V5.3/V5.4 production search engine.
"""

from pathlib import Path

import pandas as pd

from utils.nko_detector import detect_script


SENSE_MAP_FILE = Path("data/nko_sense_map.tsv")


def load_sense_map():
    if not SENSE_MAP_FILE.exists():
        raise FileNotFoundError(
            f"Missing N’Ko sense map: {SENSE_MAP_FILE}"
        )

    return pd.read_csv(
        SENSE_MAP_FILE,
        sep="\t",
        dtype=str,
        keep_default_na=False,
    )


def recognize_nko_query(text):
    """
    Analyze a query at the script and lexical levels.

    Returns a dictionary containing:
        script
        recognized_forms
        possible_concepts
    """

    if not text or not text.strip():
        return {
            "script": "UNKNOWN",
            "recognized_forms": [],
            "possible_concepts": [],
        }

    script = detect_script(text)

    if script != "NKO":
        return {
            "script": script,
            "recognized_forms": [],
            "possible_concepts": [],
        }

    df = load_sense_map()

    recognized_forms = []
    possible_concepts = []

    for _, row in df.iterrows():
        nko_form = row["NKo"]

        if nko_form in text:
            recognized_forms.append(
                {
                    "Lexical_Form_ID": row["Lexical_Form_ID"],
                    "NKo": nko_form,
                    "Latin_Transliteration": row[
                        "Latin_Transliteration"
                    ],
                }
            )

            possible_concepts.append(
                {
                    "Sense_ID": row["Sense_ID"],
                    "Meaning": row["Meaning"],
                    "Domain": row["Domain"],
                    "Concept_ID": row["Concept_ID"],
                }
            )

    return {
        "script": script,
        "recognized_forms": recognized_forms,
        "possible_concepts": possible_concepts,
    }


if __name__ == "__main__":
    print("NKO-06 — N’Ko Query Recognition Prototype")
    print("=" * 60)

    examples = [
        "ߛߌ",
        "ߖߌ",
        "ߓߊ߲߬ߞߎ",
        "ߘߎ߰ߞߟߏ",
        "Hello",
    ]

    for query in examples:
        result = recognize_nko_query(query)

        print()
        print(f"Query: {query}")
        print(f"Script: {result['script']}")
        print(
            f"Recognized forms: "
            f"{len(result['recognized_forms'])}"
        )
        print(
            f"Possible concepts: "
            f"{len(result['possible_concepts'])}"
        )