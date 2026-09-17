"""
Masini Barokɛla
N’Ko Challenge — NKO-08

Tests for the isolated N’Ko → V5 concept mapper.

These tests validate only the experimental concept-mapping
layer. They do NOT test or modify the production V5.3/V5.4
search engine.
"""

from utils.nko_v5_concept_mapper import map_concept_ids


def test_water_maps_to_irrigation():
    result = map_concept_ids(["AGRI-WATER"])

    assert result["status"] == "MAPPED"
    assert len(result["mappings"]) == 1

    mapping = result["mappings"][0]

    assert mapping["nko_concept_id"] == "AGRI-WATER"
    assert mapping["kb_category"] == "Irrigation"
    assert mapping["kb_crop"] == "General"


def test_soil_maps_to_soil_management():
    result = map_concept_ids(["AGRI-SOIL-EARTH"])

    assert result["status"] == "MAPPED"
    assert len(result["mappings"]) == 1

    mapping = result["mappings"][0]

    assert mapping["nko_concept_id"] == "AGRI-SOIL-EARTH"
    assert mapping["kb_category"] == "Soil Management"
    assert mapping["kb_crop"] == "General"


def test_seed_maps_to_seed_selection():
    result = map_concept_ids(["AGRI-SEED"])

    assert result["status"] == "MAPPED"
    assert len(result["mappings"]) == 1

    mapping = result["mappings"][0]

    assert mapping["nko_concept_id"] == "AGRI-SEED"
    assert mapping["kb_category"] == "Seed Selection"
    assert mapping["kb_crop"] == "General"


def test_unknown_concept_has_no_mapping():
    result = map_concept_ids(["UNKNOWN-CONCEPT"])

    assert result["status"] == "NO_MAPPING"
    assert result["mappings"] == []


def test_empty_concept_list_has_no_mapping():
    result = map_concept_ids([])

    assert result["status"] == "NO_MAPPING"
    assert result["mappings"] == []


def test_multiple_concepts_return_multiple_mappings():
    result = map_concept_ids(
        [
            "AGRI-WATER",
            "AGRI-SOIL-EARTH",
            "AGRI-SEED",
        ]
    )

    assert result["status"] == "MAPPED"
    assert len(result["mappings"]) == 3

    concept_ids = [
        mapping["nko_concept_id"]
        for mapping in result["mappings"]
    ]

    assert concept_ids == [
        "AGRI-WATER",
        "AGRI-SOIL-EARTH",
        "AGRI-SEED",
    ]


def test_duplicate_concept_ids_are_deduplicated():
    result = map_concept_ids(
        [
            "AGRI-WATER",
            "AGRI-WATER",
        ]
    )

    assert result["status"] == "MAPPED"
    assert len(result["mappings"]) == 1
    assert result["mappings"][0]["nko_concept_id"] == "AGRI-WATER"