# Provisional Annotated Table of Contents

**Status:** provisionally accepted by the project owner on 2026-10-29 for guiding textbook development under [ADR-0004](decisions/ADR-0004-provisional-book-architecture-acceptance.md), following external AI-assisted review and subject to its four review qualifications. The five-part, 32-chapter, four-section organization remains flexible. No chapter content, derivation or example has been authored or validated. [Book architecture](book-architecture.md) owns the editorial recommendation; [coverage](book-coverage.md) owns location audits. Accepted treatment specifications remain in [technical coverage](technical-coverage.md).

## How to read the annotations

Chapter cards name objectives, prerequisite boundaries and canonical ownership. Numbered sections specify development obligations, not achieved results. “Develop,” “derive,” “calculate” and “execute” refer to eventual textbook work. All chapters require physical interpretation, assumptions, limiting cases and human-readable calculation inputs/outputs. Check/evidence annotations distinguish mathematical/software checks from empirical validation and compliance. Essential results need later claim-level sources or explicit derivation provenance; no source passage was newly examined for this outline.

Chapter 1 gives early application motivation; all subsequent chapters revisit engineering questions. Full applications in Part V do not impose their complete prerequisites on previews. Introduction, canonical development and application locations are distinguished in the coverage mapping. Supplied technology/application interfaces must be labeled and reconciled at the named revisits. Chapter entry lists name major dependencies; transitive prerequisites and conditional extensions remain governed by accepted coverage §3.


## Part I — Observables and reasoning

### Chapter 1 — Comparisons, observables and coherent signals

**Objective:** Define what is compared and reconstruct representations without hidden phase or power conventions.

**Entry:** Declared RF baseline only.

**Canonical ownership:** K01; introductory K11. Shared results used here retain their original homes.

#### 1.1 Seven engineering questions

Motivate burst acquisition, delayed radar return, beam formation, bearing, baseline correlation, physical sensing and port measurement. Introduce D-COM/ARR/RAD/MET without their complete quantitative prerequisites; identify unavailable inputs.

#### 1.2 Operational observables

Define phase, frequency, time, delay and correlation with planes, bandwidth, observation interval, state and calibration dependence. Distinguish accuracy, stability, alignment and restart repeatability; phase at an amplitude null needs special treatment.

#### 1.3 Physical and complex representations

Develop real, analytic and envelope conversions, reconstruction, power scaling, modulation and conjugation. Reserve unresolved canonical conventions for review; explicit local assumptions cannot silently become project defaults.

#### 1.4 Requirements before numbers

Frame needs, operating states, evidence and missing limits. Compare coherent and noncoherent choices qualitatively; preview later feasibility rather than assume it.

**Examples, engineering work and verification:** Compare two intentionally different measurands and reconstruct a signal through inversion. Show what each test could establish; no common clock is assumed to guarantee phase.

### Chapter 2 — Random signals and complex phase

**Objective:** Construct justified scalar stochastic models rather than equate noise with one RMS number.

**Entry:** Chapter 1; probability is developed here.

**Canonical ownership:** K02. Shared results used here retain their original homes.

#### 2.1 Probability and expectation bridge

Develop distributions, conditional reasoning, moments and scalar covariance from engineering observations; distinguish ensemble assumptions from observed records.

#### 2.2 Processes and finite records

Develop stationarity, ergodicity and temporal dependence; separate stochastic signals, drift and deterministic spurs. A finite record cannot establish every ensemble assumption.

#### 2.3 Complex and circular quantities

Develop proper/improper complex models, phase wrapping and increments. Distinguish circular from unwrapped statistics and multiplicative phase from additive noise.

#### 2.4 Noise-to-phase approximation

Derive the local additive-noise phase relation and identify low-SNR/fade breakdown. Contrast equal marginal variance with different temporal structure; physical source construction follows in Chapter 9.

**Examples, engineering work and verification:** D-MET and P-INT model contrasts require justified Gaussian/independence assumptions. Check limits and preserve uncertainty about unobserved process behavior.

### Chapter 3 — Observation, spectra and coherence

**Objective:** Relate time and spectral descriptions to the actual observation and finite-record uncertainty.

**Entry:** Chapters 1–2; matrix refinement adds Chapter 4.

**Canonical ownership:** K03. Shared results used here retain their original homes.

#### 3.1 Spectral and time relationships

Develop auto/cross spectra and phase/frequency/time relations with sidedness, units and ordering. State when stationarity or distributional interpretations are needed.

#### 3.2 Observation operators

Derive window/filter/averaging weighting and phase-increment/complex-coherence relationships. Mark exact versus Gaussian or small-angle specializations.

#### 3.3 Finite-record statistics

Develop estimator bias/variance, fourth-moment assumptions, effective independent samples, convergence and appropriate stability measures; averaging indefinitely need not improve a result.

#### 3.4 Shared sources through unequal paths

Derive differential transfer, including pure delay, and later refine to matrix spectra. Keep general transfer here; radar and interferometry own their performance mappings.

**Examples, engineering work and verification:** X-OBS compares time/spectral calculations under changed records and filters. D-RAD contrasts delayed and zero-delay observations; neither is hardware validation.

### Chapter 4 — Vectors, covariance and conditioned solutions

**Objective:** Form coupled models, identify null directions and quantify sensitivity before inversion.

**Entry:** Chapters 1–2; no assumed specialist linear algebra.

**Canonical ownership:** K04. Shared results used here retain their original homes.

#### 4.1 Complex vectors and bases

Build matrix operations, conjugate transpose, channel ordering and units from scalar models; explain physically meaningful coordinate changes.

#### 4.2 Covariance and quadratic forms

Develop covariance matrices, weighted power and Hermitian positive-semidefinite conditions. Physical correlations will be constructed in Chapter 9.

#### 4.3 Rank and conditioned inference

Develop least squares, eigenstructure and singular values; distinguish exact null spaces, near degeneracy and numerical precision.

#### 4.4 Constraints and regularization

Show how reference constraints or regularization change the solution and what physical information justifies them. Return to matrix spectra and later coupled inference explicitly.

**Examples, engineering work and verification:** P-DF and D-ARR use a rank/conditioning calculation and covariance sanity checks. An invertible matrix alone establishes neither observability nor reliable correction.

### Chapter 5 — Inference, information and ambiguity

**Objective:** Derive representative estimators and applicable bounds while exposing indistinguishable alternatives.

**Entry:** Chapters 1–2 for scalar entry; Chapter 4 for joint parameters.

**Canonical ownership:** K05. Shared results used here retain their original homes.

#### 5.1 Scalar likelihood and least squares

Develop phase, frequency, delay and amplitude examples with explicit signal/noise models, nuisance parameters and observation support.

#### 5.2 Bias, precision and information

Derive representative performance and information bounds, stating regularity conditions; distinguish an attainable method from a lower bound.

#### 5.3 Global ambiguity and thresholds

Exhibit indistinguishable parameter sets and reference freedoms. Explain low-SNR threshold, wrapping and mismatch failures beyond local linear precision.

#### 5.4 Coupled inference and observation choice

Extend with Chapter 4 to joint parameters, conditioning and pilot/reference choices. Calibration-specific freedoms are developed in Chapter 13.

**Examples, engineering work and verification:** D-COM contrasts local precision with finite-burst acquisition; P-DF contrasts bearing precision with uniqueness. Require a mismatched-model countercase.

### Chapter 6 — Adequate calculations, models and uncertainty

**Objective:** Choose and assess the simplest adequate model for an engineering decision.

**Entry:** Chapters 1–2; Chapter 4 for coupled sensitivity.

**Canonical ownership:** K07. Shared results used here retain their original homes.

#### 6.1 Approximation and physical scale

Develop units, nondimensionalization, perturbation and limiting cases; state when neglected physics matters.

#### 6.2 Sensitivity and uncertainty

Derive covariance-aware propagation and distinguish parameter uncertainty, variability and numerical tolerance. Include a nonlinear/ambiguous case beyond first-order propagation.

#### 6.3 Numerical adequacy

Develop precision, convergence and independent-formulation checks using supplied physical models; separate mathematical/software consistency from model discrepancy.

#### 6.4 Model hierarchy and decisions

Specify later bounded model construction/execution, interpretation and empirical comparison where available. Identify unsupported extrapolation rather than promote agreement with itself to validation.

**Examples, engineering work and verification:** D-RAD and X-PROD require sensitivity and a changed assumption. Later worked models must have human-readable inputs/results; executable code cannot own essential explanation.

### Chapter 7 — Acquisition, tracking and signal retention

**Objective:** Design bounded synchronization with separate acquisition, locked operation and recovery.

**Entry:** Chapters 3 and 5; control bridge internal. Digital/remote extensions conditional.

**Canonical ownership:** K06. Shared results used here retain their original homes.

#### 7.1 From inference to dynamics

Develop detector/loop equations, feedback and feedforward alternatives; bridge elementary control from RF LTI reasoning.

#### 7.2 Locked-state transfer

Derive stability, noise bandwidth, dynamic stress and desired-signal as well as nuisance transfer. Smaller residual error can mean lost measurand.

#### 7.3 Acquisition and nonlinear failure

Separate capture/search, ambiguity, saturation, slips and faded observations from linear tracking. Develop holdover and reacquisition reasoning.

#### 7.4 Latency and realization extensions

Analyze sampled latency when Chapter 17/19 interfaces are supplied; return after Chapter 16 for remote delayed feedback. These extensions do not delay ordinary-loop foundations.

**Examples, engineering work and verification:** D-COM needs bounded recovery and fade/slip evidence; P-SEN injects a wanted physical variation. Require noise/dynamics/latency tradeoffs and defensible risk limitations.

## Part II — Physical models and system decisions

### Chapter 8 — Fields, geometry and physical transduction

**Objective:** Construct the minimum physical input model and expose what receiver injection cannot establish.

**Entry:** Chapters 1 and 4 plus declared RF fields baseline; inference adds 5.

**Canonical ownership:** K08. Shared results used here retain their original homes.

#### 8.1 Propagation and geometry

Develop phase/delay/Doppler and reference geometry, distinguishing propagation from electronic delay; identify multipath and near/far-field assumptions.

#### 8.2 Vector field to receiver ports

Bridge field/polarization bases, effective response, manifold, phase centers and loading/coupling. Keep the minimum receiver model internal.

#### 8.3 Scalar reduction and its failure

Derive conditions for scalar channels and quantify a direction/frequency/polarization mismatch; include cross-polar leakage and unobserved paths.

#### 8.4 Physical sensing interfaces

Develop representative transduction/reference paths and externally required laws with uncertainty. Detailed radiator synthesis, full-wave design and specialist sensor physics remain bounded external inputs.

**Examples, engineering work and verification:** D-ARR compares electronic and field calibration; P-SEN separates measurand from nuisance. Specialist review must challenge scalar limits and interferometric geometry.

### Chapter 9 — Physical noise, blockers and timing disturbances

**Objective:** Construct physical spectra/covariance and derive constraints from the complete waveform.

**Entry:** Chapters 2–4 and RF noise/network baseline; incident fields add 8.

**Canonical ownership:** K09. Shared results used here retain their original homes.

#### 9.1 Sources, loading and delivered noise

Bridge available/delivered power, temperature, thermal and representative active-device noise to network transfer with explicit impedances and normalization.

#### 9.2 Coupled and external noise

Construct covariance from loaded/coupled receiver and field paths rather than assume independent LNAs. Separate supplied parameters from derived relationships.

#### 9.3 Reciprocal mixing

Derive blocker/effective-LO contributions through preselection, mixer branches and observation filtering. Compare narrow-blocker/flat-spectrum limits with finite-spectrum cases.

#### 9.4 Timing-error generation

Derive small timing-error disturbance from the entire analog waveform and clock process, retaining correlations. Identify breakdown of tone-only, stationary and small-error models.

**Examples, engineering work and verification:** X-BLK derives LO/clock/filter constraints; P-INT/D-ARR use physical covariance. Missing device evidence stays open; budget assembly belongs to Chapter 12.

### Chapter 10 — Extraction, integration and rejection

**Objective:** Derive a realizable extraction method and evaluate retained information.

**Entry:** Chapters 3–5; physical interference adds 8–9.

**Canonical ownership:** K10. Shared results used here retain their original homes.

#### 10.1 Hypotheses and correlation

Develop representative likelihood/sufficient-statistic and matched-filter reasoning with explicit hypotheses and normalization.

#### 10.2 Colored weighting and accumulation

Derive coherent/noncoherent integration and mismatch consequences using Chapter 3 observation statistics, not a universal phase-loss rule.

#### 10.3 Separation and contaminated references

Develop spatial/spectral/temporal or reference-assisted rejection, degrees of freedom, training support, conditioning and leakage.

#### 10.4 Realizable decision and failure

Specify bounded extraction/rejection, false-alarm/detection conditions and retained wanted response. Digital realization follows later; analog survival must already be satisfied.

**Examples, engineering work and verification:** D-COM and P-INT compare matched/mismatched extraction; X-INV tests indistinguishable subspaces. Apparent rejection alone is not improved task performance.

### Chapter 11 — Frequency, phase and delay through the receiver

**Objective:** Exercise an end-to-end frequency/reference plan across operating states.

**Entry:** Chapters 1 and 3; ideal sampling interface supplied initially.

**Canonical ownership:** K12. Shared results used here retain their original homes.

#### 11.1 Conversion and reference signs

Develop modulation, multiplication/division, conjugation and spectral inversion with explicit reference planes.

#### 11.2 Bands and unwanted responses

Construct desired/image/alias/spur maps and exclusions. Supply ideal sample placement until converter refinement in Chapter 17.

#### 11.3 Response over bandwidth

Derive phase offset, slope/group delay and dispersive transfer; preserve waveform rather than tone-only interpretation.

#### 11.4 State-sensitive plans

Identify divider/NCO/reset-sensitive elements and exercise tone/modulation transfer. Chapter 21 owns transition sequencing and evidence.

**Examples, engineering work and verification:** D-RAD/D-MET trace references across states; reject sign mistakes and assumed deterministic hardware behavior. Plan includes implementation interfaces, not only frequency arithmetic.

### Chapter 12 — Feasibility, architecture and correlated allocations

**Objective:** Reject incompatible goals, compare architectures and close conditional allocations.

**Entry:** Chapters 5–6, 9 and 11; spatial/detection constraints add 8/10.

**Canonical ownership:** K11 quantitative; K13. Shared results used here retain their original homes.

#### 12.1 Joint feasible regions

Intersect information/ambiguity, energy/bandwidth/time, dynamics, headroom, latency and resource constraints. Calculate both gain-range and task-information/steering conflicts.

#### 12.2 Architecture and interfaces

Compare analog/digital/hybrid and shared/independent-reference alternatives with quantitative loading, drive, noise, power, latency and calibration-access envelopes.

#### 12.3 Correlated budget construction

Propagate Chapter 9 physical sources and cross-spectra to observables; distinguish margins, variability, uncertainty, correction residual and measurement uncertainty.

#### 12.4 Closure and restoration

Vary correlation, blocker, environment or missing inputs; identify which requirement/architecture change restores feasibility. Reconcile supplied application mappings and technology envelopes in later design stages.

**Examples, engineering work and verification:** All anchors need a rejected alternative and a conditional/empty feasible region. Actual technology guarantees and application limits remain inputs, not assumed performance.

### Chapter 13 — Calibration observability and operational metrology

**Objective:** Distinguish identifiable parameters from measurement precision and construct a sensitive test.

**Entry:** Chapters 1, 3–6; external paths add 8, physical noise 9.

**Canonical ownership:** K21a; K22. Shared results used here retain their original homes.

#### 13.1 Calibration measurement freedoms

Write stimulus/reference/nuisance equations, rank and reference constraints. Exhibit indistinguishable parameters and omitted paths before choosing a correction.

#### 13.2 Operational measurement equations

Develop intentional method-defined observables versus instrument imperfections, loading, floors, fixtures, de-embedding and correlated references.

#### 13.3 Uncertainty and records

Apply Chapter 6 propagation to sensitivity, bias, finite records/effective degrees of freedom and traceability. Treat nonlinear/ambiguous uncertainty explicitly where needed.

#### 13.4 Independent configurations

Compare cable/level/reference topology and supplied measurements to distinguish DUT from instrument artifacts. Measurement reasoning precedes executable calibration in Chapter 23.

**Examples, engineering work and verification:** D-MET and P-INT need interpreted data/uncertainty and a test-sensitivity assessment. Chapter 24 owns compliance decision rules; a small fit residual proves neither correction nor accuracy.

## Part III — Signal and reference realization

### Chapter 14 — Analog information preservation and gain policy

**Objective:** Design stages and operating policy under the complete signal/blocker envelope.

**Entry:** Chapters 6, 9, 11–12; actual converter interface adds 17.

**Canonical ownership:** K14. Shared results used here retain their original homes.

#### 14.1 Gain, filtering and isolation

Calculate stage noise/headroom and drive/loading/bias/dissipation choices; compare filter placement and analog survival before digital rejection.

#### 14.2 Nonlinear model adequacy

Develop AM-to-AM/PM, crest factor, intermodulation and memoryless/dynamic/measured model choices; mark IP2/IP3 extrapolation limits.

#### 14.3 Transitions and recovery

Calculate gain-state complex response, overload/history, hysteresis and time to usable data. Specify a bounded executable gain/valid-data policy.

#### 14.4 Characterization and interfaces

Compare weak-plus-blocker, multitone/modulated and pulse cases. Reserve test access, reference controls and calibration metadata; reconcile driver/converter envelopes later.

**Examples, engineering work and verification:** D-RAD/X-BLK require recovery evidence, not just low NF. Manufacturer facts must identify conditions/guarantee scope; missing evidence is a design risk.

### Chapter 15 — Synthesis and endpoint reference distribution

**Objective:** Select synthesis and distribution using actual endpoint observables.

**Entry:** Chapters 3, 7, 11–12; remote inference is Chapter 16.

**Canonical ownership:** K15a/b. Shared results used here retain their original homes.

#### 15.1 Synthesis transfer

Derive PLL/reference/oscillator transfer, multiplication/division, noise/spurs and tuning/settling with state dependence.

#### 15.2 LO requirements from the task

Use Chapter 9 blocker physics and Chapter 12 allocation to derive effective noise/spur envelopes, including internal buffers.

#### 15.3 Endpoint distribution

Calculate source-sharing through unequal branches, additive noise, loading, isolation and environmental sensitivity; compare topologies and powers.

#### 15.4 Evidence at endpoints

Evaluate branch changes and correlated test references. Include supply/routing/thermal constraints now; Chapter 22 provides their complete engineering treatment.

**Examples, engineering work and verification:** D-RAD/D-MET contrast source specifications with endpoint residuals. Shared frequency or typical curves do not establish phase repeatability or guaranteed performance.

### Chapter 16 — Distributed timing and carrier-reference inference

**Objective:** Establish bounded remote relationships and quantify unresolved freedoms.

**Entry:** Chapters 1, 3, 5 and 7; geometry adds 4/8.

**Canonical ownership:** K16. Shared results used here retain their original homes.

#### 16.1 Clock and link equations

Derive offset/rate/drift and one-/two-way equations with equipment/propagation delays and endpoint planes.

#### 16.2 Ambiguity and asymmetry

Determine offset/delay identifiability, reciprocity limits and modulo-cycle freedoms; distinguish RF phase, epoch, frequency and transport latency.

#### 16.3 Alignment, holdover and recovery

Compare shared transfer and independent estimation, derive residual growth/valid outage intervals and delayed-feedback constraints.

#### 16.4 Sampled-stream extension

Use supplied timing estimates first; add Chapter 17/19 resampling only for digital realization. Specify external geometry/reference knowledge and recovery validity.

**Examples, engineering work and verification:** P-INT and bistatic D-RAD need an asymmetric/ambiguous case and separate epoch/RF-phase evidence. Protocol and hardware selection remain external later inputs.

### Chapter 17 — Sampling and converter feasibility

**Objective:** Select rate, range, driver and clock using broadband and nonideal cases.

**Entry:** Chapters 6, 9, 11–12; reconcile analog drive with 14.

**Canonical ownership:** K17. Shared results used here retain their original homes.

#### 17.1 Sampling and anti-alias interfaces

Develop bandpass/alias placement, filtering and sample identity; distinguish arrival time from analog sampling epoch.

#### 17.2 Timing and correlation

Apply Chapter 9 complete-waveform sensitivity to aperture jitter/skew and clock/channel correlations, with conditional approximations.

#### 17.3 Quantization and distortion

Develop quantization-model conditions, coherent low-level exceptions, nonlinear/interleaving artifacts and conditional dither costs.

#### 17.4 Compatible selection

Calculate clock/range/driver/loading/common-mode/settling and recovery requirements. Compare technologies with guarantees, typical data and characterization needs separated.

**Examples, engineering work and verification:** X-BLK/X-STATE require broadband, blocker, low-level and recovery assessments beyond a sine test. Include power/reference isolation and valid-state consequences.

### Chapter 18 — Quadrature and conjugate-response fidelity

**Objective:** Estimate and correct I/Q errors while preserving real desired information.

**Entry:** Chapters 1–2, 5, 11 and 14; digital correction adds 17/19.

**Canonical ownership:** K18. Shared results used here retain their original homes.

#### 18.1 Quadrature models

Develop frequency/state-dependent desired and conjugate response, improper signals, imbalance, DC offset and leakage.

#### 18.2 Stimulus and estimation

Choose observations that distinguish leakage, response error and genuine near-DC signal; expose ambiguous cases.

#### 18.3 Bounded compensation

Develop analog/digital options and residual/noise/resource consequences. Reuse Chapter 20 general feasibility for advanced correction.

#### 18.4 Independent fidelity checks

Plan swept/modulated/near-DC level/state checks independent of fitting, then integrate procedural validity through Chapter 23.

**Examples, engineering work and verification:** D-COM/D-MET need estimated/applied correction and retained desired response. Suppressing a real signal does not count as successful offset removal.

### Chapter 19 — Multirate processing and finite resources

**Objective:** Realize a bounded sample-preserving chain within numerical and platform limits.

**Entry:** Chapters 3, 6, 11 and 17; correction adds 20, remote estimates 16.

**Canonical ownership:** K19a/b. Shared results used here retain their original homes.

#### 19.1 DDC, NCO and channelization

Develop translation/filter/decimation response, phase, group delay and sample identity through tuning and reset.

#### 19.2 Resampling and transients

Develop fractional delay/asynchronous estimates, finite filters and startup effects. General inverse feasibility follows in Chapter 20; do not teach equalization as unconstrained inversion here.

#### 19.3 Numerical realization

Calculate scaling, precision, coefficient error, truncation bias, overflow and reference-comparison residuals.

#### 19.4 Real-time interfaces

Calculate throughput, buffering, latency, clock-domain crossing, timestamps and loss detection. Establish platform resource/timing evidence rather than infer it from floating-point agreement.

**Examples, engineering work and verification:** D-COM and X-STATE exercise impulse/tone/modulated inputs, rate/reset changes, one-sample and NCO faults. A finite-length correction revisit after 20 quantifies noise gain and residual.

### Chapter 20 — Complex-response alignment and feasible correction

**Objective:** Distinguish known response, achievable compensation and lost information.

**Entry:** Chapters 4, 6, 11–12; fields add 8, digital realization 19.

**Canonical ownership:** K20. Shared results used here retain their original homes.

#### 20.1 Relative response over bandwidth

Develop amplitude/phase/delay/dispersion alignment and allocation across channel, band and state.

#### 20.2 Inverse approximation bridge

Develop necessary causal/stable/minimum-phase reasoning and finite-latency/length alternatives; formal inversion is insufficient.

#### 20.3 Noise and information limits

Calculate coefficient range/resolution, noise gain and residuals for attenuation, deep null and true rank-loss cases; do not classify every notch as irrecoverable.

#### 20.4 Correction access and prevention

Compare physical matching, analog/digital approximation and architecture change before irreversible combination. Procedural estimation/validity returns in Chapter 23.

**Examples, engineering work and verification:** D-ARR/X-INV require independent band/state residuals and a rejected correction. Analog alignment remains a valid route without DDC.

## Part IV — Valid operation and engineering evidence

### Chapter 21 — State causality, integration and diagnosis

**Objective:** Preserve observable meaning through transitions and discriminate faults.

**Entry:** Chapters 1, 11–13; add selected realization/reference methods only.

**Canonical ownership:** K23a/b/c. Shared results used here retain their original homes.

#### 21.1 Transition causality

Trace applicable PLL/divider/sampler/FIFO/NCO/filter states; distinguish epoch, transport latency, RF phase and calibration validity.

#### 21.2 Integrated configuration

Develop startup/reset/retune/link/reference-loss sequences, channel/sample identity, coefficient versions, logging and valid-data gates.

#### 21.3 Fault injection and recovery

Specify bounded integrated exercises for partial reset, drops, stale coefficients and outage; preserve raw evidence and observe end-to-end response.

#### 21.4 Diagnostic interventions

Use frequency/time/channel/environment signatures, controlled substitutions and competing hypotheses. Chapter 24 supplies rare-event confidence, not an arbitrary repeat count.

**Examples, engineering work and verification:** X-STATE and D-MET require an exercised path and supported diagnosis; successful communication or framing alignment is insufficient.

### Chapter 22 — Physical and environmental engineering

**Objective:** Translate allocations into concrete physical constraints and controlled evidence.

**Entry:** Chapters 6, 11–12, 14 and RF interconnect baseline; selected paths add 15/17/19/20.

**Canonical ownership:** K24a/b. Shared results used here retain their original homes.

#### 22.1 Coupling and power paths

Calculate representative aggressor/supply-to-phase contributions; develop return-current, impedance, isolation, regulator/filter and shield choices.

#### 22.2 Layout and access

Specify routing/stack-up/distribution/test-access constraints from sensitivities; equal physical length does not guarantee electrical matching.

#### 22.3 Thermal and mechanical response

Develop coefficients, gradients, time constants, strain, vibration, connectors and warmup. Bound externally supplied material/fabrication facts.

#### 22.4 Mitigation and comparison

Calculate residual sensitivity and interpret controlled gradient/cycling/handling or aggressor tests with reference controls; uniform chamber evidence is limited.

**Examples, engineering work and verification:** D-ARR/D-MET and X-PROD connect constraints to budgets and field validity. Calibration interfaces may be supplied before maintenance policy; no generic layout checklist discharges this chapter.

### Chapter 23 — Calibration procedures and continued coherence

**Objective:** Execute valid correction and choose maintenance without removing wanted information.

**Entry:** Chapter 13 plus 3, 5–7; selected corrections 18–20, states 21, environment 22.

**Canonical ownership:** K21b/c. Shared results used here retain their original homes.

#### 23.1 Acquisition to correction

Combine observable parameters, uncertain stimuli and feasible correction; develop ordering, interpolation/regularization and coefficient provenance.

#### 23.2 Held-out validity

Evaluate independent band/gain/level/state/environment residuals, noise gain, coefficient resources and desired-signal transfer; reject invalid corrections.

#### 23.3 Maintenance policy

Derive update cadence/latency/downtime from drift/motion and task sensitivity, including environmental evidence and remote holdover where applicable.

#### 23.4 Degraded operation and change

Evaluate fades/outages, stale calibration and reacquisition; declare invalid intervals and retain configuration. Compare fixed correction, periodic calibration and tracking.

**Examples, engineering work and verification:** All anchors use bounded executed/evaluated procedures. P-SEN explicitly varies wanted and nuisance inputs; a smaller fit or operational residual is insufficient evidence.

### Chapter 24 — Verification coverage and bounded conclusions

**Objective:** Evaluate requirements evidence with uncertainty, coverage and justified confidence.

**Entry:** Chapters 6, 12–13; add actual subsystem/application evidence.

**Canonical ownership:** K25. Shared results used here retain their original homes.

#### 24.1 Requirement-evidence arguments

Map operational claims to analysis/inspection/test/demonstration with state/environment/configuration and unresolved corners.

#### 24.2 Decision rules near limits

Use measurement uncertainty, model limitations and declared rules to assess a supplied borderline case; do not fold every uncertainty into arbitrary margin.

#### 24.3 Finite exposure and rare failures

Calculate defensible duration/exposures and bounds for slips/restarts with dependence assumptions. Zero observed failures does not imply zero probability.

#### 24.4 Kinds of assurance

Separate algebra/software consistency, physical applicability, engineering adequacy and system compliance; identify additional empirical evidence and human review needed.

**Examples, engineering work and verification:** X-STATE/X-PROD need evaluated evidence cases and bounded conclusions. Earlier verification previews point here for full decision methods.

### Chapter 25 — Production feasibility, service and configuration change

**Objective:** Calculate production effort/yield and preserve validity after repair or update.

**Entry:** Chapters 12–13, 21–24; joint variation adds 4.

**Canonical ownership:** K26a/b. Shared results used here retain their original homes.

#### 25.1 Joint variation and correction capacity

Propagate unit/lot/process/environment variation with declared correlations/bounds; calculate joint yield and coefficient range/resolution.

#### 25.2 Factory test and calibration effort

Calculate sweep/settling/acquisition/retest time, fixture uncertainty and reduced-coverage faults. Evaluate escapes/false rejects and adjustment/test access.

#### 25.3 Distribution sensitivity

Vary unsupported distributions/correlations and reference/fixture errors; a prototype or individual tolerances cannot establish population yield.

#### 25.4 Service and continued evidence

Evaluate aging/reference health, replacement/firmware change, invalidation/requalification, monitoring and regression. Require real lifetime facts for numerical reliability claims.

**Examples, engineering work and verification:** X-PROD and D-ARR element replacement require calculated effort and evaluated change evidence, not generic lifecycle prose. Actual process data remain unknown.

## Part V — Application synthesis

### Chapter 26 — Carrier-coherent communications

**Objective:** Complete D-COM from finite observations to justified waveform performance.

**Entry:** Chapters 1, 5, 7, 9–10, 12; chosen chain/calibration/evidence conditional.

**Canonical ownership:** A35. Shared results used here retain their original homes.

#### 26.1 Burst observations and ambiguity

Develop waveform/pilot/carrier/timing models and intersect acquisition, payload and buffer deadlines; choose representative families only after review.

#### 26.2 Recovery alternatives

Compare feedforward, tracking and decision-directed choices, search and mode changes using canonical inference/loop results.

#### 26.3 Residual-to-waveform mapping

Derive signal-quality/detection consequences and a multicarrier common-phase versus intercarrier contrast; include retained-signal effects of rejection.

#### 26.4 Integrated D-COM and transfer

Join earlier frequency/gain/reference/processing decisions, bounded recovery, calibration, verification and production stages. Change fade, pilot or reference assumptions for transfer.

**Examples, engineering work and verification:** Require acquisition/slip/reacquisition and blocker-survival evidence with evaluated bounded recovery. Full coding/protocol catalogues remain external; inputs are not selected here.

### Chapter 27 — Coherent radar receiver engineering

**Objective:** Complete D-RAD using delayed waveform/reference relationships and usable receive intervals.

**Entry:** Chapters 1, 3, 8–10, 12; add selected realization and 16 for bistatic.

**Canonical ownership:** A36. Shared results used here retain their original homes.

#### 27.1 Transmit-to-return observations

Develop fast/slow time, delay/Doppler/angle and coherent interval for representative pulse/sweep families; state reset/waveform assumptions.

#### 27.2 Delay-weighted disturbances

Derive leakage/clutter pedestal at weak returns using Chapter 3 unequal-path and Chapter 9 physical models with waveform weighting.

#### 27.3 Architecture and recovery

Intersect headroom/overload recovery with wanted return timing; compare reference, isolation, conversion and gain placements; include separate-reference contrast.

#### 27.4 Integrated D-RAD and evidence

Join allocation, state, processing/calibration, physical and lifecycle stages. Require delayed/dynamic test sensitivity and target retention after cancellation.

**Examples, engineering work and verification:** Reject zero-delay loopback or low NF as sufficient. Bound necessary processing internally; comprehensive SAR/mission imaging awaits U-04 review.

### Chapter 28 — Receiving arrays and beam formation

**Objective:** Complete D-ARR from vector input/noise models to pattern and production decisions.

**Entry:** Chapters 1, 4, 8–10, 12, 20; selected analog/digital/reference paths conditional.

**Canonical ownership:** A37. Shared results used here retain their original homes.

#### 28.1 Field and noise to weights

Derive weighted signal/noise response using vector manifold and physical covariance, preserving polarization/loading conventions.

#### 28.2 Pattern sensitivity

Calculate beam gain, pointing, null robustness and correlated calibration/manifold error over band/scan; explain conditioning and training contamination.

#### 28.3 Steering and correction access

Compare phase steering, true delay, digital/hybrid realization, quantization/loss/resources and access before destructive combination.

#### 28.4 Integrated D-ARR and replacement

Join calibration/OTA evidence, gradients, state validity, fixture/production and element-replacement consequences into a substantial design account.

**Examples, engineering work and verification:** Require bounded weight/alignment realization and pattern/noise evaluation. Boresight tones and electronic matching cannot establish field performance; detailed radiator synthesis external.

### Chapter 29 — Direction finding and ambiguous inference

**Objective:** Derive bearing requirements and evaluate a bounded estimator without forcing uniqueness.

**Entry:** Chapters 1, 4–5, 8–9, 12 and 20; calibration and rejection as selected.

**Canonical ownership:** A38. Shared results used here retain their original homes.

#### 29.1 Geometry and observations

Develop phase/time/amplitude comparisons and selected covariance inference with source count, snapshots and propagation assumptions.

#### 29.2 Ambiguity, bias and sensitivity

Derive local bearing sensitivity and exhibit globally indistinguishable solutions; include finite records and imperfect vector manifold.

#### 29.3 Competing physical explanations

Evaluate coherent multipath, multiple sources, polarization and receiver errors; compare additional geometry/observations with merely tighter electronics.

#### 29.4 P-DF development and evidence

Plan a substantial bounded estimator/manifold-calibration example and known-source/geometry interventions. Preserve unresolved cases and production/configuration validity.

**Examples, engineering work and verification:** D-ARR hardware is reused but beam quality does not establish bearing. Exhaustive DF algorithms external; selected methods must support actual receiver decisions.

### Chapter 30 — Interferometric correlation and references

**Objective:** Derive stochastic sensitivity and separate instrumental, geometric and source/reference freedoms.

**Entry:** Chapters 1, 3–5, 8–10, 12; remote/sampled paths add 16–19.

**Canonical ownership:** A39. Shared results used here retain their original homes.

#### 30.1 Baseline observations

Develop complex correlation/visibility and geometric/instrumental delay with declared source statistics, bands and records.

#### 30.2 Finite-integration sensitivity

Derive bias/variance including stochastic source power, colored/coupled receiver noise, effective samples and residual alignment loss.

#### 30.3 Clocks and calibration freedoms

Compare shared/independent references, delay/rate/epoch alignment and phase referencing; preserve required astrometric information and observing/instrument distinctions.

#### 30.4 P-INT development and evidence

Plan substantial stochastic correlation/alignment and bounded calibration, metadata and holdover contrasts. Imaging/observing boundary needs explicit specialist review.

**Examples, engineering work and verification:** Zero expected independent-noise correlation is not zero uncertainty; a split deterministic tone does not validate weak-source sensitivity. No complete imaging claim is made.

### Chapter 31 — Coherent physical sensing

**Objective:** Infer a physical quantity with usable range, uncertainty and wanted-signal retention.

**Entry:** Chapters 1, 5–8, 12–13; correction/remote realization as chosen.

**Canonical ownership:** A40. Shared results used here retain their original homes.

#### 31.1 Measurand transfer

Develop representative RF physical transfer, sensitivity, resolution versus accuracy and unambiguous range with externally supplied sensor-law conditions.

#### 31.2 Nuisance and observability

Exhibit wanted/reference-path changes producing indistinguishable observations; identify additional observables or restricted valid operation.

#### 31.3 Dynamics and compensation

Derive wanted/nuisance transfer through tracking, update latency, wrapping/fade recovery and environmental compensation.

#### 31.4 P-SEN development and evidence

Plan substantial physical inference with independent physical-reference comparison, uncertain nuisance variation and service drift; change measurand or dynamics for transfer.

**Examples, engineering work and verification:** Quiet electronics alone cannot establish physical accuracy. Keep essential inference internal; sensor-specific/non-RF extensions require owner/specialist decision.

### Chapter 32 — Phase-sensitive instruments and transfer measurement

**Objective:** Complete D-MET from port topology to interpreted calibrated result.

**Entry:** Chapters 1, 3, 6, 11–13, 24; selected analog/digital chain conditional.

**Canonical ownership:** A41. Shared results used here retain their original homes.

#### 32.1 Port and reference topology

Develop simultaneous ratio versus switched measurements, source/receiver coupling, level/headroom, drift and settling choices.

#### 32.2 De-embedding and correction

Derive fixture/port extension and reference corrections with uncertainty after correction; apply Chapter 13 metrology without duplicating its general theory.

#### 32.3 Discriminating instrument evidence

Vary cable, level and reference arrangements to distinguish DUT from artifacts; preserve any intentional measurement-method definition.

#### 32.4 Integrated D-MET and service

Join frequency/reference plan, analog or sampled realization, calibration/state, fixture capability and service recalibration. Change topology for transfer assessment.

**Examples, engineering work and verification:** Require executed or critically evaluated measurement and bounded instrument choice, not procedure alone. Correlated-reference repeatability is not traceable accuracy; current standards/commands remain later external facts.

## Technical appendices and reference aids

### Appendix A — Conventions and representation lookup

Provide approved envelope/Fourier/PSD/L(f)/cross-spectrum definitions, units, reference-plane and state conventions with translations to cited sources. Choices are unresolved now and require human decision before substantive derivations. Chapter 1 owns their explanation; this is lookup, not a competing canonical treatment.

### Appendix B — Targeted supporting refreshers

Offer RF-baseline remediation pointers and supplementary calculus/Fourier, algebra, probability and control exercises/identities. Chapters 2–7 own the essential specialist bridges. Appendix use must never be a hidden prerequisite or replace indispensable coherent reasoning.

### Appendix C — Engineering calculation and evidence navigation

Provide lookup routes by observable, design question, error mechanism and failure signature, linking canonical derivations, applicable conditions, input data and evidence requirements. Include unit/reference translations and reusable reporting guidance without duplicating budget, metrology or compliance theory. Plan subject/result and symbol indexes during later authoring.

## Editorial review focus

Each chapter has four substantive sections because these are the present bounded reasoning groups, not a fixed template for authoring. Expand section detail when an omission is otherwise hidden. Chapter 12 groups feasible-region selection with budget refinement; Chapter 13 groups observability before measurement; Chapter 23 groups executed procedure before maintenance; Chapter 25 groups population decisions before service change. Their internal boundaries are explicit and must be challenged for practical teaching scope. No arbitrary word/page ceiling is selected. Propose a split only if distinct learner outcomes or missing prerequisites require it; preserve canonical ownership and avoid scattering one derivation. Part V application chapters must remain substantial developments, not summaries of earlier hardware chapters.
