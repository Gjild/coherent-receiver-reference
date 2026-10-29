# Technical Coverage, Canonical Treatments and Capability Support

**Status:** draft development specification, 2026-10-28; human review pending. The [architecture](architecture.md) owns the learning/reference organization. The [inventory](competence-inventory.md) owns capability definitions and their required competence dimensions. The [design briefs and stress tests](reference-design-plan.md) challenge this specification. No technical treatment specified here has thereby been derived, implemented, physically validated or accepted.

## 1. Reading the coverage specification

K01–K26 identify shared treatments; A35–A41 identify application-specific mappings. These are Markdown navigation labels, not book numbering or a knowledge database. A treatment is bounded by a reasoning responsibility, not by page count. Suffixes a/b/c distinguish first treatment from refinement only where prerequisites differ. Dependencies are owned by §3, not inferred from identifier order.

Every treatment below requires a human-readable explanation, applicable mathematics, physical interpretation, a consequential calculation/decision, limitations and an assessment. Statements such as “derive,” “evaluate,” and “implement” specify future book obligations; they do not report work performed at this architecture stage.

**F/S/E** mean full internal / selective supporting / external treatment. F applies to essential coherent reasoning even where an adjacent discipline is S or E. Every imported fact must retain units, definitions, conditions and evidence limits. Shared source-path calculations must identify the observable, reference planes, waveform, observation filtering, time interval, operating state and calibration dependency wherever consequential.

**Evidence boundary:** this package analyzes the repository's planning requirements. It introduces no newly verified technical source claims. The existing [source examination note](../references/source-notes/competence-inventory-foundations.md) supports only its recorded S1–S9 distinctions; those passages were not re-examined here. Its evidence cannot certify the treatments below. §6 identifies required later research and review. No universal formula, PSD normalization, product requirement or current device guarantee is selected.

## 2. Canonical development obligations

### K01 — Operational observables and coherent representations

**Canonical result:** consistent conversion between physical waveforms, phasors, analytic signals, complex envelopes and sampled representations, with explicit power/phase/frequency conventions. Develop phase, frequency, delay, correlation and observation definitions; separate accuracy, temporal stability, restart repeatability and alignment. **Use/assessment:** reconstruct a waveform, follow conjugation/inversion and compare two differently filtered or referenced measurands. **Limits:** phase near amplitude nulls, wrapped versus unwrapped quantities, undefined absolute references and unresolved normalization. **Depth:** F coherent representations and reference changes; S Fourier refresher; E missing general RF remediation. K03 owns stochastic observation analysis; K22 owns instrument realization.

### K02 — Scalar stochastic and complex phase reasoning

**Canonical result:** probability/expectation and scalar covariance bridges; random processes, stationarity/ergodicity, complex proper/improper models, circular statistics and phase increments. Develop multiplicative complex phase versus additive noise, including the local additive-noise-to-phase relation and its breakdown. **Use/assessment:** compare disturbances with equal marginal phase variance and different temporal structure, construct a justified scalar model and identify unsupported Gaussian/independence assumptions. **Limits:** low SNR, fades, nonstationarity, higher moments and phase wrapping. **Depth:** F coherent stochastic reasoning; S general probability. Physical source construction belongs to K09, not a postulated correlation coefficient.

### K03 — Spectra, finite observation and coherence

**Canonical result:** auto/cross spectra, observation/window/filter weighting, phase/frequency/time relations, phase-increment and complex-coherence relationships, finite-record bias/variance and stability measures. Develop shared-source differential transfer through unequal paths, including the pure-delay limit. Identify exactly where Gaussian, stationary, small-angle or fourth-moment assumptions enter. **Use/assessment:** compare spectral/time formulations and equal-marginal-variance cases; evaluate averaging uncertainty and convergence. **Limits:** unqualified PSD integrals, nonstationary/distributional spectra, finite bandwidth and effective independent samples. **Depth:** F essential relations; S broader estimator catalogue. Matrix forms add K04; A39 owns application correlation sensitivity.

### K04 — Matrix inference and coupled response

**Canonical result:** complex vectors/matrices, covariance and quadratic forms, rank, eigenstructure, singular values, least squares, conditioning and justified constraints/regularization. **Use/assessment:** form a channel model, identify null directions and quantify sensitivity; check covariance symmetry and positive semidefiniteness. **Limits:** formal inversion versus stable inference, coordinate/reference freedoms and poorly determined physical inputs. **Depth:** S linear-algebra bridge; F coherent uses. K09 supplies physically constructed covariance; K05 owns inferential interpretation and K20 owns correction realizability.

### K05 — Parameter inference, information and ambiguity

**Canonical result:** representative phase/frequency/delay/amplitude estimation from likelihood and least squares, nuisance parameters, bias/variance, applicable information bounds and global ambiguity. Start with scalar inference; extend to coupled parameters with K04. **Use/assessment:** derive/evaluate an estimator and bound, exhibit indistinguishable parameter sets, then test mismatch and local versus global conclusions. **Limits:** regularity conditions, finite observations, low-SNR/threshold behavior, ambiguity and model error. **Depth:** F receiver-specific inference; S statistical theory. Calibration measurement freedoms belong to K21a; system feasibility to K11.

### K06 — Acquisition, tracking and desired-signal transfer

**Canonical result:** detector/loop dynamics, locked-state transfer, stability/noise bandwidth, sampled latency and dynamic stress; separate nonlinear acquisition, slips, saturation and recovery. Derive transfer of the wanted physical signal as well as nuisance disturbances. **Use/assessment:** evaluate and realize a bounded acquisition/tracking procedure including holdover and reacquisition; compare feedforward/feedback alternatives. **Limits:** no capture guarantee from linear locked-state analysis; faded or ambiguous observations and delayed feedback. **Depth:** F coherent synchronization; S control bridge. K23 owns system transition sequencing; K21c owns maintenance policy.

### K07 — Approximation, uncertainty and adequate models

**Canonical result:** dimensional and limiting-case reasoning, perturbation/sensitivity, covariance-aware uncertainty propagation, numerical convergence/precision, and nonlinear/ambiguous alternatives to first-order propagation. Develop model hierarchy and discrepancy separately from numerical error. **Use/assessment:** construct and execute a bounded analytical/computational model for a decision, compare independent formulations and state unsupported extrapolations. **Limits:** uncertain parameters, wrong physics, nonlinearity and circular validation. **Depth:** F coherent interpretation/model assessment; S general numerical tools; E tool particulars. K13 owns allocations, K22 measurement uncertainty and K25 evidence decisions; they reuse this mathematics.

### K08 — Propagation, geometry and physical transduction

**Canonical result:** phase/delay/Doppler and minimum vector field-to-port/sensor models, with bases, reference geometry, effective response, loading/coupling and cross-polar leakage. Derive the conditions for a scalar channel model. **Use/assessment:** calculate direction/frequency/polarization or sensor dependence and show which external-path changes internal injection cannot establish. **Limits:** narrowband/far-field/quasi-static assumptions, multipath, geometry and nuisance transduction. **Depth:** F minimum receiver model; S supporting fields/propagation; E full-wave radiators, detailed environments and specialist sensor laws. Externally supplied models must expose uncertainty and conventions.

### K09 — Physical disturbance generation and paths

**Canonical result:** convert physical thermal/representative active-device and external-field noise through loaded/coupled networks into delivered spectra and covariance. Develop reciprocal mixing with effective LO spectra, blocker/preselection/observation filtering and internal branch contributions; develop timing-error disturbance from the complete analog waveform and clock process. **Use/assessment:** calculate narrow-blocker/flat-spectrum limits and finite-spectrum contrasts; construct coupled covariance and derive filter/LO/clock constraints. **Limits:** source independence, impedance/power normalization, stationarity, small timing errors and unavailable physical parameters. **Depth:** F coherent source/path reasoning; S noise-network bridge; E detailed device physics and verified parameters. K13 assembles, rather than regenerates, these contributions.

### K10 — Detection, integration and signal-preserving rejection

**Canonical result:** correlation/matched filtering, applicable sufficient-statistic/likelihood reasoning, colored-noise weighting, coherent/noncoherent accumulation and reference mismatch. Develop separation/degree-of-freedom limits and effects of contaminated training or reference leakage. **Use/assessment:** realize and evaluate a bounded extraction/rejection method, calculating retained desired information, detection/correlation outcome and uncertainty. **Limits:** indistinguishable subspaces, finite support, covariance conditioning and pre-digital clipping. **Depth:** F coherent extraction/rejection; S general detection theory; E exhaustive adaptive/mission algorithms. Applications own their hypotheses, waveform mappings and task consequences.

### K11 — Requirements, joint feasibility and architecture selection

**First treatment:** formulate operational needs, states, observables, missing limits and evidence routes. **Quantitative refinement:** intersect information, ambiguity, energy/bandwidth/time, dynamics, headroom, latency and technology/resource constraints; distinguish empty, conditional and evidenced feasible regions. **Use/assessment:** calculate gain-range and information/steering conflicts, compare architectures and quantitative interfaces, identify which change restores feasibility. **Limits:** local precision is not global acquisition; supplied technology envelopes are assumptions until evidenced. **Depth:** F coherent systems reasoning; S generic systems/constrained analysis; E actual contracts, regulations and device facts. K13/subsystem results refine the initial feasible region through engineering interaction.

### K12 — End-to-end frequency, phase and delay transfer

**Canonical result:** phase signs and reference transfer through conversion, multiplication/division, filtering and sampling; desired/image/alias/spur bands, spectral inversion and group delay. **Use/assessment:** construct and exercise an annotated frequency/reference plan across states, tracking tones/modulation and identifying reset-sensitive elements. **Limits:** ideal transfer versus stateful/nonlinear hardware, constant phase versus frequency-dependent response. **Depth:** F coherent transfer; S conventional frequency-plan refresher. K15 and K17/K19 provide implementation refinements; K23 manages transitions. Sampling placement can first use a declared ideal interface rather than converter design as a prerequisite.

### K13 — Correlated allocations and budget closure

**Canonical result:** propagate physical source/path results, covariance/cross-spectra and deterministic terms to task observables; distinguish margin, variability, model/parameter uncertainty, calibration residual and measurement uncertainty. **Use/assessment:** calculate closure and sensitivity to a correlation, blocker, environment or missing parameter; compare with K11 feasibility. **Limits:** double counting common sources, incorrect independence, wrong reference planes and missing application mappings. **Depth:** F coherent allocations; S generic budgeting. Application limits and subsystem transfer specifications may be supplied initially, with explicit later reconciliation.

### K14 — Analog information preservation, nonlinearity and gain policy

**Canonical result:** gain/filter/isolation/headroom design under the full signal/blocker envelope, adequate memoryless/dynamic/measured nonlinear models, AM-to-AM/PM, crest factor, gain-state complex response and recovery. **Use/assessment:** calculate stage allocations and realize a bounded gain/valid-data policy; compare weak-signal/blocker, modulated/multitone and strong-pulse cases. **Limits:** IP2/IP3 extrapolation, memory, overload and missing loading/drive/bias evidence. **Depth:** F coherent nonlinear reasoning; S circuit design; E part/revision/operating guarantees or characterization. Converter interfaces, state and calibration access are reconciled with K17/K23/K21 rather than assumed solved.

### K15 — Synthesis and endpoint reference distribution

**First treatment (a):** PLL/reference/oscillator transfer, multiplication/division, noise/spurs, tuning/settling and state-dependent synthesis. **Endpoint refinement (b):** source-sharing through unequal branch response, additive branch noise, loading/isolation, environmental sensitivity and actual endpoint comparison. **Use/assessment:** derive an effective LO envelope from blocker conditions, compare synthesis/topology alternatives and evaluate endpoint evidence including test-reference correlation. **Limits:** frequency accuracy does not establish phase; typical data and source-sharing are not guarantees. **Depth:** F coherent synthesis/distribution; S oscillator/interconnect theory; E technology-specific guarantees. K16 owns remote inference; K23 owns sequencing.

### K16 — Distributed clock and carrier-reference inference

**Canonical result:** offset/rate/drift and one-/two-way measurement equations with propagation/equipment delays, reference freedoms, reciprocity/asymmetry and modulo-cycle ambiguity. Distinguish RF phase, frequency, sample epoch and transport latency. **Use/assessment:** evaluate an ambiguity/asymmetry case and bounded alignment/holdover/recovery method; calculate residuals and valid outage intervals separately. **Limits:** missing geometry/delay information, delayed-feedback stability and uncertain link conditions. **Depth:** F minimum distributed inference; S representative transfer methods; E protocols/hardware. Digital resampling is a conditional realization using K19, not a prerequisite for continuous reference equations.

### K17 — Sampling, timing and converter feasibility

**Canonical result:** bandpass/aliasing and anti-alias interfaces, aperture jitter/skew with correlations, quantization-model conditions, nonlinear/interleaving effects and conditional dither. **Use/assessment:** calculate rate, headroom, clock and driver/converter requirements for broadband, coherent low-level, blocker and recovery cases, not only a tone. **Limits:** total-waveform timing sensitivity, correlated quantization, front-end distortion, loading/common-mode/settling and typical-versus-guaranteed evidence. **Depth:** F coherent converter consequences; S converter theory; E device data/errata. K09 owns timing-disturbance construction; K14 analog interface results interact with selection.

### K18 — Quadrature and conjugate-response fidelity

**Canonical result:** frequency/state-dependent I/Q imbalance, improper/conjugate signal models, DC offset, leakage and desired near-DC response. **Use/assessment:** estimate/apply a bounded correction and evaluate independent swept/modulated/near-DC data with level/state variation. **Limits:** suppression of a real signal, ambiguous leakage and unsupported correction envelope. **Depth:** F coherent I/Q reasoning; E device internals. Analog quadrature does not require ADC/DDC knowledge. Digital correction adds K17/K19; general calibration validity comes from K21b.

### K19 — Multirate processing and finite-resource realization

**First treatment (a):** DDC/NCO, filtering/channelization, decimation/resampling, phase/delay, sample identity, transients and asynchronous timing estimates. **Realization (b):** numerical scaling, fixed/floating precision, overflow, coefficient error, throughput, buffering, clock-domain crossing and timestamps. **Use/assessment:** realize a bounded chain with impulse/tone/modulated and rate/reset tests; compare reference calculations and establish platform timing/resources. **Limits:** finite length, noise enhancement, startup state, lost samples and unsupported hardware claims. **Depth:** F coherent processing/resource consequences; S DSP/digital design; E HDL/core/tool details. K20 owns general correction feasibility; K23 integrates state.

### K20 — Complex-response alignment and correction feasibility

**Canonical result:** relative amplitude/phase/delay/dispersion response and physically meaningful inverse approximation; distinguish identifiable parameters, feasible compensation and irretrievable information. Develop causality/stability/minimum-phase implications, finite latency/length, coefficient range/resolution and noise gain before choosing analog/digital realization. **Use/assessment:** calculate wideband alignment residuals and deep-attenuation/null contrasts; compare prevention, approximate correction and architecture change before irreversible combination. **Limits:** clipping/aliasing/rank loss without extra information; a notch is not automatically irrecoverable. **Depth:** F correction reasoning; S necessary systems/inverse bridge. K19 supplies digital realization only where selected; K21 owns estimation procedure and validity.

### K21 — Calibration observability, procedure and maintenance

**First treatment (a):** measurement equations, stimulus/reference uncertainty, nuisance/reference freedoms, rank, omitted paths and desired-observable preservation. **Procedure (b):** combine metrology with observable parameters and feasible correction; acquire, estimate, apply and evaluate held-out residuals, noise gain, coefficient resources and provenance across states/band/environment. **Maintenance (c):** derive cadence, latency, downtime, drift/motion/outage policy and wanted-versus-nuisance transfer; reject invalid compensation or declare degraded operation. **Use/assessment:** demonstrate an indistinguishable calibration case, an executable bounded correction and an independent validity/retained-signal test. **Depth:** F all coherent reasoning; E instrument commands/specialist environmental inputs. A small fit residual is insufficient.

### K22 — Operational metrology and uncertainty

**Canonical result:** instrument measurement equations including intentional method dependence, loading, fixtures, de-embedding, corrections, correlated references, floor/dynamic range, finite-record uncertainty and traceability. Reuse K07 propagation rather than create a second uncertainty theory. **Use/assessment:** execute or critically evaluate supplied measurements, calculate uncertainty and change reference/fixture topology to test sensitivity. **Limits:** apparent cancellation, instrument floors, estimator bias, insufficient degrees of freedom and nonlinear/ambiguous propagation. **Depth:** F coherent metrology; S general measurement methods; E instrument/calibration-standard particulars. K21a is conditional where calibration observability is needed; executable calibration is not prerequisite to the first measurement treatment.

### K23 — State causality, integration and diagnosis

**First treatment (a):** initialization/reset/retune/link/reference-loss causality across applicable PLL/divider/sampler/FIFO/NCO/filter states; separate sample epoch, transport latency and RF phase. **Integration (b):** interfaces, sequencing, channel/sample identity, calibration/configuration versions, logging and valid-data gates. **Diagnosis (c):** discriminate physical hypotheses by controlled substitutions and interventions, preserving raw data and state. **Use/assessment:** implement/exercise bounded transitions and fault cases and interpret exposure/confidence through K25; evaluate a discriminating diagnostic experiment. **Depth:** F coherent state/diagnosis; S software/configuration practice; E device-specific state guarantees. No universal digital chain is assumed.

### K24 — Physical and environmental realization

**First treatment (a):** translate sensitivity allocations into routing, return-current, power/filter, shielding, coupling/isolation and test-access constraints; calculate representative aggressor/supply-to-phase paths. **Environmental refinement (b):** thermal coefficients/gradients/time constants, strain, vibration, connectors, warmup and mitigation residuals. **Use/assessment:** evaluate concrete implementation constraints and controlled aggressor/gradient/handling evidence. **Limits:** equal physical lengths, uniform chamber results and generic layout rules do not establish electrical matching or field validity. **Depth:** F coherent consequences; S SI/PI/EMI/thermal/mechanical bridges; E materials/fabrication/qualification facts. Correction interface may be supplied before maintenance policy is developed.

### K25 — Verification coverage and bounded evidence decisions

**Canonical result:** requirement-to-evidence tracing, operating/state/environment coverage, uncertainty decision rules and justified finite exposure/statistical bounds for rare failures under stated dependence assumptions. **Use/assessment:** evaluate cases near a limit and identify untested corners, false conclusions and additional evidence needed. **Limits:** zero observed failures, model/software correctness, prototype success and physical applicability are distinct claims. **Depth:** F coherent verification; S assurance/sampling methods; E mandated compliance standards. K22 supplies measurement evidence; K07 assesses model adequacy. Application observables and actual configuration define the scope of any compliance claim.

### K26 — Production feasibility and continued validity

**Production (a):** joint unit/lot/process variation and environmental residuals, coefficient range/resolution, fixture uncertainty, calibration/test sweep/settling/retest time, coverage reduction and escapes/false rejects. **Service (b):** aging, monitoring, reference health, replacements/updates and calibration invalidation/requalification. **Use/assessment:** calculate bounded joint yield/test effort, vary unsupported distributions/correlations and evaluate a repaired/updated configuration. **Limits:** a prototype is not a distribution; unknown lifetime/variation cannot support numerical reliability/yield claims. **Depth:** F coherent lifecycle decisions; S statistical manufacturing/reliability; E supplier/process/lifetime facts. Preserve uncertainty and raw configuration evidence from K21–K25.

### A35–A41 — Application-specific mappings

These treatments reuse K results but must develop the following internal bridges. The required calculations and paper probes are specified in reference-design planning §4; none has been executed here.

| Treatment | Full internal application development and assessment | Selective support / external boundary |
|---|---|---|
| A35 Communications | Waveform-dependent carrier/timing acquisition, ambiguity and residual-to-performance mapping; finite burst/pilot feasibility; multicarrier common phase versus intercarrier disturbance; bounded recovery and fading/slip assessment | S representative modulation/channel methods; E full coding/protocol catalogues |
| A36 Radar | Transmit/delayed-return reference and waveform weighting; leakage/clutter pedestal at weak targets; range/Doppler/angle consequences; gain/recovery, pulse/chirp state and bistatic contrast | S required detection/radar-processing bridge; E comprehensive mission imaging, subject to U-04 |
| A37 Arrays | Vector manifold and physical noise covariance to weighted signal/noise, beam/pattern/null/pointing outcomes; wideband phase-versus-delay steering and analog/digital/hybrid correction access; bounded weight realization | S antenna/beam methods; E radiator synthesis/full-wave design beyond K08 minimum |
| A38 DF | Geometry/manifold to bearing ambiguity, bias and uncertainty with finite snapshots; distinguish local information from global identifiability; coherent multipath/multiple-source/polarization confounds; bounded inference | S selected comparison/covariance estimators; E exhaustive DF algorithms |
| A39 Interferometry | Stochastic complex-correlation sensitivity, bias/variance including source power and effective samples; geometric/instrumental delay and phase reference freedoms; shared/independent clocks and retained astrometric information | S necessary interferometric interpretation; E complete imaging/observing practice only if U-03 review confirms boundary |
| A40 Sensing | Physical measurand transfer, sensitivity, unambiguous range, wrapping/fade recovery, nuisance cross-sensitivity and wanted-signal transfer through compensation; independent physical-reference assessment | S representative RF transduction; E specialist sensor physics; no non-RF completeness |
| A41 Instruments | Port/reference topology, ratio/switched measurements, source/receiver coupling, de-embedding and uncertainty after correction; level/cable/reference variation to distinguish DUT from artifacts | S instrument exemplars; E commands and current calibration-standard particulars |

## 3. Dependency rationale and engineering interfaces

Dependencies below specify first quantitative entry unless a refinement is named. The common reader baseline is inventory §2. “Add” names a conditional prerequisite, not a universal requirement. Transitive foundations need not be repeated in every row.

A conditional revisit may use a treatment that itself consumes the base: teach K06 ordinary loops before K16 distributed inference, then return to the remote-loop extension of K06. Likewise teach K19a ordinary filtering and K20 general correction feasibility before combining them for digital equalization. Conditional entries must not be read as prerequisites for the base treatment in full; that would recreate the cycles this architecture separates.

| Treatment / entry | Essential knowledge consumed | Conditional knowledge and supplied inputs |
|---|---|---|
| K01 | Baseline phasors/calculus/Fourier methods for physical/complex representation | Conventions explicitly declared locally; canonical choices still pending |
| K02 | K01 signal/phase representations; internal probability bridge | Physical source parameters may initially be hypothetical and labeled |
| K03 | K01 observables/transforms; K02 stochastic moments/increments | Add K04 for matrix spectra; later physical construction K09 is an assessment refinement |
| K04 | K01 complex quantities; K02 covariance definitions; internal algebra bridge | No array/ADC implementation prerequisite |
| K05 | K01 signal model; K02 probability/noise for scalar likelihood/inference | Add K04 for matrix inference; waveform and nuisance assumptions supplied |
| K06 | K03 disturbance/observation weighting; K05 inference; internal control bridge | Add K16 for remote delayed-loop application; K17/K19 for digital realization |
| K07 | K01 scaling/units; K02 randomness for uncertainty; internal numerical bridge | Add K04 for matrix sensitivities; relevant physical model supplied and scrutinized |
| K08 | K01 reference/representation; K04 vector bases and transfer; RF fields baseline | Add K05 for inference limits; external geometry/antenna/transduction inputs required |
| K09 | K02/K03 stochastic spectra; K04 coupled covariance; RF noise/network baseline | Add K08 for incident-field/vector inputs; device/network parameters supplied |
| K10 | K03 observation statistics; K04 weighting; K05 hypotheses/inference | Add K08 for propagation and K09 for physical interference construction; no compulsory DSP |
| K11 first framing | Reader operational/RF baseline; K01 for quantitative observable definitions | Application need supplied; no budget result assumed |
| K11 quantitative | K05 information/ambiguity; K07 bounded calculation; K01 requirement conditions | Add K08/K04 spatial constraints, K10 detection, K09 disturbance constraints; technology/interface envelopes may be supplied |
| K12 | K01 signal/reference signs; K03 phase/transfer/observation reasoning | Ideal sampling interface first; K17/K19 refine implementation |
| K13 | K11 quantitative feasibility/architecture; K12 transfer; K09 physical sources; K04/K07 propagation/uncertainty | Add K08 geometry and K16 distributed terms; declared application/subsystem specifications first |
| K14 | K12 transfer, K13 allocations, K07 adequacy and K09 disturbance construction | Add K17 for an actual converter interface; operating/technology envelopes supplied |
| K15a; K15b | K15a: K06 loop behavior, K12 transfer, K13 allocations. K15b: K15a plus K03 common/differential transfer | Add K16 remote inference; branch/interface/environment parameters supplied |
| K16 | K01 clock/reference definitions; K03 stability; K05 identifiability; K06 loop/holdover | Add K04/K08 joint geometry; K17/K19 only for sampled-stream realization |
| K17 | K12 sampling/frequency representation; K13 allocations; K09 timing/noise; K07 approximation | Analog drive supplied initially, reconciled with K14; actual state guarantees external |
| K18 | K01 complex signals; K02 improper/noise models; K05 estimation; K12/K14 path behavior | Add K17/K19 for digital correction; K21b for full procedural validity |
| K19a; K19b | K19a: K17 sample identity, K12 transfer, K03 filtering, K07 error. K19b: K19a plus internal digital-resource bridge | Add K04/K20 for matrix equalization; K16 supplies remote-clock estimates; platform constraints external |
| K20 | K12 complex transfer; K13 allocations; K04/K07 conditioning/error; internal causal/stable inverse bridge | Add K08 antenna response, K15 distribution, K19 digital realization; no calibration procedure needed to analyze correction feasibility |
| K21a | K01 observables, K05 identifiability, K04 rank and K07 sensitivity | Add K08 external paths, K20 multichannel alignment, K09 physical noise |
| K22 | K01 measurand, K03 finite observation, K05 estimator behavior, K07 uncertainty | Add K21a calibration references; K04/K09 coupled noise; K17/K19 sampled measurement |
| K21b | K21a identified freedoms; K22 metrology; K05/K07 inference/uncertainty | Add K18/K19/K20 selected correction, K23a state validity, K08 field/sensor calibration |
| K21c | K21b valid procedure; K03 drift observation; K06 wanted/nuisance transfer | Add K08 motion/transduction, K16 holdover and K24b environmental evidence |
| K23a | K01 relationship definitions; K12 state-sensitive transfer | Add K15/K16 reference hardware, K17/K19 sampled path; device behaviors supplied |
| K23b; K23c | K23b: K11 architecture, K23a sequencing. K23c: K22 measurements, K07 discrimination and K01 observable definitions | Add chosen realization/calibration and suspected path methods; K25 for statistical confidence of transition/failure claims |
| K24a; K24b | K24a: K12/K13 allocations, K14 physical chain and RF interconnect baseline. K24b: K24a plus K07 sensitivities | Add K15 reference paths, K17/K19 digital interfaces, K20 channel matching; calibration interfaces may be supplied |
| K25 | K11 requirement framing, K22 evidence/uncertainty and K07 limits | Add K13 budgets, K07 model assessment and appropriate subsystem/application evidence |
| K26a; K26b | K26a: K13 allocations, K21b calibration, K22 measurement and K25 evidence. K26b: K21c maintenance, K23b configuration and K25 | Add K04 joint variation, K24 environment, K26a production interchangeability for service; actual distributions/lifetime facts external |

Application entry prerequisites remain those in the inventory, translated into K treatments: all require K01/K11/K13. A35 adds K05/K06/K09/K10; A36 adds K03/K08/K09/K10; A37 adds K04/K08/K09/K10/K20; A38 adds K04/K05/K08/K09/K20; A39 adds K03/K04/K05/K08/K09/K10; A40 adds K05/K06/K07/K08/K21a; A41 adds K03/K07/K12/K21a/K22/K25. Selected implementations add the appropriate K14–K24 branches. Applications motivate early questions before their full quantitative assessments.

**Engineering interfaces, not additional learning edges:** K11/K13 exchange feasibility and allocation; K14/K15/K17/K19 exchange gain, clock, drive, timing and resource envelopes; K20/K21/K24 exchange correction access and physical prevention; K16/K19 exchange clock estimates and stream-alignment residuals; K21/K23 exchange calibration validity and operating-state metadata; K22/K25 exchange uncertainty and decision-rule evidence; K24/K26 exchange environmental/process sensitivity and practical test coverage. Reconcile these interfaces in the reference-design revisits. Missing input evidence remains a qualification, not budget closure.

## 4. Capability support and assessment matrix

Dimensions are copied from the provisional inventory: C conceptual, M mathematical, A analytical, D design, I implementation, V verification. Listing a dimension commits to an assessable result; it does not claim that assessment has occurred. For every row the reader must explain mechanisms/assumptions and interpret the calculated or observed result; M requires the relevant derivation/manipulation. I requires an executed bounded method, realization or critical evaluation of supplied implementation evidence as specified in the inventory, not a plan alone. V includes limitations and an appropriate discriminating check. Detailed result obligations are in §2 and the named probe.

All rows retain F essential coherent reasoning. The S/E boundaries and necessary externally supplied inputs are defined in their treatments; external facts cannot replace the row's calculation. “Add” means conditional knowledge. Probe identifiers resolve in reference-design planning §4. U-xx issues resolve in §6; all rows also inherit the general evidence/development limitation below.

| Capability | Dimensions | Canonical support; conditional extension | Required evaluated output / assessment | Probe; outstanding boundary |
|---|---|---|---|---|
| CAP-001 | C/A/D/V | K11, K01, K25 | Requirement/state/evidence set; identify missing limits and reject or qualify incompatible goals using calculated feasibility | All P cases; U-01/U-07 |
| CAP-002 | C/M/A/D/V | K01; K03 stochastic refinement, K22 realization | Two operational measurands with planes, filtering/time/state and explained difference; distinguish method definition from instrument error | P-MET, X-OBS; U-01/U-08 |
| CAP-003 | C/M/A | K01, K12 | Annotated real/analytic/envelope/sampled map; reconstruct power/phase and detect inversion or sign mistakes | P-COM, X-STATE; U-08 |
| CAP-004 | C/M/A | K02/K03; K04/K09 physical matrix refinement | Stochastic model, justified covariance and finite-record bias/variance; identify Gaussian/fourth-moment and low-SNR limits | P-INT, X-OBS; U-09 |
| CAP-005 | C/M/A/V | K03; add K04 matrix spectra | Weighted phase/correlation calculation with time-domain comparison, uncertainty and unequal-path transfer; reject universal RMS conversion | X-OBS, P-RAD; U-08/U-09 |
| CAP-006 | C/M/A/D/V | K05; add K04 joint inference | Derived/evaluated estimator and applicable bound; exhibit ambiguity/reference freedom and mismatch failure | P-DF, P-COM; U-09/U-10 |
| CAP-007 | C/M/A/D/I/V | K06; add K16 remote, K17/K19 digital | Executed bounded acquisition/tracking design with noise/dynamic/latency tradeoff, slip/recovery evidence and desired-signal transfer | P-COM, P-SEN; U-09 |
| CAP-008 | C/M/A | K04 | Coupled model, rank/conditioning and sensitivity calculation; justify constraint or regularization | P-DF, X-INV; U-09/U-10 |
| CAP-009 | C/M/A/V | K07; add K04 matrix case | Dimensional/limit/convergence checks; covariance uncertainty and nonlinear/ambiguous countercase, separating numerical and physical errors | X-OBS, X-PROD; U-09 |
| CAP-010 | C/M/A/D/V | K08; add K05 inference | Vector field-to-port/sensor model and scalar-limit comparison; quantify a mismatch and identify injection-blind paths | P-ARR, P-SEN; U-03/U-04/U-05 |
| CAP-011 | C/A/D/I/V | K11 quantitative, K12; add K08 apertures, K16 remote | Compared architectures with calculated drive/loading/noise/latency/power/calibration interfaces; resolve incompatibility or preserve missing evidence | P-RAD, X-BLK; U-07 |
| CAP-012 | C/M/A/D/I/V | K12; add K17/K19 sampled realization | Exercised end-to-end frequency/reference plan with phase signs, delay, spurs, alias/image exclusions and reset sensitivity | X-STATE, P-RAD; U-08 |
| CAP-013 | C/M/A/D/V | K13; add K08 geometry, K16 remote | Calculated correlated budget/closure and sensitivity to blocker/correlation/environment/unknown parameter, compared with feasible region | X-BLK, P-ARR; U-09 |
| CAP-014 | C/M/A/D/I/V | K14; add K17 converter, K23 states, K21 calibration | Stage design and executed gain/valid-data policy; evaluated AM/PM/headroom, history-dependent recovery and alternative filter placement | X-BLK, P-RAD; U-07 |
| CAP-015 | C/M/A/D/I/V | K15a, K09 | Evaluated synthesis/loop choice and effective noise/spur/settling envelope with bounded characterization or explicit evidence gaps | P-RAD, X-BLK; U-07/U-09 |
| CAP-016 | C/M/A/D/I/V | K15b; add K16 remote | Calculated endpoint common/differential transfer and implemented/evaluated loading/environment comparison accounting for correlated test reference | P-MET, P-INT; U-02/U-07 |
| CAP-017 | C/A/D/I/V | K23a; add selected K15/K16/K17/K19 | Exercised startup/reset/retune/recovery procedure; measured or supplied end-to-end response and justified exposure/confidence, not framing alone | X-STATE; U-07 |
| CAP-018 | C/M/A/D/I/V | K17; K09 complete-waveform timing | Evaluated converter/driver/clock/range selection for broadband, blocker, low-level coherent and recovery cases; separate data arrival from sample timing | X-BLK, X-STATE; U-07 |
| CAP-019 | C/M/A/D/I/V | K18; add K17/K19 digital, K21b procedure | Estimated/applied I/Q correction; independent desired/conjugate response versus frequency, level and state, including true near-DC signal | P-COM, P-MET; U-10 |
| CAP-020 | C/M/A/D/I/V | K19a; add K20 correction, K16 clock estimates | Executed rate/filter/NCO/resampling chain; quantified phase/delay, alias rejection, noise gain, finite-length residual and reset/sample faults | X-STATE, X-INV; U-07/U-08 |
| CAP-021 | C/A/D/I/V | K19b | Executed precision/load case with overflow/truncation/sample-loss analysis and platform resource/timing evidence | X-STATE; U-07 |
| CAP-022 | C/M/A/D/I/V | K20; add K08 vector, K15 reference, K19 digital | Estimated/aligned complex response; independent band/state residual, coefficient/noise/latency limits and deep-attenuation case before combination | P-ARR, X-INV; U-05/U-10 |
| CAP-023 | C/M/A/D/V | K21a; add K08 field, K20 multichannel, K09 noise | Evaluated calibration equations; indistinguishable parameter sets, omitted-path faults and reference freedoms; distinguish fit from correction feasibility | P-DF, P-SEN; U-05/U-10 |
| CAP-024 | C/M/A/D/I/V | K21b, K22; add selected K18/K19/K20/K23a/K08 | Executed bounded calibration with held-out data/conditions, uncertainty/noise gain/resources and retained wanted signal; reject invalid correction | X-INV, X-PROD; U-10 |
| CAP-025 | C/M/A/D/I/V | K21c; add K08 dynamics, K16 holdover, K24b environment | Evaluated cadence/latency/downtime policy under drift/fades/outage; quantify desired and nuisance response and degraded/recovery limits | P-SEN, P-INT; U-04 |
| CAP-026 | C/A/D/I/V | K24a; add selected K15/K17/K19/K20 | Concrete routing/power/shield/test-access constraints; calculated coupling/supply-to-phase term and interpreted aggressor comparison | X-BLK, P-MET; U-07 |
| CAP-027 | C/A/D/I/V | K24b; add K15 paths, K21 compensation | Calculated environmental sensitivity/mitigation residual and interpreted controlled gradient/cycling/handling evidence with reference controls | P-SEN, X-PROD; U-07 |
| CAP-028 | C/A/D/I/V | K23b; add chosen digital/calibration/distributed methods | Exercised integrated path, partial reset/link loss/drop/stale-coefficient cases; interpret raw data with state/identity/version metadata | X-STATE; U-07 |
| CAP-029 | C/M/A/D/I/V | K07, K03; add relevant physical/system treatments | Constructed/executed bounded model, sensitivity and independent/limit/convergence checks; state physical discrepancy and unsupported extrapolation | P-RAD, X-OBS; U-09 |
| CAP-030 | C/M/A/D/I/V | K22; add K21a calibration, K04/K09 coupled noise, K17/K19 sampled | Executed or critically evaluated measurement; covariance/finite-record uncertainty, floor/fixture/reference sensitivity and independent configuration | P-MET, P-INT; U-01/U-09 |
| CAP-031 | C/A/D/I/V | K25; add appropriate model/budget/subsystem evidence | Evaluated requirement-evidence cases and uncertainty rule, untested corners, exposure/confidence for rare events and bounded compliance conclusion | X-STATE, X-PROD; U-01/U-07 |
| CAP-032 | C/A/D/I/V | K23c; add suspected path/observability/state methods | Executed/evaluated discriminating intervention, exclusions and remaining ambiguity with preserved raw data/configuration | P-DF, P-MET; U-10 |
| CAP-033 | C/M/A/D/I/V | K26a; add K04 joint variation, K24b environment | Calculated joint yield, coefficient range/resolution, fixture/decision uncertainty and test/calibration effort; sensitivity to unsupported distributions | X-PROD; U-07 |
| CAP-034 | C/A/D/I/V | K26b; add K24b aging, K26a interchangeability | Evaluated repair/replacement/update decision with invalidation/requalification and monitoring/regression evidence; no unsupported reliability number | X-PROD, X-STATE; U-07 |
| CAP-035 | C/M/A/D/I/V | A35; add selected realization/calibration | Calculated burst acquisition/ambiguity and waveform residual performance, implemented bounded recovery, evaluated fading/slips and multicarrier contrast | P-COM; U-01/U-04 |
| CAP-036 | C/M/A/D/I/V | A36; add selected chain/tracking/alignment, K16 separate references | Calculated delayed weak-target leakage/clutter pedestal, headroom/recovery and waveform/reset allocation; bounded processing or measurement evidence | P-RAD; U-01/U-02/U-04 |
| CAP-037 | C/M/A/D/I/V | A37; add selected reference/digital/calibration/remote methods | Calculated vector pattern/noise/null sensitivity with correlation and manifold error; implemented bounded weighting/alignment; distinguish electronic/OTA evidence | P-ARR; U-01/U-05 |
| CAP-038 | C/M/A/D/I/V | A38; add tracking/calibration/rejection/remote methods | Calculated ambiguity/bearing sensitivity with multipath/polarization/manifold confounds; executed bounded estimator and preserved unresolved cases | P-DF; U-01/U-04/U-05 |
| CAP-039 | C/M/A/D/I/V | A39; add selected correlator/calibration/reference/distributed methods | Calculated stochastic finite-integration sensitivity and alignment loss; evaluated bounded correlation/calibration and retained reference information | P-INT; U-01/U-02/U-03 |
| CAP-040 | C/M/A/D/I/V | A40; add selected chain/correction/remote methods | Calculated physical sensitivity/range/uncertainty and wanted-signal transfer; evaluated wraps/fades and independent physical-reference evidence | P-SEN; U-01/U-04/U-06 |
| CAP-041 | C/M/A/D/I/V | A41; add chosen analog/digital chain/correction/remote methods | Executed/critically evaluated port measurement, corrected uncertainty and fixture/reference/level discrimination; assessed instrument choice | P-MET; U-01/U-07/U-08 |
| CAP-042 | C/M/A/D/I/V | K10; add K08 propagation, K09 physical noise | Derived/evaluated/realized detection or rejection under matched/mismatched/contaminated observations; quantify retained information and uncertainty | P-COM, P-INT, P-ARR; U-04/U-09 |
| CAP-043 | C/M/A/D/V | K11 quantitative; add K04/K08 spatial, K10 detection, K09 disturbance | Calculated intersecting gain/headroom and information/ambiguity or steering constraints; empty/conditional region and justified restoring change | X-BLK, P-DF, P-ARR; U-01/U-09 |
| CAP-044 | C/M/A/D/V | K09; add K08 incident fields | Calculated source/path spectra and physical coupled covariance; narrow-blocker limit and finite-spectrum contrast; derived LO/clock/filter constraints | X-BLK, P-INT, P-ARR; U-07/U-09 |
| CAP-045 | C/M/A/D/I/V | K16; add K04/K08 geometry, K17/K19 sampled realization | Evaluated offset/delay/asymmetry ambiguity, executed/evaluated bounded alignment/holdover/recovery with separate epoch/rate/RF-phase residuals | P-INT, P-RAD, X-STATE; U-02 |

### Reverse coverage check

This table identifies principal capability consumers of every shared treatment. It is a usefulness/ownership audit, not an exhaustive dependency list. Applications additionally consume the shared treatments through §3.

| Treatment | Principal capability consumers |
|---|---|
| K01 | 002, 003; definitions used throughout |
| K02 | 004, 005, 006, 044 |
| K03 | 004, 005, 012, 030, 039 |
| K04 | 008, 010, 013, 022, 023, 037–039 |
| K05 | 006, 007, 023, 035, 038, 043, 045 |
| K06 | 007, 015, 025, 035, 040, 045 |
| K07 | 009, 029, 030, 031, 033 |
| K08 | 010, 023, 036–040 |
| K09 | 013–016, 018, 037, 039, 044 |
| K10 | 035–039, 042 |
| K11 | 001, 011, 013, 031, 043 |
| K12 | 003, 012, 015–020 |
| K13 | 013, 014–018, 022, 026, 033 |
| K14 | 014, 018, 019, 026 |
| K15 | 015, 016, 017, 022 |
| K16 | 016, 017, 025, 036, 039, 045 |
| K17 | 018, 020, 021, 028 |
| K18 | 019, 024, 035, 041 |
| K19 | 020, 021, 024, 028 |
| K20 | 020, 022, 024, 037, 038 |
| K21 | 023, 024, 025, 033, 034 |
| K22 | 024, 030, 031, 032, 041 |
| K23 | 017, 028, 032, 034 |
| K24 | 026, 027, 033, 034 |
| K25 | 017, 031, 033, 034, 041 |
| K26 | 033, 034 |

A35–A41 each own the corresponding CAP-035–041 application output. No treatment in this decomposition lacks a capability or prerequisite purpose. This does not prove its proposed depth adequate.

## 5. Coverage findings and duplication controls

### Charter/lifecycle cross-check

| Charter responsibility | Support found in this architecture | Remaining challenge |
|---|---|---|
| Need, specification, feasibility and traceability | K01/K11/K25; CAP-001/011/031/043 | Actual operational success criteria missing; retain U-01 |
| Coherence, signals, statistics, estimation, synchronization | K01–K07/K16; CAP-002–009/045 | Bridge rigor, conventions and nonstationary/finite-record applicability |
| Architecture, frequency plan, noise/linearity/dynamic range, budgets | K09/K11–K15/K17; CAP-011–018/043/044 | Source-conditioned calculation and technology evidence, not generic noise figures |
| RF/analog, synthesis and distribution | K12/K14/K15; CAP-012/014–016 | Endpoint/state and loading evidence |
| Conversion, I/Q, recovery and DSP resources | K06/K17–K19/K23; CAP-007/017–021/028 | Keep these conditional for analog implementations |
| Multichannel, calibration and maintenance | K20/K21/K16; CAP-022–025/045 | Observability, feasible correction, retained signal and independent validity |
| PCB, power, EMI, thermal/mechanical/environment | K24 with K09/K13/K14; CAP-026/027 | Quantitative sensitivities and controlled comparisons, not layout checklists |
| Models, uncertainty, measurement and verification | K07/K22/K23c/K25; CAP-009/029–032 | Physical discrepancy and confidence cannot be inferred from software correctness |
| Manufacture, yield, configuration, service | K21/K23/K24/K26; CAP-024/028/033/034 | Joint variation, fixture/test effort and change validity require actual inputs |
| Communications, arrays/DF, radar/sensing, interferometry and instruments | A35–A41, all seven P probes | Shared mathematics must retain separate task consequences |

### Duplication and fragmentation controls

- K01 defines the observable; K03 develops stochastic observation; K22 realizes measurement; A41 designs the reporting instrument. Cross-reference those roles instead of redefining “phase stability” locally.
- K02/K04 define stochastic/matrix tools; K09 constructs physical sources; K13 allocates their consequences. A covariance spreadsheet is not a replacement for source physics.
- K05 owns general inference; K21a calibration freedoms; K20 feasible correction; K21b the executed procedure. Their assessments must demonstrate all four responsibilities separately.
- K06 owns loop and desired-signal transfer; K23 system state causality; K21c continuing validity. An implementation state machine cannot substitute for acquisition mathematics.
- K07 owns general uncertainty/model adequacy; K13 design allocations; K22 measurement uncertainty; K25 evidence decisions; K26 variation/yield. Do not combine their different uncertainty meanings into one unexplained margin.
- K08 owns vector field/sensor inputs; K20 relative electronics; A37 beam consequences; A38 bearing inference; A39 correlation; A40 physical measurand. Matching hardware or similar algebra does not equate application evidence.
- K15 physical reference distribution, K16 remote inference and K23 state validity remain separate. Shared frequency or digital link latency alone does not establish endpoint RF phase.
- K20 owns general inverse/realizability reasoning. K19 supplies digital filter realization and K21b procedural evidence. Include an analog correction route and a prevention/architecture-change route.

The stress-test findings require these distinctions; they are not new claims of measured performance. Reviewers should challenge a boundary with a missing calculation, decision or counterexample rather than simply requesting another subject heading.

## 6. Gaps, source obligations and human decisions

### 6.1 Carry-forward decisions

“Boundary review” means a decision could alter essential treatment content or learning dependencies and must be resolved or explicitly bounded before recommending the affected architecture for a table of contents. “Later input” means a particular engineering conclusion cannot yet be calculated, while a sufficiently bounded treatment specification may still be organized. None of the following is marked accepted by this pass.

| Inventory issue | Architecture disposition and affected treatments | Review / consequence |
|---|---|---|
| U-01 Application inputs | Four provisional anchors and seven independent P audits; use qualitative/symbolic envelopes, not invented limits, waveforms or distributions | Owner/application engineers confirm representative outcomes. Later input: numerical design/verification conclusions; boundary review if a new success metric needs missing reasoning |
| U-02 Distributed depth | K16 requires offset/rate/delay/asymmetry, sample epoch, carrier ambiguity and holdover; K15 physical distribution and K23 transitions remain separate | Time/frequency/application review of minimum sufficiency. Transfer protocol selection later; omission of any committed inference is a boundary blocker |
| U-03 Interferometry depth | K02/K03/K08/K09/K16/A39 include stochastic sensitivity and receiver/reference/geometry calibration; no imaging completeness asserted | Interferometry reviewer must decide whether the proposed bridge supports receiver decisions without reconstructing essential material elsewhere; boundary review |
| U-04 Application processing/propagation | A treatments own explicit residual-to-task and inference mappings; K10 is not an external placeholder for detection or rejection | Application reviewers bound waveform/algorithm/propagation families. Boundary review where omitted processing changes receiver feasibility or allocations |
| U-05 Antenna/polarimetric depth | K08 minimum vector field/manifold, K09 loaded/coupled noise, K20 electronics and A37–A39 application sensitivity are internal | Antenna/array/DF review must challenge scalar limits and injection-blind paths. Detailed radiator design later/external; minimum model adequacy is boundary review |
| U-06 RF/non-RF and sensor scope | A40 uses an RF measurand/reference example; optical/quantum/other non-RF completeness remains excluded | Owner/sensing review confirms the selected sensor bridge. Extension is a separate scope decision, not implied by transferable algebra |
| U-07 Realization/current facts | K11/K14–K19/K23–K26 retain quantified interfaces, physical constraints, production/test effort and service validity; no part/platform/qualification chosen | Hardware/production reviewers assess reasoning sufficiency. Device data, actual fabrication variation and mandated rules are later inputs requiring claim-level evidence |
| U-08 Conventions | K01/K03/K09/K12/K17/K19 identify affected interfaces; standards remain unchanged | Mathematical editor/engineer decides envelope/PSD/L(f)/cross-spectrum/nonstationary conventions before substantive derivations. Organizing obligations does not require silently choosing them |
| U-09 Mathematical depth/evidence | K02–K07/K09/K10/K16/K20 specify internal bridges, exact/approximate distinctions and assessments | Statistical signal-processing/time-frequency/metrology review tests whether the bridges support unfamiliar problems. Boundary review; most result-level research/derivation remains undone |
| U-10 Calibration and signal retention | K05/K20/K21/K22 and A treatments separately require inference, correctability, retained observable and held-out evidence | Calibration/application reviewers test confounding, resources, unobserved paths and correction rejection. Boundary review; no universal calibration algorithm selected |

### 6.2 Development gaps versus architecture omissions

All treatments remain undeveloped as textbook material. Their mathematics, implementation examples and physical applicability evidence must be established later. This is a development backlog, not evidence of a validated model. It becomes an architecture omission when a necessary result has no sufficiently specified home or cannot be reached from the reader baseline.

Specific unresolved adequacy questions from this pass are:

- **Mathematical bridge depth (K02–K07):** can finite-record complex statistics, local information bounds, global ambiguity and feedback analysis be acquired from the stated RF baseline without hidden specialist knowledge? Request reviewer counterproblems before turning these treatments into chapter allocations.
- **Physical model construction (K08–K09):** is a bounded vector/noise-network treatment sufficient for coupled arrays and weak stochastic correlation? The current source notes do not establish the needed equations. Specialist review may require extending the bridge.
- **Correction and signal retention (K18–K21):** can a reader distinguish attenuation/noise gain, nonminimum-phase or latency constraints, rank loss and confounded wanted signals? Keep both an achievable approximation and a rejected correction in future examples.
- **Implementation and lifecycle depth (K19/K23–K26):** eventual examples must contain executed/evaluated realization, state, environmental and joint-production results. Prose-only procedures would fail CAP-I/V despite apparent subject coverage.
- **Anchor representativeness:** four anchors reduce duplicated exposition but do not prove seven applications covered. Preserve P-DF/P-INT/P-SEN as independent reasoning audits, including later transfer exercises that change the model assumptions.

No missing capability is asserted as a new baseline requirement on this evidence. A confirmed gap should be assigned to an existing treatment if it fits; otherwise propose a bounded new treatment or capability revision for owner review. Never silently reduce an inventory outcome to make coverage appear complete.

### 6.3 Source and verification work required during development

Use the existing bibliography/source-note process, not a separate evidence framework. For each consequential result, identify the exact internal derivation or source passage, edition/revision, notation translation, assumptions and claim supported. Distinguish discovery, access, passage examination and support; record failures of access honestly. Illustrative review equations and S1–S9 links are not automatically checked derivations.

Research priorities follow the cross-domain risk: phase-process/observation/performance relations; loaded/coupled physical noise; finite-record correlation and source statistics; estimator/loop applicability; distributed inference; feasible correction; application mappings; then platform/physical/production evidence for chosen examples. Existing NIST/vendor/NRAO examinations retain their narrow original scope. Re-examine primary passages when developing a result rather than cite them for unsupported extensions.

The following is a routing of existing examination records, not a new examination or broader endorsement:

| Existing record | Treatment potentially supported | Exact support boundary retained |
|---|---|---|
| S1 frequency-stability handbook | K03 | Distinct stability measures and noise-dependent ordinary-variance limitations; not the planned coherence/performance derivations |
| S2 uncertainty guidance | K01/K07/K22 | Measurement-process modeling, covariance, first-order limits and disclosed method-defined measurands; not arbitrary nonlinear propagation |
| S3 converter-latency article | K23a | Digital framing versus total converter/analog alignment distinction; no examined JEDEC standard or current part guarantee |
| S4 observing-guide calibration | K21/A39 | Domain-specific separation of instrumental/observing/result calibration and timescales; no universal procedure |
| S5 two-way transfer note | K16 | Reciprocity and directional/equipment-delay limitations; not the complete remote phase/holdover treatment |
| S6 mixer-noise article | K09/K15 | Blocker-generated noise and internal LO-buffer contributions; equation images and current parts not verified |
| S7 aperture-jitter tutorial | K09/K17 | Input-slope dependence and sine-input approximation conditions; not the general correlated broadband calculation |
| S8 array-calibration paper | K09/A37/A39 | Existence of coupled receiver-noise paths; not a verified general network equation, vector manifold or sensitivity result |
| S9 ADC input-noise article | K17 | Input-correlated quantization and conditional dither limits; no universal remedy or part-performance conclusion |

Other mathematical, application and realization obligations have no sufficient claim-level support established by this architecture pass. A source in the inventory bibliography must not be assigned to a new result without examination.

For each future consequential calculation, distinguish algebraic consistency, numerical/software correctness, physical applicability and decision adequacy. Plan independent/limiting-case checks and appropriate empirical comparison; no fixed number of checks or observations proves adequacy. Rare-event confidence and compliance rules require supplied claims and dependence assumptions. Human technical acceptance remains scoped to the evidence, revision and intended use.

### 6.4 Coverage audit procedure and present result

Maintain these plain Markdown tables as treatments change. Compare each capability's dimensions and work product with its support row, trace essential prerequisites to the reader baseline, inspect conditional branches, and reverse-check every treatment for purpose. Then walk all seven P audits and cross-case probes, recording a concrete unexplained calculation or missing decision rather than a coverage score. Recheck canonical ownership whenever shared results move.

Present authorial result: every CAP-001–045 has a support/assessment row; every shared treatment has a capability consumer; all charter responsibilities and inventory U-01–U-10 have dispositions. Paper probes have routes and rejection conditions. This establishes traceability of intended development only. Human adequacy decisions above remain pending; no technical completeness, learner success, validated physics or system compliance is established. Architecture §5 owns the gate for subsequent use.
