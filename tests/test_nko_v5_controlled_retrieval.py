"""
Masini Barokɛla
N’Ko Challenge — NKO-10

Tests for the isolated N’Ko → KB controlled retrieval layer.

These tests verify that validated N’Ko Concept_ID values can
retrieve the actual supporting records from the Masini Barokɛla
knowledge base.

This test module does NOT test or modify the production
V5.3/V5.4 search engine.
"""

from utils.nko_v5_controlled_retrieval import (
    retrieve_concept_records,
)


def test_water_concept_retrieves_records():
    result = retrieve_concept_records(["AGRI-WATER"])

    assert result["status"] == "RETRIEVED"
    assert result["record_count"] == 5

    records = result["records"]

    assert [record["ID"] for record in records] == [
        "6",
        "7",
        "8",
        "9",
        "10",
    ]

    assert all(
        record["Category"] == "Irrigation"
        for record in records
    )


def test_soil_concept_retrieves_records():
    result = retrieve_concept_records(["AGRI-SOIL-EARTH"])

    assert result["status"] == "RETRIEVED"
    assert result["record_count"] == 5

    assert [record["ID"] for record in result["records"]] == [
        "36",
        "37",
        "38",
        "39",
        "40",
    ]

    assert all(
        record["Category"] == "Soil Management"
        for record in result["records"]
    )


def test_seed_concept_retrieves_records():
    result = retrieve_concept_records(["AGRI-SEED"])

    assert result["status"] == "RETRIEVED"
    assert result["record_count"] == 5

    assert [record["ID"] for record in result["records"]] == [
        "51",
        "52",
        "53",
        "54",
        "55",
    ]

    assert all(
        record["Category"] == "Seed Selection"
        for record in result["records"]
    )


def test_unknown_concept_retrieves_nothing():
    result = retrieve_concept_records(["UNKNOWN-CONCEPT"])

    assert result["status"] == "NO_RETRIEVAL"
    assert result["record_count"] == 0
    assert result["records"] == []


def test_empty_concept_list_retrieves_nothing():
    result = retrieve_concept_records([])

    assert result["status"] == "NO_RETRIEVAL"
    assert result["record_count"] == 0
    assert result["records"] == []


def test_multiple_valid_concepts_retrieve_all_records():
    result = retrieve_concept_records(
        [
            "AGRI-WATER",
            "AGRI-SOIL-EARTH",
            "AGRI-SEED",
        ]
    )

    assert result["status"] == "RETRIEVED"
    assert result["record_count"] == 15

    assert [record["ID"] for record in result["records"]] == [
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


def test_retrieved_records_contain_complete_kb_schema():
    result = retrieve_concept_records(["AGRI-WATER"])

    record = result["records"][0]

    expected_fields = {
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

    assert set(record.keys()) == expected_fields
