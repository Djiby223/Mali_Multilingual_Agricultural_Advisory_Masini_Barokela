"""
Masini Barokɛla
N’Ko Challenge — NKO-V5

Tests for the isolated N’Ko → V5 adapter.

This test module does NOT test or modify the production
V5.3/V5.4 search engine.
"""

from utils.nko_v5_adapter import adapt_nko_query


def test_nko_water_resolves_to_agri_water():
    result = adapt_nko_query("\u07d6\u07cc")

    assert result["status"] == "RESOLVED"
    assert result["script"] == "NKO"
    assert result["concept_ids"] == ["AGRI-WATER"]


def test_nko_soil_resolves_to_agri_soil_earth():
    result = adapt_nko_query("\u07d8\u07ce\u07f0\u07de\u07df\u07cf")

    assert result["status"] == "RESOLVED"
    assert result["concept_ids"] == ["AGRI-SOIL-EARTH"]


def test_nko_seed_alone_remains_ambiguous():
    result = adapt_nko_query("\u07db\u07cc")

    assert result["status"] == "AMBIGUOUS"
    assert result["concept_ids"] == []


def test_nko_seed_with_context_resolves():
    result = adapt_nko_query("\u07db\u07cc seed")

    assert result["status"] == "RESOLVED"
    assert result["concept_ids"] == ["AGRI-SEED"]


def test_nko_hair_does_not_map_to_agriculture():
    result = adapt_nko_query("\u07db\u07cc hair")

    assert result["status"] == "NON_AGRICULTURE"
    assert result["concept_ids"] == []


def test_unknown_nko_has_no_concept():
    result = adapt_nko_query("\u07ca\u07cb\u07cc")

    assert result["status"] == "NO_LEXICAL_MATCH"
    assert result["concept_ids"] == []


def test_english_query_is_not_nko():
    result = adapt_nko_query("Hello")

    assert result["status"] == "NOT_NKO"
    assert result["concept_ids"] == []


def test_empty_query_is_not_nko():
    result = adapt_nko_query("")

    assert result["status"] == "NOT_NKO"
    assert result["concept_ids"] == []
