# Founding Charter — Coherent Receiver Theory and Design

**Status:** governing project intent; technical implementation choices below are provisional until specifically accepted.

## Mission
Develop an exceptionally comprehensive, mathematically rigorous, scientifically defensible and practically applicable advanced engineering **textbook and reference** on coherent receiver theory and engineering. The audience is experienced RF engineers, including engineers with little previous specialization in coherent receivers. Codex CLI is the principal AI-assisted development environment, **not** the book's primary audience.

## Primary success criterion
After systematic end-to-end study, a qualified RF engineer should be able to approach unfamiliar coherent receiver development problems and proceed from operational need through requirements, feasibility, architecture selection, system budgets, subsystem design, synchronization, calibration, physical implementation, integration, verification and production planning, using this book as the **primary technical and methodological reference**. Component-specific information, current standards and specialized implementation details may require external sources. The book must not omit essential coherent-receiver-specific reasoning and expect the reader to reconstruct it elsewhere.

## The kind of book
- Advanced, coherent textbook **and** practical engineering design handbook.
- First principles where consequential, with derivations, assumptions, limiting cases, physical interpretation and applicability conditions.
- Integrated system reasoning: why subsystem interactions and correlations determine achievable performance.
- Learning sequence for a human engineer and practical reference navigation for future use.
- Genuine generalization to unfamiliar requirements and architectures, not memorization of worked examples.
- Contrast idealized models with nonideal hardware, calibration limitations, actual waveforms, instrument limitations and production variability.

## Required domain breadth
1. Operational needs, systems methods, specifications, feasibility and traceability.
2. Coherence definitions; complex signals, stochastic phase, correlation, spectra, estimation and synchronization.
3. Receiver architecture, frequency planning, noise, linearity, dynamic range and system error budgets.
4. RF and analog frontend, frequency conversion, synthesizers, LO/clock/reference distribution.
5. Data conversion, I/Q, digital downconversion, timing and carrier recovery, FPGA/processor consequences.
6. Multichannel coherence, amplitude/phase/delay alignment, observability, calibration and drift.
7. PCB, power, signal integrity, EMI, thermal, mechanical and environmental implementation.
8. Analytical/computational modeling, sensitivities, uncertainty, verification and measurement.
9. Manufacturing, production test, yield, reliability, configuration and lifecycle.
10. Carrier-coherent communications, arrays/DF, coherent radar/sensing and phase measurement applications.

This list describes coverage goals, **not** the final table of contents.

## Rigorous technical standards
Distinguish mathematical correctness, computational implementation correctness, physical validity, engineering adequacy and demonstrated compliance. Never claim a model is physically validated because its software tests pass. Distinguish one-/two-sided spectra, reference planes, phase accuracy/stability/repeatability, common/differential errors, deterministic/stochastic behavior, observation time, operating state and calibration dependence. Define uncertainty and identify incomplete evidence. Source citations must support the actual claims and not be fabricated.

## Scope control without dilution
- Full internal development for essential coherent-receiver reasoning.
- Selective internal development for adjacent supporting disciplines.
- Established general engineering theory and device-specific facts may be referenced externally.
- Evaluate adequacy by conceptual understanding **and** the ability to calculate, make design decisions and verify them.
- Use complete reference designs plus contrasting cases and failure analyses to check generalizability.
- Do not use page count or number of generated files as a quality metric.

## Human authority and completion
Codex may draft, research, derive, compute, check and identify issues. It cannot approve consequential engineering results on its own. Acceptance needs suitable evidence and human technical review for the declared use. Acceptance is scoped and revisable, not infallibility. Material may be released in usable intermediate editions with explicit limitations.

## Development philosophy
Use bounded technical units, minimum sufficient assurance, continuous readable outputs, consistent notation, source provenance and modest version-controlled evidence. Avoid large knowledge graphs, custom publishing engines and autonomous multi-agent infrastructure until warranted. Technical quality is uncompromising; process complexity should be proportionate.

## Immediate sequence
1. Develop the foundational reader competence and engineering capability inventory.
2. Use it with candidate reference designs to establish technical scope, dependencies and a provisional intellectual architecture.
3. Evaluate mathematical authoring/publishing tools through a genuine pilot.
4. Develop a pilot on relative phase stability in a two-channel coherent receiver from observable requirement through model, architecture choices and verification plan.
5. Revise the development system on evidence, then author progressively.

## Original intent and authority
This charter consolidates the user's clarified objective and agreed development philosophy. It does **not** claim that an inventory, chapter, design, calculation, physical model or review has been technically accepted. Requirements of the book are distinguished from provisional toolchain and repository choices in `project/decisions/`.
