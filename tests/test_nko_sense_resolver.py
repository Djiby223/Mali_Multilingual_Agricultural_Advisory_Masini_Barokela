"""
Masini Barokɛla
N’Ko Challenge — NKO-07A

Automated tests for the Contextual Sense Resolver.

This test suite validates:
    - N’Ko detection
    - mixed-script N’Ko queries
    - ambiguity detection
    - contextual agricultural resolution
    - contextual non-agricultural resolution
    - unambiguous lexical forms
    - unknown and non-N’Ko queries

This module does NOT test or modify the V5.3/V5.4 production engine.
"""

from utils.nko_sense_resolver import resolve_senses


# --------------------------------------------------
# Basic N’Ko query
# --------------------------------------------------

def test_ambiguous_si_without_context():
    result = resolve_senses("\u07db\u07cc")

    assert result["script"] == "NKO"
    assert result["status"] == "AMBIGUOUS"
    assert len(result["recognized_forms"]) == 1
    assert len(result["candidate_senses"]) == 2
    assert len(result["resolved_senses"]) == 0


# --------------------------------------------------
# Agricultural contextual resolution
# --------------------------------------------------

def test_si_seed_resolves_to_agricultural_seed():
    result = resolve_senses("\u07db\u07cc seed")

    assert result["script"] == "MIXED"
    assert result["status"] == "RESOLVED"
    assert len(result["recognized_forms"]) == 1
    assert len(result["candidate_senses"]) == 2
    assert len(result["resolved_senses"]) == 1

    resolved = result["resolved_senses"][0]

    assert resolved["Concept_ID"] == "AGRI-SEED"
    assert resolved["Domain"] == "AGRICULTURE"


# --------------------------------------------------
# Non-agricultural contextual resolution
# --------------------------------------------------

def test_si_hair_resolves_to_non_agricultural_sense():
    result = resolve_senses("\u07db\u07cc hair")

    assert result["script"] == "MIXED"
    assert result["status"] == "RESOLVED"
    assert len(result["recognized_forms"]) == 1
    assert len(result["candidate_senses"]) == 2
    assert len(result["resolved_senses"]) == 1

    resolved = result["resolved_senses"][0]

    assert resolved["Concept_ID"] == "NOT_MAPPED"
    assert resolved["Domain"] == "NON_AGRICULTURE"


# --------------------------------------------------
# Unambiguous N’Ko forms
# --------------------------------------------------

def test_water_is_unambiguous():
    result = resolve_senses("\u07d6\u07cc")

    assert result["script"] == "NKO"
    assert result["status"] == "UNAMBIGUOUS"
    assert len(result["recognized_forms"]) == 1
    assert len(result["candidate_senses"]) == 1
    assert len(result["resolved_senses"]) == 1

    assert result["resolved_senses"][0]["Concept_ID"] == "AGRI-WATER"


def test_banku_is_unambiguous():
    result = resolve_senses("\u07d8\u07ce\u07f0\u07de\u07df\u07cf")

    assert result["script"] == "NKO"
    assert result["status"] == "UNAMBIGUOUS"
    assert len(result["recognized_forms"]) == 1
    assert len(result["candidate_senses"]) == 1
    assert len(result["resolved_senses"]) == 1

    assert (
        result["resolved_senses"][0]["Concept_ID"]
        == "AGRI-SOIL-EARTH"
    )


# --------------------------------------------------
# Non-N’Ko query
# --------------------------------------------------

def test_latin_query_is_not_nko():
    result = resolve_senses("Hello")

    assert result["script"] == "LATIN"
    assert result["status"] == "NOT_NKO"
    assert result["recognized_forms"] == []
    assert result["candidate_senses"] == []
    assert result["resolved_senses"] == []


# --------------------------------------------------
# Empty query
# --------------------------------------------------

def test_empty_query():
    result = resolve_senses("")

    assert result["script"] == "UNKNOWN"
    assert result["status"] == "NOT_NKO"
    assert result["recognized_forms"] == []
    assert result["candidate_senses"] == []
    assert result["resolved_senses"] == []


# --------------------------------------------------
# Whitespace query
# --------------------------------------------------

def test_whitespace_query():
    result = resolve_senses("   ")

    assert result["script"] == "UNKNOWN"
    assert result["status"] == "NOT_NKO"
    assert result["recognized_forms"] == []
    assert result["candidate_senses"] == []
    assert result["resolved_senses"] == []


# --------------------------------------------------
# Unknown N’Ko text
# --------------------------------------------------

def test_unknown_nko_text():
    result = resolve_senses("\u07ca\u07cb\u07cc")

    assert result["script"] == "NKO"
    assert result["status"] == "NO_LEXICAL_MATCH"
    assert result["recognized_forms"] == []
    assert result["candidate_senses"] == []
    assert result["resolved_senses"] == []


# --------------------------------------------------
# Context must not invent a sense
# --------------------------------------------------

def test_ambiguous_si_with_unrelated_context_remains_ambiguous():
    result = resolve_senses("\u07db\u07cc tractor")

    assert result["script"] == "MIXED"
    assert result["status"] == "AMBIGUOUS"
    assert len(result["recognized_forms"]) == 1
    assert len(result["candidate_senses"]) == 2
    assert len(result["resolved_senses"]) == 0


# --------------------------------------------------
# Explicit agricultural context
# --------------------------------------------------

def test_si_with_agricultural_context_resolves():
    result = resolve_senses("\u07db\u07cc agriculture")

    assert result["script"] == "MIXED"
    assert result["status"] == "RESOLVED"
    assert len(result["resolved_senses"]) == 1

    assert result["resolved_senses"][0]["Concept_ID"] == "AGRI-SEED"


# --------------------------------------------------
# Explicit non-agricultural context
# --------------------------------------------------

def test_si_with_french_hair_context_resolves():
    result = resolve_senses("\u07db\u07cc cheveux")

    assert result["script"] == "MIXED"
    assert result["status"] == "RESOLVED"
    assert len(result["resolved_senses"]) == 1

    assert result["resolved_senses"][0]["Concept_ID"] == "NOT_MAPPED"