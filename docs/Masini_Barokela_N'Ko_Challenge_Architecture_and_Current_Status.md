# Masini Barokɛla — N’Ko Challenge
## Architecture and Current Status

**Project:** Mali Multilingual Agricultural Advisory — Masini Barokɛla  
**Experimental branch:** `feature/nko-challenge-nko01`  
**Current checkpoint:** NKO-V5 adapter validation  
**Status:** Experimental N’Ko subsystem validated through NKO-V5  
**Production V5.3/V5.4:** Preserved and isolated

---

## 1. Purpose

The N’Ko Challenge is an experimental research and engineering track within the Masini Barokɛla project.

Its objective is to determine how N’Ko-script agricultural input can eventually be recognized, analyzed, semantically interpreted, and connected to the Masini Barokɛla multilingual agricultural advisory architecture.

The N’Ko work is deliberately developed as an isolated experimental subsystem.

The validated V5.3/V5.4 production search engine is not modified by the N’Ko experiments.

---

## 2. Important Linguistic Principle

N’Ko is treated in this project primarily as a writing system used to represent Manding languages.

It should therefore not be treated as a separate spoken language.

A future N’Ko input layer may represent Bambara, Maninka, or related Manding linguistic content written in N’Ko.

This distinction is important because script detection, lexical recognition, language identification, and semantic interpretation are separate technical problems.

---

## 3. Architectural Principle

The N’Ko subsystem follows a layered experimental architecture:

```text
N’Ko Input
    |
    v
NKO-01 — Script Detection
    |
    v
NKO-02 — Unicode Validation
    |
    v
NKO-03 — Normalization
    |
    v
NKO-04 — Character Inspection
    |
    v
NKO-05 — Lexical Validation
    |
    v
NKO-06 — Query Recognition
    |
    v
NKO-07A — Contextual Sense Resolution
    |
    v
NKO-V5 — Experimental Adapter
    |
    v
Future controlled integration
with Masini Barokɛla V5 architecture


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

## 5. NKO-08 Controlled Concept Mapping

NKO-08 introduces a controlled experimental mapping layer between validated N’Ko `Concept_ID` values and existing Masini Barokɛla knowledge-base categories.

The mapping is deliberately semantic and controlled. It does **not** perform knowledge-base retrieval and does **not** modify the production V5.3/V5.4 search engine.

### NKO-08 Mapping Resources

The following experimental resources were created:

* `data/nko_v5_concept_map.tsv`
* `utils/nko_v5_concept_mapper.py`
* `tests/test_nko_v5_concept_mapper.py`

The validated experimental concept mappings are:

| N’Ko Concept_ID | KB Category | KB Crop | Status | Evidence |
| --- | --- | --- | --- | --- |
| `AGRI-WATER` | Irrigation | General | CANDIDATE_VALIDATED | KB records 6–10 |
| `AGRI-SOIL-EARTH` | Soil Management | General | CANDIDATE_VALIDATED | KB records 36–40 |
| `AGRI-SEED` | Seed Selection | General | CANDIDATE_VALIDATED | KB records 51–55 |

These mappings represent controlled semantic links to existing Masini Barokɛla knowledge-base categories. They are not production retrieval rules.

### NKO-08 Validation

The dedicated NKO-08 concept-mapper test suite passed:

**7/7 tests passed**

The tests validate:

* water → `Irrigation`
* soil/earth → `Soil Management`
* seed → `Seed Selection`
* unknown Concept_ID → no mapping
* empty Concept_ID list → no mapping
* multiple Concept_ID values → multiple mappings
* duplicate Concept_ID values → deduplicated mappings

The NKO-08 mapper stops at controlled semantic mapping. It does **not** retrieve answers from the knowledge base.

---

## 6. NKO-09 Controlled KB Support Evaluation

NKO-09 introduces a separate controlled evaluation layer to determine whether the validated N’Ko Concept_ID mappings are supported by actual records in the Masini Barokɛla knowledge base.

The evaluation is evidence-based: it checks whether the KB category produced by NKO-08 has real knowledge-base records. It does not retrieve an answer for an N’Ko question.

### NKO-09 Evaluation Architecture

```text
Validated Concept_ID
    |
    v
NKO-08 Concept Mapper
    |
    v
KB Category / Crop Mapping
    |
    v
NKO-09 Controlled KB Support Evaluation
    |
    v
Actual KB Records
```

### NKO-09 Controlled Results

The validated mappings were evaluated against the current Masini Barokɛla knowledge base:

| Concept_ID | KB Category | KB Record Count | Supporting KB Records | Result |
| --- | --- | ---: | --- | --- |
| `AGRI-WATER` | Irrigation | 5 | 6, 7, 8, 9, 10 | **SUPPORTED** |
| `AGRI-SOIL-EARTH` | Soil Management | 5 | 36, 37, 38, 39, 40 | **SUPPORTED** |
| `AGRI-SEED` | Seed Selection | 5 | 51, 52, 53, 54, 55 | **SUPPORTED** |

The dedicated NKO-09 controlled evaluator test suite passed:

**7/7 tests passed**

The NKO-09 evaluator establishes **knowledge-base support evidence** for the validated concept mappings. It does **not** establish end-to-end N’Ko question answering through the production retrieval engine.

### NKO-09 Experimental Boundary

NKO-09 does **not**:

* retrieve answers from the knowledge base
* call the production V5.3/V5.4 search engine
* modify `search_question_v5_2`
* modify `app.py`
* introduce fuzzy matching
* perform new linguistic interpretation
* change production retrieval logic

The NKO-09 stage is therefore an evaluation layer, not a production retrieval layer.

---

## 7. Current Experimental Boundary and Checkpoint

At this stage, the N’Ko experimental subsystem has progressed through controlled KB support evaluation.

Current validation status:

* NKO-01 through NKO-07A: validated
* NKO-V5 adapter: **8/8 tests passed**
* NKO-08 concept mapper: **7/7 tests passed**
* NKO-09 controlled KB evaluator: **7/7 tests passed**
* Complete N’Ko experimental test group: **85/85 tests passed**
* Full project regression: **85/85 tests passed**
* Production V5.3/V5.4: **preserved and isolated**
* Working tree: **clean**
* Experimental branch: **synchronized with origin**

### Current Experimental Architecture

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
NKO-09 Controlled KB Support Evaluation
    |
    v
Verified Supporting KB Records
    |
    v
Future controlled retrieval experiment
```

No direct connection to the production V5.3/V5.4 retrieval engine has been activated.

Any future retrieval experiment should be introduced as a separately tested, reversible, and explicitly controlled stage, while preserving the current production boundary.
