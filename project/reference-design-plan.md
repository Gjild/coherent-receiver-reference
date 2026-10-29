# Reference Designs, Worked-Example Progression and Architecture Stress Tests

**Status:** provisional briefs and authorial paper coverage audits, developed on 2026-10-28; provisionally accepted by the project owner on 2026-10-29 as part of the planning package under [ADR-0003](decisions/ADR-0003-provisional-architecture-acceptance.md), subject to its four review qualifications. No reference design has been solved, implemented, measured, selected as a product or technically accepted. The owner selected provisional anchors, leaving final selection and numerical requirements for human review.

The [architecture](architecture.md) owns progression and readiness. [Technical coverage](technical-coverage.md) owns the K01–K26/A35–A41 treatment definitions and capability support. The [inventory](competence-inventory.md) supplies the seven P cases and contrasting responsibilities. This document develops their use as architecture tests without converting them into product specifications.

## 1. Selection and input rules

Use four provisional anchors to provide substantial recurring design contexts. They cover unknown signal-reference recovery, spatial combination, delayed transmit/receive reference behavior and calibrated port measurement. Shared development is reused; DF, interferometry and physical sensing remain independent audits because their inference and evidence differ from the anchors.

The selection is an editorial hypothesis, not proof of representativeness. Confirm it by asking whether every essential decision has either an anchor development stage or a bounded contrasting case, and whether unfamiliar problems require more than copying one design. If an audit exposes substantial unshared reasoning, enlarge its example treatment or reconsider an anchor rather than suppress the distinction.

Before any numerical design, supply or explicitly label illustrative: operating band and waveform, bandwidth, signal/interference/source statistics, geometry/transduction, observation/update/acquisition time, error/availability limits, operating/reset/environment envelope, allowed calibration downtime, resource/power/cost constraints and verification decision rule. Unknown manufacturer, production and lifetime data remain unknown. A symbolic inequality is useful for exposing a missing input but does not establish a realizable numerical allocation.

## 2. Provisional substantial design anchors

### D-COM — Burst carrier-coherent receiver

- **Purpose and observable:** recover a finite information-bearing burst with initially unknown carrier/timing under specified channel and blocker conditions. Success includes acquisition/ambiguity and payload behavior, not merely a locked-loop residual.
- **Alternatives:** pilot-aided feedforward versus tracking/decision-directed recovery; analog conversion versus sampled-chain placement; preselection/gain alternatives and single-carrier versus multicarrier contrast. No modulation, pilot duration, part or sample rate is selected.
- **Core knowledge:** K01–K07/K09–K15/A35; K17–K19/K23 for a digital realization. Calibration adds K18/K21; measurement/lifecycle adds K22/K25/K26.
- **Eventual work products:** calculated feasible acquisition region and residual-to-waveform performance, justified frequency/gain/reference plan, bounded recovery implementation and independent fade/slip/blocker evidence.
- **Input/review dependency:** communications reviewer supplies representative waveform/pilot/offset/dynamic envelopes and success metric. Protocol/coding completeness is not implied.

### D-ARR — Wideband receiving array with calibration access

- **Purpose and observable:** maintain a specified receiving pattern/noise outcome over frequency, scan, polarization, state and environment. Geometry and acceptance limits remain unset.
- **Alternatives:** analog phase steering, true-delay, digital or hybrid combination; physical matching versus correction before combination; injection versus over-the-air calibration.
- **Core knowledge:** K04/K08–K15/K20–K25/A37; digital realization adds K17/K19 and distributed operation adds K16. K26 covers element replacement and factory adjustment.
- **Eventual work products:** vector manifold and physical noise covariance, beam/null sensitivity and feasible allocations, correction-access decision, bounded weighting/alignment and independent pattern/noise evidence.
- **Input/review dependency:** antenna/array review must confirm the minimum vector/coupled-noise model and external radiator boundary. D-ARR does not subsume DF ambiguity or interferometric sensitivity.

### D-RAD — Coherent pulsed or swept radar receive path

- **Purpose and observable:** preserve a weak delayed return's range/Doppler information amid leakage/clutter across a specified coherent interval. A pulsed/swept family comparison is provisional; no mission waveform or target/clutter envelope is chosen.
- **Alternatives:** shared versus separate references, conversion placement, isolation/filter/gain placement, continuous versus reset waveform states. Bistatic operation is a contrast that adds K16.
- **Core knowledge:** K03/K08–K17/K23–K25/A36; processing adds K19, multichannel operation K20/K21. Include recovery and valid-data intervals rather than only steady noise.
- **Eventual work products:** delay-dependent reference transfer and pedestal calculation, headroom/recovery feasible region, waveform/reset allocation, bounded processing/measurement evidence and lifecycle coverage.
- **Input/review dependency:** radar review bounds waveform, leakage/clutter and required receiver/processing bridge. Comprehensive SAR or mission imaging remains uncommitted under U-04.

### D-MET — Phase-sensitive transfer instrument

- **Purpose and observable:** report phase/delay/relative stability at specified DUT/reference ports, levels, filtering, records and operating states with credible uncertainty. An analog implementation remains a legitimate teaching route.
- **Alternatives:** simultaneous ratio versus switched/reference topology, common versus independent references, fixture corrections and observation methods, analog versus sampled reporting.
- **Core knowledge:** K01/K03/K05/K07/K11–K15/K21a/K22/K25/A41; selected correction/implementation adds K18–K21b/K23/K24. K26 addresses fixture capability and service recalibration.
- **Eventual work products:** operational measurement equation, reference/frequency plan, correction residual and uncertainty, topology/level/fixture discrimination and bounded instrument selection.
- **Input/review dependency:** metrology reviewer and owner choose the instrument family, measurand, reference/standard inputs and decision rule. The existing dual-channel relative-phase pilot remains a later, separate task; this brief does not execute it.

## 3. How substantial examples shape teaching

The following stages revisit the same briefs with increasingly capable models. They are not book chapters or the required engineering execution order. Within each revisit, make assumptions and supplied interfaces visible, then replace them when the relevant method has been developed.

| Revisit | Shared contribution | Application contrast and eventual work product |
|---|---|---|
| Observable and physical question | K01; requirement framing in K11 | Unknown burst carrier, element reference, delayed transmit reference and DUT port comparison; annotated reference/observation map |
| Statistical/inferential calculation | K02–K07; K08/K09 physical inputs | Acquisition ambiguity, spatial covariance, delayed reference noise and measurement uncertainty; derive the relevant observable rather than substitute one phase metric |
| Extraction and feasibility | K10/K11/K12 | Burst deadline, wideband steering, weak return amid leakage and instrument sensitivity; calculate conditional/empty regions and reject a wrong architecture |
| Architecture and allocation | K13–K20 as applicable | Gain/filter/clock choices, correction before combination, reference distribution and analog/digital partition; quantitative interface/budget comparison |
| Realization, calibration and change | K21–K24, selected digital methods | Bounded implementations, held-out correction residuals, startup/retune/fade/drift and aggressor/environment evidence; show desired-signal transfer |
| Evidence and lifecycle | K22/K25/K26 | Task-relevant tests, uncertainty/confidence, joint variation, fixture capability and replacement/requalification; bounded conclusions and remaining claims |

Every anchor eventually needs at least one substantial integrated worked development and contrasting failures, not a string of unrelated mini-examples. The learning value is the visible connection from assumptions to calculations, architecture and evidence. Keep diagrams, calculation inputs and interpreted outputs human-readable without executing software. Later code may reproduce selected calculations but cannot own essential explanation.

P-DF, P-INT and P-SEN below need substantial bounded worked examples of their distinctive inference, even if they do not become complete hardware reference designs. In particular, add a stochastic correlation calculation for P-INT and a desired-signal/nuisance ambiguity calculation for P-SEN; deterministic split-tone or quiet-electronics examples cannot substitute.

Reserve transfer assessments for later authoring that change an assumption: independent rather than shared references, wide rather than narrow bandwidth, stochastic rather than deterministic source, field rather than injection calibration, or a new measurand. A successful transfer assessment requires the reader to change the model and evidence, not just insert different numbers. No exercises are authored here.

## 4. Paper stress-test records

### 4.1 Audit method and result meaning

Each record identifies missing inputs, a reasoning route, a consequential calculation/decision, a misleading alternative and evidence that would distinguish it. The **architecture finding** records whether the required reasoning has a home and what uncertainty remains. These paper checks have been performed by tracing the proposed treatments against the inventory cases. Calculations, realizations, measurements, source verification and learner performance have not been performed. A found route is evidence of planned support, not proof that an unbuilt treatment works.

### P-COM — Unknown carrier in a finite burst

- **Inputs/route:** waveform/pilots, SNR, offsets, dynamics and acquisition deadline; K01 → K02/K03/K05/K06 → K10/K11 → K13/K14/K17/A35, with K19/K23 if digital.
- **Calculation/decision:** intersect finite-observation ambiguity/estimation and acquisition time with payload/buffer deadlines; compare feedforward and tracking choices. In the multicarrier contrast, separate common-phase correction from intercarrier disturbance. Include analog survival before rejection.
- **Wrong choice/evidence:** reject excellent locked-state noise as sufficient when the burst cannot be acquired or clips; require bounded recovery, fade/slip/reacquisition and retained-signal evaluation under supplied conditions.
- **Architecture finding:** A35 must own the waveform performance bridge, K06 acquisition, K11 feasibility and K09/K14 blocker physics. Route specified; waveform-family adequacy remains U-01/U-04/U-09 review.

### P-RAD — Delayed return versus loopback

- **Inputs/route:** waveform/reference access, target delay/motion, leakage/clutter and usable receive interval; K08/K12/K03/K09 → K10/A36 → K11/K13/K14/K17/K23; add K16 for independent references.
- **Calculation/decision:** derive delayed common-source transfer and waveform-weighted leakage/clutter pedestal at the weak target; intersect headroom with saturation/limiter/converter recovery. Compare reference and isolation/filter/gain placements.
- **Wrong choice/evidence:** reject zero-delay loopback or steady noise figure as proof; require delayed/dynamic and transition-sensitive processing/measurement evidence, including target retention after cancellation.
- **Architecture finding:** K03 owns general unequal-path transfer, K09 disturbance generation and A36 radar interpretation. Keeping these separate avoids duplicated phase-noise derivations. Waveform/mission depth remains U-02/U-04.

### P-ARR — Wideband scanned receiving beam

- **Inputs/route:** geometry, scan, band, field/polarization, noise and pattern goals; K04/K08/K09 → K10/K13/K20/A37 → K21/K24/K22/K25.
- **Calculation/decision:** calculate weighted signal/noise and beam/null outcomes with physical covariance and manifold/calibration error; compare phase, delay and digital/hybrid steering, correction access, quantization, loss and resources.
- **Wrong choice/evidence:** reject a boresight tone, independent-noise assumption or correction after destructive combination as sufficient. Compare electronic and over-the-air evidence across band/scan and contaminated-training cases.
- **Architecture finding:** internal vector/noise bridges and pre-combination access are required, while digital realization remains conditional. Scalar-only treatment would fail this audit. Specialist depth remains U-05/U-09/U-10.

### P-DF — Bearing with ambiguous geometry or propagation

- **Inputs/route:** source count/statistics, geometry, polarization, snapshots/SNR and propagation assumptions; K05/K04/K08/K09 → K20/K21a/A38 → K11/K22/K23c.
- **Calculation/decision:** exhibit competing indistinguishable parameter sets, then calculate local sensitivity with manifold uncertainty. Compare geometry, estimator family and additional observation/calibration options.
- **Wrong choice/evidence:** reject precise electronic phase or a local information bound as proof of unique bearing. Use known-source/geometry changes and competing multipath/multiple-source hypotheses; permit an unresolved inference.
- **Architecture finding:** A38 requires independent inference development even where D-ARR supplies hardware. Injection cannot establish a direction-dependent manifold. Algorithm/field-model depth remains U-04/U-05.

### P-INT — Weak stochastic correlation across apertures

- **Inputs/route:** source statistics, bands/records, baselines, geometry and clocks; K02/K03/K04/K08/K09 → K05/K10/A39; add K16 and then K17/K19 for independent sampled clocks.
- **Calculation/decision:** derive finite-integration bias/variance including stochastic source power, colored/coupled noise and effective samples; calculate delay/rate/epoch loss, asymmetry and holdover. Compare common-reference transfer with independent clocks/recorded alignment.
- **Wrong choice/evidence:** reject zero expected uncorrelated-noise correlation as zero measurement uncertainty or a split deterministic tone as stochastic sensitivity validation. Require finite-record stochastic correlation and independent alignment/reference evidence.
- **Architecture finding:** general observation statistics belong to K03, physical covariance to K09, application sensitivity/reference freedoms to A39 and remote inference to K16. Imaging-boundary sufficiency remains U-02/U-03/U-09.

### P-SEN — Measurand versus nuisance reference change

- **Inputs/route:** physical transfer law, reference-path sensitivity, dynamics, ambiguity/range and update limits; K08/K05/K21a/A40 → K06/K21c → K22/K25/K24.
- **Calculation/decision:** determine indistinguishable wanted/nuisance changes and which extra observation resolves them; derive wanted/nuisance transfer through compensation, wrapping/fade recovery and update latency.
- **Wrong choice/evidence:** reject quieter residual phase if tracking removes the measurand. Compare with an independent physical reference and vary nuisance paths; restrict valid operation when inference remains unobservable.
- **Architecture finding:** physical transduction and desired-signal transfer cannot be hidden in a general calibration chapter. K08/K06/K21c and A40 provide separate obligations. Sensor choice and physics boundary remain U-04/U-06/U-10.

### P-MET — Port phase/stability with correlated test references

- **Inputs/route:** measurand, port planes, level, observation method, reference topology, fixture and limit; K01/K03/K12/K21a → K22/A41 → K25; chosen analog/digital correction adds only its necessary branch.
- **Calculation/decision:** calculate fixture/correction/level-dependent residual and covariance-aware uncertainty; compare simultaneous ratio and switched/reference arrangements including drift/settling/headroom.
- **Wrong choice/evidence:** reject repeatability as traceable accuracy or a low shared-reference residual as proof for independent operational references. Vary cable/level/reference and disclose any intentionally changed measurand.
- **Architecture finding:** operational definition, measurement realization and instrument design need distinct homes, with an analog route preserved. Instrument choice, decision rule and conventions remain U-01/U-07/U-08.

### 4.2 Cross-case failure probes

| Probe | Inputs and dependency chain to challenge | Required calculation/decision and misleading alternative | Discriminating evidence / architecture finding |
|---|---|---|---|
| X-OBS Temporal structure and observation | Two processes with equal marginal variance, distinct increments/correlation; chosen window/filter/record. K02 → K03 → K10/A35/A36/A39, K07/K22 for uncertainty | Calculate weighted accumulation/correlation and finite-record uncertainty, compare applicable time/spectral forms; reject a universal RMS phase-to-performance conversion or indefinite averaging | Change weighting/record length and model assumptions. General statistics have a canonical home; application metric cannot be inferred without its own bridge. U-08/U-09 remain |
| X-BLK Complete-waveform survival | Wanted signal plus blocker/leakage spectra, gain/clock/LO/filter and recovery constraints. K09/K11 → K13/K14/K15/K17, K24 aggressor paths | Calculate reciprocal mixing, waveform-sensitive timing, intersecting gain/headroom and usable receive interval; compare prevention/filter/gain placement. Reject wanted-tone jitter, low NF or digital cancellation alone | Evaluate level/history/recovery and path/LO/clock variations, with missing part guarantees explicit. Physical generation precedes allocations; nonlinear model adequacy and current facts remain U-07/U-09 |
| X-INV Identifiability versus correctability | Measured response including deep attenuation, nonminimum-phase/latency limits, true rank loss and unobserved paths. K05/K21a → K20 → selected K18/K19/K21b | Compare feasible approximate correction, noise gain, finite resources and residual against prevention/architecture change; reject perfect inversion from a small fit residual. Do not declare all notches irrecoverable | Held-out band/state/level/desired-signal tests and access before combination. General inverse bridge is explicitly internal; U-10 specialist adequacy still pending |
| X-STATE Reset, sample identity and outage | Applicable power/reset/retune/drop/reference-loss events, device states and failure claim. K12/K15/K16/K17/K19 → K23a/b → K22/K25 | Separate epoch, transport latency, RF phase and calibration validity; evaluate state sequence/reacquisition and exposure/confidence for rare failures. Reject common clock, framing alignment or zero observed failures as deterministic phase proof | Repeat end-to-end transitions with raw sample/state metadata and reference controls under supplied dependence assumptions. Sampled/remote paths conditional; state guarantees and observation duration need evidence |
| X-PROD Prototype versus population/service | Supplied unit/lot/environment variation or bounds, adjustment range, fixture uncertainty, sweep/settling/retest time and changed configuration. K13/K21b/K22/K24/K25 → K26 | Calculate joint yield, coefficient feasibility, test effort, uncertainty-dependent escapes/rejects and requalification after replacement/update. Reject individual tolerances, one prototype or unknown lifetime distributions as production/reliability evidence | Sensitivity to correlations/distributions/fixtures, independent coverage and preserved calibration/configuration records. Quantitative production/service reasoning has an internal home; actual distributions/lifetime facts remain external inputs |

## 5. Findings, review and use limits

The paper audits retain seven distinct application consequences and five cross-case probes. Each has an identified reasoning chain, a calculation/decision, a tempting wrong conclusion and a discriminating evidence obligation. They require the added physical disturbance, feasibility and distributed inference responsibilities (CAP-044/043/045), and the strengthened nonlinear, correction-limit, signal-retention, vector-model and production outcomes to remain substantive.

The anchors provide shared context but do not establish coverage by themselves. P-DF, P-INT and P-SEN reveal where hardware reuse is insufficient; X-OBS and X-INV prevent broad mathematical headings from hiding missing derivations. X-STATE and X-PROD force implementation, evidence and lifecycle consequences into the progression.

Human review must confirm anchor suitability, application success envelopes, mathematical/physical bridge adequacy and the specialist/external boundaries identified in technical coverage §6. Ask reviewers to supply a counterproblem or missing engineering decision. Final selection of anchor configurations and numerical requirements is deferred; these briefs do not impose unapproved product requirements. ADR-0003 provisionally accepts planning use while carrying these boundary questions forward; it does not resolve technical adequacy. Motivating examples may precede full quantitative methods. Actual textbook development, including the later dual-channel relative-phase-stability pilot, must test educational and engineering adequacy.

No reference design, exercise set, chapter, computational model, publishing pilot or technical acceptance is produced by this stage. The [architecture readiness gate](architecture.md) controls subsequent use.
