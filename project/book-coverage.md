# Book Coverage, Dependencies and Design Staging

**Status:** provisionally accepted by the project owner on 2026-10-29 for guiding textbook development under [ADR-0004](decisions/ADR-0004-provisional-book-architecture-acceptance.md), following external AI-assisted review and subject to its four review qualifications. The audit remains authorial planning evidence, not independent technical review or demonstrated textbook adequacy. Locations refer to the [annotated contents](annotated-toc.md). [Accepted coverage](technical-coverage.md) owns definitions, depth, dependency rationales and capability support; [inventory](competence-inventory.md) owns outcomes and dimensions. These tables are location indexes, not a second knowledge architecture. All accepted F/S/E boundaries remain in force.

## 1. Canonical treatment locations

A canonical home commits to the entire accepted treatment obligation, not just its heading. Shared derivations have one home; refinements below preserve the accepted first-treatment distinctions. Introduction means motivation or a supplied result; application means a distinct engineering consequence. Neither discharges canonical development. No mathematical normalization is chosen here.

| Treatment | Canonical sections | Introduction / refinement / application locations |
|---|---|---|
| K01 | 1.2–1.3 | Seven problems 1.1; measurement realization 13.2; instrumentation 32.1–32.3 |
| K02 | 2.1–2.4 | Scalar first; physical refinement 9.1–9.2; stochastic correlation 30.2 |
| K03 | 3.1–3.4 | Matrix refinement using 4.2; delayed radar 27.2; finite correlation 30.2 |
| K04 | 4.1–4.4 | Matrix spectra revisit after 4; joint inference 5.4; coupled fields/noise 8–9 |
| K05 | 5.1–5.4 | Scalar before joint; calibration freedoms 13.1; application ambiguity 26.1/29.2/31.2 |
| K06 | 7.1–7.4 | Distributed delayed-loop extension 16.3; digital realization 17/19; signal retention 31.3 |
| K07 | 6.1–6.4 | Applied throughout; allocations 12.3, measurement uncertainty 13.3, yield 25.1–25.3 |
| K08 | 8.1–8.4 | Vector/scalar contrast 8.3; beam/bearing/correlation/sensor mappings 28–31 |
| K09 | 9.1–9.4 | Budget assembly 12.3; LO/converter constraints 15.2/17.2; stochastic sensitivity 30.2 |
| K10 | 10.1–10.4 | Analog survival 14.1; waveform/beam/correlation mappings 26–30 |
| K11 first framing | 1.4 | Motivation 1.1; no full feasibility prerequisite for examples |
| K11 quantitative | 12.1–12.2, 12.4 | First use supplied application/technology envelopes; reconcile in 14–20 and 26–32 |
| K12 | 11.1–11.4 | Representations 1.3; converter/DSP refinements 17.1/19.1; state sequencing 21.1–21.2 |
| K13 | 12.3–12.4 | Sources from 9; application mapping initially supplied; final reconciliation 26.4/27.4/28.4/32.4 |
| K14 | 14.1–14.4 | Reciprocal interface with 17.4; gain/valid-data realization 14.3; radar recovery 27.3 |
| K15a | 15.1–15.2 | General loop theory remains 7; effective noise source physics remains 9.3 |
| K15b | 15.3–15.4 | Full physical sensitivities 22; reference test correlation 13/32 |
| K16 | 16.1–16.4 | Continuous inference before sampled-stream realization 19.2; applications 27.3/30.3 |
| K17 | 17.1–17.4 | Ideal sample interface 11.2; complete-waveform timing construction remains 9.4 |
| K18 | 18.1–18.4 | Analog route first; digital realization revisit after 19; full procedure 23.1–23.2 |
| K19a | 19.1–19.2 | Supplied clock estimates from 16 when remote; equalization revisit after 20 |
| K19b | 19.3–19.4 | Digital-resource bridge internal; integrated identity/configuration 21.2 |
| K20 | 20.1–20.4 | Analog/digital alternatives; selected digital correction returns to 19.2; array consequences 28.3 |
| K21a | 13.1 | General identifiability remains 5; field blind paths 8.3; analog instrument route preserved |
| K21b | 23.1–23.2 | Observability/metrology 13; selected correction 18–20; state validity 21 |
| K21c | 23.3–23.4 | Environmental evidence 22; remote holdover 16; signal retention 31.3 |
| K22 | 13.2–13.4 | General uncertainty mathematics remains 6; instrument topology 32; application-specific uncertainty retained |
| K23a | 21.1 | Reset-sensitive elements previewed 11.4/15/17/19; confidence method 24.3 |
| K23b | 21.2–21.3 | Selected realization/configuration interfaces; full calibration dependency conditional, not universal |
| K23c | 21.4 | Metrology from 13; field diagnoses 29.4/32.3; statistical confidence from 24 |
| K24a | 22.1–22.2 | Access/isolation/physical constraints introduced 8/12/14–20; now quantitatively consolidated |
| K24b | 22.3–22.4 | Correction interface may be supplied; maintenance policy uses this evidence in 23.3 |
| K25 | 24.1–24.4 | Evidence questions enter 1.4/13.4; full decision/exposure methods here before applications |
| K26a | 25.1–25.3 | Capacity/access implications enter 12/20/22/23; joint variation and effort developed here |
| K26b | 25.4 | Builds on 21/23/24; anchor change cases 28.4/32.4 |
| A35 | 26.1–26.4 | D-COM motivation 1.1; inferential/physical/realization revisits 5/7/9/12/14/17/19 |
| A36 | 27.1–27.4 | D-RAD motivation 1.1; delayed transfer 3.4, disturbance 9.3, recovery 14.3 |
| A37 | 28.1–28.4 | D-ARR motivation 1.1; physical input 8/9, conditioning 4, correction 20 |
| A38 | 29.1–29.4 | P-DF motivation 1.1; ambiguity 5.3, manifold 8.2; array hardware does not replace inference |
| A39 | 30.1–30.4 | P-INT motivation 1.1; stochastic input/observation 2/3/9, remote reference 16 |
| A40 | 31.1–31.4 | P-SEN motivation 1.1; transduction 8.4, signal retention 7.2/23.3 |
| A41 | 32.1–32.4 | D-MET motivation 1.1; observable 1.2, metrology 13; analog path remains available |

## 2. Capability outcomes and competence dimensions

The following audit targets reproduce the accepted coverage matrix's required evaluated outputs for location checking; they do not redefine inventory outcomes. C/M/A/D/I/V retain the accepted meanings. All listed dimensions need eventual assessed work: explanation for C, development for M, calculation for A, justified decisions for D, bounded executed/evaluated realization for I as permitted by the inventory, and interpreted discriminating evidence for V. The chapter/section annotations and their work/evidence cards jointly carry these commitments. None is executed now. Conditional support, probes and U issues remain in accepted coverage §4/§6 rather than being independently redefined here.

| Capability | Required dimensions | Book sections | Evaluated-output audit target (accepted coverage §4) |
|---|---|---|---|
| CAP-001 | C/A/D/V | 1.2, 1.4; 12.1–12.2, 24.1 | Requirement/state/evidence set; identify missing limits and reject or qualify incompatible goals using calculated feasibility |
| CAP-002 | C/M/A/D/V | 1.2; 3.2, 13.2 | Two operational measurands with planes, filtering/time/state and explained difference; distinguish method definition from instrument error |
| CAP-003 | C/M/A | 1.3, 11.1–11.4 | Annotated real/analytic/envelope/sampled map; reconstruct power/phase and detect inversion or sign mistakes |
| CAP-004 | C/M/A | 2.1–2.4, 3.3; 4.2, 9.2 | Stochastic model, justified covariance and finite-record bias/variance; identify Gaussian/fourth-moment and low-SNR limits |
| CAP-005 | C/M/A/V | 3.1–3.4; 13.3 | Weighted phase/correlation calculation with time-domain comparison, uncertainty and unequal-path transfer; reject universal RMS conversion |
| CAP-006 | C/M/A/D/V | 5.1–5.4 | Derived/evaluated estimator and applicable bound; exhibit ambiguity/reference freedom and mismatch failure |
| CAP-007 | C/M/A/D/I/V | 7.1–7.4; 26.2, 31.3 | Executed bounded acquisition/tracking design with noise/dynamic/latency tradeoff, slip/recovery evidence and desired-signal transfer |
| CAP-008 | C/M/A | 4.1–4.4 | Coupled model, rank/conditioning and sensitivity calculation; justify constraint or regularization |
| CAP-009 | C/M/A/V | 6.1–6.4 | Dimensional/limit/convergence checks; covariance uncertainty and nonlinear/ambiguous countercase, separating numerical and physical errors |
| CAP-010 | C/M/A/D/V | 8.1–8.4; 28.1 | Vector field-to-port/sensor model and scalar-limit comparison; quantify a mismatch and identify injection-blind paths |
| CAP-011 | C/A/D/I/V | 12.1–12.2, 12.4; 14.4, 17.4 | Compared architectures with calculated drive/loading/noise/latency/power/calibration interfaces; resolve incompatibility or preserve missing evidence |
| CAP-012 | C/M/A/D/I/V | 11.1–11.4; 19.1, 21.1 | Exercised end-to-end frequency/reference plan with phase signs, delay, spurs, alias/image exclusions and reset sensitivity |
| CAP-013 | C/M/A/D/V | 12.3–12.4 | Calculated correlated budget/closure and sensitivity to blocker/correlation/environment/unknown parameter, compared with feasible region |
| CAP-014 | C/M/A/D/I/V | 14.1–14.4 | Stage design and executed gain/valid-data policy; evaluated AM/PM/headroom, history-dependent recovery and alternative filter placement |
| CAP-015 | C/M/A/D/I/V | 15.1–15.2; 9.3 | Evaluated synthesis/loop choice and effective noise/spur/settling envelope with bounded characterization or explicit evidence gaps |
| CAP-016 | C/M/A/D/I/V | 15.3–15.4; 22.1–22.4 | Calculated endpoint common/differential transfer and implemented/evaluated loading/environment comparison accounting for correlated test reference |
| CAP-017 | C/A/D/I/V | 21.1–21.3; 24.3 | Exercised startup/reset/retune/recovery procedure; measured or supplied end-to-end response and justified exposure/confidence, not framing alone |
| CAP-018 | C/M/A/D/I/V | 17.1–17.4 | Evaluated converter/driver/clock/range selection for broadband, blocker, low-level coherent and recovery cases; separate data arrival from sample timing |
| CAP-019 | C/M/A/D/I/V | 18.1–18.4; 23.2 | Estimated/applied I/Q correction; independent desired/conjugate response versus frequency, level and state, including true near-DC signal |
| CAP-020 | C/M/A/D/I/V | 19.1–19.2; 20.2–20.3, 21.3 | Executed rate/filter/NCO/resampling chain; quantified phase/delay, alias rejection, noise gain, finite-length residual and reset/sample faults |
| CAP-021 | C/A/D/I/V | 19.3–19.4 | Executed precision/load case with overflow/truncation/sample-loss analysis and platform resource/timing evidence |
| CAP-022 | C/M/A/D/I/V | 20.1–20.4; 23.1–23.2 | Estimated/aligned complex response; independent band/state residual, coefficient/noise/latency limits and deep-attenuation case before combination |
| CAP-023 | C/M/A/D/V | 13.1; 8.3–8.4 | Evaluated calibration equations; indistinguishable parameter sets, omitted-path faults and reference freedoms; distinguish fit from correction feasibility |
| CAP-024 | C/M/A/D/I/V | 23.1–23.2; 13.3, 20.2–20.3 | Executed bounded calibration with held-out data/conditions, uncertainty/noise gain/resources and retained wanted signal; reject invalid correction |
| CAP-025 | C/M/A/D/I/V | 23.3–23.4; 31.3 | Evaluated cadence/latency/downtime policy under drift/fades/outage; quantify desired and nuisance response and degraded/recovery limits |
| CAP-026 | C/A/D/I/V | 22.1–22.2; 14.4, 15.4 | Concrete routing/power/shield/test-access constraints; calculated coupling/supply-to-phase term and interpreted aggressor comparison |
| CAP-027 | C/A/D/I/V | 22.3–22.4 | Calculated environmental sensitivity/mitigation residual and interpreted controlled gradient/cycling/handling evidence with reference controls |
| CAP-028 | C/A/D/I/V | 21.2–21.3; 19.4 | Exercised integrated path, partial reset/link loss/drop/stale-coefficient cases; interpret raw data with state/identity/version metadata |
| CAP-029 | C/M/A/D/I/V | 6.3–6.4; 27.2 | Constructed/executed bounded model, sensitivity and independent/limit/convergence checks; state physical discrepancy and unsupported extrapolation |
| CAP-030 | C/M/A/D/I/V | 13.2–13.4; 30.2, 32.3 | Executed or critically evaluated measurement; covariance/finite-record uncertainty, floor/fixture/reference sensitivity and independent configuration |
| CAP-031 | C/A/D/I/V | 24.1–24.4 | Evaluated requirement-evidence cases and uncertainty rule, untested corners, exposure/confidence for rare events and bounded compliance conclusion |
| CAP-032 | C/A/D/I/V | 21.4; 13.4, 29.4 | Executed/evaluated discriminating intervention, exclusions and remaining ambiguity with preserved raw data/configuration |
| CAP-033 | C/M/A/D/I/V | 25.1–25.3; 23.2 | Calculated joint yield, coefficient range/resolution, fixture/decision uncertainty and test/calibration effort; sensitivity to unsupported distributions |
| CAP-034 | C/A/D/I/V | 25.4; 21.2, 23.4 | Evaluated repair/replacement/update decision with invalidation/requalification and monitoring/regression evidence; no unsupported reliability number |
| CAP-035 | C/M/A/D/I/V | 26.1–26.4 | Calculated burst acquisition/ambiguity and waveform residual performance, implemented bounded recovery, evaluated fading/slips and multicarrier contrast |
| CAP-036 | C/M/A/D/I/V | 27.1–27.4 | Calculated delayed weak-target leakage/clutter pedestal, headroom/recovery and waveform/reset allocation; bounded processing or measurement evidence |
| CAP-037 | C/M/A/D/I/V | 28.1–28.4 | Calculated vector pattern/noise/null sensitivity with correlation and manifold error; implemented bounded weighting/alignment; distinguish electronic/OTA evidence |
| CAP-038 | C/M/A/D/I/V | 29.1–29.4 | Calculated ambiguity/bearing sensitivity with multipath/polarization/manifold confounds; executed bounded estimator and preserved unresolved cases |
| CAP-039 | C/M/A/D/I/V | 30.1–30.4 | Calculated stochastic finite-integration sensitivity and alignment loss; evaluated bounded correlation/calibration and retained reference information |
| CAP-040 | C/M/A/D/I/V | 31.1–31.4 | Calculated physical sensitivity/range/uncertainty and wanted-signal transfer; evaluated wraps/fades and independent physical-reference evidence |
| CAP-041 | C/M/A/D/I/V | 32.1–32.4 | Executed/critically evaluated port measurement, corrected uncertainty and fixture/reference/level discrimination; assessed instrument choice |
| CAP-042 | C/M/A/D/I/V | 10.1–10.4; 26.3, 30.2 | Derived/evaluated/realized detection or rejection under matched/mismatched/contaminated observations; quantify retained information and uncertainty |
| CAP-043 | C/M/A/D/V | 12.1–12.2, 12.4 | Calculated intersecting gain/headroom and information/ambiguity or steering constraints; empty/conditional region and justified restoring change |
| CAP-044 | C/M/A/D/V | 9.1–9.4 | Calculated source/path spectra and physical coupled covariance; narrow-blocker limit and finite-spectrum contrast; derived LO/clock/filter constraints |
| CAP-045 | C/M/A/D/I/V | 16.1–16.4; 30.3 | Evaluated offset/delay/asymmetry ambiguity, executed/evaluated bounded alignment/holdover/recovery with separate epoch/rate/RF-phase residuals |

## 3. Dependency and cohesion audit

The following authorial checks apply accepted coverage §3 to the proposed sections. They are reading-route inspections, not automatic proof of sufficient prerequisites. Numerical chapter order alone is insufficient: distinguish entry, later refinement, supplied interfaces and conditional realization.

| Dependency / interaction | Proposed resolution | Authorial finding / remaining challenge |
|---|---|---|
| Scalar probability before covariance matrices | 2 precedes 4; scalar spectra in 3; matrix refinement after 4.2 | No matrix prerequisite is silently imposed on Chapter 2. Finite-record statistics need actual mathematical bridge review. |
| Scalar inference versus joint inference | 5.1–5.3 use 1–2; 5.4 adds 4 | One canonical inference chapter keeps precision and ambiguity together; likelihood bridge remains undeveloped. |
| Observation/inference before loops | 3/5 precede 7; 7.1 supplies control bridge | Digital/remote extensions in 7.4 are explicitly later revisits, not assumptions for ordinary loops. |
| Physical covariance before budget assembly | 4/8/9 precede 12.3 | Source construction stays in 9; 12 propagates and allocates. Applications derive their own performance mappings. |
| Requirements versus feasibility versus budgets | 1.4 frames; 12.1 uses 5/6 plus conditional 8/9/10; 12.2 selects; 12.3 allocates with 11/9 | Same-chapter order resolves first feasibility/closure without claiming subsystem evidence already exists. |
| Application targets before full application chapters | 1 motivates; 12 uses declared supplied mappings; 26–32 derive/reconcile them | Early examples allowed. Unsupported supplied values cannot count as evidenced feasibility. |
| Calibration versus measurement | 13.1 observability from 4/5/6; 13.2–13.4 metrology from 1/3/5/6; executable procedure in 23 | No executed calibration prerequisite for initial metrology; field/correction paths are conditional additions. |
| Analog/converter choice | 14 uses declared drive/load envelopes; 17 refines and reconciles | Reciprocal engineering interaction, not a teaching cycle. Missing part data stays unresolved. |
| Distributed inference versus sampled alignment | 16 continuous equations first; 19.2 consumes timing estimates after sampling foundations | Analog references do not require DSP. Remote delayed-loop extension returns to 7.4 after 16. |
| Quadrature correction before digital realization | 18 develops analog response/estimation; selected digital revisit after 19; procedural validity in 23 | General correction feasibility remains 20. Advanced digital implementations must not be silently assumed in initial 18.3. |
| DSP versus general inverse feasibility | 19 first teaches ordinary filtering/resampling; 20 develops inverse bridge; digital equalization revisit returns to 19.2 | No unconstrained inverse is taught as a prerequisite to its own feasibility analysis. |
| State/calibration/environment interaction | 21 supplies state validity, 22 environmental sensitivities using declared correction interface, 23 procedure/maintenance | Drift policy consumes environment after its own development. State exercises needing calibrated metadata revisit after 23. |
| Metrology versus compliance and production | 13 first; 24 uses evidence/uncertainty; 25 uses allocations/calibration/state/environment and 24 | Earlier transition tests supply observations, not premature rare-event/compliance conclusions. |
| Quantitative application entry | 26–32 follow all shared canonical homes; conditional realization selected explicitly | All accepted A prerequisites have prior homes. This does not imply every shared chapter is compulsory for every realization. |

### Fragmentation, repetition and scope findings

- K02 scalar models, K03 observation, K04 coupled tools, K09 source physics and K13 budgets are separate reasoning responsibilities. Connect them through recurring examples and explicit physical inputs; do not duplicate stochastic theory in each application.
- K05 inference, K21a observability, K20 correctability and K21b procedure retain distinct homes. Chapter 13 places the observable/reference question beside measurement; Chapters 20/23 add realization and validity. Review whether these cross-references are navigable on a first calibration problem.
- K06, K23 and K21c distinguish loop physics, state causality and continued validity. Wanted-signal transfer remains canonical in 7; applications and maintenance derive their specific consequences.
- General uncertainty mathematics remains 6; allocation, measurement, evidence and population decisions remain 12/13/24/25. Local summaries must name which uncertainty is being propagated.
- Chapter 12 has two outputs: feasible architecture/interfaces (12.1–12.2) and allocations/closure (12.3–12.4). Chapter 13 has calibration freedoms (13.1) and measurement realization (13.2–13.4). These groupings resolve adjacent decisions without combining their definitions. If reviewed teaching develops excessive scope, split at those boundaries, not within a derivation.
- Chapter 23 groups procedure then continued validity; Chapter 25 groups population then service. Both need consequential calculations and evaluated evidence, not descriptive summaries. Their four-section plans expose concrete work products, but manageable manuscript length remains untested.
- No chapter lacks a treatment, capability or prerequisite role; no purely lifecycle heading substitutes for a calculation. Part V owns seven distinct application assessments. Analog paths are explicit, avoiding accidental universal ADC/DDC prerequisites.

No new baseline capability or confirmed missing canonical responsibility is asserted by this audit. Unproven development depth remains a risk. A concrete missing result with no reachable home would become an architecture finding requiring a proposed correction and human decision.

## 4. Reference-design staging

These entries reserve eventual work products; no design is solved. D identifiers and briefs remain owned by the accepted reference-design plan. At every revisit expose observable, planes, waveform, observation/time, state, calibration dependence, assumptions and inputs. Each final integrated development collects the earlier work into a connected engineering argument, including rejected alternatives and evidence limitations.

| Stage | D-COM | D-ARR | D-RAD | D-MET |
|---|---|---|---|---|
| Motivate / define | 1.1–1.4 unknown carrier and finite burst | 1.1–1.4 element references and beam goal | 1.1–1.4 delayed transmit reference | 1.1–1.4 DUT/reference ports |
| Statistical / physical reasoning | 2/3/5/7 acquisition, ambiguity, tracking; 9 blocker input | 4/8/9 covariance, manifold and physical noise | 3.4/8/9 delayed transfer, geometry and mixing | 3/5/6 observation, inference and uncertainty |
| Extraction / feasibility | 10/11/12 burst deadline and gain conflict | 10/11/12 wideband steering and physical feasibility | 10/11/12 weak return amid leakage | 11/12/13 sensitivity, reference and test limits |
| Architecture / realization | 14/15/17/18/19 gain, reference, sampling and processing | 15/20 physical matching, correction access, phase/delay alternatives; 17/19 only if sampled | 14/15/17 recovery/reference allocation; 16 for bistatic, 19 if processed digitally | 14/15 analog reference topology; 17–19 only if selected |
| Calibration / state / physical change | 13/21/22/23 I/Q, fade, restart and drift | 13/20/21/22/23 alignment, OTA access and gradients | 13/21/22/23 pulse/chirp states, recovery and calibration | 13/21/22/23 fixtures, warmup, correction and reference change |
| Evidence / population / service | 24/25 acquisition exposure, joint variation, test time | 24/25 pattern evidence, coefficient/test capacity and element replacement | 24/25 delayed/dynamic coverage and production limits | 24/25 uncertainty rule, fixture capacity and service recalibration |
| Integrated development / transfer | 26.4 joins stages; change pilot/fade or waveform | 28.4 joins stages; change scan/band or calibration path | 27.4 joins stages; change delay/reference or waveform state | 32.4 joins stages; change topology, observation or DUT level |

**Input reconciliation:** Chapter 12 supplies declared application mappings and technology envelopes, not unexplained performance claims. Chapters 14–20 replace chain assumptions with derived methods and compatible interfaces; 21–25 reconcile state, correction, environment and evidence constraints; 26–32 establish the task mappings. If a revisit invalidates an earlier choice, show revised feasibility/allocation rather than retain contradictory budgets. Unknown real inputs remain open even at the final illustrative design stage. Reference examples cannot establish product compliance.

### Seven application and five failure-probe routes

| Probe | Book route | Consequential result / tempting conclusion to reject | Discriminating assessment reserved |
|---|---|---|---|
| P-COM | 5/7/9/10/12 → 14/17/19 → 26 | Acquisition/ambiguity and payload feasibility; reject excellent locked-state noise as burst success | Bounded recovery with fades/slips, multicarrier and blocker contrasts |
| P-RAD | 3/8/9/11/12 → 14/17/21 → 27 | Delayed pedestal and usable recovery interval; reject loopback/NF alone | Delayed/dynamic target retention with pulse/sweep state and bistatic contrast |
| P-ARR | 4/8/9/10/12/20 → 13/22/23 → 28 | Vector beam/noise/null sensitivity and correction access; reject boresight scalar matching | Band/scan/polarization and electronic versus OTA evidence, contaminated training |
| P-DF | 4/5/8/9/20 → 13/21 → 29 | Global ambiguity plus local bearing sensitivity; reject precise electronics as unique bearing | Bounded estimator and known-geometry/source interventions with competing multipath hypotheses |
| P-INT | 2/3/4/8/9/10 → 16/19 if remote sampled → 30 | Stochastic finite-integration uncertainty and alignment loss; reject zero expected noise correlation as zero uncertainty | Substantial stochastic example, independent clock/reference evidence, retained astrometric information |
| P-SEN | 5/7/8/13 → 22/23 → 31 | Wanted/nuisance indistinguishability and compensation transfer; reject quiet residual as physical accuracy | Substantial physical inference with independent reference, wraps/fades and nuisance variation |
| P-MET | 1/3/6/11/13 → 24 → 32 | Corrected port result/uncertainty; reject correlated repeatability as traceable accuracy | Level/cable/reference topology changes and interpreted calibrated data |
| X-OBS | 2/3/6 → 10/13/27/30 | Weighted performance/finite-record uncertainty for equal marginal variances; reject universal RMS conversion | Time/spectral comparison and changed record/filter with approximation limits |
| X-BLK | 9/12 → 14/15/17/22 | Reciprocal mixing, waveform timing and intersecting headroom/recovery constraints; reject wanted-tone jitter or digital cancellation alone | Level/history, clock/LO/path and filtering variations with missing guarantees explicit |
| X-INV | 5/13/20 → selected 18/19/23 | Identifiability versus finite-resource inverse residual/noise gain/rank loss; reject perfect inversion from small fit error | Held-out band/state/desired-signal data; achievable approximation and rejected correction |
| X-STATE | 11/15/16/17/19 → 21/24 | Distinct RF phase, epoch, latency and calibration validity; reject framing/common clock/zero failures as proof | End-to-end transition and outage exercises with raw state metadata and justified exposure |
| X-PROD | 12/13/22/23/24 → 25 | Joint yield/correction capacity, test time and service validity; reject individual tolerances/prototype as population | Distribution/correlation/fixture sensitivity, escapes/rejects and replacement requalification |

These paper routes identify planned calculations and evidence, not completed walkthroughs. P-DF/INT/SEN need substantial independent developments despite shared hardware. Specialist scope qualifications in book architecture §4 remain active.

## 5. Review gate and check record

The planning acceptance criteria retained for subsequent development require all treatment obligations and all 45 capability outputs/dimensions to be locatable, prerequisite routes accessible from the declared baseline, conditional paths preserved, and unresolved boundaries visible. Canonical ownership must survive editorial regrouping. An authorial traceability pass is insufficient to establish that a reader can perform the work.

Human decisions remain: suitability of grouping and mathematical bridges; anchor selection; interferometry/vector/polarization/application-processing sufficiency; implementation/production depth; and which bounded issues prevent recommendation for a stated use. All U-01–U-10 remain governed by accepted coverage §6. Planning suitability is now provisionally accepted under [ADR-0004](decisions/ADR-0004-provisional-book-architecture-acceptance.md); these technical adequacy questions remain open.

The later pilot must evaluate actual explanation, consequential calculations, justified architecture/correction decisions and interpretation of evidence, including an unfamiliar changed assumption. Coverage, code execution and repeated AI reasoning cannot alone establish educational adequacy, physical validity or compliance.

Mechanical checks and their actual results are recorded in [current work](current-work.md). There is no new checking framework. Claims about treatment depth, source support and engineering adequacy await development and suitable human review.
