# Masini Barokɛla V5.3
## Architecture and Validation Record

**Project:** Mali Multilingual Agricultural Advisory Chatbot  
**Version:** V5.3  
**Freeze Commit:** `ed9e688`  
**Branch:** `main`  
**Validation Status:** PASS — 84/84 formal tests + 4/4 targeted French smoke tests

---

## 1. V5.3 Purpose

V5.3 is the controlled search and intent-detection stabilization release of the Masini Barokɛla agricultural advisory system.

The principal objective was to eliminate the major V5.2 search-loop behavior in which a General knowledge-base record could incorrectly outrank a crop-specific record even when the user's intent and crop were correctly detected.

V5.3 preserves the General-record fallback behavior while introducing intent-aware crop specificity.

---

## 2. Core Architecture

The V5.3 search pipeline consists of:

1. User question
2. Language detection/routing
3. Intent detection
4. Crop detection
5. Intent-to-category mapping
6. Candidate filtering
7. Intent-aware crop specificity
8. Multicomponent similarity scoring
9. Candidate intent validation
10. Confidence thresholding
11. Best-match selection

The principal modules are:

- `utils/intent_v5.py`
- `utils/search_v5_2.py`
- `data/knowledge_base_v5.json`

---

## 3. Intent Detection

`detect_intent_v5()` identifies the agricultural domain, specific sub-intent, and crop where applicable.

Examples include:

- `PLANTING_TIME`
- `PLANTING_DEPTH`
- `PLANTING_SPACING`
- `PLANTING_IMPORTANCE`
- `GENERAL`

Crop normalization supports, among others:

- Millet
- Maize
- Rice
- Sorghum
- Cotton
- Groundnut

English, French, and Bambara language routing are supported.

---

## 4. Candidate Filtering

The V5.3 candidate filter preserves both crop-specific and General records when appropriate.

The logic is:

- Apply category filtering when matching records exist.
- Apply crop filtering while retaining records whose crop is `General`.
- Preserve the existing candidate pool when a crop-specific record does not exist.

This prevents the loss of useful General knowledge-base records.

---

## 5. Intent-Aware Crop Specificity

V5.3 introduces a surgical refinement inside `search_question_v5_2()`.

When:

- a crop is detected,
- a specific sub-intent is detected, and
- crop-specific records exist for that intent,

the search is restricted to those crop-specific records.

If no crop-specific record exists for that intent, the existing candidate pool is retained so that a General record can serve as the fallback.

This resolves the key V5.2 failure mode without breaking General fallback behavior.

---

## 6. Scoring Model

Candidate relevance uses a weighted composite score:

- WRatio: 45%
- Token similarity: 25%
- Meaningful-token coverage: 30%

Additional mechanisms include:

- Exact meaningful-token bonus: +20
- Intent-alignment bonus: +10
- Score capped at 100

Specific intents use the configured minimum score threshold of 70.

General intent requires a higher confidence threshold of 85.

---

## 7. Critical V5.2 Bug Resolved

The problematic behavior occurred when a question such as:

`Quelle est la meilleure période pour planter le maïs ?`

correctly detected:

- Intent: `PLANTING_TIME`
- Crop: `Maize`

but could nevertheless return the General planting-time record instead of the Maize-specific record.

A first attempted correction restricted filtering too aggressively and caused the opposite problem: Millet planting-time questions failed because no Millet-specific planting-time record existed.

The final V5.3 solution therefore uses intent-aware crop specificity with General fallback.

---

## 8. Targeted French Validation

The four critical French cases were validated successfully:

| Question type | Expected record | Result |
|---|---:|---:|
| Millet planting time | ID 1 | PASS |
| Maize planting time | ID 2 | PASS |
| Millet planting depth | ID 3 | PASS |
| Maize planting spacing | ID 4 | PASS |

**Targeted smoke test: 4/4 — 100%**

---

## 9. Regression Validation

The intent regression suite produced:

**37/37 PASS — 100.0%**

No regression failures were detected.

---

## 10. End-to-End Integration Validation

The V5.2/V5.3 integration suite produced:

**18/18 PASS — 100.0%**

All expected IDs and corrected intent expectations were validated successfully.

The four French test cases were updated to reflect the specific intent semantics implemented by V5.3.

---

## 11. V5.3 Robustness Validation

The V5.3 robustness suite produced:

**29/29 PASS — 100.0%**

The suite covered English, French, Bambara, paraphrased questions, and negative cases.

Negative cases correctly returned no match where appropriate.

---

## 12. Overall Validation

Formal validation:

- Intent regression: 37/37
- Integration: 18/18
- Robustness: 29/29

**Combined formal result: 84/84 — 100.0%**

Additional targeted French smoke test:

**4/4 — 100%**

V5.3 therefore reached the defined freeze criteria.

---

## 13. Git Freeze State

At the freeze-point inspection:

```text
On branch main
Your branch is up to date with 'origin/main'.

nothing to commit, working tree clean
```

Current commit:

```text
ed9e688 (HEAD -> main, origin/main, origin/HEAD) Changed "expected_intent"
```

The V5.3 validated state is therefore synchronized between the local `main` branch and `origin/main`.

---

## 14. Freeze Decision

**V5.3 STATUS: FROZEN**

No further functional modifications should be made to the V5.3 search or intent-detection implementation unless a new defect is discovered that requires reopening the release.

Future development should proceed as V5.4 work rather than modifying the frozen V5.3 behavior.

---

## 15. Recommended Next Phase

The next development phase is **Masini Barokɛla V5.4 System Integration**.

V5.4 should build on the frozen V5.3 search and intent foundation and focus on controlled integration with the broader chatbot application.

V5.3 should remain the validated baseline for subsequent regression testing.