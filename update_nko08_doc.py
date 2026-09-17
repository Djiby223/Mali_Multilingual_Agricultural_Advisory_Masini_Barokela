from pathlib import Path

path = Path(
    "docs/Masini_Barokela_N'Ko_Challenge_Architecture_and_Current_Status.md"
)

text = path.read_text(encoding="utf-8")

text = text.replace(
    "**Current checkpoint:** NKO-V5 adapter validation",
    "**Current checkpoint:** NKO-08 controlled concept mapping",
)

text = text.replace(
    "**Status:** Experimental N’Ko subsystem validated through NKO-V5",
    "**Status:** Experimental N’Ko subsystem validated through NKO-08",
)

marker = "## 5. Current Experimental Boundary"

if marker not in text:
    raise SystemExit("ERROR: Section 5 marker not found.")

new_sections = """## 5. NKO-08 Controlled Concept Mapping

NKO-08 introduces an isolated experimental mapping layer between validated N’Ko agricultural `Concept_ID` values and the existing Masini Barokɛla knowledge-base classification fields.

The mapping layer does **not** perform knowledge-base retrieval.

It does **not** perform fuzzy matching or linguistic interpretation.

It does **not** modify the production V5.3/V5.4 search engine.

### Mapping resources

The NKO-08 implementation consists of:

- `data/nko_v5_concept_map.tsv`
- `utils/nko_v5_concept_mapper.py`
- `tests/test_nko_v5_concept_mapper.py`

The current controlled mappings are:

| N’Ko Concept_ID | KB Category | KB Crop | Evidence |
|---|---|---|---|
| `AGRI-WATER` | `Irrigation` | `General` | KB records 7–10 |
| `AGRI-SOIL-EARTH` | `Soil Management` | `General` | KB records 36–40 |
| `AGRI-SEED` | `Seed Selection` | `General` | KB records 51–55 |

These mappings are experimental semantic mappings based on existing Masini Barokɛla knowledge-base categories. They are not yet production retrieval rules.

### NKO-08 validation

The dedicated NKO-08 concept-mapper test suite passed:

**7/7 tests passed**

The validated cases include:

- water concept → `Irrigation`
- soil/earth concept → `Soil Management`
- seed concept → `Seed Selection`
- unknown concept → `NO_MAPPING`
- empty concept list → `NO_MAPPING`
- multiple concepts → multiple mappings
- duplicate concept IDs → deduplicated mapping

### Complete N’Ko validation

Following NKO-08 implementation, the complete N’Ko experimental test group was executed:

**78/78 tests passed**

This confirms that NKO-08 operates without regression against the previously validated N’Ko detection, normalization, inspection, query recognition, sense mapping, sense resolution, and NKO-V5 adapter layers.

### Full project regression

The complete Masini Barokɛla test suite was then executed:

**78/78 tests passed**

This confirms that the NKO-08 experimental mapping layer currently operates without regression against the complete project test suite.

---

## 6. Current Experimental Boundary

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
Validated Concept_ID
    |
    v
NKO-V5 Adapter
    |
    v
NKO-08 Concept Mapper
    |
    v
Experimental KB Category / Crop Mapping
    |
    v
Future controlled V5 integration