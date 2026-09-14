# Masini Barokɛla — N’Ko Challenge
## Architecture and Current Status

**Project:** Mali Multilingual Agricultural Advisory — Masini Barokɛla  
**Experimental branch:** `feature/nko-challenge-nko01`  
**Current checkpoint:** `98f80f2`  
**Status:** Experimental N’Ko subsystem validated through NKO-07A  
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