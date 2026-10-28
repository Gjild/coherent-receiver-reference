# Foundational Reader Competence and Engineering Capability Inventory

**Status:** provisionally accepted by the project owner on 2026-10-28 as the foundational capability baseline for the next intellectual-architecture stage. **Acceptance scope:** planning and coverage input only; mathematical derivations, physical models, engineering methods and application-specific performance conclusions are not independently validated by this decision. See [ADR-0002](decisions/ADR-0002-provisional-competence-baseline.md).

This inventory specifies the understanding and engineering actions the textbook must enable for an experienced RF engineer entering coherent receiver engineering. The intended endpoint is reasoned development of unfamiliar systems from operational need through production and lifecycle planning, using the book as the primary technical and methodological reference. It does not certify a reader, establish a completed design, or supply accepted chapter architecture.

The [charter](charter.md) governs this provisional baseline. The [current task](current-work.md) bounds it. Existing scope, architecture, reference-design candidates and mathematical conventions remain provisional. Capability descriptions below are proposed learning and engineering requirements, not derivations or demonstrated receiver performance. Selected, narrowly scoped source examinations support specific distinctions; see §9 and the linked evidence note. Most of the proposed breadth still needs specialist review and later claim-level research.

## 1. How to use and assess this inventory

Read §2 for the assumed reader baseline and §3 for application boundaries. Section 4 owns the capability entries; §5 shows major dependencies and coverage; §6 exercises them against qualitative problems. Sections 7–9 record assessment, review reconciliation, unresolved decisions and evidence. These divisions are navigation aids, not proposed book parts.

### 1.1 Construction method and granularity

The inventory combines backward reasoning from required engineering work products, forward reasoning from scientific foundations, lifecycle coverage and application contrasts. A subject-first outline would expose disciplines but could confuse mentioning a subject with enabling engineering. Lifecycle decomposition alone could underdevelop mathematics; application decomposition alone could duplicate foundations or overfit examples. The combined approach is adopted provisionally because each pass tests the others.

A capability is a coherent responsibility with an observable outcome: a formulation, calculation, justified decision, implementation specification, procedure or assessment. “Understand phase noise” is insufficient. Defining the relevant phase observable, selecting a defensible disturbance model, propagating correlations to the output and specifying an adequate measurement is assessable. Separate capabilities are warranted where decisions, prerequisites or evidence differ materially. Supporting foundations have assessable reasoning outcomes even when they do not produce hardware.

Identifiers are independent of chapter numbers. Their quantity is an outcome of decomposition, not a completeness target. Dependencies name major prerequisites, not every interaction. Each entry has one canonical responsibility; application entries add distinctive reasoning and reference shared methods.

### 1.2 Competence dimensions and coverage depth

| Dimension | Required evidence of learning |
|---|---|
| C — conceptual | Explain mechanisms, assumptions, physical interpretation and failure regions |
| M — mathematical | Formulate representations, derive or manipulate essential relationships, check units and limiting cases |
| A — analytical | Calculate performance, sensitivities, uncertainty and applicability |
| D — design | Select and justify architecture, allocations, methods and tradeoffs |
| I — implementation | Realize and exercise a bounded hardware, processing or operating solution; check interfaces, resource limits and state behavior |
| V — verification | Execute and interpret suitable checks/measurements, quantify uncertainty and diagnose failure without overstating conclusions |

A dimension listed in an entry denotes a required outcome, not a score or an equal amount of exposition. Required work products are evaluated technical results, not merely plans: with supplied inputs the reader must perform the calculation, implement the bounded method or execute and interpret the measurement relevant to that dimension. This inventory specifies those future assessments; it does not claim they have been executed now. C/M foundations need not each be a complete design procedure. The outcome, method and evidence bullets describe what the dimensions mean for that entry.

Coverage labels are **F: full internal**, **S: selective internal**, **E: external support**. F means the essential reasoning must be developed inside the book, with assumptions, derivations where consequential, physical interpretation, engineering use and limits. S means a bounded bridge or supporting method, including the knowledge needed to use it safely. E means general background or current/device-specific detail may be referenced externally; essential coherent-receiver decisions still require an internal bridge. Mixed labels describe different portions of an entry, not permission to leave its main outcome unspecified. No core capability below is wholly delegated to E.

## 2. Reader baseline and foundational bridging

RF experience is an input assumption to confirm, not evidence of competence in every adjacent discipline. Baseline checks should eventually be short reader self-assessments; the tasks below define their intended level without creating exercises now.

| Proposed assumed prerequisite | Observable baseline | Required internal bridge |
|---|---|---|
| Complex impedance, phasors and networks | Interpret impedance and S-parameters at stated reference planes; distinguish power and voltage ratios | Time-varying complex envelopes, sign/scaling conventions and phase/delay reference changes: CAP-002/003/012 |
| Conventional receiver noise and linearity | Construct a basic gain/noise cascade; reason about compression, intermodulation and bandwidth | Physical/correlated disturbances, reciprocal mixing, coherent leakage and gain-state effects: CAP-004/013/014/044 |
| Frequency conversion and filtering | Identify desired and image bands and ordinary mixer products | End-to-end phase transfer, spectral inversion, alias zones and coherent frequency planning: CAP-012/019 |
| Circuit and transmission-line reasoning | Interpret loading, matching, loss, reflections and ordinary interconnect delay | Differential delay, dispersion, reference distribution, coupled noise and distributed clock relationships: CAP-016/022/026/044/045 |
| Calculus, elementary differential equations and basic Fourier methods | Differentiate/integrate engineering functions and interpret an LTI transfer function | Stochastic filtering, sampled/multirate systems, loops and observation operators: CAP-003–007/018/020 |
| Basic laboratory practice | Set reference levels, avoid overload and document instrument configuration | Phase measurands, calibration traceability, common-reference effects and uncertainty: CAP-002/030/031 |

Probability, stochastic processes, circular statistics, cross-spectra, estimation, matrix conditioning, control-loop analysis, numerical uncertainty and multichannel calibration are **not assumed** merely from RF experience. CAP-004–009 provide bridges and coherent-specific development. Readers missing a general RF prerequisite may need external remediation; the book must state the prerequisite and retain the coherent-specific bridge.

The scientific baseline must also be tested physically: the reader must distinguish electromagnetic propagation from electronic transfer delay; additive noise from phase fluctuations; unknown signal parameters from receiver defects; and an observable relative quantity from an unobservable absolute reference. These abilities are developed by CAP-002–010 and revisited in system work.

## 3. Receiver classes and coherence requirements

### 3.1 Define the engineering question before choosing a metric

For every system, specify what is compared with what: incoming carrier and local estimate, transmitter and delayed return, channels, array elements, spatial baselines, sensor reference, or instrument ports. State reference planes and sign conventions; carrier/band; observation interval and filtering; waveform and signal conditions; operating/environmental state; calibration history; and the task consequence of error.

Separate phase accuracy, temporal stability, restart repeatability, frequency offset, sampling-time alignment, delay/group-delay response and usable correlation. Identify deterministic terms, random terms, common/differential effects and unknown nuisance parameters. “Coherent” without an operational observable and conditions is incomplete. A metric such as RMS phase error, a correlation statistic, an application error measure or a stability statistic is useful only after its definition and relevance are established. No single metric is imposed across these classes.

| Class / comparison | Reader must specify | Distinctive decisions and failure boundaries | Canonical application entry |
|---|---|---|---|
| Carrier-coherent communications: received waveform versus recovered reference | Carrier/timing residuals, acquisition/tracking conditions and signal-quality/error outcomes for the chosen waveform | Which offsets can be estimated; pilot/data dependence, ambiguity, slips and reacquisition; externally fixed phase may be unnecessary | CAP-035 |
| Coherent radar: transmit waveform/reference versus return across fast time, pulses and channels | Waveform-dependent phase/frequency/delay errors, coherent processing interval and range/Doppler/angle consequences | Shared-source effects depend on path delay; waveform/reset state, leakage and clutter matter | CAP-036 |
| Receiving phased arrays: element responses versus intended weights | Beam gain/pattern/pointing and complex response versus frequency, scan, state and environment | Phase-only versus delay correction, analog/digital/hybrid combination, coupling and drift | CAP-037 |
| Direction finding: spatial observations versus a calibrated manifold | Bearing bias/uncertainty, ambiguity and usable field of view under stated signal/propagation conditions | Geometry, receiver calibration and propagation can be confounded; beam quality alone is insufficient | CAP-038 |
| Interferometry: signals across baselines and epochs | Complex correlation/visibility, geometric and instrumental delay, integration and phase-reference assumptions | Source structure, geometry, clocks and propagation must be separated as far as observable; full imaging is a separate depth question | CAP-039 |
| Coherent sensing: signal/reference relationship versus physical state | Measurand transfer, phase/delay sensitivity, ambiguity, drift and update behavior | Physical transduction and nuisance effects determine usable accuracy; a quiet receiver alone is insufficient | CAP-040 |
| Phase-sensitive measurement: defined instrument ports/reference paths | Transfer phase/delay or phase/time difference, reference planes, correction model and uncertainty | Instrument/cable/switch effects, traceability, repeatability and residual uncertainty must be distinguished | CAP-041 |

These classes overlap. A phased-array radar exercises several rows; it does not remove the need to audit each row. Passive radiometry and correlation receivers enter through interferometry and stochastic-signal foundations where relevant. Interferometry is not treated as synonymous with DF, nor coherent sensing as a duplicate of radar.

### 3.2 Architectural contrasts and boundary survey

Audit the capabilities against single/multiple channels; colocated/distributed receivers; shared/independent references; continuous/restarted/retuned operation; narrow/wide bandwidth; direct/low-IF/heterodyne/direct-sampling conversion; analog/digital/hybrid combination; and shared/separate transmit-receive references. Also vary continuous, burst, pulsed and swept observations, strong blockers, weak signals, motion and changing environments. These are contrast axes, not a mandate to enumerate their Cartesian product.

| Additional application or boundary | Provisional disposition and implication |
|---|---|
| GNSS, satellite links, telemetry and burst links | Communications and timing stress cases; core synchronization and propagation reasoning included, protocol-specific implementations external |
| Passive/bistatic/multistatic radar, SAR and distributed apertures | Required contrast cases for reference availability, motion, timing and geometry; comprehensive mission processing remains unresolved (U-02/U-04) |
| Radio astronomy / long-baseline interferometry | Include correlation, reference, delay and calibration reasoning; full imaging, observing practice and specialist propagation depth require review (U-03) |
| Polarimetric receivers | Include a vector field-to-port/manifold model, cross-polar leakage and calibration observability; comprehensive polarimetric inference remains optional (U-05) |
| Channel sounding, vector instruments, lock-in and displacement sensing | Include through CAP-040/041; transducer and instrument-specific facts may be external |
| Optical coherent reception, quantum receivers, ultrasound and other non-RF systems | Do not claim comprehensive coverage; transferable principles may inform contrasts, but extension of the RF-focused scope needs human decision (U-06) |
| Noncoherent receivers | Include comparisons that justify coherent design or show when it is unnecessary; no parallel general noncoherent-receiver textbook |

Newly identified applications must be mapped, explicitly deferred or raised as scope questions. Their absence from an example list does not authorize silent exclusion.

## 4. Capability inventory

In each **P / coverage / relevance** field, **Learning** names essential foundations for the stated responsibility; **Conditional** names additional knowledge only for the specified implementation or task; **Interactions** names engineering inputs and iterative handoffs, not learning prerequisites. Learning links define the core learning dependency. Foundation entries may introduce scalar/ideal concepts first and revisit their assessments with later matrix, physical or implementation models; such explicitly identified refinements are interactions, not prerequisites for first introduction. Later interface particulars and application requirements may be supplied as inputs before their full treatment. Application codes refer to §6; the reader baseline in §2 still applies. Open issues U-xx are in §8. All coverage decisions are provisional.

### A. Requirements, observables and foundations

#### CAP-001 — Translate operational need into a feasible engineering specification

- **Outcome / dimensions:** C/A/D/V. Produce an operational-state description, requirement tree and evidence plan linking mission outcomes to receiver observables; identify missing requirements before sizing hardware.
- **Physics / methods:** Translate signal, interference, geometry, motion and environmental envelopes into measurable conditions; distinguish bounds, probabilistic targets, tolerances and assumptions. Compare coherent and noncoherent approaches where appropriate.
- **Decisions / implementation:** Define reference boundaries, interfaces, acquisition time, availability, calibration downtime, production constraints and requirement ownership. Negotiate incompatible goals rather than inventing values.
- **Evidence / failure:** Translate supplied operational needs into testable requirements and use CAP-043 to reject or qualify incompatible combinations. Record assumptions and missing limits rather than inventing them. Work product: evaluated requirement set, including infeasibility or conditional-feasibility conclusions and verification routes.
- **P / coverage / relevance:** Learning: reader baseline. Interactions: CAP-002 defines observables; CAP-043 tests feasibility and CAP-031 defines evidence. F for coherent requirements reasoning, S for generic systems methods, E for current contractual/regulatory particulars. All classes; U-01/U-07.

#### CAP-002 — Define coherence observables and their reference conditions

- **Outcome / dimensions:** C/M/A/D/V. Write an operational definition of the required relative quantity and distinguish accuracy, stability, alignment and repeatability.
- **Physics / methods:** Define phase/frequency/time/delay and correlation observables, reference planes, filtering and observation operators; distinguish angle-valued data from unwrapped phase and deterministic drift from fluctuations.
- **Decisions / implementation:** Select a task-relevant measure, unwrap policy, observation interval, operating states and calibration dependency; identify what “absolute” means relative to an available reference.
- **Evidence / failure:** Define and compare two operational measurands, including intentional bandwidth, filtering, estimation and finite-record dependence; distinguish these from unintended instrument response, corrections and uncertainty. A measurand legitimately defined by its measurement method must report that method [S2]. Work product: observable definitions and a worked interpretation of why their measured values or tests differ.
- **P / coverage / relevance:** Learning: baseline phasors/calculus. Interactions: CAP-004/005 refine stochastic measures after the basic observable definitions; CAP-030 realizes the measurement. F because all consequential claims require operational definitions. All classes; U-01/U-08.

#### CAP-003 — Formulate consistent real, complex and sampled signal representations

- **Outcome / dimensions:** C/M/A. Translate a physical waveform through real passband, analytic signal, complex envelope and sampled representations without losing power, phase or frequency orientation.
- **Physics / methods:** Fourier transforms, convolution, energy/power relations, modulation, quadrature and sampling; explicitly select normalization, carrier signs and units locally until canonical conventions are reviewed.
- **Decisions / implementation:** Establish model and interface definitions for mixer, I/Q and DSP chains; distinguish signal bandwidth from observation/noise bandwidth.
- **Evidence / failure:** Reconstruct the physical signal, check dimensional/power consistency and track a tone through conjugation or spectral inversion. Work product: annotated representation and convention map; identify sign/scaling errors before calibration.
- **P / coverage / relevance:** Learning: baseline calculus/Fourier methods. S for general transform refresher, F for coherent representations and conversions. All classes; U-08.

#### CAP-004 — Model random signals and correlated physical disturbances

- **Outcome / dimensions:** C/M/A. Specify a stochastic model that distinguishes ensemble assumptions from finite observed records and keeps cross-channel correlation visible.
- **Physics / methods:** Random variables/processes, expectation, covariance, complex/proper versus improper statistics where needed, stationarity/ergodicity conditions, phase increments and circular statistics. Formulate additive and multiplicative disturbances in complex signals; derive the local additive-noise-to-phase transformation and identify breakdown near amplitude nulls or low SNR. Distinguish signal randomness, phase noise, deterministic spurs and drift.
- **Decisions / implementation:** Decide when linearization, Gaussian approximations or stationarity are defensible and where a richer model or empirical evidence is needed.
- **Evidence / failure:** Construct a physically justified covariance/cross-covariance example using CAP-044 and test its Hermitian symmetry, positive semidefiniteness and reference definitions. Derive finite-record estimator bias/variance under stated distribution assumptions; distinguish zero expected cross-correlation from nonzero estimation uncertainty, including stochastic source power and effective independent samples. Explain where Gaussian/fourth-moment assumptions enter. Work product: evaluated stochastic model, not a correlation map alone.
- **P / coverage / relevance:** Learning: CAP-003 and probability bridge. Interactions: CAP-008 develops matrix covariance after scalar stochastic foundations; CAP-044 supplies physical source constructions for later assessment. F for coherent stochastic reasoning; S for general probability development. All classes; U-09.

#### CAP-005 — Relate spectra and stability measures to the actual observation

- **Outcome / dimensions:** C/M/A/V. Choose and interpret frequency-domain and time-domain descriptions for the stated phase/time observable.
- **Physics / methods:** Auto/cross-spectra, transfer functions, finite windows, averaging, aliasing, integration bounds, phase/frequency relationships, stability statistics and confidence limits. Derive phase-increment statistics, complex coherence and observation-weighted accumulation from the underlying process; identify which results require Gaussian, stationary or small-angle assumptions. Derive the differential phase transfer for a shared source through unequal paths, including the pure-delay limiting case. Specify PSD sidedness, units and cross-spectrum order; do not extend a stationary spectrum to a nonstationary process without justification.
- **Decisions / implementation:** Select filters, record lengths and measures appropriate to noise type and task; distinguish instrument bandwidth and algorithm weighting from a physical cutoff. NIST SP 1065 distinguishes stability measures and warns about ordinary variance for some oscillator noise types [S1].
- **Evidence / failure:** Calculate task-relevant weighted phase/correlation behavior for two disturbances with equal marginal phase variance but different temporal structure. Evaluate finite-observation uncertainty and compare a spectral calculation with an applicable time-domain formulation. Reject unqualified PSD-to-RMS or universal coherence claims. Work product: evaluated observation-aware analysis with approximation and convergence limits; NIST stability cautions [S1] do not supply these application derivations.
- **P / coverage / relevance:** Learning: CAP-002/003/004. Conditional: CAP-008 for matrix cross-spectra. Interactions: CAP-044 supplies physical noise and CAP-042 maps to detection/integration. F for coherent interpretation/derivations, S for the wider estimator catalogue. All classes; U-08/U-09.

#### CAP-006 — Estimate signal parameters and determine identifiability

- **Outcome / dimensions:** C/M/A/D/V. Formulate estimation of phase, frequency, delay, amplitude or other task parameters, and identify information that the observations cannot determine.
- **Physics / methods:** Likelihood and least-squares reasoning, nuisance parameters, bias/variance, information bounds with regularity assumptions, ambiguity functions, linearization and sensitivity to SNR/model mismatch.
- **Decisions / implementation:** Choose pilots, references, observation duration and estimator structure; distinguish precision under a local model from global ambiguity resolution and acquisition success.
- **Evidence / failure:** Derive and evaluate a representative estimator and applicable information bound under supplied signal/noise assumptions; test indistinguishable parameter sets, nuisance freedoms, conditioning, bias and out-of-model cases. Compare local precision with global ambiguity and acquisition behavior. Work product: calculated estimator performance and an explicit identifiability/failure assessment.
- **P / coverage / relevance:** Learning: CAP-003/004. Conditional: CAP-008 for matrix methods. Interactions: CAP-043 applies limits at system level. F for essential estimation/identifiability, S for general statistical theory. All classes; U-09/U-10.

#### CAP-007 — Analyze acquisition, tracking and feedback behavior

- **Outcome / dimensions:** C/M/A/D/I/V. Specify a synchronization loop or tracking procedure with separate acquisition, steady tracking, disturbance response and loss-of-lock behavior.
- **Physics / methods:** Phase/frequency detector behavior, loop transfer functions, sampled control, noise bandwidth, stability margins, acquisition nonlinearity and dynamic stress. Distinguish linear locked-state analysis from capture guarantees.
- **Decisions / implementation:** Calculate loop noise/dynamic tradeoffs, stability margins and latency effects; implement a bounded acquisition/tracking state procedure with holdover, slip detection and reacquisition. Derive transfer of the desired physical signal as well as disturbances, so that tracking does not silently remove the measurand. Treat delayed distributed feedback using CAP-045 when applicable.
- **Evidence / failure:** Evaluate a supplied acquisition/tracking problem with frequency offset, fading, saturation and transitions; quantify residual error and justified acquisition/slip-risk evidence rather than extending locked-state analysis into a capture guarantee. Work product: evaluated loop/state design and interpreted results, including desired-signal retention.
- **P / coverage / relevance:** Learning: CAP-003–006 plus control bridge. Interactions: CAP-045 applies loop foundations to distributed synchronization; CAP-017/025 use loop behavior. F for coherent synchronization, S for general control theory. Communications, radar, sensing and references; U-09.

#### CAP-008 — Use matrix methods to solve coupled channel and parameter problems

- **Outcome / dimensions:** C/M/A. Construct and interpret complex vector/matrix models for arrays, calibration, estimation and correlated error budgets.
- **Physics / methods:** Covariance matrices, quadratic forms, rank, eigenstructure, least squares, singular values and conditioning; distinguish inversion of a formal matrix from a stable, identifiable solution.
- **Decisions / implementation:** Choose reference constraints, weighting and regularization with explicit physical justification; preserve units and channel ordering.
- **Evidence / failure:** Inspect rank deficiencies and near-degenerate geometry or calibration stimuli; explain how small input errors affect the result. Work product: matrix formulation, solvability statement and sensitivity assessment.
- **P / coverage / relevance:** Learning: CAP-003/004 plus linear-algebra bridge. S for general algebra, F for coherent matrix uses. Arrays, DF, interferometry, calibration and budgets; U-09/U-10.

#### CAP-009 — Control approximation, numerical and uncertainty errors

- **Outcome / dimensions:** C/M/A/V. Distinguish exact relationships, approximations, parameter uncertainty and numerical artifacts in a proposed engineering method.
- **Physics / methods:** Nondimensionalization, perturbation/sensitivity analysis, uncertainty propagation with covariance, convergence, finite precision and nonlinear/ambiguous cases needing methods beyond first-order propagation.
- **Decisions / implementation:** Select an adequate calculation method, validity region, precision and reporting limits. Keep physical variability separate from numerical tolerance.
- **Evidence / failure:** Execute dimensional, limiting-case, convergence and independent-formulation checks for a consequential calculation. Evaluate an uncertainty example with covariance and a nonlinear/ambiguous case where first-order propagation is inadequate. Work product: calculated result with approximation, numerical and parameter-uncertainty contributions distinguished; measurement-specific use is CAP-030 and [S2] supports only the stated propagation limits.
- **P / coverage / relevance:** Learning: CAP-003/004. Conditional: CAP-008 for matrix problems. Interactions: CAP-030 applies measurement uncertainty. S for general numerics, F for coherent error interpretation. All classes; U-09.

#### CAP-010 — Separate propagation, geometry and transduction from receiver errors

- **Outcome / dimensions:** C/M/A/D/V. Formulate how the arriving field or sensed physical state produces the observed receiver inputs, identifying effects that calibration inside the receiver cannot establish.
- **Physics / methods:** Propagation phase/delay, Doppler, geometry, multipath and environmental path changes. Construct a minimum vector model linking incident field components through antenna effective response/manifold and coupling/loading to receiver ports and cross-polar leakage. State coordinate/polarization bases, phase centers/reference geometry and narrowband, far-field and quasi-static assumptions; derive when a scalar per-channel response is adequate.
- **Decisions / implementation:** Place antenna/sensor and receiver boundaries; choose needed geometry, reference paths, polarization information and external environmental knowledge.
- **Evidence / failure:** Evaluate a direction/frequency/polarization-dependent example and show which parameters an electronic injection cannot identify. Compare scalar matching with the required vector/manifold model and quantify a representative mismatch effect. Work product: evaluated field-to-port/sensor model with externally required antenna, geometry and environmental inputs. Full-wave radiator design and comprehensive polarimetric science remain external, not this minimum receiver model.
- **P / coverage / relevance:** Learning: CAP-002/003/008 and RF fields baseline. Conditional: CAP-006 for identifiability. F for the minimum vector/manifold/receiver model, S for supporting propagation/antenna physics, E for detailed radiator/environmental models. All classes; U-03/U-04/U-05.

#### CAP-042 — Derive detection, coherent integration and signal-preserving rejection from the signal model

- **Outcome / dimensions:** C/M/A/D/I/V. Derive, evaluate and realize a bounded detection, integration or interference-rejection method from the available signal/noise observations; calculate performance and retained desired-signal information.
- **Physics / methods:** Correlation, matched filtering, sufficient statistics where applicable, likelihood ratios, colored-noise weighting, coherent/noncoherent accumulation and phase/timing mismatch. Use CAP-004/005 for complex coherence and finite-observation statistics. For rejection, assess spatial/spectral/temporal or reference-assisted separation, degrees of freedom, training support, covariance conditioning, reference leakage and model mismatch. State hypotheses, nuisance parameters and false-alarm/detection conditions; indistinguishable desired/interfering subspaces cannot be separated by an unsupported linear model.
- **Decisions / implementation:** Calculate integration duration, weighting, rejection structure, normalization and processing loss for supplied conditions. Demonstrate desired-observable transfer/distortion and sensitivity to contaminated training. Require analog headroom before relying on digital rejection; choose a realizable method rather than an unconstrained inverse.
- **Evidence / failure:** Evaluate matched/mismatched references, correlated noise and contaminated cancellation/training cases. Compare retained signal, detection/correlation outcome and uncertainty with a simpler alternative. Work product: executed calculation or bounded processing implementation with failure limits; more accumulation or deeper apparent rejection is not automatically improved task performance.
- **P / coverage / relevance:** Learning: CAP-003/004/005/006/008. Conditional: CAP-010 for propagation/dynamics, CAP-044 for physical interference/noise. Interactions: CAP-020/021 realize digital methods after the detection/rejection foundations; CAP-035–040 interpret task outcomes. F for coherent detection/integration/rejection, S for general detection theory, E for exhaustive adaptive/mission algorithms. U-04/U-09.

#### CAP-043 — Establish quantitative system feasibility and operating regions

- **Outcome / dimensions:** C/M/A/D/V. Derive and evaluate a feasible operating region for supplied system requirements; demonstrate an empty or conditional region when requirements cannot jointly be met, and identify the needed requirement or architecture change.
- **Physics / methods:** Combine signal energy/SNR, waveform bandwidth and observation duration with estimation bounds, ambiguity, dynamics, latency/settling and observability under stated assumptions. Distinguish physical/information limits from architecture/resource/available-technology limits and insufficient evidence; local bounds do not prove global acquisition or ambiguity resolution.
- **Decisions / implementation:** Calculate intersecting gain/noise/headroom inequalities, usable processing/calibration intervals and geometry/waveform constraints. Compare prevention, correction and changed operating envelopes. Do not assert a universal resolution limit independent of waveform, SNR, nuisance parameters or estimator assumptions.
- **Evidence / failure:** Evaluate at least a gain-range conflict and a task-information/ambiguity or wideband-steering conflict using supplied symbolic or numerical inputs. Show which change restores feasibility, and test sensitivity to unsupported inputs. Work product: calculated operating regions, infeasibility/conditional-feasibility conclusions and required evidence; a trade-study plan alone is insufficient.
- **P / coverage / relevance:** Learning: CAP-001/002/006/009. Conditional: CAP-008/010 for spatial problems, CAP-042 for detection, CAP-044 for disturbance constraints. Interactions: CAP-011 chooses architecture and CAP-013/subsystem entries refine allocations. F for coherent feasibility reasoning, S for general constrained-analysis tools. All classes; U-01/U-09.

#### CAP-044 — Construct and propagate physical noise and interference models

- **Outcome / dimensions:** C/M/A/D/V. Derive physically justified input/output disturbance spectra and channel covariance from actual sources, paths, loading and signal/blocker conditions; calculate their consequences and identify where a scalar noise figure or independent-source model is inadequate.
- **Physics / methods:** Relate available/delivered noise power, equivalent temperature, PSD and complex covariance with explicit bandwidth, normalization, reference impedance and loading. Include thermal/dissipative and representative shot/flicker active-device contributions with operating assumptions, external antenna/source fields, mismatch and coupled receiver paths using a bounded noise-wave or equivalent network model where necessary. Use measured/verified parameters rather than assuming all branches or LNAs independent; [S8] supports the existence of coupled amplifier-noise paths, not a universal network model.
- **Decisions / implementation:** Derive reciprocal-mixing contributions from blocker and effective LO spectra through actual preselection, mixing and observation filtering, including internal LO-buffer contributions [S6]. Derive small timing-error disturbances from the complete analog waveform and sampling-clock process [S7], preserving relevant source/clock/channel correlations. Compare gain/filter/rejection placement and derive oscillator/clock/interface requirements from allowable degradation; distinguish disturbance generation here from budget assembly in CAP-013 and nonlinear gain control in CAP-014.
- **Evidence / failure:** Calculate a narrow-blocker/flat-noise limiting case and a finite-spectrum or multiblocker contrast; evaluate a physically constructed coupled-channel covariance rather than postulating a diagonal matrix. Quantify when flat-spectrum, small-error, independent-source or stationary assumptions fail. Use CAP-004/005 for finite-record uncertainty and CAP-039 for correlation sensitivity. Work product: evaluated source/path model and design constraints with missing physical evidence explicit.
- **P / coverage / relevance:** Learning: CAP-003/004/005/008 and RF noise/network baseline. Conditional: CAP-010 for antenna/vector inputs. Interactions: CAP-018 supplies converter-specific refinements after the source/path model; CAP-013 assembles budgets; CAP-014–016/018/037/039 use these contributions. F for coherent physical noise/interference reasoning and necessary derivations, S for noise-network bridges, E for detailed device physics/current parameters. All classes; U-07/U-09.

### B. Architecture, budgets and signal/reference chains

#### CAP-011 — Select a feasible receiver architecture

- **Outcome / dimensions:** C/A/D/I/V. Select and substantiate a realizable receiver architecture using CAP-043 feasibility results, quantitative interface checks and competing technology choices; identify assumptions requiring evidence.
- **Physics / methods:** Signal/reference flow, conversion/sampling placement, analog/digital/hybrid partition, resource and performance bounds; compare shared and independent references and centralized/distributed processing.
- **Decisions / implementation:** Trade sensitivity, bandwidth, dynamic range, coherent observability, calibration access, power, cost, latency, scale and maintainability. Identify early risk-reduction experiments rather than asserting feasibility from a block diagram.
- **Evidence / failure:** Compare representative architectures with calculated interface and resource allocations, including loading, drive/termination, noise/linearity, latency, power, calibration access and state behavior. Trace consequential manufacturer facts to part/revision/conditions, separating guarantees, typical data and unknowns. Resolve a supplied incompatibility by redesign or a bounded characterization result. Work product: defensible architecture selection and interface/reference-plane map; missing evidence is not a passing allocation.
- **P / coverage / relevance:** Learning: CAP-001/002/003/043. Conditional: CAP-010 for apertures/sensors, CAP-045 for distributed references. Interactions: CAP-013 and subsystem capabilities iterate allocations and selections. F for coherent architecture/selection methods, E for verified current device facts. All classes; U-07.

#### CAP-012 — Design frequency and phase transfer through the complete chain

- **Outcome / dimensions:** C/M/A/D/I/V. Produce a frequency plan that also accounts for phase signs, delays and reference relationships through mixing, multiplication/division and sampling.
- **Physics / methods:** Desired/image/alias bands, harmonics and spurs, transfer functions, spectral inversion and group delay; distinguish phase offset from frequency-dependent delay.
- **Decisions / implementation:** Choose conversion stages, filters, sample rates and frequency-agility procedures; specify which oscillator and digital states must be known.
- **Evidence / failure:** Track test tones and modulation across operating bands and states, checking end-to-end phase orientation and undesired response. Work product: annotated frequency/reference plan with exclusions and reset-sensitive elements.
- **P / coverage / relevance:** Learning: CAP-002/003/005. Interactions: CAP-018 refines sampling-zone choices after the base frequency-plan concepts; CAP-015/020 supply oscillator/processing implementations. F for coherent transfer, S for conventional planning refreshers. All classes; U-08.

#### CAP-013 — Build coupled performance and error budgets

- **Outcome / dimensions:** C/M/A/D/V. Allocate receiver performance from application outcomes to sources of noise, distortion, timing, amplitude, phase and delay error with correlations and sensitivity included.
- **Physics / methods:** Use CAP-044 to generate physical contributions and CAP-004/005/008 to propagate covariance/cross-spectra, deterministic bounds and stochastic allocations through actual reference planes and operating states. Keep margin, physical variability, parameter uncertainty, correction residual and measurement uncertainty distinct; avoid double counting shared sources.
- **Decisions / implementation:** Trade oscillator, clock, analog, converter, processing, calibration and environmental allocations; identify dominant interactions and feasibility limits.
- **Evidence / failure:** Calculate allocations and budget closure for supplied conditions, then vary a dominant correlation, blocker, environment or unavailable parameter. Compare closure with CAP-043 feasible regions and quantify which allocation or requirement fails. Work product: evaluated budget and sensitivity/uncertainty results; application metrics remain owned by CAP-035–041.
- **P / coverage / relevance:** Learning: CAP-002/004/005/008/009/011/012/044. Conditional: CAP-010 for geometry, CAP-045 for distributed budgets. Interactions: application requirements and subsystem results are inputs, not universal prior learning. F for coherent budgets, S for generic mechanics. All classes; U-09.

#### CAP-014 — Design the RF/analog chain for usable coherent information

- **Outcome / dimensions:** C/M/A/D/I/V. Design and evaluate gain, filtering, conversion, protection and switching that preserve usable complex information across the actual signal/blocker envelope, including overload and gain transitions.
- **Physics / methods:** Apply physical noise/interference contributions from CAP-044. Select an adequate memoryless, dynamic or measured nonlinear model for AM-to-AM/AM-to-PM behavior, intermodulation, leakage, impedance/load interactions and memory effects. Derive crest-factor/headroom constraints and complex response versus level, history and gain state. Identify where small-signal or IP2/IP3 extrapolation fails and where empirical characterization is necessary.
- **Decisions / implementation:** Calculate stage gain/filter/linearity/isolation allocations and choose component technologies with compatible drive, matching, loading, bias and dissipation. Design gain management, including channel coordination, hysteresis/settling as needed and valid-data intervals through switching, saturation and recovery. Distinguish missing manufacturer evidence from an assumed capability; obtain bounded evidence or preserve the risk.
- **Evidence / failure:** Evaluate weak-signal-plus-blocker, multitone/modulated crest-factor, strong-pulse and recovery cases; quantify residual phase/amplitude distortion and time to usable data. Compare alternative gain/filter placement using CAP-043/044. Work product: calculated chain design, implemented bounded gain policy and interpreted characterization; low noise figure or a two-tone intercept alone is insufficient.
- **P / coverage / relevance:** Learning: RF baseline, CAP-003/004/009/012/013/044. Conditional: CAP-018 for converter interfaces. Interactions: CAP-017/024/028 preserve state/calibration validity. F for coherent analog/nonlinear/gain reasoning, S for general circuit design, E for verified component facts. All classes; U-07.

#### CAP-015 — Select and analyze oscillators and synthesizers

- **Outcome / dimensions:** C/M/A/D/I/V. Relate oscillator/synthesizer behavior to the task observable, including phase noise, spurs, tuning and settling.
- **Physics / methods:** Reference and oscillator transfer through PLLs, multiplication/division, correlated noise and nonlinear/state-dependent behavior; distinguish nominal frequency accuracy from phase behavior.
- **Decisions / implementation:** Calculate reference/oscillator loop tradeoffs and derive a required effective LO-noise/spur envelope from supplied signal and blocker conditions using CAP-044. Compare representative synthesis technologies against tuning, settling, drive/termination, isolation, supply sensitivity and phase-state requirements; include internal buffers and unavailable guarantees.
- **Evidence / failure:** Evaluate a candidate synthesizer/loop at relevant frequencies, offsets and transitions using verified input data or explicitly bounded assumptions; compare calculated noise/settling with appropriate characterization and explain remaining uncertainty. Work product: evaluated technology/loop selection and evidence gaps, without promoting typical curves to guarantees.
- **P / coverage / relevance:** Learning: CAP-005/007/012/013/044. Interactions: CAP-016/017 establish endpoint/state behavior. F for coherent synthesis, S for oscillator circuit theory, E for part/revision-specific facts. All classes; U-07/U-09.

#### CAP-016 — Engineer LO, clock and reference distribution

- **Outcome / dimensions:** C/M/A/D/I/V. Design distribution that delivers the required differential and common-reference performance at actual endpoints.
- **Physics / methods:** Source-sharing, unequal transfer functions/delays, additive branch noise, skew, dispersion, reflections, loading and environmental sensitivity. Analyze what cancels in the specified observable and what does not.
- **Decisions / implementation:** Choose topology, buffering, power levels, isolation, connectors, routing, monitoring and distributed transfer/recovery where needed.
- **Evidence / failure:** Calculate endpoint common/differential disturbance transfer and compare branches under loading, cable and environmental changes. Select buffers, power levels and routing with interface/isolation checks; execute and interpret a bounded endpoint comparison that accounts for test-reference correlation. Work product: evaluated distribution design and residual evidence. CAP-045 owns distributed clock/reference inference; shared hardware alone is not an endpoint phase guarantee.
- **P / coverage / relevance:** Learning: CAP-002/005/012/013/015. Conditional: CAP-045 for distributed transfer. Interactions: CAP-022 uses endpoint allocations for channel matching. F for endpoint distribution, S for interconnect design, E for particular transfer hardware. Reference comparisons and multichannel systems; U-02.

#### CAP-017 — Establish synchronization and repeatability across state transitions

- **Outcome / dimensions:** C/A/D/I/V. Specify and verify startup, reset, retune, link-recovery and reference-loss sequences that establish the required signal relationship.
- **Physics / methods:** Divider, PLL, sampling, framing, FIFO, NCO and filter states; distinguish sample epoch, transport latency and analog/RF phase. A vendor discussion separates JESD204B framing latency from converter analog latency [S3].
- **Decisions / implementation:** Define initialization order, synchronization events, metadata, valid-data gating and whether calibration or reacquisition is required after each transition.
- **Evidence / failure:** Implement and exercise representative startup/reset/retune/recovery sequences; inspect end-to-end phase/time response and valid-data gating, with repeat counts and confidence assumptions suited to the failure claim. Work product: evaluated transition procedure and residual repeatability, not just a state table. Digital link alignment is insufficient evidence of analog-to-output coherence.
- **P / coverage / relevance:** Learning: CAP-002/012. Conditional: CAP-015/016 for synthesized/distributed references, CAP-018/020 for sampled/digital paths, CAP-045 for distributed clocks. Interactions: CAP-024/028 implement calibration/integration rules. F for transition reasoning, E for current device/interface guarantees. All stateful receivers; U-07.

#### CAP-045 — Establish distributed reference, timing and carrier-phase relationships

- **Outcome / dimensions:** C/M/A/D/I/V. Derive and realize a bounded method for establishing the task-required relationship among remote clocks, sample epochs and carrier phases; quantify remaining reference freedoms, uncertainty and valid holdover interval.
- **Physics / methods:** Derive clock offset/rate/drift and one-way/two-way measurement equations with endpoint/reference planes, propagation/equipment delays and reciprocity assumptions. Determine delay/offset identifiability and residual directional-asymmetry effects [S5]. Distinguish frequency agreement, time/epoch alignment, RF phase, modulo-cycle ambiguity and data transport latency; none alone establishes the others without an explicit transfer model.
- **Decisions / implementation:** Compare shared-reference transfer, independent-reference estimation and local holdover for supplied observations and link conditions. Calculate rate-mismatch accumulation, sample-epoch reconstruction/resampling requirements where digital, outage uncertainty and delayed-feedback bandwidth/stability limits. Specify reference switching, valid-data/reacquisition rules and what external timing/geometry knowledge is indispensable; protocols and current hardware are external inputs.
- **Evidence / failure:** Evaluate an offset/delay ambiguity and asymmetric two-way case, then execute or evaluate a bounded reference-alignment/recovery example. Quantify sample/time and carrier-phase residuals separately during steady operation, outage and return. Work product: evaluated distributed coherence method with task-specific limits; timestamps, round-trip agreement or frequency lock alone are not proof.
- **P / coverage / relevance:** Learning: CAP-002/003/005/006/007. Conditional: CAP-008/010 for joint geometry/clock inference. Interactions: CAP-018/020 realize sampled-stream alignment after core clock/reference models; CAP-016 builds distribution, CAP-017 controls transitions, CAP-025 maintains validity. F for distributed coherent inference/limitations, S for transfer-method examples, E for protocol/device particulars. Distributed radar, arrays/DF, interferometry, sensing and remote measurement; U-02.

#### CAP-018 — Select sampling and data conversion from signal and timing requirements

- **Outcome / dimensions:** C/M/A/D/I/V. Choose sampling architecture, rate, filtering and converter performance consistent with the required coherent information.
- **Physics / methods:** Aliasing/bandpass sampling, aperture timing and jitter/skew correlations, quantization, nonlinear distortion and interleaving. Use CAP-044 for timing-error generation from the entire analog waveform and clock spectrum, not the wanted tone alone. Test the assumptions behind independent white quantization noise for coherent inputs; distinguish encoder nonlinearities, front-end distortion, input noise and the conditional role of dither [S9].
- **Decisions / implementation:** Calculate converter range, headroom, anti-alias filtering and clock allocations under supplied wanted/blocker conditions. Compare technologies and verify driver/ADC/clock compatibility: bandwidth, loading, common-mode/drive, settling, reference/supply sensitivity, integrated filtering, state behavior and verified operating conditions. Include dither costs where used; it is not a universal cure.
- **Evidence / failure:** Evaluate broadband, coherent low-level, strong-blocker and overload/recovery cases in addition to a tone. Quantify converter/clock/driver contributions and identify missing guarantees requiring characterization. Work product: evaluated conversion/interface selection and residual error, with sample timing distinguished from data arrival.
- **P / coverage / relevance:** Learning: CAP-003/004/005/009/012/013/044. Interactions: CAP-014 supplies analog drive/gain, CAP-017 handles states. F for coherent sampling consequences, S for general converter theory, E for verified device facts/errata. Digital receivers; U-07.

#### CAP-019 — Preserve and correct quadrature and complex-response fidelity

- **Outcome / dimensions:** C/M/A/D/I/V. Determine how I/Q imbalance, DC offsets, leakage and conjugate images affect intended signal recovery or phase observation.
- **Physics / methods:** Quadrature downconversion and complex/improper-signal models as needed; frequency- and state-dependent amplitude/phase imbalance, image response and LO feedthrough.
- **Decisions / implementation:** Choose real versus quadrature paths, analog matching, correction structures and calibration stimuli; distinguish leakage estimation from suppression of a genuine near-DC signal.
- **Evidence / failure:** Estimate and apply a bounded I/Q correction; evaluate swept/modulated and near-DC desired-signal cases with data independent of the fit. Quantify residual conjugate/desired response and distortion from correction, including level/state changes. Work product: evaluated impairment/correction model with validity limits; removing a true signal is not a successful offset correction.
- **P / coverage / relevance:** Learning: CAP-003/004/006/012/014. Conditional: CAP-018/020 for digital correction. Interactions: CAP-024 supplies calibration procedure. F for quadrature reasoning/correction, E for device internals. Communications, radar, sensing and instruments; U-10.

#### CAP-020 — Design coherent digital frequency translation and filtering

- **Outcome / dimensions:** C/M/A/D/I/V. Specify DDC, channelization, decimation and resampling while preserving required phase, delay and sample identity.
- **Physics / methods:** NCO phase, multirate transforms, filter response/delay, alias rejection, transients and fractional-delay interpolation. Keep waveform latency distinct from phase slope and startup transients.
- **Decisions / implementation:** Calculate rates, passbands, filter/interpolation accuracy, precision and state rules. For equalization/resampling assess pole/zero and minimum-phase implications for causal/stable inversion, finite length, latency and noise enhancement versus residual distortion; compare a feasible approximation with an unattainable exact inverse. Track sample epochs and NCO phase through rate changes, asynchronous clocks and tuning.
- **Evidence / failure:** Realize and evaluate a bounded chain with impulse, tone and modulated inputs and alternate rate/reset states. Quantify delay/phase, alias rejection, finite-length residual and noise enhancement; identify one-sample/NCO mismatches. Work product: evaluated processing method and state behavior, not only a specification.
- **P / coverage / relevance:** Learning: CAP-003/005/009/012/018. Conditional: CAP-008 for matrix equalization. Interactions: CAP-045 supplies remote-clock estimates for asynchronous streams, CAP-021 realizes resources and CAP-024 uses corrections. F for coherent processing, S for general DSP filter design, E for core/library particulars. Digital receivers; U-07/U-08.

#### CAP-021 — Realize signal processing within resource and numerical constraints

- **Outcome / dimensions:** C/A/D/I/V. Translate a selected algorithm into a feasible FPGA/processor partition with predictable numerical and real-time behavior.
- **Physics / methods:** Fixed/floating point, scaling, overflow, truncation bias, coefficient precision, throughput, buffering, latency and clock-domain crossings; relate artifacts to the receiver observable.
- **Decisions / implementation:** Allocate compute, memory, interfaces and timing; define sample-loss detection, timestamps and valid-data behavior under overload.
- **Evidence / failure:** Implement and exercise a bounded processing function at representative precision and load; compare with a reference calculation and measure or otherwise establish timing/resource limits for the declared platform. Quantify overflow, truncation, latency and sample-loss consequences. Work product: evaluated realization and unresolved hardware evidence, not an inference of hardware correctness from floating-point agreement.
- **P / coverage / relevance:** Learning: CAP-009/018/020. Interactions: CAP-028 integrates the platform and CAP-031 assesses evidence. F for coherent implementation consequences, S for digital design, E for HDL/tool/platform details. Digital receivers; U-07.

### C. Multichannel calibration and physical realization

#### CAP-022 — Specify and align multichannel complex response

- **Outcome / dimensions:** C/M/A/D/I/V. Define channel matching in amplitude, phase and delay over the required band, states and operating conditions.
- **Physics / methods:** Relative transfer functions, phase slopes, dispersion, covariance and channel coupling; distinguish constant offsets, delay errors and frequency-dependent residuals.
- **Decisions / implementation:** Calculate amplitude/phase/delay equalization and residual allocation across band/states; compare physical matching with analog or digital correction before irreversible combination. Bound inverse-response noise enhancement, coefficient range/resolution, causal/stable realizability and permitted latency. Identify when prevention or architecture change is necessary rather than correction.
- **Evidence / failure:** Estimate and align a representative complex response; evaluate independent residuals across frequency and state, including a deep attenuation/null case. Distinguish identifiable response from correctable response, and independently required channel information from information discarded by combination. Work product: evaluated alignment with residual/noise/latency limits; vector antenna response is supplied by CAP-010, not established by scalar electronic matching.
- **P / coverage / relevance:** Learning: CAP-002/005/008/012/013. Conditional: CAP-010 for antenna/vector response, CAP-016 for distributed hardware references, CAP-020 for digital equalization. Interactions: CAP-023/024 establish calibration. F for multichannel matching/correction limits. Multichannel classes; U-05/U-10.

#### CAP-023 — Determine calibration observability and reference integrity

- **Outcome / dimensions:** C/M/A/D/V. Show which hardware/signal parameters can be inferred from the proposed calibration observations and which remain ambiguous or outside the reference path.
- **Physics / methods:** Measurement equations, rank, reference constraints, nuisance parameters, stimulus uncertainty, coupling and injection-path errors; distinguish identifiability from estimator precision.
- **Decisions / implementation:** Choose injection/loopback/over-the-air paths, known references and independent observables; include antenna/sensor effects where required by the task.
- **Evidence / failure:** Write and evaluate a calibration measurement equation, construct indistinguishable parameter combinations and omitted-path faults, and identify desired-signal/nuisance freedoms. Show what an injection can and cannot establish, including direction/polarization dependence where relevant. Work product: demonstrated observability and unobserved-error assessment; neither a small fit residual nor identifiability proves correction feasibility.
- **P / coverage / relevance:** Learning: CAP-002/006/008/009. Conditional: CAP-010 for antennas/sensors, CAP-022 for multichannel alignment, CAP-044 for physical noise limits. Interactions: CAP-024/030 implement correction/measurement. F for observability and retained information. All calibrated receivers; U-05/U-10.

#### CAP-024 — Design, apply and validate a calibration procedure

- **Outcome / dimensions:** C/M/A/D/I/V. Execute a bounded acquisition, estimation and correction procedure; quantify independent residuals and preserved desired-observable response over its declared valid envelope.
- **Physics / methods:** Calibration transfer/matrix estimation, uncertainty, interpolation, regularization, correction ordering and reference-path stability. Evaluate correction noise enhancement, causal/stable implementation, finite resources and latency with CAP-020/022 where applicable. Distinguish parameter identification, approximate compensation and recovery of information; clipping, aliasing or rank loss cannot generally be undone without additional information.
- **Decisions / implementation:** Choose factory versus operational calibration, stimulus coverage, storage/versioning, update rules, valid states and invalidation triggers; retain coefficients and provenance with configuration.
- **Evidence / failure:** Apply corrections and evaluate held-out conditions/data, residual uncertainty, noise gain and desired-signal transfer; include band/gain/environment changes and a case where correction must be rejected or restricted. Work product: executed bounded calibration and evaluated validity, including coefficients/resources and retained information. NRAO [S4] supplies only a domain-specific calibration-timescale example.
- **P / coverage / relevance:** Learning: CAP-006/009/023/030. Conditional: CAP-017 for state-dependent validity, CAP-020 for digital corrections, CAP-022 for multichannel alignment, CAP-010 for field/sensor calibration. Interactions: CAP-025/033 use operational/factory results. F for coherent calibration, E for instrument-specific commands. All calibrated classes; U-10.

#### CAP-025 — Maintain coherence under drift, motion and changing conditions

- **Outcome / dimensions:** C/M/A/D/I/V. Decide when fixed correction, periodic calibration, continuous tracking or degraded operation is appropriate.
- **Physics / methods:** Drift spectra, environmental sensitivities, motion-induced change, estimator update/latency and unobservable change; separate transducer/propagation dynamics from receiver drift.
- **Decisions / implementation:** Calculate update/cadence/latency tradeoffs, calibration downtime and validity thresholds from task consequences. Derive desired-signal and nuisance transfer through tracking/compensation; choose fixed correction, tracking or degraded operation without silently removing the measurand. Include distributed holdover using CAP-045 when needed.
- **Evidence / failure:** Evaluate a maintenance/tracking policy under drift, motion, fades, outages and environmental gradients. Inject a desired physical variation as well as a nuisance change and quantify what is retained, attenuated or ambiguous. Work product: evaluated coherence-maintenance behavior and recovery limits; a smaller residual alone is not success.
- **P / coverage / relevance:** Learning: CAP-002/005/007/023/024. Conditional: CAP-010 for motion/transduction/propagation and CAP-045 for distributed holdover. Interactions: CAP-027 supplies environmental evidence. F for maintaining coherent information, E for specialist environmental models. Dynamic/long-lived systems; U-04.

#### CAP-026 — Translate coherent allocations into PCB, power and interconnect design

- **Outcome / dimensions:** C/A/D/I/V. Produce physical constraints connecting sensitive signal/reference paths to layout, power integrity, shielding and test access.
- **Physics / methods:** Coupling, return currents, impedance discontinuities, supply modulation, crosstalk, isolation and differential path response; connect aggressors and sensitivities to phase/noise/spur budgets.
- **Decisions / implementation:** Choose stack-up/routing constraints, reference partition, distribution levels, regulators/filtering, shielding and monitor points. Avoid assuming length matching alone establishes matching of electrical transfer.
- **Evidence / failure:** Translate supplied allocations into actual routing, power/filtering/shielding and test-access choices; calculate a representative coupling/supply-to-phase contribution and execute or interpret an aggressor/path comparison. Work product: evaluated physical constraints and mitigation evidence. Length matching or a layout checklist alone does not establish electrical matching.
- **P / coverage / relevance:** Learning: CAP-012/013/014 and RF interconnect baseline. Conditional: CAP-015/016 for LO/reference paths, CAP-018/021 for converter/digital interfaces, CAP-022 for multichannel matching. Interactions: CAP-027/028 handle environment/integration. F for coherent implications, S for SI/PI/EMI, E for fabrication/regulatory facts. Hardware classes; U-07.

#### CAP-027 — Control thermal, mechanical and environmental effects

- **Outcome / dimensions:** C/A/D/I/V. Connect environmental changes to system-level coherent errors and specify mitigations and representative tests.
- **Physics / methods:** Temperature-dependent phase/delay/gain, gradients and time constants, cable/connector strain, vibration, warmup and power-state changes; distinguish uniform chamber conditions from internal spatial gradients.
- **Decisions / implementation:** Select packaging, materials, mounting, sensors, thermal regulation and operating/calibration envelopes; expose residual sensitivity rather than assuming compensation is complete.
- **Evidence / failure:** Calculate a representative environmental sensitivity and mitigation residual; execute or interpret thermal-gradient/cycling, vibration or handling evidence with reference-path controls. Work product: evaluated environmental allocation and validity limits; uniform chamber results alone need not cover internal gradients.
- **P / coverage / relevance:** Learning: CAP-009/013/026. Conditional: CAP-016 for reference paths, CAP-024/025 for calibration/compensation. Interactions: CAP-033/034 assess manufacturing/service variation. F for coherent effects, S for supporting thermal/mechanical reasoning, E for detailed mechanics/standards. Physical systems; U-07.

#### CAP-028 — Integrate hardware, firmware and configuration into an observable system

- **Outcome / dimensions:** C/A/D/I/V. Define interfaces and bring-up procedures that preserve the meaning of samples, calibration and operating states.
- **Physics / methods:** End-to-end timing/state causality, control/data-plane interactions, synchronization handshakes, configuration provenance and fault containment.
- **Decisions / implementation:** Specify firmware/driver sequencing, timestamps, channel identity, correction versions, lock indicators, logging and valid-data gates; partition subsystem responsibilities and integration stages.
- **Evidence / failure:** Bring up and exercise a bounded integrated path, including applicable partial reset, reference/link loss, dropped samples and stale coefficients. Interpret raw data and state metadata against the observable specification. Work product: demonstrated interface/state behavior and diagnosed failures, not merely successful communication or an integration checklist.
- **P / coverage / relevance:** Learning: CAP-001/002/011/017. Conditional: CAP-020/021 for digital realization, CAP-024 for calibrated states, CAP-045 for distributed sample/reference metadata. Interactions: CAP-032/034 handle diagnosis/service. F for coherent integration, S for software/configuration practice, E for platform code. Integrated receivers; U-07.

### D. Modeling, measurement, verification and lifecycle

#### CAP-029 — Formulate and assess models for an engineering decision

- **Outcome / dimensions:** C/M/A/D/I/V. Construct, execute and assess the simplest adequate analytical or computational model for a declared engineering decision; quantify its applicability and evidence limitations.
- **Physics / methods:** Signal/reference/error models, sensitivity, correlated sources, deterministic/stochastic cases, approximation hierarchy and model discrepancy. Distinguish mathematical correctness, software correctness and physical applicability.
- **Decisions / implementation:** Decide which impairments, states and correlations must be represented, which parameters need measurement and which conclusions cannot be inferred.
- **Evidence / failure:** Calculate a representative result and sensitivities, execute independent/limiting-case and numerical checks, and compare with appropriate reference or empirical evidence where available. Identify model discrepancy and unsupported extrapolation. Work product: evaluated model and bounded engineering conclusion. The reader must do this work in the eventual book; no model is developed by this inventory revision.
- **P / coverage / relevance:** Learning: CAP-003/004/005/009. Conditional: CAP-006/008 for estimation/matrix problems, CAP-010 for propagation, CAP-013 for budgets and relevant subsystem capabilities. Interactions: CAP-030 provides empirical evidence. F for coherent model construction/evaluation, S for general numerical tools. All classes; U-09.

#### CAP-030 — Design a measurement with a defensible uncertainty statement

- **Outcome / dimensions:** C/M/A/D/I/V. Set up, execute and interpret a bounded measurement of the declared quantity, with calibration/reference paths and a defensible uncertainty statement.
- **Physics / methods:** Operational measurement equation, intentional observation/estimation method versus instrument imperfections, sensitivity coefficients, covariance, floors/dynamic range, loading, corrections and residual uncertainty. Evaluate finite-record statistics/effective degrees of freedom, including stochastic source contributions where relevant; separate bias, repeatability and estimator uncertainty. Method-defined measurands are legitimate when disclosed [S2].
- **Decisions / implementation:** Choose phase/time/correlation or transfer measurements, fixtures, de-embedding, reference independence and record length; document traceability appropriate to the intended claim.
- **Evidence / failure:** Execute or critically evaluate a representative measurement, including instrument floor, fixtures, correlated references and an independent configuration where practical. Calculate uncertainty with applicability limits; distinguish a low apparent residual from a sensitive test. Work product: interpreted data and uncertainty budget, not a procedure alone. [S2] supports covariance and first-order limits, not arbitrary nonlinear propagation.
- **P / coverage / relevance:** Learning: CAP-002/005/006/009. Conditional: CAP-023 for calibration observability, CAP-008/044 for coupled noise, CAP-018/020 for sampled measurements. Interactions: CAP-024 applies calibration and CAP-031 assesses compliance. F for coherent metrology, S for general methods, E for instrument particulars. All classes; U-01/U-09.

#### CAP-031 — Establish verification coverage and make bounded compliance assessments

- **Outcome / dimensions:** C/A/D/I/V. Trace each requirement to analysis, inspection, test or demonstration with configurations, conditions, uncertainty and decision rules stated.
- **Physics / methods:** Evidence sufficiency, test coverage, statistical sampling, worst-case reasoning and applicability limits; separate model validation, design verification and system compliance.
- **Decisions / implementation:** Define test matrices over frequency, gain, environment, calibration and transitions; identify required hardware evidence and engineering review. Define treatment of uncertainty near a limit before interpreting a pass/fail result.
- **Evidence / failure:** Execute or evaluate representative requirement-evidence cases, apply a stated uncertainty decision rule and identify untested corners. For slips/restarts or other rare events, calculate defensible observation duration, exposures and statistical bounds under declared dependence assumptions; zero observed failures is not zero failure probability. Work product: evaluated compliance evidence with unresolved claims; software tests alone are not system compliance.
- **P / coverage / relevance:** Learning: CAP-001/002/009/030. Conditional: CAP-013 for budget evidence, CAP-029 for model evidence and relevant subsystem methods. Interactions: supplied application requirements and implemented configuration define the assessed use. F for coherent verification, S for assurance methods, E for mandated standards. All classes; U-01/U-07.

#### CAP-032 — Diagnose failures and isolate competing physical explanations

- **Outcome / dimensions:** C/A/D/I/V. Use a failed observable to formulate and discriminate hypotheses across signal, reference, propagation, processing and measurement paths.
- **Physics / methods:** Error signatures versus frequency, time, channel, environment and operating state; causal interventions, substitutions and controlled changes; recognize ambiguous evidence.
- **Decisions / implementation:** Choose informative tests and safe operating changes before applying correction; preserve raw data/configuration and distinguish root cause from symptom suppression.
- **Evidence / failure:** Execute a bounded discriminating experiment or evaluate supplied interventions, showing which hypotheses are excluded and what remains ambiguous. Work product: supported diagnosis and corrective-action check with preserved raw data/configuration; one phase trace is insufficient for a unique cause.
- **P / coverage / relevance:** Learning: CAP-002/009/030. Conditional: CAP-013/017/023/028 and subsystem methods for the suspected paths. F for coherent diagnosis, S for general diagnostic practice. All classes; U-10.

#### CAP-033 — Plan production calibration, test coverage and yield

- **Outcome / dimensions:** C/M/A/D/I/V. Estimate joint production yield, calibration adjustment needs and test/calibration effort, then evaluate a production strategy against variation, coverage, cost and throughput constraints.
- **Physics / methods:** Propagate correlated unit/lot/process variation, environmental sensitivities and calibration residuals through task requirements. Use declared distributions or defensible bounds; assess coefficient range/resolution, fixture uncertainty, measurement capability and test sensitivity. Individual tolerance compliance is not a calculation of joint yield.
- **Decisions / implementation:** Calculate frequency/gain/temperature/state sweep effort, settling/acquisition time, retest/rework burden and calibration downtime. Compare correction range and residual requirements with feasible factory adjustment/test access. Validate reduced/surrogate coverage against the faults it may miss; justify guard bands without treating unknown variation as measured statistics.
- **Evidence / failure:** Evaluate joint yield and calibration/test time for a bounded supplied production case; vary unsupported distributions/correlations and fixture errors to expose sensitivity. Assess escapes and false rejects with uncertainty. Work product: calculated production feasibility and evidence gaps, not a yield claim extrapolated from one prototype.
- **P / coverage / relevance:** Learning: CAP-009/013/024/030/031. Conditional: CAP-027 for environmental coverage and CAP-008 for joint matrix variation. Interactions: CAP-034 uses production/service evidence. F for coherent production feasibility, S for statistical manufacturing, E for supplier/process particulars. Manufactured systems; U-07.

#### CAP-034 — Preserve performance through reliability, service and configuration change

- **Outcome / dimensions:** C/A/D/I/V. Specify how aging, repairs, replacements and updates affect calibration validity, availability and continued evidence of performance.
- **Physics / methods:** Drift/failure mechanisms, environmental history, reference health, calibration dependencies and interchangeability; distinguish gradual loss of accuracy from total failure.
- **Decisions / implementation:** Define monitoring, field recalibration, replaceable-unit boundaries, retained records and regression scope after hardware/firmware changes; account for obsolescence and changed component behavior.
- **Evidence / failure:** Evaluate a repaired, replaced or updated system, apply calibration invalidation/requalification rules and interpret representative monitoring/regression evidence. Work product: supported maintenance decision and residual lifecycle risk; no numerical reliability claim without appropriate data.
- **P / coverage / relevance:** Learning: CAP-025/028/031. Conditional: CAP-027 for environmental aging and CAP-033 for production/service interchangeability. F for coherent lifecycle decisions, S for reliability methods, E for lifetime/qualification facts. Deployed systems; U-07.

### E. Application-specific engineering outcomes

These entries require shared capabilities rather than repeating their derivations. Full coverage refers to essential receiver reasoning for the declared application family; it does not promise every mission algorithm, protocol or instrument implementation.

#### CAP-035 — Engineer carrier-coherent communications reception

- **Outcome / dimensions:** C/M/A/D/I/V. Derive carrier/timing acquisition and tracking requirements from the selected waveform, channel and reception objective, then select a feasible receiver strategy.
- **Physics / methods:** Apply CAP-004/005/042 to carrier/timing/channel estimation, ambiguity, equalization, Doppler, phase noise and interference. Derive waveform-specific residual-to-performance relationships, including a multicarrier contrast separating common phase correction from intercarrier disturbance. Relate finite pilot/burst observations to acquisition and ambiguity resolution before payload use.
- **Decisions / implementation:** Choose synchronization/equalization partition, pilot assumptions, acquisition search, loop modes and buffering; identify which transmitter/receiver phase is unknown but recoverable.
- **Evidence / failure:** Calculate acquisition/ambiguity feasibility and residual detection/signal-quality performance for a supplied burst; implement a bounded recovery method and evaluate fading/slips, multicarrier phase variation and desired-signal distortion from rejection. Work product: evaluated receiver/recovery choice and evidence limits, not only an error allocation or test plan.
- **P / coverage / relevance:** Learning: CAP-002/006/007/011/013/042/044. Conditional: CAP-014–021 for the chosen analog/converter/DSP chain, CAP-023–025 for calibration, CAP-028 for digital integration. Interactions: CAP-030/031/033/034 supply evidence and lifecycle assessments. F for coherent recovery/error reasoning, S for modulation/coding, E for protocols. P-COM; U-01/U-04.

#### CAP-036 — Engineer coherent radar reception and processing interfaces

- **Outcome / dimensions:** C/M/A/D/I/V. Connect transmitter/return coherence and receiver impairments to range, Doppler, angle and detection behavior for declared waveforms and observation intervals.
- **Physics / methods:** Waveform delay/Doppler response, fast/slow-time sampling, coherent accumulation, transmit/receive reference correlations, leakage, clutter, motion and pulse/chirp phase state.
- **Decisions / implementation:** Allocate reference, timing, waveform and receiver errors; choose synchronization and calibration across pulses/channels; identify processing assumptions affected by hardware.
- **Evidence / failure:** Calculate a leakage/clutter-induced phase-noise pedestal against a delayed weak target, using actual path/reference transfer and waveform weighting; evaluate gain/headroom and recovery time. Contrast delayed returns with loopback and bistatic with shared-reference operation. Work product: evaluated waveform/receiver allocation and bounded processing or measurement evidence, with missing mission inputs explicit.
- **P / coverage / relevance:** Learning: CAP-002/005/010/011/013/042/044. Conditional: CAP-007 for tracking, CAP-014–021 for the selected chain, CAP-022–025 for multichannel/calibration, CAP-045 for separate references. Interactions: CAP-030/031/033/034 assess evidence/lifecycle. F for coherent waveform/receiver consequences, S for radar processing, E for mission-specific imaging. P-RAD; U-04.

#### CAP-037 — Engineer coherent receiving arrays and beam formation

- **Outcome / dimensions:** C/M/A/D/I/V. Translate beam requirements into element-response, geometry, weighting, calibration and implementation constraints.
- **Physics / methods:** Use CAP-010 for the vector manifold/coupling and CAP-044 for physically constructed channel-noise covariance. Calculate weighted signal/noise response, beam/pattern/pointing sensitivity and null robustness; derive phase versus delay steering consequences over bandwidth/scan. Include degrees of freedom, training contamination, polarization leakage and correlated calibration errors where task-relevant.
- **Decisions / implementation:** Choose analog/digital/hybrid partition and correction access; allocate element errors by pattern consequences rather than only channel matching.
- **Evidence / failure:** Calculate beam sensitivity and a pattern/null outcome with correlated noise and a bounded calibration/manifold error, comparing phase-only and delay or digital alternatives. Realize and evaluate a bounded weight/alignment example, distinguishing electronic from over-the-air evidence. Work product: evaluated pattern/noise allocation and failure limits; a channel test alone does not establish an array outcome.
- **P / coverage / relevance:** Learning: CAP-008/010/011/013/022/042/044. Conditional: CAP-016/017 for references/states, CAP-018/020 for digital arrays, CAP-023/024 for calibration, CAP-045 for distributed arrays. Interactions: CAP-026/027/030/031 supply physical/evidence constraints. F for coherent array reasoning, S for antenna methods, E for radiator design. P-ARR; U-05.

#### CAP-038 — Engineer direction-finding inference and receiver requirements

- **Outcome / dimensions:** C/M/A/D/I/V. Derive receiver/manifold accuracy and calibration needs from a stated bearing-estimation problem and geometry.
- **Physics / methods:** Phase/time/amplitude comparisons, spatial sampling, covariance-based methods where justified, ambiguity, conditioning, multipath, polarization and near/far-field assumptions; distinguish resolution, precision, bias and identification failure.
- **Decisions / implementation:** Choose geometry and estimator family consistent with signals, snapshots and calibration access; identify what can be corrected electronically and what requires external geometry or propagation knowledge.
- **Evidence / failure:** Calculate representative bearing sensitivity/ambiguity under supplied geometry and imperfect vector manifold; test coherent multipath, multiple sources and receiver error as competing explanations. Implement/evaluate a bounded estimator and identify unresolved cases rather than forcing a unique bearing. Work product: evaluated inference, calibration needs and field-evidence limits.
- **P / coverage / relevance:** Learning: CAP-006/008/010/011/013/022/044. Conditional: CAP-007 for tracking, CAP-023–025 for manifold calibration, CAP-042 for rejection/detection and CAP-045 for distributed receivers. Interactions: CAP-030/031 assess field evidence. F for DF receiver/inference reasoning, S for representative estimators, E for exhaustive algorithms. P-DF; U-04/U-05.

#### CAP-039 — Engineer interferometric correlation and reference calibration

- **Outcome / dimensions:** C/M/A/D/I/V. Specify a complex correlation observable and the delay/reference/calibration chain needed to interpret it across the intended baselines and integration intervals.
- **Physics / methods:** Use CAP-004/005/044 for stochastic signals, physical coupled noise and complex correlation. Derive finite-integration estimator bias/variance and sensitivity including stochastic source power, colored/limited-band data, effective independent samples and alignment error. Separate geometric/instrumental delay, fringe behavior, clock offset/rate, propagation and source/reference freedoms; use CAP-045 for distributed clocks.
- **Decisions / implementation:** Choose time/frequency alignment, phase referencing, calibration observations and required external geometry/clock knowledge; identify remaining reference freedoms and data metadata.
- **Evidence / failure:** Calculate finite-integration correlation sensitivity and residual alignment loss for supplied source/noise and clock conditions; compare shared/independent references and evaluate a bounded correlation/calibration example. Separate uncertainty from correlated bias and preserve required astrometric/reference information. Work product: evaluated correlator/reference choice; a split deterministic source does not establish weak stochastic-signal sensitivity. [S4] supports only the stated calibration distinctions.
- **P / coverage / relevance:** Learning: CAP-002/004/005/006/008/010/011/013/042/044. Conditional: CAP-016/017 for references/states, CAP-018/020/021 for digital correlators, CAP-022–025 for calibration, CAP-028 for digital metadata, CAP-045 for separate clocks. Interactions: CAP-030/031 establish evidence. F for correlation/sensitivity/reference foundations, S for interferometric interpretation, E for specialist imaging. P-INT; U-03.

#### CAP-040 — Engineer coherent sensing from physical quantity to reported result

- **Outcome / dimensions:** C/M/A/D/I/V. Relate a chosen physical measurand to phase, frequency, delay or complex-amplitude observations and identify the usable range and ambiguity.
- **Physics / methods:** Transduction/path sensitivity, phase wrapping, motion dynamics, multi-observable inference, drift and environmental cross-sensitivity; separate sensitivity from accuracy and resolution from unambiguous range.
- **Decisions / implementation:** Choose reference path, modulation/diversity, tracking bandwidth and environmental compensation; identify sensor effects that receiver-only calibration cannot remove.
- **Evidence / failure:** Calculate measurand sensitivity, ambiguity and uncertainty with a nuisance reference-path change; derive transfer through tracking/compensation and test fades/wrap recovery. Execute or interpret a comparison with an independent physical reference. Work product: evaluated physical inference and retained-signal response, including cases that remain unobservable; quiet electronics alone do not demonstrate physical accuracy.
- **P / coverage / relevance:** Learning: CAP-002/006/007/009/010/011/013/023. Conditional: CAP-014–021 for the selected chain, CAP-024/025 for correction, CAP-045 for distributed sensing. Interactions: CAP-027/030/031 supply environmental/physical evidence. F for coherent inference/signal retention, S for representative transduction, E for specialist sensor physics. P-SEN; U-04/U-06.

#### CAP-041 — Engineer phase-sensitive instruments and transfer measurements

- **Outcome / dimensions:** C/M/A/D/I/V. Specify a receiver instrument that reports phase/time/transfer quantities at declared ports with usable calibration and uncertainty.
- **Physics / methods:** Ratio/reference measurements, path de-embedding, source/receiver coupling, phase/time conversion, bandwidth/averaging and instrument drift; distinguish repeatability from traceable accuracy.
- **Decisions / implementation:** Choose reference and switching topology, calibration standards, dynamic range, settling and port-extension procedures; account for correlated source/reference effects.
- **Evidence / failure:** Execute or critically evaluate a supplied transfer/phase measurement and calculate the uncertainty after reference/fixture corrections. Vary level, cable and reference topology to distinguish DUT behavior from receiver error, preserving intentional method dependence. Work product: evaluated instrument/technology choice and interpreted calibrated result, not an uncertainty/test plan alone.
- **P / coverage / relevance:** Learning: CAP-002/005/009/011/012/013/023/030/031. Conditional: CAP-014–022 for the selected analog or digital implementation, CAP-024/025 for correction, CAP-045 for remote references. Interactions: CAP-026/027 constrain fixtures/environment. F for phase-sensitive receiver/metrology, S for instrument examples, E for commands/standards. P-MET; U-01/U-07.

## 5. Coverage and major dependencies

### 5.1 Charter and lifecycle cross-check

This table records where a responsibility is developed, not evidence that its engineering method has already been validated.

| Charter domain / lifecycle responsibility | Canonical capability homes | Coverage assessment / remaining boundary |
|---|---|---|
| Operational need, requirements, feasibility, traceability | CAP-001/002/011/031/043 | Quantitative feasible regions and incompatibility decisions explicit; actual product limits remain inputs |
| Coherence, complex signals, stochastic phase, correlation, spectra | CAP-002–005 | Present; conventions and statistical depth U-08/U-09 |
| Estimation, synchronization and mathematical support | CAP-006–009/017/045 | Acquisition, information limits and minimum distributed relationships explicit; specialist methods remain bounded |
| Detection, correlation and coherent accumulation | CAP-042/035/036/039 | Present; waveform/noise assumptions and processing depth require review |
| Architecture, frequency planning, noise, linearity, budgets | CAP-011–014/043/044 | Physical disturbance generation, nonlinear gain management and calculated budget closure separated |
| RF/analog conversion, synthesis, references | CAP-012/014–016/019/045 | Technology/interface selection and reference relationships explicit; current part data external |
| Conversion, I/Q, DDC, recovery, FPGA/processor consequences | CAP-007/017–021/028/035 | Present; platform details remain external |
| Multichannel alignment, observability, calibration and drift | CAP-022–025 | Observability, feasible correction, desired-signal retention and residual assessment explicit; U-10 |
| PCB, power, SI, EMI, thermal, mechanical, environment | CAP-026/027 | Present at coherent consequence/interface depth |
| Modeling, sensitivity, uncertainty, measurement, verification | CAP-009/029–032 | Present; no physical validation performed |
| Manufacturing, production, yield, reliability, configuration | CAP-024/028/030/033/034 | Joint yield, correction resources, calibration/test effort and uncertainty explicit; specialist review needed |
| Communications, radar/sensing, arrays/DF and phase measurement | CAP-035–041 | All named rows mapped; specialist breadth U-02–U-06 |
| Integration, diagnosis, service and lifecycle evidence | CAP-028/031–034 | Present; certification-specific requirements external |

### 5.2 Major learning dependencies and engineering interactions

| Relation type | Foundations / input | Enables / use | Boundary |
|---|---|---|---|
| Learning | Baseline + CAP-002/003 | CAP-004–009/012 | Define representations/references before stochastic calculations |
| Learning | CAP-003–006/008 | CAP-042 | Detection/integration methods require signal/noise and estimation foundations |
| Learning | CAP-001/002/006/009 | CAP-043, then CAP-011 | Quantitative feasibility precedes defensible architecture selection; subsystem particulars may initially be supplied |
| Learning | CAP-003–005/008 + RF noise/network baseline | CAP-044, then CAP-013/014–016/018 | Construct physical sources/covariance before assembling budgets and allocations |
| Learning | CAP-002/003/005/006/007 | CAP-045 | Distributed inference needs explicit clock, measurement and loop foundations |
| Learning | CAP-002/006/008/009 | CAP-023 | General calibration observability does not require a multichannel/digital chain |
| Learning | CAP-002/005/006/009 | CAP-030, then CAP-024/031 | Operational metrology precedes executed calibration and compliance interpretation |
| Conditional | CAP-010 + CAP-022 | CAP-023/024 for antenna/multichannel calibration | Field/manifold and alignment knowledge only when those paths are in scope |
| Conditional | CAP-018/020/021 | CAP-022/028/037/041 for sampled/digital implementations | No digital prerequisite for analog alignment or instruments |
| Conditional / interaction | CAP-045 | CAP-016/017/025 and remote-clock applications; CAP-020 exchanges stream-alignment parameters | Distributed inference is conditional for remote references; sampled implementation and clock estimates interact after their own foundations |
| Interaction | CAP-011/013/014–027/043 | Architecture, allocations, physical realization and calibration access | Iterate feasibility and design; not a circular foundational learning requirement |
| Interaction | CAP-017/024/025/028 | State validity, calibration and integration | Share operating-state/interface results without imposing one universal implementation order |
| Learning / conditional | CAP-009/013/024/030/031; CAP-027 when environment matters | CAP-033/034 | Production/service uses measured or bounded variation and declared conditions |

Architecture, budgets, calibration access and physical design constrain one another iteratively. They are engineering interactions, not a demand for circular teaching. Introduce a motivated system problem early, develop minimum foundations, then revisit architecture with progressively better models. Likewise CAP-001 can introduce an observable qualitatively before CAP-002–009 supply its full mathematics.

Conditional links identify implementation-specific extensions after the core foundations; where two methods exchange results, their shared use is an interaction rather than a requirement to learn each in full first. For example, analog port metrology can use CAP-002/005/006/009/030/041 without CAP-018/020/022; analog array alignment uses CAP-010/022 without a DDC, while digital array correction adds CAP-018/020/021. The eventual architecture should distinguish learning order from engineering execution and reference lookup. Foundation clusters and application entry points can support multiple reading paths; no book part or chapter numbering is approved here.

### 5.3 Depth and redundancy assessment

The shared scientific core is CAP-002–010/042/044; quantitative system feasibility is CAP-043; signal/reference and system methods are CAP-011–025/045; realization and evidence methods are CAP-026–034. Application entries CAP-035–041 own task-specific mappings, observables and failure conditions. Their references to shared methods must not become duplicate derivations.

Canonical boundaries needing editorial discipline:

- CAP-002 defines observables; CAP-005 analyzes their stochastic/spectral behavior; CAP-030 realizes their measurement; CAP-041 designs an instrument around them.
- CAP-006 owns general estimation/identifiability; CAP-023 applies it to calibration references; CAP-024 owns the actual correction procedure.
- CAP-007 owns loop/tracking theory; CAP-017 owns system transitions; CAP-025 owns maintaining valid performance over changing conditions.
- CAP-009 owns general approximation/uncertainty reasoning; CAP-013 owns design allocation; CAP-030 owns measurement uncertainty; CAP-031 owns requirement-evidence decisions.
- CAP-022 owns channel response; CAP-037 owns beam consequences; CAP-038 owns direction inference; CAP-039 owns baseline correlation. Similar hardware does not imply identical task acceptance.
- CAP-042 owns general detection, accumulation and signal-preserving rejection; application entries select assumptions and interpret task performance.
- CAP-043 owns feasible operating regions and incompatibility conclusions; CAP-011 owns architecture selection, CAP-013 budget assembly and CAP-014 nonlinear gain operation.
- CAP-044 owns physical source/path/covariance construction; CAP-004/005 own stochastic mathematics and CAP-037/039 application sensitivity.
- CAP-045 owns distributed clock/reference inference and its limits; CAP-016 owns physical distribution and CAP-017 state transitions.
- CAP-010 owns the minimum vector field/manifold model; full-wave radiator design, detailed environmental models and specialist polarimetric interpretation are external only beyond that minimum.

For each future treatment, the depth test is whether a reader can explain the mechanism, carry out consequential calculations, choose a defensible design and specify adequate evidence within the declared use. Full treatment requires essential derivations and nonideality/limiting-case reasoning. Selective treatment must explicitly name the assumption or interface supplied externally. A bibliography link without that bridge is inadequate.

## 6. Qualitative problem walkthroughs and contrasting failures

These are paper coverage audits, not solved designs or numerical models. All frequencies, bandwidths, waveforms, environmental limits, error limits and production quantities remain unspecified unless described qualitatively. The work products below are capabilities to be taught; they have not been calculated or demonstrated. Each walkthrough includes lifecycle obligations through the common production/service tail. Capability lists are task routes, not universal learning prerequisites: use the chosen implementation and §4 conditional links. The decision probes below specify calculations and alternatives the book must enable; none is reported as a solved or physically verified design.

### P-COM — Recover a burst communications signal with an initially unknown carrier

- **Need / observable:** Recover information after an acquisition interval despite initial carrier/timing uncertainty and a changing channel. Waveform, pilots, allowable errors, offsets and dynamics must be supplied before allocation.
- **Walkthrough:** CAP-001/035 identify waveform-dependent success criteria; CAP-002–007/042 distinguish acquisition, tracking, ambiguity and signal detection. CAP-011–020 select the conversion, reference, analog and recovery chain. CAP-021/028 define buffering, sample validity and reacquisition behavior. CAP-030/031 plan signal/error and acquisition tests; CAP-033/034 carry frequency/state coverage into factory and service procedures.
- **Contrast / failure:** A receiver with excellent locked-state residual phase can fail to acquire a short burst or suffer slips during fading. An independent transmitter cannot generally be treated as a distributed branch of the receiver LO.
- **Coverage finding:** Recovery of an unknown signal reference needs explicit development, beyond hardware channel stability. CAP-007/035 provide the home; coding/protocol detail remains selective/external.
- **Required calculation:** Calculate the feasible acquisition interval from supplied pilot/burst observations, offsets, SNR and ambiguity constraints (CAP-006/007/043); compare it with payload deadlines and buffering. For a multicarrier contrast, calculate residual common-phase and intercarrier disturbance using CAP-005/035/042, rather than substituting one RMS phase number.
- **Architecture / rejection decision and assessment:** Compare pilot-aided feedforward estimation with tracking/decision-directed recovery, and preselection/gain alternatives under a blocker (CAP-014/044). Reject a solution that closes locked-state noise but cannot acquire in time or clips before digital rejection. Evaluate the implemented bounded recovery, retained desired signal and reacquisition evidence.
- **Remaining boundary:** Burst/pilot/offset/dynamic conditions and the selected performance criterion; communications specialist review required.

### P-RAD — Preserve a pulsed or swept radar return across coherent processing

- **Need / observable:** Retain range/Doppler information and, if multichannel, angle information over the declared waveform and processing interval. Target delay/motion, leakage/clutter envelope and transmitter reference access are missing inputs.
- **Walkthrough:** CAP-001/002/010/036 establish the reference/geometry model; CAP-005/012/013/042 propagate waveform and reference errors into processing outcomes. CAP-014–020/022 specify receive/transmit interfaces, sampling and pulse/chirp/reset state. CAP-023–028 cover calibration and environmental/processing realization. CAP-029–031 specify delayed-return, dynamic and environmental evidence; CAP-033/034 preserve this coverage after manufacture/repair.
- **Contrast / failure:** A short loopback may not expose delayed-reference noise behavior; nominal synchronization can omit pulse/chirp phase state. A bistatic contrast removes the shared-source assumption.
- **Coverage finding:** Transmit-receive relationship, delay and motion must remain explicit in CAP-036; generic oscillator quality alone is inadequate.
- **Required calculation:** Calculate delay-dependent reference-noise transfer and the resulting leakage/clutter pedestal at a weak target location in range/Doppler; propagate waveform/observation weighting and include physical noise generation (CAP-005/036/042/044). Intersect gain/headroom constraints with limiter/amplifier/converter recovery and the required usable receive interval (CAP-014/018/043).
- **Architecture / rejection decision and assessment:** Compare shared/separate references, single/multiple conversion and isolation/filter/gain placements; use CAP-045 for independent transmit/receive clocks. Reject a zero-delay-loopback conclusion that does not cover target delay, or a low-noise chain still recovering during the required return. Evaluate target retention after cancellation rather than leakage suppression alone.
- **Remaining boundary:** Waveform families, clutter/detection depth and multistatic/SAR processing; U-02/U-04 and radar review.

### P-ARR — Maintain a receiving beam over bandwidth and scan

- **Need / observable:** Achieve a declared beam/pattern outcome while steering over a band and environment. Geometry, scan range, bandwidth, polarization and permitted pattern degradation must be specified.
- **Walkthrough:** CAP-001/010/037 translate pattern goals to array response; CAP-008/013/022 allocate errors. CAP-011/016/018/020 compare analog, digital and hybrid combination and phase versus delay correction. CAP-023/024 determine what remains observable before and after combination. CAP-026/027 address coupling and gradients; CAP-030/031 separate electronic and over-the-air evidence; CAP-033/034 handle element replacement and recalibration.
- **Contrast / failure:** Single-tone boresight matching can leave unacceptable response at band edges or other scan angles. Correction after analog combination may lack access to individual channel errors.
- **Coverage finding:** The array outcome cannot be inferred from identical channel specifications alone. CAP-010/023/037 explicitly retain geometry, coupling and correction-access reasoning.
- **Required calculation:** Construct the vector manifold and noise covariance from field, loading, coupling and receiver paths (CAP-010/044), then calculate weighted signal/noise sensitivity and a beam/null outcome under calibration error (CAP-008/022/037/042). Include bandwidth/scan/polarization dependence and compare feasible error allocations (CAP-043).
- **Architecture / rejection decision and assessment:** Compare analog phase steering, true-delay and digital/hybrid combination against band/scan, loss, quantization/settling, correction access and power constraints. Reject independent-noise or scalar-matching assumptions without a physical basis. Test contaminated training/reference leakage for desired-signal suppression, and evaluate electronic versus over-the-air residual evidence.
- **Remaining boundary:** Radiator/electromagnetic detail and polarimetric depth; U-05 and array review.

### P-DF — Estimate bearing with a multichannel receiver in uncertain propagation

- **Need / observable:** Produce bearing estimates with stated bias/uncertainty and ambiguity behavior. Source count, SNR, geometry, polarization and propagation assumptions are required inputs.
- **Walkthrough:** CAP-001/006/008/010/038 establish the inference and observability conditions. CAP-013/016–022 translate them to channel/reference requirements. CAP-023/024 assess injection versus manifold calibration; CAP-027/028 preserve geometry/configuration. CAP-030–032 require known-source/geometry and competing-hypothesis tests; CAP-033/034 carry manifold/configuration validity through production and service.
- **Contrast / failure:** A stable electronic phase difference can still correspond to several bearings, and receiver-only correction cannot establish the propagation manifold. A nominal single-source case does not cover multiple emitters or multipath.
- **Coverage finding:** DF must retain an independent inference entry, rather than being absorbed into array beamforming. CAP-006/010/038 cover the gap.
- **Required calculation:** Evaluate geometry/manifold rank, ambiguity and bearing sensitivity under source count, coherent multipath and uncertain polarization/receiver response (CAP-006/008/010/038). Distinguish a local covariance/information bound from globally identifiable direction; quantify sensitivity to a supplied manifold error and finite snapshots.
- **Architecture / rejection decision and assessment:** Compare baseline/geometry choices, comparison versus covariance estimators, and electronic versus over-the-air calibration. Identify conditions where more electronic phase precision does not resolve ambiguity or confounded propagation; require added observations, changed geometry or an explicitly restricted operating region (CAP-023/043). Evaluate a bounded estimator without forcing an unsupported unique answer.
- **Remaining boundary:** Estimator families and propagation/field-test depth; U-04/U-05 and DF review.

### P-INT — Correlate signals from separated receiving apertures

- **Need / observable:** Recover an interpretable complex cross-correlation over specified baselines, bands and integration times. Source statistics, geometry and timing/reference knowledge must be supplied.
- **Walkthrough:** CAP-002–006/008/010/039/042 define visibility/correlation, integration and geometric versus instrumental delay. CAP-011/016–022 establish sample identity, alignment and correlator interfaces. CAP-023–025 distinguish instrument and observing-condition calibration. CAP-027/028 preserve geometry/state metadata; CAP-030/031 require known-reference or source comparisons; CAP-033/034 preserve per-station calibration and reference health.
- **Contrast / failure:** Splitting a laboratory source into two ports does not establish separated-aperture performance with changing geometry, propagation and independent clocks.
- **Coverage finding:** Correlation receivers and baseline/reference freedoms require an explicit home; CAP-004/010/023/039 supply it. NRAO calibration practice [S4] supports keeping instrumental and observing-condition effects distinct.
- **Required calculation:** Derive finite-integration complex-correlation bias/variance including stochastic source power, receiver/coupled noise, filtering and effective independent samples (CAP-004/005/039/044). Calculate residual geometric/instrumental delay and clock-rate/epoch uncertainty, including asymmetry/holdover where remote clocks are used (CAP-045).
- **Architecture / rejection decision and assessment:** Compare common-reference transfer with independent clocks plus recorded data/alignment, checking required channelization/resampling and metadata. Reject zero expected independent-noise correlation as a zero-uncertainty claim. Evaluate a bounded stochastic correlation example, not only a split tone, and state reference freedoms/information retained after calibration.
- **Remaining boundary:** Distributed timing and specialist imaging/propagation depth; U-02/U-03 and interferometry review.

### P-SEN — Infer displacement or another physical change from phase

- **Need / observable:** Report a physical quantity with stated accuracy, unambiguous range and update behavior. Transduction law, reference-path behavior, motion and environmental sensitivities are missing inputs.
- **Walkthrough:** CAP-001/002/006/010/040 establish the physical measurement equation and ambiguities. CAP-007/013–020 choose tracking and receiver allocations. CAP-023–027 distinguish receiver calibration from sensor/reference-path correction. CAP-029/030 require comparison with an independent physical reference; CAP-031–034 address acceptance, diagnostic signatures, production variation and field drift.
- **Contrast / failure:** Small residual electronic phase does not establish physical accuracy when reference-path temperature changes. A small-motion demonstration does not establish phase-unwrapping reliability over larger motion or fades.
- **Coverage finding:** Physical transduction and nuisance sensitivity must precede conversion of a phase number to a measurand; CAP-010/040 retain that reasoning.
- **Required calculation:** Evaluate a physical measurement equation with desired motion/transduction and reference-path disturbances that can mimic it; determine what additional observation makes them distinguishable (CAP-006/010/023/040/043). Derive desired-signal transfer through tracking/compensation and quantify ambiguity recovery through fades and phase wraps (CAP-007/025).
- **Architecture / rejection decision and assessment:** Compare reference-path design, tracking bandwidth and modulation/diversity, or accept restricted valid intervals where recovery is unobservable. Reject a compensation that quiets residual phase by removing the physical signal. Execute or interpret a bounded independent-reference comparison, including uncertainty and the retained signal, not only repeatability.
- **Remaining boundary:** Selected sensor families and validation references; U-04/U-06 and sensing review.

### P-MET — Measure transfer phase or relative phase stability at defined ports

- **Need / observable:** Report a transfer/relative quantity at declared planes and conditions with a credible uncertainty statement. Accuracy versus stability purpose, band, record/averaging, signal level and calibration access need specification.
- **Walkthrough:** CAP-002/003/005/009/041 define the reported quantity. CAP-012–024 establish reference topology, converter/processing state and correction. CAP-026/027 control fixture and environmental effects; CAP-030 creates the measurement equation/uncertainty budget. CAP-031/032 assess limits and alternative explanations; CAP-033/034 extend calibration traceability and configuration control through manufacture/service.
- **Contrast / failure:** A repeatable trace may retain a systematic cable error. A shared test reference may suppress a noise contribution relevant with independent operational references. Digital alignment does not establish the entire RF phase path [S3].
- **Coverage finding:** Instrument/reference topology must be analyzed as part of the measurement process, with residual uncertainty rather than an unqualified “calibrated” label. CAP-023/030/041 own these distinctions.
- **Required calculation:** Define an operational DUT/reference measurement, including method-dependent filter/estimator and reference planes (CAP-002/030/041). Calculate correction residual and uncertainty with level-dependent receiver response, fixtures and correlated references, and assess whether the measurement can discriminate the required effect (CAP-014/023/024/044).
- **Architecture / rejection decision and assessment:** Compare simultaneous-ratio and switched/reference measurements with their drift, settling and headroom constraints. Change signal level, reference/fixture configuration and observation method to discriminate DUT behavior from receiver artifacts. Reject a lower apparent residual caused by common-reference cancellation or changed measurand; evaluate interpreted calibrated data and uncertainty.
- **Remaining boundary:** Specific instrument class, uncertainty decision rule and accepted conventions; U-01/U-07/U-08 and metrology review.

### 6.1 Cross-case stress checks and resulting coverage decisions

| Stress case | Cases affected | Required capability / draft disposition |
|---|---|---|
| Shared reference but unequal paths or different reset states | P-RAD/ARR/DF/INT/MET | CAP-005/016/017/022/045; derive transfer and assess timing/phase separately |
| Bandwidth expands after single-frequency calibration | P-ARR/DF/MET/RAD | CAP-012/020/022/024; require frequency-dependent matching and validity limits |
| Calibration bypasses antenna, fixture or sensing path | P-ARR/DF/INT/SEN/MET | CAP-010/023/030; require explicit unobserved path list |
| Weak desired signal with strong blocker or leakage | P-COM/RAD/SEN/MET | CAP-014/018/019/043/044; calculate generated noise, feasible headroom and recovery |
| Integration uses a mismatched reference or unjustified noise assumptions | P-COM/RAD/INT/SEN | CAP-006/042; make detection/integration reasoning explicit instead of hiding it within generic DSP |
| Firmware change, dropped sample or partial reset | All digital cases | CAP-017/020/021/028/034; configuration and sample validity are engineering outputs |
| Long record, drift or poorly justified averaging | P-INT/SEN/MET and long observations elsewhere | CAP-004/005/025/030; retain observation/filter/statistical assumptions |
| Calibration fits its own data but fails elsewhere | All calibrated cases | CAP-023/024/031; distinguish identifiability, fitting and independent residual evidence |
| Prototype succeeds but production fixtures conceal variation | All manufactured cases | CAP-024/030/033/034; evaluate joint yield, adjustment range, fixture capability and test effort |
| Calibrated response has a deep null or unattainable inverse | P-ARR/DF/MET/COM | CAP-020/022/024; calculate noise enhancement, residual, causality and finite resources |
| Cancellation or compensation removes the measurand | P-COM/ARR/INT/SEN/MET | CAP-007/023–025/042; evaluate desired-signal transfer and surrendered information |
| Apparent coherent average ignores coupled noise or source statistics | P-ARR/INT/DF | CAP-004/005/010/044; construct covariance physically and evaluate finite-record uncertainty |

The walkthroughs found obligations that a simple RF-plus-DSP subject list would miss: acquisition versus tracking, end-to-end state, correction access, external-path observability, physical inference ambiguity, test-reference correlation and production validity. These have explicit calculation/decision homes in this revision. Routing, required methods and rejection conditions were checked on paper; no audit is a completed calculation, successful design or demonstration of technical completeness.

## 7. Draft assessment and acceptance criteria

### 7.1 Checks performed in constructing the draft

- **Breadth:** Compared the capability groups with every charter domain and all seven named application rows (§5.1/§6). Each has identified outcomes and lifecycle references. Additional application boundaries are visible in §3.2.
- **Capability quality:** Entries require evaluated results under supplied conditions: derivations, calculated feasible regions/budget closure, bounded implementations, interpreted measurements and joint yield/test-effort assessments. Foundation assessments remain mathematical/physical reasoning rather than artificial hardware deliverables. Assessment obligations were inspected manually; none is claimed executed by a reader now.
- **Dependencies:** Core learning, implementation-conditional extensions and engineering interactions are separated in every capability and §5.2. Analog/single-channel metrology and analog array paths were checked for unnecessary conversion/DDC requirements; digital paths add those methods explicitly. No exhaustive graph has been constructed.
- **Redundancy:** Shared versus application ownership and potentially overlapping responsibilities are separated in §5.3. These boundaries need editorial review as development proceeds.
- **Consistency:** Application-specific acceptance is retained; shared clock, digital alignment, mathematical checks, physical validation and compliance are not conflated. Canonical mathematical conventions remain unresolved.
- **Usefulness:** The qualitative walkthroughs identify decision paths and failure probes, but do not demonstrate that a reader can yet perform them. That requires later developed treatments and reader/engineering review.
- **Evidence:** Only the selected passages in §9 were examined. The rest is proposed coverage and engineering judgement pending specialist examination; absence of a citation is not evidence that a topic is unimportant or established.

These are authorial/manual draft checks, not independent technical review. A repository integrity check can establish expected files exist; it cannot establish any of these scientific conclusions.

### 7.2 Provisional acceptance and continuing technical review

The project owner has accepted this inventory provisionally as a planning and coverage input for architecture development, as recorded in [ADR-0002](decisions/ADR-0002-provisional-competence-baseline.md). The competence-inventory task is closed for that stated use. Independent assessment of technical adequacy remains pending; unresolved scope questions, source gaps and applicability limitations are preserved.

The following technical review criteria remain applicable as the baseline is used and revised; project-owner planning acceptance does not establish that each has been independently demonstrated:

1. The baseline is plausible for experienced RF engineers and the bridges remove hidden specialist prerequisites.
2. Each named application has appropriate observables and distinctive engineering methods; any deferred depth has acceptable consequences for the charter's primary-reference goal.
3. Full/selective/external choices retain essential coherent-receiver reasoning internally.
4. Capability granularity supports teaching and practical lookup without duplication or disconnected topic lists.
5. Dependencies are sufficient for both systematic study and end-to-end engineering; representative cases do not leave unexplained decisions.
6. Technical conflicts, unsupported distinctions and critical source gaps are corrected or explicitly block the relevant use.
7. Unresolved boundaries have decisions or clearly bounded provisional treatment; no critical omission is hidden behind a broad label.
8. CAP-043/044/045 and the strengthened nonlinear, correction-limit, signal-preservation, vector-model and production outcomes are technically adequate, not merely represented by headings. No core method may be dropped as an optional specialist extension.

**Accepted use and limits:** Use this baseline to plan technical coverage and knowledge dependencies in the next intellectual-architecture stage. The consolidated review dispositions in §7.3 and unresolved questions in §8 remain in force. This acceptance is not independent validation of future derivations, physical models, engineering methods or application-specific performance conclusions, nor evidence of system compliance. Unresolved physical/information contradictions or omission of an essential internal method must still be surfaced and may require revision of the baseline. The next stage is identified but not started; implementation requires a separate instruction under [current work](current-work.md).

Acceptance of consequential technical results remains a human engineering decision for a stated use and revision, backed by appropriate evidence under the existing standard. The project-owner decision recorded here is limited to planning use; the AI-assisted reviews do not constitute independent validation. Counts of capabilities, citations, chapters or files are not acceptance criteria.

### 7.3 Consolidation and disposition of both AI-assisted reviews

The two reports are the sections “Review 1” and “Review 2” in [the supplied review file](../reviews/20261018_review_of_competence-inventory.md). R1.n and R2.n below refer to their numbered findings; the filename is retained without inferring a review date. Severity labels were not adopted as technical evidence. Classification separates a missing responsibility from an insufficient outcome, dependency error, optional scope and already adequate content. Changes specify future reader competence, not completed textbook results or independent validation.

| Findings | Technical assessment / disposition | Canonical correction or justified boundary |
|---|---|---|
| R1.1; R2.1 | Genuine distinct responsibility: quantitative rejection/qualification of requirements | Added CAP-043; CAP-001/011/013 use its results. R2's no-new-entry option is not adopted: feasible regions are an independently assessable output, while CAP-011 retains architecture/technology selection. |
| R1.2; R2.2 | Genuine distinct responsibility for physical disturbance generation, not just budget assembly | Added CAP-044; strengthened CAP-013/015/018. Adopt R2's separate home to keep physical source/path construction out of overloaded CAP-014; no separate capability for every mechanism. |
| R2.3; nonlinear portion of R1.2 | Insufficiently explicit existing outcome | CAP-014 owns nonlinear model adequacy, memory, gain/headroom, transitions and recovery; CAP-018 owns converter/quantization limits and CAP-017/028 valid states. Exhaustive nonlinear-device theory is not required. |
| R2.4 | Missing physical construction/sensitivity outcomes within shared foundations and applications | CAP-044 supplies loaded/coupled network noise; CAP-004/005 finite-record statistics; CAP-037/039 evaluated array/correlation sensitivity. No additional matrix/noise capability is needed. |
| R1.3; R2.5 | Insufficiently binding mathematical/application bridge | CAP-004/005 require complex phase/increment/observation relationships and approximation limits; CAP-013/042 and applications use them. No universal coherence metric or unconditional PSD-to-performance conversion is accepted. |
| R1.4; R2.6 | Insufficient correction-feasibility outcome; identifiability itself already present | CAP-020/022/024 calculate noise gain, causal/stable/finite-resource residuals and information loss; CAP-023 retains observability. Do not claim every notch is uncorrectable: distinguish attenuation/noise penalty from genuine information loss and allowed approximation. |
| R1.5; R2.7 | Genuine distinct distributed inference responsibility | Added CAP-045, retaining CAP-016 hardware distribution and CAP-017 transition control. R2's incorporation-only option is not adopted: offset/delay inference and holdover need their own evaluated output. Specific transfer protocols/hardware remain external. |
| R1.6; R2.8 | Insufficient component/interface assessment specificity | CAP-011/014–018/021/026/027 require quantitative technology/interface checks and identify missing manufacturer evidence. Do not import arbitrary present-day parts, detailed circuit recipes or unconditional typical-data guarantees. |
| R1.7; R2.12 | Insufficient discriminating application audit | §6 adds actual required calculations, architecture alternatives, wrong-choice rejection and assessment for all seven classes; CAP-035–041 strengthened. Categories are adequate; no eighth category or solved design is required. |
| R1.8; R2.9 | Existing responsibilities lack explicit retained-signal requirement; R2 additionally identifies interference rejection | CAP-007/023–025/042 and applications require desired-signal transfer, training/reference contamination, separation limits and surrendered information. General rejection is developed inside CAP-042; exhaustive adaptive/EW algorithms remain optional. |
| R2.10 | Insufficiently fixed minimum scope, not a mandate for a full antenna/polarimetry textbook | CAP-010/022/023/037–039 commit to vector field/manifold/loading/leakage and scalar-model limits. U-05 now concerns specialist depth beyond that minimum. |
| R1.9; prerequisite portion of R2.11 | Incorrect universal learning dependencies | §4/§5.2 separate Learning, Conditional and Interactions; CAP-019/022–024/026/030/035–041 no longer force ADC/DDC/multichannel paths onto every receiver. Engineering iteration is retained, not forced into an acyclic workflow. |
| R1.10; assessment portion of R2.11 | Insufficiently assessable outcomes, not missing lifecycle disciplines | CAP-009/013/017/021/024/026–034 and the global dimension definitions require executed/evaluated work; CAP-029 includes actual model construction. Verification includes finite exposure/confidence, not arbitrary counts. |
| R2.13 | Quantitative refinement of an already present production responsibility | CAP-024/030/033 require joint yield, coefficient range/resolution, calibration/test time, fixture uncertainty and sensitivity to unsupported distribution assumptions; CAP-034 retains service validity. No extra production governance capability. |
| R1.11 | Incorrect categorical measurand restriction | CAP-002/005/030/041 distinguish intentional method dependence from instrument imperfections; [S2] extended only for the newly examined D.4.1 passage. |
| Both source audits and scope assessments | Existing narrow attributions/evidence distinctions adequate; broad expansion not justified | Preserve S1–S4 limits. Newly examined sources support only identified additions (§9). General RF remediation, every estimator/protocol, full-wave design, complete imaging and optical/quantum scope remain external/deferred; essential coherent reasoning does not. |

The reviews' illustrative numbers, equations and source links were not promoted automatically to accepted engineering results. This revision commits to deriving the necessary relationships under stated assumptions; it does not reproduce the review examples as product specifications. Remaining choices in §8 restrict implementation/detail, not the newly committed core outcomes.

## 8. Uncertainties, review decisions and exclusions

| Issue | Type / affected capabilities | Provisional treatment and consequence | Human review needed |
|---|---|---|---|
| U-01: Application success metrics and product requirements | Scope / CAP-001/002/031/035–041 | Use qualitative briefs; do not invent limits, distributions, waveforms or decision rules. Detailed allocations remain impossible until supplied | Systems and application engineers: confirm representative outcomes and required case envelopes |
| U-02: Distributed implementation depth | Scope/technical / CAP-007/016/017/025/036/039/045 | Core offset/rate/delay/phase inference, asymmetry, holdover and sample-epoch reasoning committed in CAP-045; particular transfer technologies/protocols external | Time/frequency and application reviewers: verify this minimum is sufficient; choose representative transfer implementations later |
| U-03: Interferometry versus complete imaging/astronomy treatment | Scope / CAP-010/039 | Receiver correlation, delay/reference and calibration foundations included; comprehensive imaging/observing treatment uncommitted | Interferometry specialist: assess the minimum bridge needed for engineering use |
| U-04: Breadth of application processing and propagation | Scope / CAP-010/035–040 | Develop processing consequences needed for receiver decisions; avoid comprehensive coding, detection, imaging or geophysical texts | Application engineers: identify methods whose omission would force reconstruction elsewhere |
| U-05: Specialist antenna/polarimetric depth | Scope/technical / CAP-010/022/023/037–039/044 | Minimum vector field/manifold, loading/coupling, cross-polar leakage and noise models committed; detailed radiators/full-wave design and comprehensive polarimetric science external | Antenna/array/DF/interferometry reviewers: verify minimum model and scalar-limit criteria; decide specialist extensions |
| U-06: Non-RF coherent systems and sensor physics | Scope / CAP-040 and §3.2 | RF-centered core; list transferable contrasts without claiming optical/quantum/non-RF completeness | Project owner and sensing specialist: decide whether extensions are necessary |
| U-07: Device, implementation, regulatory and production detail | Evidence/scope / CAP-011–021/026–028/031/033/034/041 | Teach selection/evidence methods; use externally verified current facts later. No installed part, platform or qualification standard chosen | Hardware, implementation and production reviewers: validate sufficiency and handoff boundaries |
| U-08: Mathematical conventions | Technical decision / CAP-002/003/005/012/020 | Existing standards list unresolved envelope, PSD, phase-noise and cross-spectrum conventions. No universal normalization is silently selected | Mathematical/technical editor and engineer before substantive derivations |
| U-09: Mathematical depth and source coverage | Reader/evidence / CAP-004–009/013/029/030/042–045 | Require internal coherent reasoning with targeted supporting bridges; most methods still await passage-level research and derivation | Statistical signal processing/time-frequency/metrology reviewers: assess rigor, prerequisites and applicability |
| U-10: Calibration observability, feasible correction and retained signal | Technical/evidence / CAP-006/019/020/022–025/032/042 | Measurement equations, reference freedoms, correction resources/noise gain, unobserved paths and retained-signal checks are required; no universal algorithm asserted | Calibration and application specialists: challenge identifiability, realizability, signal retention and operational validity |

### Review priorities

First review the observable/application survey, reader baseline and full-versus-selective boundaries: errors there would distort the later architecture. Then review correlated-error reasoning, acquisition/state promises, calibration observability and measurement sufficiency. Finally check physical implementation, integration, manufacturing and service obligations for practical omissions. These are review responsibilities, not a requirement to create a reviewer organization or extra governance files.

Questions for human engineering review include whether the application contrasts are sufficiently representative; whether the mathematical bridges are adequate without becoming general textbooks; whether the committed distributed/reference and vector/noise models are sufficient; and whether implementation/production outcomes are concrete enough for real practice. Reviewers should add a counterexample or missing engineering decision when challenging a boundary.

### Explicit exclusions and subsequent use

This task does not produce manuscript chapters, a final table of contents, solved reference designs, numerical component requirements, computational models, new tooling/infrastructure, formal knowledge graphs, publishing results or final technical acceptance. It does not modify the charter or promote provisional scope/architecture documents to accepted specifications. General RF remediation, exhaustive application algorithms and current component/standard details are external only to the extent justified above.

The project-owner decision permits this provisional baseline to serve as the planning and coverage input when the next architecture stage is separately started. Carry unresolved issues and coverage qualifications forward. Do not turn headings directly into chapters or automatically advance to the pilot or architecture phase; the next stage remains not started in [current work](current-work.md).

## 9. Sources and evidence boundary

The linked [source examination note](../references/source-notes/competence-inventory-foundations.md) records original and newly examined passages, supported distinctions, limitations and bibliographic qualifications. Revision-source examinations are dated 2026-10-28; previous examination claims are not expanded without fresh access. Canonical entries are in `references/references.bib`. These sources support selected boundaries, not the completeness of the inventory or every capability method.

- **[S1]** W. J. Riley, *Handbook of Frequency Stability Analysis*, NIST SP 1065, July 2008, §§3.3 and 5.2.1–5.2.2, printed pp. 6, 13–15. Supports distinguishing stability measures and the noise-dependent limitations of ordinary variance. [NIST full text](https://tsapps.nist.gov/publication/get_pdf.cfm?pub_id=50505).
- **[S2]** NIST TN 1297, 1994 edition, online §5.1–5.2, Appendix A.1–A.3 and newly examined Appendix D.4.1. Supports measurement-process modeling, covariance, first-order propagation limits and explicit method-defined measurands. [Section 5](https://www.nist.gov/pml/nist-technical-note-1297/nist-tn-1297-5-combined-standard-uncertainty), [Appendix A](https://www.nist.gov/pml/nist-technical-note-1297/nist-tn-1297-appendix-law-propagation-uncertainty), [Appendix D.4](https://www.nist.gov/pml/nist-technical-note-1297/nist-tn-1297-appendix-d4-measurand-defined-measurement-method).
- **[S3]** Ian Beavers, “Demystifying Deterministic Latency within JESD204B Converters,” Analog Devices, February 1, 2014, questions defining deterministic latency and distinguishing total converter latency and analog sample alignment. Supports the narrower digital-framing latency distinction; it is not examination of the JEDEC standard or a current part guarantee. [Article](https://www.analog.com/en/resources/technical-articles/demystifying-deterministic-latency-within-jesd204b-converters.html).
- **[S4]** NRAO VLA observing guide, “Calibration,” subsection “Calibration Basics,” live web page, revision/date not stated in examined passage. Supports separating instrument, observing-condition and result calibration, with differing timescales. [NRAO page](https://science.nrao.edu/facilities/vla/docs/manuals/obsguide/calibration).

- **[S5]** NIST, *Two Way Time Transfer*, live page; opening reciprocity and equipment/propagation-delay discussion. Supports symmetry/asymmetry limitations; date/revision not established. [NIST page](https://tf.nist.gov/time/twoway.htm).
- **[S6]** Analog Devices, *Wideband LO Noise in Passive Transmit-Receive Mixer ICs*, September 23, 2005; introduction and Mixer Noise Model prose. Supports blocker-generated noise and internal LO-buffer contributions; equations/current parts not verified. [Article](https://www.analog.com/en/resources/technical-articles/wideband-lo-noise-in-passive-transmitreceive-mixer-ics.html).
- **[S7]** Walt Kester, *MT-007*, Revision A, October 2008, printed pp. 3–4. Supports slope-dependent jitter errors and the conditions of the sine-input approximation, not a universal broadband allocation. [Tutorial](https://www.analog.com/media/en/training-seminars/tutorials/MT-007.pdf).
- **[S8]** Rogers, Pratap, Kratzenberg and Diaz, *Calibration of active antenna arrays using a sky brightness model*, Radio Science 39(2), 2004, §6 prose. Supports coupled receiver-noise paths; equation images and numerical results not checked. [Paper](https://agupubs.onlinelibrary.wiley.com/doi/full/10.1029/2003RS003016).
- **[S9]** Analog Devices / Analog Dialogue, *ADC Input Noise*, dither/SFDR discussion, live page with date/revision not established. Supports input-correlated quantization and conditional dither limits; no device-performance result adopted. [Article](https://www.analog.com/en/resources/analog-dialogue/articles/adc-input-noise.html).

Further source examination is needed for application-specific metrics, estimator/loop applicability, array/DF/interferometric models, nonlinear impairments, physical implementation and production methods. The two AI-assisted critiques were consolidated; no human technical review, physical measurement or model validation is claimed by this revision.
