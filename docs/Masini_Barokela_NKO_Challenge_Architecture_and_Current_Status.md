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

``	ext
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

## 7. NKO-10 Controlled KB Retrieval

NKO-10 introduces a separate controlled retrieval layer that retrieves complete Masini Barokɛla knowledge-base records for validated N’Ko Concept_ID mappings.

The retrieval layer accepts only validated Concept_ID values produced by the experimental NKO-V5 pipeline. It does not accept arbitrary N’Ko text and does not perform linguistic interpretation, fuzzy matching, or answer generation.

### NKO-10 Retrieval Architecture

````text
Validated Concept_ID
    |
    v
NKO-08 Concept Mapper
    |
    v
KB Category / Crop Mapping
    |
    v
NKO-10 Controlled KB Retrieval
    |
    v
Complete KB Records
``

### NKO-10 Controlled Results

The validated mappings were used to retrieve complete records from the current Masini Barokɛla Master Knowledge Base:

| Concept_ID | KB Category | Retrieved Records | Record Count | Result |
| --- | --- | --- | ---: | --- |
| AGRI-WATER | Irrigation | 6, 7, 8, 9, 10 | 5 | **RETRIEVED** |
| AGRI-SOIL-EARTH | Soil Management | 36, 37, 38, 39, 40 | 5 | **RETRIEVED** |
| AGRI-SEED | Seed Selection | 51, 52, 53, 54, 55 | 5 | **RETRIEVED** |

A combined retrieval using the three validated concepts returned all 15 supporting records.

The retrieved records preserve the complete 11-column Master Knowledge Base schema:

ID, Category, English Question, English Answer, French Question, French Answer, Bambara Question, Bambara Answer, Crop, Region, Season

The dedicated NKO-10 controlled retrieval test suite passed:

**7/7 tests passed**

The complete N’Ko experimental test group subsequently passed:

**92/92 tests passed in 1.82 seconds**

### NKO-10 Experimental Boundary

NKO-10 does **not**:

* accept arbitrary N’Ko text
* perform linguistic interpretation
* perform fuzzy matching
* call the production V5.3/V5.4 search engine
* modify search_question_v5_2
* modify app.py
* generate final answers
* change production retrieval logic

NKO-10 is therefore a controlled experimental retrieval layer and not a production retrieval layer.

---

## 8. NKO-11 End-to-End Experimental Validation

NKO-11 validates the complete isolated experimental N’Ko pipeline from an N’Ko query through controlled retrieval of supporting Master Knowledge Base records.

The validated path is:

```text
N’Ko Query
    |
    v
NKO-V5 Adapter
    |
    v
Validated Concept_ID
    |
    v
NKO-08 Concept Mapper
    |
    v
KB Category / Concept Mapping
    |
    v
NKO-09 Controlled KB Support Evaluation
    |
    v
NKO-10 Controlled KB Retrieval
    |
    v
Complete Supporting KB Records
    |
    v
NKO-12 Controlled Answer Assembly
    |
    v
Localized, Auditable Answer Package
```

### NKO-11 Validation Results

* NKO-12 controlled answer assembly: **8/8 tests passed**

The dedicated NKO-11 test module validates seven controlled cases:

* Water: N’Ko input resolves to **AGRI-WATER**, maps to **Irrigation**, passes controlled KB evaluation, and retrieves records **6–10**.
* Soil: N’Ko input resolves to **AGRI-SOIL-EARTH**, maps to **Soil Management**, and retrieves records **36–40**.
* Seed with context: N’Ko input plus the English context `seed` resolves to **AGRI-SEED**, maps to **Seed Selection**, and retrieves records **51–55**.
* Bare seed expression: remains **AMBIGUOUS** and stops at the adapter.
* Non-agricultural seed sense: resolves to **NON_AGRICULTURE** and stops at the adapter.
* Unknown N’Ko input: produces **NO_LEXICAL_MATCH** and stops at the adapter.
* Combined controlled retrieval: the three validated Concept_IDs retrieve all **15** supporting records.

The dedicated NKO-11 test suite passed:

**7/7 tests passed**

The combined Concept_ID retrieval test is a downstream integration/control test. It deliberately does not invent an unsupported multi-concept N’Ko sentence; the validated Concept_IDs are supplied directly to the mapper, evaluator, and retrieval layers.

### NKO-11 End-to-End Boundary

NKO-11 remains strictly experimental and isolated.

It does **not**:

* modify `app.py`
* modify `search_question_v5_2`
* activate direct production V5.3/V5.4 retrieval
* replace the production search engine
* perform unrestricted fuzzy retrieval from arbitrary N’Ko text
* generate production chatbot answers
* change the production retrieval logic

The end-to-end pipeline therefore demonstrates controlled technical feasibility without changing the production architecture.

---
---

## 9. NKO-12 Controlled Answer Assembly

NKO-12 introduces a controlled answer-assembly layer that consumes records already retrieved by the isolated NKO-11 pipeline and prepares a language-specific, auditable answer package.

NKO-12 does not independently retrieve knowledge, resolve N’Ko senses, perform fuzzy matching, or generate new agricultural advice.

### NKO-12 Answer Assembly Architecture

The NKO-12 assembler receives the retrieved result from NKO-11 and assembles the selected language’s question and answer while preserving supporting record metadata.

The supported answer-package languages are:

* English
* Français
* Bamanankan

The assembled package preserves the source record’s ID, question, answer, Crop, Region, and Season fields.

### NKO-12 Validation Results

The dedicated NKO-12 test module validates eight controlled cases:

* Water answer package in English
* Water answer package in French
* Water answer package in Bamanankan
* No retrieval result produces no answer package
* Invalid language produces no answer package
* Retrieved-record metadata is preserved
* Retrieval input is not mutated
* NKO-11 → NKO-12 water answer-package integration

The integration test runs the actual NKO-11 controlled pipeline for the validated N’Ko water input, passes its retrieved output to NKO-12, and verifies the resulting package and preserved metadata.

The dedicated NKO-12 test suite passed:

**8/8 tests passed**

### NKO-12 Experimental Boundary

NKO-12 remains strictly experimental and isolated.

It does **not**:

* modify `app.py`
* modify `search_question_v5_2`
* activate direct production V5.3/V5.4 retrieval
* replace the production search engine
* retrieve records independently
* generate new or unsupported agricultural advice

NKO-12 demonstrates controlled, localized answer-package assembly from retrieved knowledge while preserving the production architecture boundary.

---


## 10. Current Experimental Boundary and Checkpoint

At this stage, the N’Ko experimental subsystem has progressed through controlled KB support evaluation, controlled KB retrieval, isolated end-to-end pipeline validation, and controlled localized answer assembly.

Current validation status:

* NKO-01 through NKO-07A: validated
* NKO-V5 adapter: **8/8 tests passed**
* NKO-08 concept mapper: **7/7 tests passed**
* NKO-09 controlled KB evaluator: **7/7 tests passed**
* NKO-10 controlled KB retrieval: **7/7 tests passed**
* NKO-11 end-to-end validation: **7/7 tests passed**
* NKO-12 controlled answer assembly: **8/8 tests passed**
* Complete N’Ko experimental test group: **99/99 tests passed**
* Full project regression: **107/107 tests passed**
* Production V5.3/V5.4: **preserved and isolated**
* Working tree: **clean before this documentation update**
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
NKO-V5 Adapter
    |
    v
Validated Concept_ID
    |
    v
NKO-08 Concept Mapper
    |
    v
Experimental KB Category / Concept Mapping
    |
    v
NKO-09 Controlled KB Support Evaluation
    |
    v
NKO-10 Controlled KB Retrieval
    |
    v
Complete Supporting KB Records
    |
    v
NKO-12 Controlled Answer Assembly
    |
    v
Localized, Auditable Answer Package
```

No direct connection to the production V5.3/V5.4 retrieval engine has been activated.

Any future production integration should be introduced as a separately tested, reversible, and explicitly controlled stage, while preserving the current production boundary.
