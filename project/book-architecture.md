# Provisional Book Architecture

**Status:** provisionally accepted by the project owner on 2026-10-29 as suitable for guiding textbook development under [ADR-0004](decisions/ADR-0004-provisional-book-architecture-acceptance.md), following external AI-assisted review and subject to its four review qualifications. Acceptance does not establish mathematical correctness, physical-model validity, educational effectiveness, experimental verification or receiver-performance compliance. No manuscript, derivation, engineering model or solved design is produced by this stage.

## 1. Authority and recommendation

The [charter](charter.md) defines success: an experienced RF engineer should learn coherent receiver engineering systematically and subsequently use the book as the primary technical and methodological design reference. The [inventory](competence-inventory.md), [technical architecture](architecture.md), [canonical coverage](technical-coverage.md) and [design briefs](reference-design-plan.md) remain authoritative for their respective responsibilities under ADR-0002/0003. This document assigns exposition and navigation; it does not replace their capability definitions, dependencies or treatment obligations.

Recommend five parts containing the 32 provisional chapters in the [annotated contents](annotated-toc.md). This count results from grouping coherent reasoning responsibilities; it is neither a target nor a commitment to volumes or length. Chapter numbers locate exposition; K/A and CAP identifiers retain their accepted meanings.

| Part | Chapters | Intellectual purpose and exit ability |
|---|---|---|
| I — Observables and reasoning | 1–7 | Begin with engineering comparisons, then acquire probability, observation, matrix, inference, model-adequacy and control bridges. Explain what can be observed, estimated and tracked, with assumptions and failure regions. |
| II — Physical models and system decisions | 8–13 | Construct field/noise inputs, extraction and transfer models; compare feasibility and allocations; establish calibration observability and operational metrology. Turn a qualitative need into conditional quantitative decisions and testable observables. |
| III — Signal and reference realization | 14–20 | Develop analog, reference, converter, quadrature, processing and correction methods. Select compatible interfaces and distinguish identifiable from realizable correction. Analog, sampled and distributed branches are conditional. |
| IV — Valid operation and engineering evidence | 21–25 | Integrate states and physical/environmental constraints, execute valid calibration, assess requirements evidence and production/service consequences. Connect configuration and operating envelopes to bounded claims. |
| V — Application synthesis | 26–32 | Complete seven distinct residual-to-task mappings and integrated design developments. Transfer shared reasoning to unfamiliar waveforms, geometries, references and measurands. |

Part V consolidates quantitative application treatments; applications enter Chapter 1 and recur in every part. Its location does not prohibit earlier application calculations using explicitly supplied mappings. Part IV supplies complete engineering methods; physical constraints, test access, state validity and production consequences already appear in Chapters 1, 8–20. Its methods are not optional concluding advice.

## 2. Alternative organizations and comparative routes

Three plausible candidates were compared as editorial proposals, not through learner trials. Each must retain all accepted obligations.

| Candidate | Major grouping and treatment placements | Representative route and benefit | Concrete weakness / disposition |
|---|---|---|---|
| Foundation–subsystem–application blocks | K01–K10 foundations; K11–K20 systems/chains; K21–K26 calibration/evidence/lifecycle; A35–A41 applications | Phase-noise question: statistics → physical disturbance → synthesis → radar. Clear ownership and concise lookup. | Calibration observability/metrology arrive after hardware choices that require test access. A long abstract opening delays why observation matters. Retain its canonical ownership but move problems and measurement reasoning earlier. |
| Application-led | Communications, radar, arrays, DF, interferometry, sensing and instruments each develop necessary shared methods, with a shared reference core | Start with a burst receiver, learn inference and tracking in context. Immediate task relevance. | Interferometry repeats covariance/finite-record theory; array-first readers may meet rank before its bridge. Either repetition or continual jumps are required. Use application-led reference routes, not seven independent foundation sequences. |
| Concept-led with recurring designs — recommended | Parts I–V above; early observables/metrology; recurring D-COM/ARR/RAD/MET; independent P-DF/INT/SEN | Burst question: 1 → 2/3/5/7 → 9/10/12 → 14/17/19 → 26. Instrument question: 1/3/5/6 → 11/12/13 → 24/32 with selected analog realization. | Long shared core still risks delaying task payoff. Chapter-level design revisits, early calculations with supplied inputs and distinct previews mitigate this; actual pilot must test whether they suffice. |

A lifecycle baseline would order need → architecture/budgets → subsystem design → integration/calibration → verification/production. Its engineering familiarity is useful for lookup, but teaching quantitative budgets before physical source models hides prerequisites; designing calibration after hardware hides observability/access constraints. Retain lifecycle completeness checks and cross-references rather than that sequence.

No candidate is selected by a numerical coverage score. The recommended choice balances accessible dependencies, theory cohesion and practical lookup. Its strongest unresolved risk is whether the mathematical bridges and early examples provide enough payoff before complete applications.

## 3. Teaching, examples and reference navigation

### Development rules

Each substantial treatment connects an engineering question to physical explanation, mathematical development, a calculation/decision, realization constraints and discriminating evidence. Chapter annotations specify obligations rather than completed results. They use a consistent review card without imposing identical prose structures on all eventual chapters.

Keep full general derivations at one canonical home. Local introductions may restate definitions, interpret a result, summarize assumptions and explain why it applies. Applications must derive their own waveform/geometry/measurand mapping, not copy shared theory or merely substitute a universal RMS phase metric. Scalar introductions and later matrix/physical refinements are labeled where their prerequisites differ.

Develop K02–K07 internally from calculus, elementary Fourier/LTI and RF practice. Do not assume probability, circular statistics, cross-spectra, conditioning, likelihood or control expertise. Appendix remediation cannot carry essential steps needed for the main argument. Reader baseline checks will eventually test actual reasoning rather than professional tenure.

### Example hierarchy

- Local worked calculations isolate a mechanism with explicit inputs, planes, conventions and limits.
- Contrasting cases change an assumption or architecture and require rejection of a plausible wrong conclusion.
- Four substantial reference designs accumulate coherent work products, culminating in integrated developments in Chapters 26, 27, 28 and 32; those chapters link their earlier stages into a continuous design account.
- Independent bounded examples in Chapters 29–31 teach DF ambiguity, stochastic interferometric sensitivity and physical-signal retention. They may expand if specialist review reveals substantial unshared reasoning.
- Transfer assessments change the model: shared to independent references, narrow to wide bandwidth, injection to field calibration, deterministic to stochastic input, or a different measurand. Changing numbers alone is insufficient.

[Coverage and staging](book-coverage.md) assigns each revisit and failure probe. All numerical product requirements, platforms and distribution data remain unselected. Illustrative assumptions must be labeled; missing evidence cannot become a closed budget.

### Reference routes after sequential study

| Entry question | Route to result, method and evidence |
|---|---|
| Is the requirement jointly feasible? | 1 observables → 12 feasible region; 5/10 information, 9 physical sources, 14/17 headroom; relevant application mapping → 24 evidence. |
| What LO/clock performance is needed? | 11 reference transfer → 9 disturbance generation → 12 allocation → 15/17 selection → 27 or other task consequence → 13/24 test limits. |
| What can calibration recover? | 13 observability → 18/20 correction feasibility → 23 procedure → 13 independent uncertainty; 8 for paths injection misses. |
| Why does coherence fail after retune/outage? | 21 state/identity → 11/15/16/19 suspected mechanism → 13 diagnostic evidence → 24 justified transition exposure. |
| Does a quieter residual improve the sensor? | 1 measurand → 7 desired-signal transfer → 23 maintenance → 31 physical inference → 13/24 independent evidence. |
| Can the design be produced and maintained? | 25 joint variation/test effort/change → 12 budgets, 22 physical sensitivities, 23 correction validity, 21 configuration, 24 decision rules. |

Analog instrument route: 1–6 as needed → 11/12/13 → selected 14/15 → 24/32. It does not require converter, DSP or multichannel correction chapters. Analog array route adds 4/8/9/10/20/28 and selected reference/calibration methods; 17/19 are added only for sampled realization. These are lookup routes, not claims that all transitive prerequisites can be skipped by a new reader.

Appendices provide convention lookup after human decisions, supporting RF/mathematical refreshers, unit/representation translations, and calculation/measurement navigation aids. They do not own a second version of essential theory. No index or publishing system is implemented now; the proposed book needs subject/result and symbol lookup at authoring time.

## 4. Risks, boundaries and review decisions

The [coverage audit](book-coverage.md) records authorial traceability findings. Mapping establishes intended support, not educational or engineering adequacy. No sources were newly examined; existing S1–S9 evidence retains its narrow scope. Future result-level research must use the existing bibliography/source-note process and distinguish derived, assumed, simulated, externally reported and measured results.

| Decision / risk | Proposed boundary or mitigation | Review consequence |
|---|---|---|
| U-01 anchor inputs and representativeness | Preserve four provisional briefs; use symbolic/qualitative envelopes now. | Owner/application reviewers choose numerical success envelopes later; change anchors if independent audits expose missing reasoning. |
| U-02 distributed depth | Chapter 16 contains offset/rate/delay/asymmetry, ambiguity, epoch and holdover; protocols external. | Time/frequency review tests sufficiency, especially delayed control and independent-reference application routes. |
| U-03 interferometry | Chapters 3/8/9/16/30 retain stochastic sensitivity, geometry/reference freedoms and calibration. Full imaging remains uncommitted. | Specialist must judge whether receiver decisions are possible without reconstructing essential material elsewhere. Affected recommendation remains qualified. |
| U-04 processing/propagation | Chapters 10 and 26–31 contain task mappings necessary for receiver choices; exhaustive coding/imaging/algorithm catalogues external. | Application reviewers name missing decisions/counterproblems, not just extra topic headings. |
| U-05 vector/polarization | Chapters 8/9/20/28–30 retain vector manifold, loading/coupling, leakage, noise and scalar-limit criteria. | Antenna/array/DF/interferometry review must assess minimum model adequacy; radiator synthesis/full-wave design external. |
| U-06 sensor/non-RF scope | Chapter 31 uses an RF physical-measurand bridge. No optical/quantum completeness. | Owner/sensing specialist chooses representative transduction later. |
| U-07 implementation/production facts | Chapters 14–25 require quantitative interfaces, finite resources, physical constraints and evaluated work products. | Hardware/production review tests depth. No present device guarantee, measured population or mandated standard is invented. |
| U-08 conventions | Chapter 1 and Appendix A reserve affected choices; unresolved standards remain unchanged. | Mathematical editor/engineer decides envelope, PSD, L(f), cross-spectrum and nonstationary conventions before substantive derivations. |
| U-09 bridges and sources | Chapters 2–7 include the missing specialist foundations; all derivations remain development obligations. | Request unfamiliar counterproblems and later learner assessment; no coverage count substitutes for adequacy. |
| U-10 observability/correctability/retained signal | Chapters 5/13/20/23 and applications distinguish inference, feasible compensation, wanted response and held-out evidence. | Calibration/application reviewers challenge confounding, unobserved paths and resources. |

Potential editorial weaknesses are an abstract opening (mitigate through recurring engineering questions), fragmented shared results (ownership audit), overloaded Chapters 12/13/23/25 (explicit section outcomes and review below), and superficial implementation (required I/V work products). No significant missing baseline responsibility has been established by this authorial pass. If review establishes one, document affected CAP/K/A, missing decision, consequence and a proposed bounded baseline correction; do not silently change accepted specifications.

ISSUE-001 remains a mathematical-authoring gate. ISSUE-004/006 and U issues remain specialist/adequacy obligations. Publishing, environment and dependency issues ISSUE-002/003/005 are deferred to their authorized stages; they do not justify infrastructure changes here.

## 5. Acceptance and subsequent pilot

The project owner has provisionally accepted planning use under [ADR-0004](decisions/ADR-0004-provisional-book-architecture-acceptance.md); its four review qualifications and continuing technical-review obligations remain in force. Decisions changing essential content/dependencies block the affected recommendation until resolved or explicitly bounded by the owner. This administrative record does not extend acceptance beyond the owner’s stated use or modify ADR-0002/0003.

A later dual-channel relative-phase-stability pilot must test whether an RF-engineer reader can define the observable and states, construct correlated physical models, perform consequential calculations, compare reference/calibration alternatives, recognize false shared-clock or quiet-residual conclusions, and propose interpretable measurement evidence. Give the reader a changed path delay, reference topology or observation operator and require a changed model and justified decision. Review actual reasoning and engineering work, not heading recall or coverage alone. Mathematical/software checks, physical validity, engineering adequacy and compliance remain separate claims. The pilot and publishing evaluation are not executed here.

**Stopping boundary:** the book-architecture stage is closed for provisional planning use. Technical authoring standards, publishing validation and the initial technical pilot are subsequent work, not yet started. Do not begin chapters, substantive derivations, solved designs, models, publishing work or final technical acceptance.
