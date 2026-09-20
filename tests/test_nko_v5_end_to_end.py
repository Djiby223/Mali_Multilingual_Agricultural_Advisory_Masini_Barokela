"""
Masini Barokɛla
N’Ko Challenge — NKO-11

End-to-end validation of the isolated experimental N’Ko pipeline.

This test module verifies the complete controlled path:

    N’Ko query
        ↓
    NKO-V5 adapter
        ↓
    Concept mapping
        ↓
    Controlled KB evaluation
        ↓
    Controlled KB retrieval

This module does NOT test or modify the production
V5.3/V5.4 search engine.
"""

from utils.nko_v5_adapter import adapt_nko_query
from utils.nko_v5_concept_mapper import map_concept_ids
from utils.nko_v5_controlled_evaluator import evaluate_concept_ids
from utils.nko_v5_controlled_retrieval import retrieve_concept_records


def run_controlled_pipeline(query):
    """Run the isolated experimental N’Ko pipeline."""
    adapted = adapt_nko_query(query)

    if adapted["status"] != "RESOLVED":
        return {
            "status": adapted["status"],
            "stage": "ADAPTER",
            "adapted": adapted,
            "mapped": None,
            "evaluated": None,
            "retrieved": None,
        }

    mapped = map_concept_ids(adapted["concept_ids"])

    if mapped["status"] != "MAPPED":
        return {
            "status": mapped["status"],
            "stage": "MAPPER",
            "adapted": adapted,
            "mapped": mapped,
            "evaluated": None,
            "retrieved": None,
        }

    evaluated = evaluate_concept_ids(adapted["concept_ids"])

    if evaluated["status"] != "SUPPORTED":
        return {
            "status": evaluated["status"],
            "stage": "EVALUATOR",
            "adapted": adapted,
            "mapped": mapped,
            "evaluated": evaluated,
            "retrieved": None,
        }

    retrieved = retrieve_concept_records(adapted["concept_ids"])

    return {
        "status": retrieved["status"],
        "stage": "RETRIEVAL",
        "adapted": adapted,
        "mapped": mapped,
        "evaluated": evaluated,
        "retrieved": retrieved,
    }


def test_water_end_to_end():
    result = run_controlled_pipeline("\u07d6\u07cc")

    assert result["status"] == "RETRIEVED"
    assert result["stage"] == "RETRIEVAL"
    assert result["adapted"]["concept_ids"] == ["AGRI-WATER"]
    assert result["mapped"]["mappings"][0]["kb_category"] == "Irrigation"
    assert result["evaluated"]["evaluations"][0]["supported"] is True
    assert [record["ID"] for record in result["retrieved"]["records"]] == [
        "6",
        "7",
        "8",
        "9",
        "10",
    ]


def test_soil_end_to_end():
    result = run_controlled_pipeline("\u07d8\u07ce\u07f0\u07de\u07df\u07cf")

    assert result["status"] == "RETRIEVED"
    assert result["adapted"]["concept_ids"] == ["AGRI-SOIL-EARTH"]
    assert result["mapped"]["mappings"][0]["kb_category"] == "Soil Management"
    assert [record["ID"] for record in result["retrieved"]["records"]] == [
        "36",
        "37",
        "38",
        "39",
        "40",
    ]


def test_seed_with_context_end_to_end():
    result = run_controlled_pipeline("\u07db\u07cc seed")

    assert result["status"] == "RETRIEVED"
    assert result["adapted"]["concept_ids"] == ["AGRI-SEED"]
    assert result["mapped"]["mappings"][0]["kb_category"] == "Seed Selection"
    assert [record["ID"] for record in result["retrieved"]["records"]] == [
        "51",
        "52",
        "53",
        "54",
        "55",
    ]


def test_ambiguous_seed_stops_at_adapter():
    result = run_controlled_pipeline("\u07db\u07cc")

    assert result["status"] == "AMBIGUOUS"
    assert result["stage"] == "ADAPTER"
    assert result["adapted"]["concept_ids"] == []
    assert result["mapped"] is None
    assert result["evaluated"] is None
    assert result["retrieved"] is None


def test_non_agricultural_sense_stops_at_adapter():
    result = run_controlled_pipeline("\u07db\u07cc hair")

    assert result["status"] == "NON_AGRICULTURE"
    assert result["stage"] == "ADAPTER"
    assert result["adapted"]["concept_ids"] == []
    assert result["retrieved"] is None


def test_unknown_nko_stops_at_adapter():
    result = run_controlled_pipeline("\u07ca\u07cb\u07cc")

    assert result["status"] == "NO_LEXICAL_MATCH"
    assert result["stage"] == "ADAPTER"
    assert result["adapted"]["concept_ids"] == []
    assert result["retrieved"] is None


def test_multiple_valid_concepts_retrieve_all_records():
    concept_ids = [
        "AGRI-WATER",
        "AGRI-SOIL-EARTH",
        "AGRI-SEED",
    ]

    mapped = map_concept_ids(concept_ids)
    evaluated = evaluate_concept_ids(concept_ids)
    retrieved = retrieve_concept_records(concept_ids)

    assert mapped["status"] == "MAPPED"
    assert evaluated["status"] == "SUPPORTED"
    assert retrieved["status"] == "RETRIEVED"
    assert retrieved["record_count"] == 15

    assert [record["ID"] for record in retrieved["records"]] == [
        "6",
        "7",
        "8",
        "9",
        "10",
        "36",
        "37",
        "38",
        "39",
        "40",
        "51",
        "52",
        "53",
        "54",
        "55",
    ]
