# ADR-0004 — Provisional Book Architecture Acceptance for Textbook Development

**Status:** provisionally accepted by the project owner for the limited use below. **Decision recorded:** 2026-10-29. **Authority:** the project owner's explicit stage-closeout instruction, following external AI-assisted review. No independent specialist approval or unprovided review findings are asserted.

## Decision and accepted artifacts

Accept the following package as suitable for **guiding textbook development** and close the provisional book-architecture and annotated-table-of-contents stage. The artifacts are identified by SHA-256 of their exact working-tree bytes immediately before this administrative closeout:

| Artifact | SHA-256 before administrative updates |
|---|---|
| [book-architecture](../book-architecture.md) | `ae968f5e7bd26d9753e4b023d43adf1fd94662a40195514f756d527d6a4f1908` |
| [annotated-toc](../annotated-toc.md) | `d27d8e1fd2855a2f1830cdcfad3c8cacf32f6092acbde3cc477db5222b3e6494` |
| [book-coverage](../book-coverage.md) | `1f83a6d07ded5d59f6b600db18ccdd26fcad111714a205792dbbcd624f3206b5` |

Repository HEAD at acceptance capture was `f44759b78d7ad2c44329cc27a68d5386dd63db98`. The planning artifacts were staged additions, not contents of that committed revision; the file hashes above identify the accepted package. Subsequent status/link updates do not change its chapter/section organization or technical obligations. No commit or tag is created by this closeout.

## Review qualifications

1. **Foundational progression:** Chapters 1–7 must connect mathematical foundations to meaningful receiver-engineering questions and consequential calculations early enough to sustain understanding and practical relevance.
2. **Integrated designs:** D-COM, D-ARR, D-RAD and D-MET must eventually provide continuous engineering developments covering requirements, feasibility, architecture tradeoffs, budgets, subsystem decisions, implementation, calibration, verification, production implications and justified design iteration. Scattered examples alone are insufficient.
3. **Flexible organization:** the five parts, 32 chapters and four sections per chapter are provisional. Revise boundaries when mathematical dependencies, practical depth or pedagogical needs justify it; structural uniformity is not a requirement. This administrative closeout does not rewrite the table of contents.
4. **Continuing qualifications:** [ADR-0002](ADR-0002-provisional-competence-baseline.md), [ADR-0003](ADR-0003-provisional-architecture-acceptance.md), inventory U-01–U-10 and technical coverage §6 dispositions, unresolved mathematical conventions, specialist application boundaries and evidence limitations remain in force. In particular preserve early motivation before full application prerequisites, accessible K02–K07 bridges, explicit interferometry/vector antenna/polarization/application-processing boundary review, and later testing of actual educational and engineering adequacy.

## Limits and consequences

Acceptance is limited to planning suitability. It does not establish mathematical correctness, physical-model validity, educational effectiveness, experimental verification or receiver-performance compliance. External AI-assisted review is not independent physical evidence. No new source examination, derivation, model execution, measurement or learner assessment is claimed. Capability definitions, canonical treatment specifications and reference-design briefs remain unchanged; a significant discovered weakness requires a documented proposed correction and human decision.

[Current work](../current-work.md) records closure, checks and continuing issues. Technical authoring standards development, publishing validation and the initial dual-channel relative-phase-stability pilot are subsequent work, **not yet started**. Their mention does not authorize execution. No manuscript drafting, substantial derivations, computational modeling or publishing infrastructure begins here.
