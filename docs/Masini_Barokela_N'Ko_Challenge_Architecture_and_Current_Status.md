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
```

No direct connection to the production V5.3/V5.4 retrieval engine has yet been activated.

Any future integration should be introduced as a separately tested and reversible stage.

---

## 6. Current Checkpoint

At this stage, the N’Ko experimental subsystem has been validated through the NKO-V5 adapter boundary.

Current validation status:

- NKO-01 through NKO-07A: validated
- NKO-V5 adapter: **8/8 tests passed**
- Full project regression: **71/71 tests passed**
- Production V5.3/V5.4: **preserved and isolated**
- Working tree after validation: **clean**

The next development stage should focus on controlled evaluation of how validated N’Ko agricultural concepts could be mapped to existing Masini Barokɛla knowledge-base concepts, without directly modifying the production search engine.
