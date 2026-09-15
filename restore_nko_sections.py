from pathlib import Path

docs = Path("docs")

candidates = [
    p for p in docs.glob("*.md")
    if "Challenge_Architecture_and_Current_Status" in p.name
    and not p.name.endswith(".backup.md")
]

assert len(candidates) == 1, f"Expected exactly one target document, found: {candidates}"

p = candidates[0]
t = p.read_text(encoding="utf-8")

assert "## 4. NKO-V5 Adapter Validation" not in t, \
    "Sections 4-6 already present — no change made"

t = t.replace(
    "**Current checkpoint:** `98f80f2`",
    "**Current checkpoint:** NKO-V5 adapter validation"
)

t = t.replace(
    "validated through NKO-07A",
    "validated through NKO-V5"
)

sections = """

---

## 4. NKO-V5 Adapter Validation

The experimental NKO-V5 adapter provides a controlled interface between the N’Ko semantic layer and a future Masini Barokɛla V5 integration layer.

The adapter delegates N’Ko recognition and contextual sense resolution to the experimental N’Ko subsystem, extracts validated agricultural `Concept_ID` values, and returns a stable V5-facing structure containing `status`, `script`, `recognized_forms`, `resolved_senses`, and `concept_ids`.

The adapter does **not** perform knowledge-base retrieval.

The adapter does **not** modify the production V5.3/V5.4 search engine.

### Validation result

The dedicated NKO-V5 adapter test suite passed:

**8/8 tests passed**

The validated cases include:

- N’Ko water → `RESOLVED` → `AGRI-WATER`
- N’Ko soil → `RESOLVED` → `AGRI-SOIL-EARTH`
- ambiguous seed query → `AMBIGUOUS`
- seed with agricultural context → `RESOLVED` → `AGRI-SEED`
- seed with non-agricultural context → `NON_AGRICULTURE`
- unknown N’Ko input → `NO_LEXICAL_MATCH`
- English input → `NOT_NKO`
- empty input → `NOT_NKO`

### Full regression validation

Following NKO-V5 adapter validation, the complete Masini Barokɛla test suite was executed:

**71/71 tests passed**

This confirms that the experimental N’Ko adapter currently operates without regression against the existing project test suite.

---

## 5. Current Experimental Boundary

The current architecture remains intentionally isolated:

```text
N’Ko Input
    |
    v
NKO Detection / Recognition
    |
    v
Sense Resolution
    |
    v
NKO-V5 Adapter
    |
    v
Validated Concept_ID
    |
    v
Future controlled V5 integration