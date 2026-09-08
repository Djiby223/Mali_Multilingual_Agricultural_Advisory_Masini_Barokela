"""
Masini Barokɛla
N’Ko Challenge — NKO-06B

Automated tests for N’Ko Query Recognition.
"""

from utils.nko_query import recognize_nko_query


def test_nko_query_is_detected():
    result = recognize_nko_query("ߖߌ")

    assert result["script"] == "NKO"


def test_latin_query_is_not_detected_as_nko():
    result = recognize_nko_query("Hello")

    assert result["script"] == "LATIN"
    assert result["recognized_forms"] == []
    assert result["possible_concepts"] == []


def test_water_is_recognized():
    result = recognize_nko_query("ߖߌ")

    assert len(result["recognized_forms"]) == 1
    assert len(result["possible_concepts"]) == 1

    assert result["recognized_forms"][0]["Lexical_Form_ID"] == (
        "NKO-LF-003"
    )

    assert result["possible_concepts"][0]["Concept_ID"] == (
        "AGRI-WATER"
    )


def test_soil_banku_is_recognized():
    result = recognize_nko_query("ߓߊ߲߬ߞߎ")

    assert len(result["recognized_forms"]) == 1
    assert result["recognized_forms"][0]["Lexical_Form_ID"] == (
        "NKO-LF-001"
    )

    assert result["possible_concepts"][0]["Concept_ID"] == (
        "AGRI-SOIL-EARTH"
    )


def test_soil_duukolo_is_recognized():
    result = recognize_nko_query("ߘߎ߰ߞߟߏ")

    assert len(result["recognized_forms"]) == 1
    assert result["recognized_forms"][0]["Lexical_Form_ID"] == (
        "NKO-LF-002"
    )

    assert result["possible_concepts"][0]["Concept_ID"] == (
        "AGRI-SOIL-EARTH"
    )


def test_ambiguous_si_has_one_lexical_form():
    result = recognize_nko_query("ߛߌ")

    assert len(result["recognized_forms"]) == 1


def test_ambiguous_si_has_two_senses():
    result = recognize_nko_query("ߛߌ")

    assert len(result["possible_concepts"]) == 2

    concept_ids = {
        item["Concept_ID"]
        for item in result["possible_concepts"]
    }

    assert "AGRI-SEED" in concept_ids
    assert "NOT_MAPPED" in concept_ids


def test_unknown_nko_text_has_no_known_lexical_forms():
    result = recognize_nko_query("ߒߞߏ")

    assert result["script"] == "NKO"
    assert result["recognized_forms"] == []
    assert result["possible_concepts"] == []


def test_empty_query():
    result = recognize_nko_query("")

    assert result["script"] == "UNKNOWN"
    assert result["recognized_forms"] == []
    assert result["possible_concepts"] == []


def test_whitespace_query():
    result = recognize_nko_query("   ")

    assert result["script"] == "UNKNOWN"
    assert result["recognized_forms"] == []
    assert result["possible_concepts"] == []


def test_nko_forms_remain_deduplicated():
    result = recognize_nko_query("ߛߌ")

    lexical_ids = [
        item["Lexical_Form_ID"]
        for item in result["recognized_forms"]
    ]

    assert lexical_ids == ["NKO-LF-004"]