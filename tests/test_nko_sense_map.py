"""
Masini Barokɛla
N’Ko Challenge — NKO-05F

Sense Validation & Consistency Tests

Purpose:
    Validate the N’Ko lexical sense mapping layer.

This module is experimental.
It does NOT modify the V5.3/V5.4 production engine.
"""

from pathlib import Path

import pandas as pd

from utils.nko_detector import is_nko_character


DATA_FILE = Path("data/nko_sense_map.tsv")


def load_data():
    assert DATA_FILE.exists(), f"Missing file: {DATA_FILE}"

    df = pd.read_csv(
        DATA_FILE,
        sep="\t",
        dtype=str,
        keep_default_na=False,
    )

    return df


def test_file_exists():
    assert DATA_FILE.exists()


def test_required_columns():
    df = load_data()

    required = {
        "Lexical_Form_ID",
        "Sense_ID",
        "NKo",
        "Latin_Transliteration",
        "Language",
        "Meaning",
        "French_Meaning",
        "Domain",
        "Concept_ID",
        "Validation_Status",
        "Source",
        "Notes",
    }

    assert required.issubset(df.columns)


def test_sense_ids_are_unique():
    df = load_data()

    assert df["Sense_ID"].is_unique


def test_lexical_forms_may_have_multiple_senses():
    df = load_data()

    counts = df.groupby("Lexical_Form_ID")["Sense_ID"].count()

    # NKO-LF-004 (sí) is deliberately ambiguous.
    assert counts["NKO-LF-004"] == 2


def test_every_sense_has_one_mapping_decision():
    df = load_data()

    assert df["Concept_ID"].notna().all()
    assert (df["Concept_ID"].str.strip() != "").all()


def test_non_agricultural_sense_is_not_mapped_to_agriculture():
    df = load_data()

    non_agri = df[df["Domain"] == "NON_AGRICULTURE"]

    assert len(non_agri) > 0
    assert (non_agri["Concept_ID"] == "NOT_MAPPED").all()


def test_agricultural_senses_have_agricultural_concepts():
    df = load_data()

    agri = df[df["Domain"] == "AGRICULTURE"]

    assert len(agri) > 0
    assert (agri["Concept_ID"].str.startswith("AGRI-")).all()


def test_all_nko_forms_are_detected_as_nko():
    df = load_data()

    for text in df["NKo"]:
        assert text.strip() != ""

        for char in text:
            if not char.isspace():
                assert is_nko_character(char), (
                    f"Character {char!r} in {text!r} "
                    "was not recognized as N’Ko"
                )


def test_source_attested_records_have_sources():
    df = load_data()

    attested = df[df["Validation_Status"] == "SOURCE_ATTESTED"]

    assert len(attested) > 0
    assert (attested["Source"].str.strip() != "").all()


def test_si_has_two_distinct_senses():
    df = load_data()

    si_rows = df[df["Latin_Transliteration"] == "sí"]

    assert len(si_rows) == 2
    assert set(si_rows["Sense_ID"]) == {
        "NKO-S-004",
        "NKO-S-005",
    }

    assert "AGRI-SEED" in set(si_rows["Concept_ID"])
    assert "NOT_MAPPED" in set(si_rows["Concept_ID"])


def test_soil_forms_share_canonical_concept():
    df = load_data()

    soil = df[
        df["Latin_Transliteration"].isin(
            ["bànku", "dùukolo"]
        )
    ]

    assert len(soil) == 2
    assert set(soil["Concept_ID"]) == {"AGRI-SOIL-EARTH"}


def test_no_empty_core_fields():
    df = load_data()

    core_columns = [
        "Lexical_Form_ID",
        "Sense_ID",
        "NKo",
        "Latin_Transliteration",
        "Language",
        "Meaning",
        "Domain",
        "Concept_ID",
        "Validation_Status",
        "Source",
    ]

    for column in core_columns:
        assert (df[column].str.strip() != "").all()


if __name__ == "__main__":
    print("NKO-05F — Sense Validation Tests")
    print("=" * 60)
    print(f"Data file: {DATA_FILE}")
    print(f"Records: {len(load_data())}")
    print("Run with: python -m pytest tests/test_nko_sense_map.py -v")