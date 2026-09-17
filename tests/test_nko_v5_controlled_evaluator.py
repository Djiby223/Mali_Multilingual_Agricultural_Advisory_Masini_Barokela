"""
Masini Barokɛla
N’Ko Challenge — NKO-09

Tests for the isolated N’Ko → KB controlled evaluator.

These tests verify that validated N’Ko Concept_ID values are
supported by real Masini Barokɛla knowledge-base records.

This test module does NOT test or modify the production
V5.3/V5.4 search engine.
"""

from utils.nko_v5_controlled_evaluator import evaluate_concept_ids


def test_water_concept_is_supported():
    result = evaluate_concept_ids(["AGRI-WATER"])

    assert result["status"] == "SUPPORTED"

    evaluation = result["evaluations"][0]

    assert evaluation["concept_id"] == "AGRI-WATER"
    assert evaluation["kb_category"] == "Irrigation"
    assert evaluation["kb_record_count"] == 5
    assert evaluation["kb_record_ids"] == [
        "6",
        "7",
        "8",
        "9",
        "10",
    ]
    assert evaluation["supported"] is True


def test_soil_concept_is_supported():
    result = evaluate_concept_ids(["AGRI-SOIL-EARTH"])

    assert result["status"] == "SUPPORTED"

    evaluation = result["evaluations"][0]

    assert evaluation["concept_id"] == "AGRI-SOIL-EARTH"
    assert evaluation["kb_category"] == "Soil Management"
    assert evaluation["kb_record_count"] == 5
    assert evaluation["kb_record_ids"] == [
        "36",
        "37",
        "38",
        "39",
        "40",
    ]
    assert evaluation["supported"] is True


def test_seed_concept_is_supported():
    result = evaluate_concept_ids(["AGRI-SEED"])

    assert result["status"] == "SUPPORTED"

    evaluation = result["evaluations"][0]

    assert evaluation["concept_id"] == "AGRI-SEED"
    assert evaluation["kb_category"] == "Seed Selection"
    assert evaluation["kb_record_count"] == 5
    assert evaluation["kb_record_ids"] == [
        "51",
        "52",
        "53",
        "54",
        "55",
    ]
    assert evaluation["supported"] is True


def test_unknown_concept_has_no_support():
    result = evaluate_concept_ids(["UNKNOWN-CONCEPT"])

    assert result["status"] == "NO_SUPPORT"
    assert result["evaluations"] == []


def test_empty_concept_list_has_no_support():
    result = evaluate_concept_ids([])

    assert result["status"] == "NO_SUPPORT"
    assert result["evaluations"] == []


def test_multiple_valid_concepts_are_supported():
    result = evaluate_concept_ids(
        [
            "AGRI-WATER",
            "AGRI-SOIL-EARTH",
            "AGRI-SEED",
        ]
    )

    assert result["status"] == "SUPPORTED"
    assert len(result["evaluations"]) == 3

    concept_ids = [
        evaluation["concept_id"]
        for evaluation in result["evaluations"]
    ]

    assert concept_ids == [
        "AGRI-WATER",
        "AGRI-SOIL-EARTH",
        "AGRI-SEED",
    ]

    assert all(
        evaluation["supported"]
        for evaluation in result["evaluations"]
    )


def test_evaluation_contains_mapping_evidence():
    result = evaluate_concept_ids(["AGRI-WATER"])

    evaluation = result["evaluations"][0]

    assert evaluation["mapping_status"] == "CANDIDATE_VALIDATED"
    assert evaluation["evidence"] == "KB records 6-10"
    assert evaluation["kb_record_count"] == len(
        evaluation["kb_record_ids"]
    )
