"""Read-only structural audit for the Masini Barokela evidence pilot."""

import csv
from collections import Counter
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parent.parent
INPUT_FILE = PROJECT_ROOT / "data" / "Masini_Barokela_Context_Pilot_v1.tsv"

REQUIRED_COLUMNS = (
    "Pilot_ID",
    "KB_ID",
    "Category",
    "Exact_English_Answer",
    "Step15_Status",
    "Evidence_Source",
    "Source_Type",
    "Supported_Claims",
    "Qualification",
    "Evidence_Attachment_Status",
)

ALLOWED_REVIEW_STATUSES = {
    "SOURCE_ATTESTED",
    "VALIDATED",
    "REVIEW_REQUIRED",
}

ALLOWED_ATTACHMENT_STATUSES = {
    "SOURCE_RECORD_VERIFIED",
    "NOT_VALIDATED",
}


def audit_rows(fieldnames, rows):
    """Return structural errors, review warnings, and status counts."""
    errors = []
    warnings = []

    if fieldnames is None:
        return {
            "errors": ["The TSV file has no header row."],
            "warnings": [],
            "record_count": 0,
            "review_status_counts": {},
            "attachment_status_counts": {},
        }

    missing_columns = [
        column for column in REQUIRED_COLUMNS
        if column not in fieldnames
    ]

    if missing_columns:
        errors.append(
            "Missing required columns: " + ", ".join(missing_columns)
        )

    if missing_columns:
        return {
            "errors": errors,
            "warnings": warnings,
            "record_count": len(rows),
            "review_status_counts": {},
            "attachment_status_counts": {},
        }

    if not rows:
        errors.append("The TSV contains no data records.")

    pilot_ids = [
        (row.get("Pilot_ID") or "").strip()
        for row in rows
    ]
    id_counts = Counter(pilot_ids)

    for pilot_id, count in sorted(id_counts.items()):
        if not pilot_id:
            errors.append("A record has an empty Pilot_ID.")
        elif count > 1:
            errors.append(
                f"Duplicate Pilot_ID '{pilot_id}' occurs {count} times."
            )

    review_status_counts = Counter()
    attachment_status_counts = Counter()

    for row_number, row in enumerate(rows, start=2):
        pilot_id = (row.get("Pilot_ID") or "").strip() or (
            f"row {row_number}"
        )

        for column in REQUIRED_COLUMNS:
            if not (row.get(column) or "").strip():
                errors.append(
                    f"{pilot_id}: required field '{column}' is empty."
                )

        review_status = (row.get("Step15_Status") or "").strip()
        attachment_status = (
            row.get("Evidence_Attachment_Status") or ""
        ).strip()

        if review_status:
            review_status_counts[review_status] += 1
            if review_status not in ALLOWED_REVIEW_STATUSES:
                errors.append(
                    f"{pilot_id}: unrecognized Step15_Status "
                    f"'{review_status}'."
                )

        if attachment_status:
            attachment_status_counts[attachment_status] += 1
            if attachment_status not in ALLOWED_ATTACHMENT_STATUSES:
                errors.append(
                    f"{pilot_id}: unrecognized Evidence_Attachment_Status "
                    f"'{attachment_status}'."
                )

        if review_status == "REVIEW_REQUIRED":
            warnings.append(
                f"{pilot_id}: human review is still required."
            )

        if attachment_status == "NOT_VALIDATED":
            warnings.append(
                f"{pilot_id}: evidence attachment is marked NOT_VALIDATED."
            )

    return {
        "errors": errors,
        "warnings": warnings,
        "record_count": len(rows),
        "review_status_counts": dict(sorted(review_status_counts.items())),
        "attachment_status_counts": dict(
            sorted(attachment_status_counts.items())
        ),
    }


def audit_file(path=INPUT_FILE):
    """Read a UTF-8 TSV and audit its structure without modifying it."""
    with Path(path).open(
        "r", encoding="utf-8-sig", newline=""
    ) as handle:
        reader = csv.DictReader(handle, delimiter="\t")
        return audit_rows(reader.fieldnames, list(reader))


def main():
    print("Masini Barokela Evidence Pilot Audit")
    print("=" * 40)
    print(f"Input: {INPUT_FILE}")

    try:
        result = audit_file()
    except (OSError, UnicodeError, csv.Error) as exc:
        print(f"ERROR: Could not read the pilot: {exc}")
        return 1

    print(f"\nRecords examined: {result['record_count']}")

    print("\nReview status counts:")
    for status, count in result["review_status_counts"].items():
        print(f"  {status}: {count}")

    print("\nEvidence attachment status counts:")
    for status, count in result["attachment_status_counts"].items():
        print(f"  {status}: {count}")

    print(f"\nErrors: {len(result['errors'])}")
    for error in result["errors"]:
        print(f"  ERROR: {error}")

    print(f"\nWarnings: {len(result['warnings'])}")
    for warning in result["warnings"]:
        print(f"  WARNING: {warning}")

    if result["errors"]:
        print("\nAudit result: FAIL (structural errors found)")
        return 1

    print("\nAudit result: PASS (structural checks passed)")
    print("This result does not certify scientific validity.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())