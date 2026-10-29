# Technical Coverage and Knowledge-Dependency Architecture

**Status:** draft architecture developed on 2026-10-28 under the project owner's instruction to implement the architecture plan. Pending human review and acceptance for planning use. Neither ADR-0002 nor authorization to produce this document approves its technical contents or authorizes a table of contents.

## 1. Purpose, authority and deliverable ownership

The [charter](charter.md) requires a book from which an experienced RF engineer can learn to reason about unfamiliar coherent receivers and later obtain practical design guidance. The [competence inventory](competence-inventory.md), provisionally accepted under [ADR-0002](decisions/ADR-0002-provisional-competence-baseline.md), supplies the 45 capability requirements. Its mathematical, physical and engineering content has not thereby been independently validated.

This architecture specifies the knowledge development needed to support those requirements. It establishes provisional treatment boundaries, learning dependencies, engineering-reference routes and tests of coverage. It is neither a chapter outline nor a completed technical treatment. No derivation, numerical allocation, component selection, computational model or physical validation is supplied here.

Three documents have distinct responsibilities:

- This document owns the intellectual organization, reader progression, cross-domain relationships, navigation and readiness decision.
- [Technical coverage](technical-coverage.md) owns treatment specifications K01–K26 and A35–A41, dependency rationales, capability traceability and gaps. These identifiers denote bounded reasoning responsibilities, not chapters or a formal graph.
- [Reference-design planning](reference-design-plan.md) owns provisional design briefs, staged example contributions and paper stress tests. It does not supply solved designs.

The governing [scope](scope.md) and [technical standards](../standards/technical-authoring.md) remain provisional. This package develops their implications without replacing the charter, changing capability definitions or selecting unresolved mathematical conventions. Inventory §8 issues remain open; their architecture dispositions are in technical coverage §6.

## 2. Method and appropriate granularity

### 2.1 Derivation from capabilities

For each inventory entry, work backward from its required evaluated output: what must the engineer formulate, calculate, decide, realize or interpret? Extract the necessary result or method, then identify its mathematical and physical prerequisites. Work forward from the reader baseline to check whether that knowledge can actually be acquired. Finally challenge the proposed route with application and failure cases.

Merge requirements that need the same reasoning under the same applicability conditions. Keep task-specific mappings separate when they change the observable, inference, desired signal, ambiguity or evidence. Split an entry when its starting prerequisites or required assessment differ materially; use a named first treatment and refinement where that avoids a false circular dependency.

This pass yields 26 shared treatments and seven application treatments. Their number is a consequence of the present decomposition, not a completeness target. Each specifies a result-development obligation, engineering use and failure check. Individual formulas, components and citations are not separate architecture entries. Subsequent authoring may combine or divide exposition while retaining these obligations and canonical ownership.

### 2.2 Meaning of dependencies

**Essential learning:** the receiving treatment uses a defined representation, result or reasoning operation from the prerequisite. The dependency rationale must name that use; topical similarity is insufficient.

**Conditional learning:** additional knowledge is required only for a named implementation or task. Digital correction adds sampling and DSP; it is not an assumed prerequisite for analog port metrology or analog array alignment.

**Engineering interaction:** methods exchange requirements, parameters, constraints or evidence after their foundations exist. Architecture, budgets, physical realization and calibration access interact iteratively. Their interaction does not impose a circular teaching sequence.

An early problem may supply an interface specification, noise parameter or application target before teaching how it is obtained. It must label that input, its assumptions and the later refinement. Supplied inputs cannot be treated as demonstrated technology performance.

### 2.3 Development depth

Full internal treatment includes essential derivation, assumptions, physical interpretation, limiting cases, consequential calculations and failure recognition. Selective support develops the mathematics or physics needed to use those results correctly. External material supplies general remediation, specialist extensions or verified current facts through an explicit interface.

The boundary applies to reasoning, not whole disciplines. For example, detailed antenna design may be external while field-to-port response, coupling and calibration limits remain internal. Complete statistical theory may be external while likelihood, nuisance freedoms, finite-record uncertainty and applicable estimation limits remain internal. A reference is not a substitute for the essential coherent-receiver bridge.

## 3. Knowledge clusters and relationships

### 3.1 Fundamental clusters

| Cluster | Mathematical and physical knowledge that must be developed | Treatment homes |
|---|---|---|
| Observables and representations | Relative quantities, reference changes, physical versus analytic waveforms, complex envelopes, sampling representations and convention consistency | K01, K12 |
| Stochastic observation | Probability bridge, complex and circular statistics, phase increments, covariance, spectra, observation filtering and finite-record statistics | K02–K04 |
| Inference and dynamics | Likelihood/least squares, nuisance parameters, reference freedoms, ambiguity, feedback, acquisition and desired-signal transfer | K05–K06, K16 |
| Approximation and model adequacy | Sensitivities, uncertainty, numerical errors, model hierarchy, limiting cases and physical discrepancy | K07 |
| Physical generation and transfer | Propagation/transduction, vector fields and networks, loading/coupling, source noise, blockers and waveform-dependent timing errors | K08–K09, K12, K14–K15 |
| Information extraction | Correlation, detection, observation-weighted integration, rejection and retained information | K10, A35–A41 |
| Feasibility and allocation | Joint constraints, architecture/interfaces, correlated budgets and conditional operating regions | K11, K13 |
| Realization and correction | Sampling, quadrature, multirate processing, finite resources, complex-response alignment, realizable inverse approximation | K17–K20 |
| Calibration and metrology | Observability, reference integrity, procedure validity, operational measurement equations and uncertainty | K21–K22 |
| State, physical implementation and lifecycle | Initialization, data validity, integration, diagnosis, environmental sensitivities, evidence decisions, production and service | K23–K26 |

The last cluster contains engineering methods rather than one common physical theory. Its quantitative support comes from the earlier clusters; its obligations cannot be discharged by generic lifecycle prose.

### 3.2 Mathematical and physical connections across domains

The following are requirements for later development, not derivations or claims of universal model applicability.

| Relationship to develop | Domains joined | Required qualification and engineering consequence |
|---|---|---|
| Complex signal transfer under modulation, conjugation, filtering and sampling | RF conversion, I/Q, DDC, calibration and instrument phase | Track frequency orientation, normalization and reference planes before interpreting phase or power |
| Phase differences/increments, complex correlation and observation-weighted accumulation | Oscillator analysis, communications, radar, arrays and interferometry | Separate exact relationships from Gaussian, stationary and small-angle specializations; equal marginal phase variance need not imply equal task performance |
| Source/path transfer to covariance or cross-spectrum and then weighted output | Distribution, noise budgets, arrays, correlation and test references | Construct physical correlations before propagating them; identify shared terms and avoid double counting |
| Frequency-dependent phase, delay and geometry | Frequency planning, wideband steering, distributed timing and de-embedding | Distinguish propagation, electronic response, phase offset, group delay and sample epoch; include bandwidth and state |
| Measurement sensitivity, rank, conditioning and information | Estimation, DF, calibration, sensor inference and distributed clocks | Distinguish reference freedom, global ambiguity, local precision and numerical instability |
| Feedback/correction transfer of desired and nuisance quantities | Carrier recovery, oscillator control, drift compensation, sensing and cancellation | Define what must be retained; a smaller residual can correspond to suppression of wanted information |
| Nonlinearity and sampling-time sensitivity under the complete waveform | Blocker rejection, gain control, synthesizer/clock selection and converters | Preserve headroom, valid-data intervals and operating conditions; ideal digital rejection does not establish analog survival |
| Sensitivity and uncertainty propagation to decisions | Design allocations, metrology, production yield and compliance | Keep design margin, variability, parameter uncertainty, model discrepancy and measurement uncertainty distinct; bound linear approximations |

Canonical ownership belongs to the corresponding K treatment in technical coverage §2. Applications own their waveform-, geometry- or measurand-specific performance mappings. They must explain those mappings rather than repeat a conflicting general derivation.

## 4. Reader progression and engineering-reference use

### 4.1 Entry assumptions and internal bridges

Use inventory §2 as the entry contract: phasors/networks, ordinary noise and linearity, conversion/filtering, circuits/interconnects, calculus/basic Fourier methods and laboratory practice. Their eventual self-assessments must test observable reasoning rather than years of experience.

Internally develop probability and scalar stochastic reasoning in K02, matrix methods in K04, inference in K05, control in K06 and numerical/uncertainty reasoning in K07. Introduce vector field/network bridges in K08–K09 and sampled/multirate bridges in K17/K19 as needed. Do not assume those specialisms from general RF experience. Missing general RF knowledge can trigger precise external remediation, but coherent-specific reasoning stays internal.

### 4.2 Progressive learning route

These are learning passes, not proposed parts or chapter numbering. Parallel branches and revisits are intentional.

| Pass | Develop | What the reader should then be able to do |
|---|---|---|
| Motivate and define | Qualitative design briefs; K01; requirement framing in K11 before its quantitative assessment | State what is compared, where, over which interval and states; expose missing requirements |
| Build minimum reasoning | K02; scalar K03/K05/K07; K04 before matrix refinements; K06 once inference exists | Select signal/noise descriptions, recognize ambiguity, interpret observation dependence and test an approximation |
| Establish physical and information support | K08–K10 and K12; quantitative K11 after K05/K07 | Construct relevant physical inputs, evaluate extraction/feasibility and reject unsupported operating regions |
| Allocate and compare | K13; K14–K15; K17 sampling and later I/Q in K18; K16 where distributed | Compare architecture/interface alternatives using correlated budgets and actual signal/blocker/state conditions |
| Realize and calibrate | K19–K20 as conditional branches; K21a observability and K22 metrology, then K21b procedure; K23 state/integration; K24 | Choose accessible, realizable corrections and physical constraints; preserve sample, reference and calibration meaning |
| Maintain and assess | K21c maintenance; K23 diagnosis; K25; K26; progressively completed applications | Interpret residual evidence, diagnose competing mechanisms, evaluate production/service decisions and state remaining claims |

Application interpretation enters early as motivation and returns with quantitative depth. Metrology begins once its foundations exist, alongside design development; it is not postponed until hardware completion. K07 model-adequacy checks accompany every consequential model. A35–A41 are synthesis responsibilities rather than mandatory final-only reading.

### 4.3 Explicit cycle resolutions

| Apparent cycle | Resolution and supplied-input boundary |
|---|---|
| Stochastic mathematics needs physical covariance; physical noise needs statistics | K02/K03 teach scalar definitions and observation mathematics. K04 develops matrix covariance. K09 then constructs physical covariance for later assessment; no full noise-network prerequisite for initial probability |
| Estimation needs matrices; matrix methods need stochastic examples | K05 first treats scalar parameters and nuisance freedoms. Matrix inference adds K04; K04 uses established K02 covariance definitions |
| Requirements need feasibility; feasibility needs requirements and budgets | K11 first formulates an operational brief. Quantitative feasibility uses supplied signal/technology envelopes and K05/K07; K13 and subsystem results subsequently refine it |
| Calibration needs measurement; measurement needs calibration | K21a develops observability without an executed calibration. K22 uses this only where calibration references matter. K21b then combines metrology with correction and independent residual assessment |
| Analog design needs converter choice; converter choice needs analog design | K14 and K17 use declared interface envelopes independently after K13. Reconcile their driver, range, filtering and timing constraints as an engineering interaction |
| Distributed synchronization needs resampling; resampling needs clock estimates | K16 develops continuous clock/reference inference. K19 teaches resampling from supplied timing estimates. Their combined digital realization is a conditional extension |
| Maintenance, environment and service seem mutually prerequisite | K24 derives physical sensitivities using declared correction interfaces; K21c applies them to update policy. K26 service evaluates validity using those results rather than supplying their foundations |

### 4.4 Reference routes

The engineer may enter through any row below. Each route must expose its input assumptions and lead back to the canonical result, calculation method and evidence requirement. It does not imply all listed treatments must be read sequentially.

| Entry question | Principal route |
|---|---|
| Is the requirement jointly feasible? | K01 → K11; consult K05/K10 for information, K09/K14/K17 for physical constraints, K13 for allocation |
| What oscillator, clock or filtering performance is needed? | K12/K13 → K09/K15/K17 → relevant A treatment → K22/K25 |
| What can calibration establish or correct? | K21a → K20 or K18/K19 as applicable → K21b → K22; use K08 for external field/sensor paths |
| Why does coherence fail after reset, retune or outage? | K23a/K23b → K12/K15/K16/K19 as applicable → K23c/K22 → K25 |
| How does channel error affect the task? | K20/K13 → A37 beam, A38 bearing or A39 correlation; use K08/K09 for field and noise inputs |
| Does a quieter residual mean a better instrument or sensor? | K01 → K06/K21c → A40/A41 → K22/K25 |
| Can this design be manufactured and maintained? | K26 → K13/K21/K22/K24/K25; inspect configuration dependencies in K23 |

Route checks also preserve alternatives: analog single-channel metrology uses K01/K03/K05/K07/K11/K12/K13/K21a/K22/K25/A41 with an analog chain, without compulsory K17, K19 or K20. Analog array alignment adds K04/K08/K09/K20/A37 and analog reference/correction methods without compulsory digital conversion. Sampled and distributed realizations add their named conditional treatments.

## 5. Assurance, review and readiness

### 5.1 Checks and findings of this architecture pass

The capability matrix was constructed against every inventory entry, retaining its competence dimensions and explicit output. A reverse treatment-use table and charter/lifecycle audit are in technical coverage §§4–5. The dependency table distinguishes foundational entry from refinement. Reference-design planning §4 records the seven application paper audits and cross-cutting failure probes, including what misleading conclusion each must reject.

These are authorial coverage checks. They support the claim that the proposed development obligations have been mapped; they do not establish that the future treatments are sufficient in practice. No example has been calculated, hardware implemented, source re-examined or independent specialist review performed by this stage. Mechanical check results are recorded in [current work](current-work.md), separate from these editorial findings.

No change to the 45 capability definitions is proposed by this pass. Concrete adequacy questions remain in the gap register, especially the depth of mathematical bridges, application mappings, field/noise models, correction limits and realization/production methods. A reviewer finding a missing essential result must reopen the relevant architecture boundary or baseline entry.

### 5.2 Completion criteria for subsequent use

Before recommending use to construct a provisional table of contents, require:

1. Every capability dimension and evaluated output has a named treatment route, prerequisites, input boundary and assessment; no heading-only substitution remains.
2. Essential dependencies admit a learning progression, including refinements; conditional branches do not impose digital, multichannel or distributed knowledge universally.
3. Shared results have canonical ownership and application-specific bridges; no essential coherent reasoning is delegated to an external citation alone.
4. Every application audit and reference-design stage can identify the required calculation, decision and discriminating evidence without an unexplained dependency.
5. Physical applicability, approximation limits and desired-signal retention obligations are explicit wherever they affect a decision.
6. All inventory U-01–U-10 issues and new gaps have bounded dispositions; a decision changing essential treatment scope or prerequisites blocks the affected recommendation.
7. The project owner reviews the reader contract, provisional anchors and coverage boundaries. Relevant engineering reviewers assess consequential disputed boundaries and identify counterexamples or needed changes. Actual acceptance records identify revision and intended use under the existing standard.

**Current recommendation:** this is a completed draft package for review, not an accepted architecture or an unqualified recommendation to begin a table of contents. Mapping and paper-route checks are present. Human decisions in technical coverage §6 remain pending, particularly U-03/U-04/U-05/U-09 where insufficient depth could change treatment boundaries. Numerical case requirements and particular parts may remain deferred if that does not conceal a coverage gap. No final technical acceptance is granted by Codex.

After those decisions, an authorized table-of-contents task may organize the treatments into parts and chapters, testing both learning and reference navigation. Stop here until separately instructed; publishing evaluation, the relative-phase pilot and manuscript development remain outside this stage.
