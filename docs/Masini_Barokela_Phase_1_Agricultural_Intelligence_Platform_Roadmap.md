# Masini Barokɛla — Phase 1
## Agricultural Intelligence Platform Architecture and Roadmap

**Document status:** Initial architecture proposal
**Phase:** 1 — Platform Foundations and Controlled Expansion
**Project:** Masini Barokɛla
**Initiative:** Masini AI Initiative

---

## 1. Purpose

Masini Barokɛla is an agricultural intelligence and advisory platform that
organizes agricultural knowledge and helps users make better-informed
production decisions.

The purpose of Phase 1 is to establish a controlled architectural path from
the existing multilingual agricultural advisory chatbot toward a broader
agricultural intelligence platform.

Phase 1 will prioritize trustworthy agricultural knowledge, traceable
evidence, relevant contextual information, measurable quality, and incremental
implementation.

This document defines the proposed direction. It does not claim that planned
capabilities have already been implemented.

## 2. Architectural Principles

The following principles govern Phase 1.

1. Preserve validated production behavior unless a change is explicitly
   authorized and validated.
2. Build incrementally, with a defined purpose and acceptance criteria for
   every new capability.
3. Distinguish verified evidence, source-attested information, expert
   judgments, hypotheses, and unverified claims.
4. Represent uncertainty honestly. The platform must not manufacture
   agricultural facts or present unsupported recommendations as established
   knowledge.
5. Keep agricultural concepts, user language, writing system, and retrieval
   behavior conceptually distinct.
6. Design for Mali's agricultural contexts while avoiding assumptions that
   all regions, crops, soils, seasons, and farming systems are identical.
7. Prefer free or low-cost, maintainable tools when they meet project needs.
8. Validate every material change through reproducible tests and documented
   review.
9. Preserve human review for consequential or insufficiently supported
   agricultural recommendations.
10. Separate architectural proposals from implemented and validated
    capabilities.

## 3. Existing Technical Baseline

The following repository artifacts provide the initial reference baseline.

- `docs/Masini_Barokela_V5.3_Architecture_and_Validation.md`
- `docs/Masini_Barokela_V5.4_Development_Roadmap.md`
- `docs/Masini_Barokela_NKO_Challenge_Architecture_and_Current_Status.md`
- `data/Masini_Barokela_Master_Knowledge_Base.tsv`
- `data/knowledge_base_v5.json`
- `data/Masini_Barokela_Context_Pilot_v1.tsv`

The precise contents and current status of these artifacts should be checked
against the repository whenever implementation decisions depend on them.

### 3.1 Production retrieval

V5.3 provides the documented search and intent foundation. Its freeze decision
establishes the validated baseline for subsequent regression testing.

V5.4 documents the controlled integration direction, including knowledge-base
expansion, multilingual expansion, evaluation, search robustness, safety and
relevance, conversation context, and production readiness.

Phase 1 must respect these version-specific decisions. It must not silently
replace the production retrieval system or treat experimental components as
production-ready.

### 3.2 Agricultural knowledge and evidence

The existing knowledge base provides the initial agricultural knowledge
foundation.

The answer-level evidence review and context-pilot work provide a path toward
assessing the support for individual agricultural answers.

Evidence-review statuses must retain their documented meanings. In particular,
source attestation must not automatically be interpreted as independent
scientific validation.

### 3.3 N'Ko research

The N'Ko challenge is a separate experimental workstream.

Its detector, normalization, lexical resolution, and concept-mapping work
should remain isolated from production retrieval until explicit integration
criteria have been established and passed.

N'Ko is a writing system that can represent Manding languages; it must not be
treated as a separate spoken language.

## 4. Phase 1 Objectives

Phase 1 has six principal objectives.

1. Establish a clear architecture for agricultural intelligence.
2. Improve the traceability and reviewability of agricultural advice.
3. Define a structured representation of agricultural concepts and context.
4. Establish a reliable evaluation framework for existing and new capabilities.
5. Identify suitable data sources for future regional, seasonal, and crop-level
   intelligence.
6. Create a controlled implementation roadmap with measurable acceptance
   criteria.

## 5. Scope and Boundaries

### 5.1 In scope

- Architecture and repository documentation.
- Knowledge-base quality and evidence assessment.
- Agricultural concept and context modeling.
- Evaluation datasets and repeatable tests.
- Language and writing-system boundaries.
- Research into relevant agricultural data sources.
- Small, independently testable prototypes.
- Future integration planning for regional and seasonal information.

### 5.2 Not automatically in scope

The following capabilities are not assumed to exist or become production
features merely because they appear in this roadmap:

- Operational weather forecasting.
- Rainfall prediction or climate modeling.
- Drought monitoring and geospatial dashboards.
- Crop-yield prediction.
- Automated diagnosis of crop diseases or pests.
- Farm-specific fertilizer or pesticide prescriptions.
- Fully integrated N'Ko production support.
- Autonomous agricultural decision-making.

Each capability requires a separate feasibility assessment, appropriate data,
defined limitations, validation, and an explicit integration decision.

## 6. Proposed Target Architecture

The following logical layers describe the intended direction. They are an
architectural proposal, not a claim that all layers already exist as separate
software modules.

### Layer 1 — User interaction

Responsibilities:

- Receive agricultural questions.
- Present answers in supported interface languages.
- Communicate clarification requests and limitations.
- Provide understandable explanations and references where available.

The existing application remains the starting point.

### Layer 2 — Language and query interpretation

Responsibilities:

- Identify the language or writing system when supported.
- Normalize queries without destroying meaningful distinctions.
- Identify agricultural concepts and relevant intent.
- Handle ambiguity and insufficient information explicitly.

Experimental N'Ko processing remains separate until integration is approved.

### Layer 3 — Agricultural knowledge

Responsibilities:

- Organize agricultural knowledge by topic and concept.
- Retain relevant crop, location, season, and farming-context information
  where available.
- Maintain stable identifiers and traceable relationships.
- Distinguish established records from proposed or unverified additions.

### Layer 4 — Evidence and quality

Responsibilities:

- Associate answers and claims with identifiable sources where possible.
- Record source type, review status, limitations, and relevant qualifications.
- Identify unsupported, outdated, conflicting, or ambiguous claims.
- Provide a review path for consequential recommendations.

Evidence status must be represented accurately and must not be inferred from
the mere presence of a source URL.

### Layer 5 — Agricultural context

Potential contextual dimensions include:

- Crop and crop variety.
- Geographic area.
- Agricultural season and growth stage.
- Soil and water conditions.
- Weather and rainfall observations.
- Pest and disease observations.
- Farming practices and resource constraints.

Context should only influence an answer when the required information is
available and sufficiently reliable. Missing context must not be silently
invented.

### Layer 6 — Intelligence and analytical services

Future services may include:

- Context-aware retrieval.
- Rules-based agricultural guidance.
- Summaries of relevant observations and trends.
- Comparisons across regions or seasons.
- Statistical analysis and predictive models when justified by suitable data.

These services must be independently testable. Predictive models must not be
presented as operational merely because a prototype produces an output.

### Layer 7 — Evaluation, monitoring, and governance

Responsibilities:

- Regression testing.
- Retrieval relevance and answer-quality evaluation.
- Evidence-quality review.
- Language-specific testing.
- Logging and investigation of failures where appropriate.
- Versioning, release decisions, and rollback planning.

Privacy, data minimization, maintainability, and human review apply across
the architecture rather than belonging to only one layer.

## 7. Proposed Data and Knowledge Strategy

### 7.1 Knowledge records

Future knowledge-base improvements should consider stable record identifiers,
category, agricultural concept, crop applicability, language, answer content,
source attribution, review status, and relevant qualifications.

Additional fields should be introduced only when their meaning, ownership,
validation, and effect on existing code are understood.

The current knowledge-base schema must be inspected before any migration.

### 7.2 Evidence management

Evidence work should distinguish at least the following concepts:

- **Source identified:** a potentially relevant source has been located.
- **Source attested:** the recorded source has been associated with the claim
  according to the project's documented review procedure.
- **Claim validated:** the claim has been assessed against defined validation
  criteria.
- **Review required:** uncertainty, ambiguity, or insufficient evidence
  remains unresolved.

The project must define the operational meaning of each status and preserve
the distinctions already used in existing evidence-review artifacts.

### 7.3 External agricultural data

Potential sources for future evaluation include rainfall observations,
weather records, soil information, crop statistics, vegetation indicators,
agricultural research, and official technical guidance.

Before adopting a source, assess:

- Authority and scientific suitability.
- Geographic and temporal coverage.
- Spatial and temporal resolution.
- Update frequency and data completeness.
- Licensing and permitted use.
- Processing requirements and reproducibility.
- Limitations and uncertainty.

No external dataset should be incorporated into production solely because
it is publicly accessible.

## 8. Language and Concept Strategy

Masini Barokɛla serves multilingual agricultural communication. Language
support and agricultural knowledge quality are related but distinct concerns.

Phase 1 should preserve this distinction:

1. A user query is expressed in a language and possibly a writing system.
2. Query interpretation identifies relevant meaning and agricultural intent.
3. Agricultural concepts connect the query to applicable knowledge.
4. Evidence and context determine what can responsibly be answered.
5. The response is presented in a supported language.

N'Ko experiments should continue to use explicit normalization, lexical
resolution, ambiguity handling, and concept mapping.

No experimental mapping should be assumed correct for every dialect,
spelling, or agricultural context. Authoritative examples and review criteria
must be established before wider integration.

## 9. Evaluation and Acceptance Framework

Every new capability must have defined tests before it is accepted.

The evaluation framework should include:

- Correctness of expected answers.
- Retrieval relevance and resistance to misleading matches.
- Appropriate handling of ambiguous queries.
- Unsupported-answer and uncertainty handling.
- Crop and context specificity.
- Language-specific behavior.
- Regression against established tests.
- Traceability of evidence.
- Performance and operational cost where relevant.

Existing test suites must be identified and their actual results recorded.
Historical pass counts are useful evidence of prior validation, but they do
not establish that the current checkout passes without a new test run.

A release candidate must not be accepted solely because it passes a narrow
set of new tests. Relevant existing regression tests must also pass.

## 10. Implementation Roadmap

The stages below are proposed sequencing, not a claim of completed work.

### Phase 1A — Architecture and baseline

Deliverables:

- This architecture and roadmap document.
- Inventory of current production components and dependencies.
- Mapping of existing validation records and test suites.
- Explicit separation of production, research, and proposed capabilities.

Acceptance criteria:

- Existing architecture documents are referenced accurately.
- Unverified implementation assumptions are recorded as open questions.
- Production boundaries and validation requirements are documented.

### Phase 1B — Knowledge and evidence quality

Deliverables:

- Review of the current knowledge-base schema.
- Assessment of existing answer-level evidence records.
- Documented evidence-status definitions.
- Prioritized list of knowledge gaps and ambiguities.

Acceptance criteria:

- Existing records are preserved unless a separately reviewed change is
  authorized.
- Review status and evidence limitations are traceable.
- Proposed changes have explicit validation criteria.

### Phase 1C — Agricultural concept and context model

Deliverables:

- Initial concept model for selected agricultural topics.
- Definitions for relevant crop, region, season, and growth-stage context.
- Mapping proposal connecting concepts to existing knowledge records.
- Tests for ambiguity and missing context.

Acceptance criteria:

- Concepts have clear meanings and stable identifiers where needed.
- Mappings are reviewable and testable.
- Missing information does not silently become assumed fact.
- Existing retrieval behavior remains unchanged until integration is approved.

### Phase 1D — Data-source feasibility

Deliverables:

- Shortlist of relevant agricultural data sources.
- Source-quality and licensing assessment.
- One narrowly scoped analytical use case selected for investigation.
- Data-quality and validation plan.

Acceptance criteria:

- The selected source is suitable for the intended question.
- Coverage, limitations, and update requirements are documented.
- The proposed use case is feasible with available resources.
- No predictive accuracy claim is made without an appropriate evaluation.

### Phase 1E — Controlled prototype

Deliverables:

- One independently testable prototype based on the selected use case.
- Defined inputs, outputs, limitations, and failure behavior.
- A small evaluation dataset and reproducible tests.
- A documented decision on whether integration is justified.

Acceptance criteria:

- Prototype results are reproducible.
- Known limitations are visible to reviewers.
- Relevant existing regression tests pass if shared components are involved.
- Production integration requires a separate explicit decision.

### Phase 1F — Integration readiness review

Deliverables:

- Integration proposal and dependency assessment.
- Security, privacy, performance, and maintainability review as applicable.
- Regression and acceptance-test results.
- Rollback plan and documented release decision.

Acceptance criteria:

- The feature meets its defined quality requirements.
- Existing production behavior is protected by relevant regression tests.
- Evidence and uncertainty are represented appropriately.
- The integration decision and remaining risks are documented.

## 11. Change-Control Rules

Until a specific implementation task is approved:

- Do not modify the frozen V5.3 retrieval behavior.
- Do not silently replace V5.4 integration decisions.
- Do not connect experimental N'Ko modules to production retrieval.
- Do not alter production knowledge-base records as part of architecture drafting.
- Do not delete or rename existing documentation or data artifacts.
- Do not introduce dependencies without documenting their purpose.
- Do not treat an experimental result as a validated production capability.

For any approved code change:

1. Identify the files and behavior affected.
2. Define expected behavior and acceptance tests.
3. Make the smallest appropriate change.
4. Run targeted tests.
5. Run relevant regression tests.
6. Inspect the diff and repository status.
7. Document the result and commit only after review.

## 12. Initial Risks and Open Questions

The following items require investigation rather than assumption:

- Which V5.4 integration capabilities are present in the current checkout?
- What are the current knowledge-base schema and data-quality limitations?
- Which agricultural claims still require stronger evidence?
- Which crop and geographic context should be prioritized first?
- Which external datasets offer adequate coverage and permitted use?
- What is the smallest useful intelligence prototype for Mali?
- How should agricultural experts participate in validation?
- What measurable thresholds are appropriate for each proposed capability?
- Which multilingual and N'Ko capabilities are ready for further evaluation?

These questions should be resolved incrementally as their answers become
necessary for implementation.

## 13. Definition of Phase 1 Success

Phase 1 will be successful when the project has:

- A documented and reviewed target architecture.
- A clear separation between existing, experimental, and proposed capabilities.
- A traceable approach to agricultural evidence and knowledge quality.
- An initial, testable agricultural concept and context model.
- A justified data-source and prototype choice.
- Reproducible acceptance and regression tests.
- A documented integration decision based on evidence rather than assumption.

The objective is not to add the largest number of features. It is to establish
a reliable foundation on which agricultural intelligence can be developed
incrementally and responsibly.

## 14. Relationship to Existing Documentation

This document complements rather than replaces:

- `docs/Masini_Barokela_V5.3_Architecture_and_Validation.md`
- `docs/Masini_Barokela_V5.4_Development_Roadmap.md`
- `docs/Masini_Barokela_NKO_Challenge_Architecture_and_Current_Status.md`

The version-specific documents remain the references for their respective
technical workstreams. This Phase 1 document defines the broader agricultural
intelligence direction and its proposed implementation sequence.

---

**Next action:** review this document, verify its alignment with the current
repository, and commit it only after the review is complete.
