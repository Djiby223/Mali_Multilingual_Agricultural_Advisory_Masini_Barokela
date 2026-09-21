"""
Masini Barokɛla
N’Ko Challenge — NKO-12

Controlled answer assembly tests.

This test module validates the isolated transformation of
already-retrieved Master Knowledge Base records into a
language-specific controlled answer package.

It does NOT:
    - perform N’Ko detection
    - perform sense resolution
    - perform KB retrieval
    - perform fuzzy matching
    - call the production V5.3/V5.4 search engine
    - modify app.py
"""

from utils.nko_v5_controlled_retrieval import retrieve_concept_records
from utils.nko_v5_answer_assembler import assemble_answer_package
from test_nko_v5_end_to_end import run_controlled_pipeline


def test_water_english_answer_package():
    retrieval = retrieve_concept_records(["AGRI-WATER"])

    result = assemble_answer_package(
        retrieval,
        language="English",
    )

    assert result["status"] == "ANSWER_PACKAGE_READY"
    assert result["language"] == "English"
    assert result["record_count"] == 5

    assert [answer["ID"] for answer in result["answers"]] == [
        "6",
        "7",
        "8",
        "9",
        "10",
    ]

    assert result["answers"][0]["answer"] == (
        "Tomato plants should be watered regularly, especially during "
        "dry periods, while avoiding waterlogging."
    )


def test_water_french_answer_package():
    retrieval = retrieve_concept_records(["AGRI-WATER"])

    result = assemble_answer_package(
        retrieval,
        language="Français",
    )

    assert result["status"] == "ANSWER_PACKAGE_READY"
    assert result["language"] == "Français"
    assert result["record_count"] == 5

    assert [answer["ID"] for answer in result["answers"]] == [
        "6",
        "7",
        "8",
        "9",
        "10",
    ]

    assert result["answers"][0]["answer"] == (
        "Régulièrement, surtout en période sèche, sans excès d’eau."
    )


def test_water_bambara_answer_package():
    retrieval = retrieve_concept_records(["AGRI-WATER"])

    result = assemble_answer_package(
        retrieval,
        language="Bamanankan",
    )

    assert result["status"] == "ANSWER_PACKAGE_READY"
    assert result["language"] == "Bamanankan"
    assert result["record_count"] == 5

    assert [answer["ID"] for answer in result["answers"]] == [
        "6",
        "7",
        "8",
        "9",
        "10",
    ]


def test_no_retrieval_produces_no_answer_package():
    retrieval = retrieve_concept_records(["UNKNOWN-CONCEPT"])

    result = assemble_answer_package(
        retrieval,
        language="English",
    )

    assert result["status"] == "NO_ANSWER_PACKAGE"
    assert result["record_count"] == 0
    assert result["answers"] == []


def test_invalid_language_produces_no_answer_package():
    retrieval = retrieve_concept_records(["AGRI-WATER"])

    result = assemble_answer_package(
        retrieval,
        language="N’Ko",
    )

    assert result["status"] == "NO_ANSWER_PACKAGE"
    assert result["record_count"] == 0
    assert result["answers"] == []

def test_answer_package_preserves_metadata():
    retrieval = retrieve_concept_records(["AGRI-WATER"])

    result = assemble_answer_package(
        retrieval,
        language="English",
    )

    assert result["answers"][0]["Crop"] == retrieval["records"][0]["Crop"]
    assert result["answers"][0]["Region"] == retrieval["records"][0]["Region"]
    assert result["answers"][0]["Season"] == retrieval["records"][0]["Season"]


def test_answer_assembly_does_not_mutate_retrieval_result():
    retrieval = retrieve_concept_records(["AGRI-WATER"])

    original_records = [record.copy() for record in retrieval["records"]]

    assemble_answer_package(
        retrieval,
        language="English",
    )

    assert retrieval["records"] == original_records

def test_nko11_to_nko12_water_answer_package():
    pipeline = run_controlled_pipeline("\u07d6\u07cc")

    assert pipeline["status"] == "RETRIEVED"
    assert pipeline["stage"] == "RETRIEVAL"

    result = assemble_answer_package(
        pipeline["retrieved"],
        language="English",
    )

    assert result["status"] == "ANSWER_PACKAGE_READY"
    assert result["language"] == "English"
    assert result["record_count"] == 5

    assert [answer["ID"] for answer in result["answers"]] == [
        "6",
        "7",
        "8",
        "9",
        "10",
    ]

    assert result["answers"][0]["answer"] == (
        "Tomato plants should be watered regularly, especially during "
        "dry periods, while avoiding waterlogging."
    )

    assert result["answers"][0]["Crop"] == (
        pipeline["retrieved"]["records"][0]["Crop"]
    )
    assert result["answers"][0]["Region"] == (
        pipeline["retrieved"]["records"][0]["Region"]
    )
    assert result["answers"][0]["Season"] == (
        pipeline["retrieved"]["records"][0]["Season"]
    )
