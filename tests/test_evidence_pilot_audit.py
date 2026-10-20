"""Tests for the read-only agricultural evidence pilot audit."""

from scripts.audit_evidence_pilot import (
    ALLOWED_ATTACHMENT_STATUSES,
    ALLOWED_REVIEW_STATUSES,
    REQUIRED_COLUMNS,
    audit_rows,
)


def make_row(**overrides):
    """Build a complete, valid sample pilot record."""
    row = {
        column: f"sample-{column}"
        for column in REQUIRED_COLUMNS
    }
    row.update({
        "Pilot_ID": "P01",
        "KB_ID": "KB1",
        "Category": "Planting",
        "Exact_English_Answer": "Plant at the locally appropriate time.",
        "Step15_Status": "SOURCE_ATTESTED",
        "Evidence_Source": "Example source for testing",
        "Source_Type": "Institutional guidance",
        "Supported_Claims": "Example claim",
        "Qualification": "Apply local context.",
        "Evidence_Attachment_Status": "SOURCE_RECORD_VERIFIED",
    })
    row.update(overrides)
    return row


def valid_fields():
    return list(REQUIRED_COLUMNS)


def test_valid_record_passes_without_errors_or_warnings():
    result = audit_rows(valid_fields(), [make_row()])

    assert result["errors"] == []
    assert result["warnings"] == []
    assert result["record_count"] == 1
    assert result["review_status_counts"] == {"SOURCE_ATTESTED": 1}
    assert result["attachment_status_counts"] == {
        "SOURCE_RECORD_VERIFIED": 1
    }


def test_missing_header_is_reported():
    result = audit_rows(None, [])

    assert any("no header row" in error for error in result["errors"])


def test_missing_required_column_is_reported():
    fields = [
        column for column in REQUIRED_COLUMNS
        if column != "Evidence_Source"
    ]

    result = audit_rows(fields, [make_row()])

    assert any(
        "Evidence_Source" in error and "Missing required columns" in error
        for error in result["errors"]
    )


def test_empty_dataset_is_reported():
    result = audit_rows(valid_fields(), [])

    assert any("no data records" in error for error in result["errors"])


def test_duplicate_pilot_ids_are_reported():
    result = audit_rows(
        valid_fields(),
        [make_row(), make_row(KB_ID="KB2")],
    )

    assert any("Duplicate Pilot_ID 'P01'" in error for error in result["errors"])


def test_empty_required_value_is_reported():
    result = audit_rows(
        valid_fields(),
        [make_row(Evidence_Source="   ")],
    )

    assert any(
        "P01" in error and "Evidence_Source" in error
        for error in result["errors"]
    )


def test_unknown_review_status_is_reported():
    result = audit_rows(
        valid_fields(),
        [make_row(Step15_Status="UNRECOGNIZED_STATUS")],
    )

    assert any(
        "unrecognized Step15_Status" in error
        for error in result["errors"]
    )


def test_unknown_attachment_status_is_reported():
    result = audit_rows(
        valid_fields(),
        [make_row(Evidence_Attachment_Status="UNKNOWN")],
    )

    assert any(
        "unrecognized Evidence_Attachment_Status" in error
        for error in result["errors"]
    )


def test_review_and_attachment_warnings_do_not_create_errors():
    result = audit_rows(
        valid_fields(),
        [
            make_row(
                Step15_Status="REVIEW_REQUIRED",
                Evidence_Attachment_Status="NOT_VALIDATED",
            )
        ],
    )

    assert result["errors"] == []
    assert len(result["warnings"]) == 2
    assert any("human review is still required" in w for w in result["warnings"])
    assert any("NOT_VALIDATED" in w for w in result["warnings"])


def test_all_declared_statuses_are_accepted():
    rows = []
    for index, review_status in enumerate(sorted(ALLOWED_REVIEW_STATUSES)):
        for attachment_status in sorted(ALLOWED_ATTACHMENT_STATUSES):
            rows.append(
                make_row(
                    Pilot_ID=f"P{index}{attachment_status[:1]}",
                    Step15_Status=review_status,
                    Evidence_Attachment_Status=attachment_status,
                )
            )

    result = audit_rows(valid_fields(), rows)

    assert result["errors"] == []
    assert result["record_count"] == len(rows)