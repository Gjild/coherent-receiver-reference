# Visual-needs audit — existing manuscript, 2026-10-30

**Current status (2026-10-30):** approved visual remediation is complete as checked
provisional drafts. All V01–V28 and mandatory state amendments are delivered and
separately reviewed. See [final dispositions](#final-execution-dispositions) and
[execution/acceptance assessment](visual-pedagogy-review.md). Human acceptance
remains pending; stop before K08–K10.

The specifications and “missing/specified/pending” statements below preserve the
original audit boundary, not current production status. Original baseline HEAD
was eb4be1141cded238090adcba957b167a4009ae64 with a clean tree and no commit
authorization. The owner's later resume expressly authorized isolated checkpoints.

## Requirements and method

Audience: experienced RF engineers without assumed specialist probability, matrix, inference or control knowledge (competence inventory §2). Charter, accepted architecture/annotated contents and their qualifications govern coverage; local conventions remain local. Every substantive section was read as a learning argument, including examples, counterexamples and transfer tasks. Nine dimensions assessed: physical paths/planes; complex geometry; time/phase/frequency; spectra/correlation; inference/uncertainty; tradeoffs; calibration/evidence; states/tracking; connected progression. A section need not exercise all dimensions. The specifications below record the dimensions that contribute to its actual argument; no figure quota was used.

Assessment is based on source exposition. Browser/image inspection is a separate, currently incomplete obligation. Existing mathematical source provenance is retained: these proposals visualize manuscript derivations and labeled synthetic models, not newly examined external results or measurements. No new convention or canonical treatment is proposed.

## Section coverage ledger

I = indispensable to the visual learning argument; S = strongly beneficial. References to another chapter's visual mean interpretive cross-reference, not duplicate asset generation. Section rows sharing a visual need not each acquire a figure. Explicit equations/tables remain the reference model.

| Manuscript | Substantive section | Visual disposition |
|---|---|---|
| [phase-comparison](../book/phase-comparison.qmd) | Begin at the physical ports | V01; missing explanatory support. |
| [phase-comparison](../book/phase-comparison.qmd) | Give the voltage a complex representation | V02; missing explanatory support. |
| [phase-comparison](../book/phase-comparison.qmd) | Derive the conversion sign | V03; missing explanatory support. |
| [phase-comparison](../book/phase-comparison.qmd) | Follow one complete measurement | V02, V03; missing explanatory support. |
| [phase-comparison](../book/phase-comparison.qmd) | Change the reference before interpreting a change | V01, V02, V04; missing explanatory support. |
| [phase-comparison](../book/phase-comparison.qmd) | What the comparison can establish | V04, V16; missing explanatory support. |
| [scalar-stochastic-phase](../book/scalar-stochastic-phase.qmd) | From repetitions to a probability model | V05; missing explanatory support. |
| [scalar-stochastic-phase](../book/scalar-stochastic-phase.qmd) | Processes, records and a decision about averaging | V06; missing explanatory support. |
| [scalar-stochastic-phase](../book/scalar-stochastic-phase.qmd) | Complex and angle-valued observations | V07; missing explanatory support. |
| [scalar-stochastic-phase](../book/scalar-stochastic-phase.qmd) | When additive voltage noise becomes phase noise | V08; missing explanatory support. |
| [observation-weighted-coherence](../book/observation-weighted-coherence.qmd) | Define the operator before integrating noise | V09; missing explanatory support. |
| [observation-weighted-coherence](../book/observation-weighted-coherence.qmd) | Increments and complex coherence answer different questions | V10; missing explanatory support. |
| [observation-weighted-coherence](../book/observation-weighted-coherence.qmd) | Shared sources and unequal paths | V11; missing explanatory support. |
| [observation-weighted-coherence](../book/observation-weighted-coherence.qmd) | What a finite record can establish | V12; missing explanatory support. |
| [covariance-quadratic-forms](../book/covariance-quadratic-forms.qmd) | A vector is an ordered set of observables | V13; missing explanatory support. |
| [covariance-quadratic-forms](../book/covariance-quadratic-forms.qmd) | Build covariance from sources rather than choosing correlations | V13; missing explanatory support. |
| [covariance-quadratic-forms](../book/covariance-quadratic-forms.qmd) | Null directions, coordinates and what rank means | V13; missing explanatory support. |
| [covariance-quadratic-forms](../book/covariance-quadratic-forms.qmd) | Invertibility is not reliable inference | V14; missing explanatory support. |
| [phase-delay-inference](../book/phase-delay-inference.qmd) | Specify the observations and unknowns | V15; missing explanatory support. |
| [phase-delay-inference](../book/phase-delay-inference.qmd) | Derive the fit from a likelihood | V15; missing explanatory support. |
| [phase-delay-inference](../book/phase-delay-inference.qmd) | What an information bound actually bounds | V15, V16; missing explanatory support. |
| [phase-delay-inference](../book/phase-delay-inference.qmd) | Follow a consequential calculation | V15; missing explanatory support. |
| [phase-delay-inference](../book/phase-delay-inference.qmd) | A precise local fit can be globally wrong | V16; missing explanatory support. |
| [model-adequacy-uncertainty](../book/model-adequacy-uncertainty.qmd) | Start with a decision and its scales | V17; missing explanatory support. |
| [model-adequacy-uncertainty](../book/model-adequacy-uncertainty.qmd) | Derive sensitivity and retain covariance | V13, V17; missing explanatory support. |
| [model-adequacy-uncertainty](../book/model-adequacy-uncertainty.qmd) | Follow the delay budget through a changed assumption | V17; missing explanatory support. |
| [model-adequacy-uncertainty](../book/model-adequacy-uncertainty.qmd) | A zero derivative does not mean zero uncertainty | V18; missing explanatory support. |
| [model-adequacy-uncertainty](../book/model-adequacy-uncertainty.qmd) | Numerical agreement must be about distinct formulations | V19; missing explanatory support. |
| [model-adequacy-uncertainty](../book/model-adequacy-uncertainty.qmd) | Choose the smallest model that preserves the decision | V16, V21; missing explanatory support. |
| [tracking-signal-retention](../book/tracking-signal-retention.qmd) | Build the loop from its physical actions | V20; missing explanatory support. |
| [tracking-signal-retention](../book/tracking-signal-retention.qmd) | Trace the wanted signal before selecting bandwidth | V21; missing explanatory support. |
| [tracking-signal-retention](../book/tracking-signal-retention.qmd) | Noise bandwidth and a worked tradeoff | V21; missing explanatory support. |
| [tracking-signal-retention](../book/tracking-signal-retention.qmd) | Acquisition and nonlinear failure are separate calculations | V22; missing explanatory support. |
| [relative-phase-stability](../book/relative-phase-stability.qmd) | Start with a decision | V01, V23; missing explanatory support. |
| [relative-phase-stability](../book/relative-phase-stability.qmd) | Representations and the first physical model | V02, V08; missing explanatory support. |
| [relative-phase-stability](../book/relative-phase-stability.qmd) | A short probability and spectral bridge | V11, V13; missing explanatory support. |
| [relative-phase-stability](../book/relative-phase-stability.qmd) | Which statistic did the requirement mean? | V09, V10; missing explanatory support. |
| [relative-phase-stability](../book/relative-phase-stability.qmd) | From phase to an engineering consequence | V10; missing explanatory support. |
| [relative-phase-stability](../book/relative-phase-stability.qmd) | A fair endpoint comparison | V23; missing explanatory support. |
| [relative-phase-stability](../book/relative-phase-stability.qmd) | Calibration, drift and implementation | V24; missing explanatory support. |
| [relative-phase-stability](../book/relative-phase-stability.qmd) | Thermal reference and maintenance allocation | V25; missing explanatory support. |
| [relative-phase-stability](../book/relative-phase-stability.qmd) | Constant uncertainty and time-varying updates | V26; missing explanatory support. |
| [relative-phase-stability](../book/relative-phase-stability.qmd) | Measurement and uncertainty: an executable protocol | V27, V28; missing explanatory support. |
| [relative-phase-stability](../book/relative-phase-stability.qmd) | Check your reasoning and use this as a reference | V10, V11, V24, V27; missing explanatory support. |

The opening motivation of each of the eight technical pages is also assessed: its question is supported by that page's first specified visual; a separate opening illustration would duplicate it. Preface: no technical visual required. References: bibliography navigation, no additional technical graphic required. Publishing pilot: both algebra demonstrations, symbol table and figure/navigation check assessed; no additional scientific graphic needed. Reused reference-plane SVG is appropriate as an inclusion test, not independent teaching evidence. There are no separately configured reader-facing appendices in the current book.

## Visual specifications

Each proposed figure is introduced after its model is defined and before the engineering interpretation/decision it supports. Captions identify synthetic/model status, assumptions and limits; alt text conveys the main relationship. Numeric labels and units must survive normal-width and narrow HTML rendering. Existing canonical mathematical arguments remain unchanged.

### V01 — Indispensable

- Location: `phase-comparison.qmd`, **Begin at the physical ports**.
- Form/content: Paired RF→mixer→Q→extraction→O vector diagram with endpoint LO branches and a marked added 25 ps RF delay.
- Purpose/error prevented: Separate physical planes from coordinate changes; prevent referring an O comparison directly to P.
- Model, labels and assumptions: Chapter 1 ideal mixing and extraction equations; P/L/Q/O, volts, common epoch, lower/upper LO explicitly distinguished. No hardware accuracy implied.
- Independent check: Trace both channel contributions; delay gives −9 degrees at 1 GHz before conversion; upper-side sign reverses.
- Disposition: specified, not implemented or visually inspected.

### V02 — Indispensable

- Location: `phase-comparison.qmd`, **Give the voltage a complex representation**.
- Form/content: Equal-scale I/Q phasors and relative-angle arc; second panel rotates both by a common reference; show conjugation separately.
- Purpose/error prevented: Explain z2 conj(z1), invariance and orientation; avoid an absolute phase interpretation.
- Model, labels and assumptions: z1=0.1 exp(j12°), z2=0.1 exp(j52°) V; product angle 40°, magnitude 0.01 V². Label carrier, epoch, I/Q volts and peak scaling.
- Independent check: Complex multiplication and common rotation preserve the product; conjugation reverses angle.
- Disposition: specified, not implemented or visually inspected.

### V03 — Indispensable

- Location: `phase-comparison.qmd`, **Derive the conversion sign**.
- Form/content: Two signed-frequency strips and contribution arrows for lower/upper LO, with positive-IF extraction.
- Purpose/error prevented: Prevent negating added positive-IF phase when conversion side changes.
- Model, labels and assumptions: fR=1 GHz, fL=990/1010 MHz, fIF=10 MHz; retained signed difference ±10 MHz; output contributions ±Δφ∓Δλ+Δβ.
- Independent check: Evaluate real mixer products and positive-frequency extraction; reproduce 40° and −26°.
- Disposition: specified, not implemented or visually inspected.

### V04 — Indispensable

- Location: `phase-comparison.qmd`, **What the comparison can establish**.
- Form/content: Wrapped samples and two possible continuations, with an amplitude-invalid gap; companion delayed waveform.
- Purpose/error prevented: Prevent unique delay/cycle-count claims and interpolation through fades.
- Model, labels and assumptions: Principal angle (−180°,180°], time in declared illustrative seconds, phase degrees; 179→−179 can mean +2° or −358°. No valid continuation through zero amplitude.
- Independent check: Wrap both candidate trajectories to identical samples; verify physical delay moves waveform right and phase negative.
- Disposition: specified, not implemented or visually inspected.

### V05 — Strongly beneficial

- Location: `scalar-stochastic-phase.qmd`, **From repetitions to a probability model**.
- Form/content: State-conditioned density mixture with within-state and between-state scales.
- Purpose/error prevented: Show quiet records do not establish restart repeatability; zero covariance is not independence.
- Model, labels and assumptions: Equal Gaussian states ±a with variance v, explicitly synthetic; phase rad, density rad⁻¹. Separate discrete X,Y=X² inset if needed.
- Independent check: Normalize density and recover v+a²; exactly sum three-point dependence example.
- Disposition: specified, not implemented or visually inspected.

### V06 — Indispensable

- Location: `scalar-stochastic-phase.qmd`, **Processes, records and a decision about averaging**.
- Form/content: RMS versus sample count for independent, record-constant and mixed errors.
- Purpose/error prevented: Prevent the universal square-root-of-N improvement claim.
- Model, labels and assumptions: N=1…1000; RMS rad on log axes; curves .02/√N, .02, √(.012²/N+.016²); .003 rad target. Ensemble errors, fixed state.
- Independent check: Finite covariance sums independently reproduce N=1,100 and persistent floor.
- Disposition: specified, not implemented or visually inspected.

### V07 — Indispensable

- Location: `scalar-stochastic-phase.qmd`, **Complex and angle-valued observations**.
- Form/content: Complex-plane supports: proper four-point law, jointly Gaussian circular contours, Gaussian-marginal diagonal law; unit-circle mean near ±179°.
- Purpose/error prevented: Prevent propriety implying circularity, Gaussian marginals implying joint Gaussianity, and arithmetic averaging of angles.
- Model, labels and assumptions: Normalized dimensionless quadratures for distribution examples; contours only for declared joint Gaussian model, no coverage interpretation; phase circle degrees.
- Independent check: Compute P for discrete support; rotated support changes; circular vector mean lies near 180°.
- Disposition: specified, not implemented or visually inspected.

### V08 — Indispensable

- Location: `scalar-stochastic-phase.qmd`, **When additive voltage noise becomes phase noise**.
- Form/content: Signal-frame geometry with parallel/perpendicular noise plus exact atan2 and linear phase-error comparison.
- Purpose/error prevented: Expose small-noise condition and fade failure; prevent replacing v/2 by v.
- Model, labels and assumptions: A in V; nparallel/A and nperp/A dimensionless; exact atan2(nperp,A+nparallel); use declared fixed nparallel slices, no invented empirical distribution.
- Independent check: Spot-check signed quadrants and small-error limit; mark undefined origin and breakdown rather than extrapolate.
- Disposition: specified, not implemented or visually inspected.

### V09 — Indispensable

- Location: `observation-weighted-coherence.qmd`, **Define the operator before integrating noise**.
- Form/content: Observation weights and spectral gains; box sinc², increment 4sin² and their product for separated averages.
- Purpose/error prevented: Prevent brick-wall averaging and confusion of absolute, increment and calibrated statistics.
- Model, labels and assumptions: Normalized time t/T, offset fT dimensionless; W for real phase, T=L=1 s illustration; gain dimensionless; two-sided real f, show positive half with symmetry stated.
- Independent check: Transform time weights; DC/zero checks and direct covariance versus spectral integrals with declared convergent PSD.
- Disposition: specified, not implemented or visually inspected.

### V10 — Indispensable

- Location: `observation-weighted-coherence.qmd`, **Increments and complex coherence answer different questions**.
- Form/content: Exponential covariance average RMS and coherent-power curves versus T/tc, with Gaussian and two-point increment contrast.
- Purpose/error prevented: Separate phase-average uncertainty, E|C|² and |E C|²; variance alone does not fix coherence.
- Model, labels and assumptions: Use σ=1 rad for coherent power, R=σ² exp(−|τ|/tc); normalized T/tc; Γ=cos(a) versus exp(−a²/2), signed Γ explicitly, not magnitude.
- Independent check: Pairwise time quadrature refined versus series; T=10 power .456410 and exp(−var average)=.835269; frozen phase limit.
- Disposition: specified, not implemented or visually inspected.

### V11 — Indispensable

- Location: `observation-weighted-coherence.qmd`, **Shared sources and unequal paths**.
- Form/content: One source split through unequal delay responses plus exact differential gain and small-offset approximation.
- Purpose/error prevented: Make common-source correlation visible and show cancellation requires matched responses.
- Model, labels and assumptions: |H2−H1|²=4sin²(π f Δτ); x=f|Δτ| dimensionless; exact bounded by 4; approximation (2πx)²; mark approximation error region.
- Independent check: Compare complex exponentials independently, x=0,.1,.5,1; radar f=1 kHz, Δτ=100 µs gives .381966.
- Disposition: specified, not implemented or visually inspected.

### V12 — Strongly beneficial

- Location: `observation-weighted-coherence.qmd`, **What a finite record can establish**.
- Form/content: Estimator uncertainty and effective sample count for explicitly declared correlation models.
- Purpose/error prevented: Prevent treating N samples as N independent repetitions or using mean-estimator N_eff universally.
- Model, labels and assumptions: N dimensionless; stationary AR(1) ρm=ρ^m for selected positive and negative ρ; mean SD normalized to σ and known-mean variance-estimator SD separately, Gaussian only for fourth moments.
- Independent check: Independent covariance double sums; N=1 and ρ=0 limits; sample-mean subtraction bias identity.
- Disposition: specified, not implemented or visually inspected.

### V13 — Indispensable

- Location: `covariance-quadratic-forms.qmd`, **Build covariance from sources rather than choosing correlations**.
- Form/content: Source-to-channel arrow diagram and covariance ellipse with difference/quiet-weight directions.
- Purpose/error prevented: Retain shared contribution and wanted response; prevent covariance contours being assumed probability regions.
- Model, labels and assumptions: x1=u+e1, x2=2u+e2; independent RMS .02,.01,.03 rad. Equal-scale phase axes rad; ellipse xᵀC⁻¹x=1 is geometry, no probability claim unless Gaussian explicitly introduced.
- Independent check: Source sum versus quadratic form .0014/.0013 rad²; eigenvalues/determinant; rank-one limit along (1,2), null (−2,1).
- Disposition: specified, not implemented or visually inspected.

### V14 — Indispensable

- Location: `covariance-quadratic-forms.qmd`, **Invertibility is not reliable inference**.
- Form/content: Forward response geometry and inverse error versus sensitivity separation.
- Purpose/error prevented: Separate rank, singular values, covariance modes and reliable inference.
- Model, labels and assumptions: A=[[1,1],[1,1+ε]], ε dimensionless; σn=1 mV; RMS b-error V versus |ε| log axes; ε=0 unidentifiable.
- Independent check: Direct difference noise variance versus inverse; reproduce .141421 V at .01 and 1.41421 V at .001; input/output scales declared.
- Disposition: specified, not implemented or visually inspected.

### V15 — Indispensable

- Location: `phase-delay-inference.qmd`, **Follow a consequential calculation**.
- Form/content: Phase-frequency fit with five observations and local precision versus frequency-span scale.
- Purpose/error prevented: Show centered intercept, negative delay slope and the information lever arm.
- Model, labels and assumptions: x=(−2,−1,0,1,2) MHz; a=.3 rad, τ=5 ns, σ=.02 rad; axes MHz/rad and span scale/delay SD ns; error bars individual assumed 1 SD, not fit coverage.
- Independent check: Fit slope independently; Sxx=1e13 Hz²; SD 1.00658 ns and doubled value on half-span.
- Disposition: specified, not implemented or visually inspected.

### V16 — Indispensable

- Location: `phase-delay-inference.qmd`, **A precise local fit can be globally wrong**.
- Form/content: Two unwrapped delay branches with identical wrapped sample phasors; nuisance-delay ridge inset.
- Purpose/error prevented: Prevent a local bound or small residual proving uniqueness or DUT accuracy.
- Model, labels and assumptions: 5 and 1005 ns on 1 MHz grid; phase rad versus RF offset MHz; total τDUT+d fixed; no exact wrapped-noise likelihood claim.
- Independent check: Compare exp(jφ) at all grid points; algebraic invariance under (τDUT+c,d−c).
- Disposition: specified, not implemented or visually inspected.

### V17 — Indispensable

- Location: `model-adequacy-uncertainty.qmd`, **Follow the delay budget through a changed assumption**.
- Form/content: Delay uncertainty versus shared-source temporal correlation and endpoint coupling, with target.
- Purpose/error prevented: Expose timing and coupling assumptions behind cancellation and decision reversal.
- Model, labels and assumptions: Δf=10 MHz; V=.00036 rad²; locals .00004 each; SD ns; ρ of shared draws, not total errors; target .15 ns; separate coupling model .5.
- Independent check: Source-sum propagation; threshold .987741; .142353 and .20751 ns checks; frequency uncertainty separately stated.
- Disposition: specified, not implemented or visually inspected.

### V18 — Indispensable

- Location: `model-adequacy-uncertainty.qmd`, **A zero derivative does not mean zero uncertainty**.
- Form/content: Cosine response near maximum with input scale and first-/second-order versus exact output SD.
- Purpose/error prevented: Show zero slope does not mean zero uncertainty and opposite phase branches coincide.
- Model, labels and assumptions: δ rad, y=cosδ dimensionless; Gaussian σ rad; exact SD=(1−exp(−σ²))/√2; second-order σ²/√2 and zero first-order.
- Independent check: Density quadrature of moments versus analytic expression; σ=.2 gives .0277261; symmetry check.
- Disposition: specified, not implemented or visually inspected.

### V19 — Strongly beneficial

- Location: `model-adequacy-uncertainty.qmd`, **Numerical agreement must be about distinct formulations**.
- Form/content: Direct subtraction versus stable series and independent integral near short observation limit.
- Purpose/error prevented: Distinguish arithmetic failure from model disagreement and physical validation.
- Model, labels and assumptions: x=T/tc logarithmic, dimensionless g; double precision explicitly; x near 1e−8 and larger; no connecting invalid values through log errors.
- Independent check: High-precision decimal arithmetic and converged 2∫(1−v)exp(−xv)dv; g→1.
- Disposition: specified, not implemented or visually inspected.

### V20 — Indispensable

- Location: `tracking-signal-retention.qmd`, **Build the loop from its physical actions**.
- Form/content: Feedback block diagram with incoming wanted+nuisance, detector noise, integrator and separate true/detector residual outputs.
- Purpose/error prevented: Prevent noise sign mistakes and suppressing the wanted measurand unnoticed.
- Model, labels and assumptions: θhat dot=k(θ+n−θhat); phases rad, k s⁻¹, frequency command rad/s; e=θ−θhat; detector=e+n; same input plane/epoch.
- Independent check: Algebraic elimination yields T=k/(s+k), E=s/(s+k), e=Eθ−Tn; step response.
- Disposition: specified, not implemented or visually inspected.

### V21 — Indispensable

- Location: `tracking-signal-retention.qmd`, **Noise bandwidth and a worked tradeoff**.
- Form/content: Wanted T/E magnitudes and RMS-versus-corner tradeoff with feasible region and wanted-signal annotation.
- Purpose/error prevented: Prevent choosing bandwidth from residual noise alone.
- Model, labels and assumptions: f/fc dimensionless; fc Hz, S0=1e−6 rad²/Hz two-sided |f|≤1000 Hz; Ω=π rad/s; true RMS rad; .02 rad target; show desired 1 Hz attenuation.
- Independent check: Finite-band numerical integral versus arctan; reproduce 10/100 Hz table; |T|²+|E|²=1, complex T+E=1.
- Disposition: specified, not implemented or visually inspected.

### V22 — Indispensable

- Location: `tracking-signal-retention.qmd`, **Acquisition and nonlinear failure are separate calculations**.
- Form/content: Nonlinear phase-line at Ω/k below/equal/above one plus holdover bound and latency boundary.
- Purpose/error prevented: Separate linear settling, nonlinear slips, valid acquisition and holdover expiry.
- Model, labels and assumptions: e rad, edot/k dimensionless; stable/unstable equilibria; t seconds for .02+2π .1t; mark .1 rad limit; kL=π/2 is marginal, no practical margin claim.
- Independent check: Derivative equilibrium sign, tangency at equality; .127324 s expiry and Lcrit=1/(4fc); no stochastic capture guarantee.
- Disposition: specified, not implemented or visually inspected.

### V23 — Indispensable

- Location: `relative-phase-stability.qmd`, **A fair endpoint comparison**.
- Form/content: Endpoint architecture panels and integrated variance versus branch-density tradeoff with limit and example envelopes.
- Purpose/error prevented: Explain preference reversal from distribution noise; avoid universal architectural superiority.
- Model, labels and assumptions: Pilot G, Sr=1e−6 rad²/Hz two-sided 1≤|f|≤10000 Hz; delay mismatch 10/100 ns; b per endpoint rad²/Hz, RMS degrees; independent branches only.
- Independent check: Independent integration versus Vcommon+39996b; reproduce table and ~1.71e−8 branch threshold.
- Disposition: specified, not implemented or visually inspected.

### V24 — Indispensable

- Location: `relative-phase-stability.qmd`, **Calibration, drift and implementation**.
- Form/content: Fixed-LO calibration measurement arrangement with training/held-out comb tones, Q-to-O acquisition and fixture slope explicitly shown.
- Purpose/error prevented: Show what calibration can identify and why retuning or fixture unknowns confound delay.
- Model, labels and assumptions: RF MHz, fixed 990 MHz LO, IF 9–11.5 MHz; 32 Msample/s before channelization, 100 ksample/s per tone; P/L/Q/O; distinguish known-stimulus from wanted use.
- Independent check: Trace fixed-LO and retuned slope equations; verify all tone/IF frequencies and held-out exclusion from fit.
- Disposition: specified, not implemented or visually inspected.

### V25 — Indispensable

- Location: `relative-phase-stability.qmd`, **Thermal reference and maintenance allocation**.
- Form/content: Calibration snapshot/application timeline with gated data, correction age sawtooth and bounded drift.
- Purpose/error prevented: Prevent using snapshot center as application time or adding SD to a deterministic bound.
- Model, labels and assumptions: P=2 s, T=.01/.05 s, settle .02 s, after-end latency .1 s; seconds, degrees; drift .216°/s; 0.5° deterministic limit separate from snapshot SD.
- Independent check: Oldest age P+T/2+.1; center bias .216T/4; .45522/.46170°; gated fractions 6.5/8.5%.
- Disposition: specified, not implemented or visually inspected.

### V26 — Indispensable

- Location: `relative-phase-stability.qmd`, **Constant uncertainty and time-varying updates**.
- Form/content: Frozen coefficient versus update staircase and observation mask; randomized-origin triangular covariance and sinc² PSD panel.
- Purpose/error prevented: Prevent static accuracy uncertainty being added to DC-rejecting variance or update noise discarded as DC.
- Model, labels and assumptions: c held between updates; t/P and fP dimensionless; Rc/vc triangle, Sc/(vcP)=sinc²; stationary only for independent errors with uniformly randomized origin.
- Independent check: Zero-sum weights reject a constant; Fourier triangle transform and integrated PSD area vc; cross-covariances retained for general case.
- Disposition: specified, not implemented or visually inspected.

### V27 — Indispensable

- Location: `relative-phase-stability.qmd`, **Measurement and uncertainty: an executable protocol**.
- Form/content: Measurement-chain/swap diagram including source, fixtures, receivers, acquisition and independent Q comparison.
- Purpose/error prevented: Prevent agreement of correlated measurements being treated as absolute truth; expose swap invariants.
- Model, labels and assumptions: Use eq-measurement at fixed channel labels; independent comparison has its own acquisition/instrument terms and shared δQ; no blanket independence.
- Independent check: Term-by-term sign table for input fixture swap and acquisition swap; m−m′ removes δQ, retains instrument difference.
- Disposition: specified, not implemented or visually inspected.

### V28 — Strongly beneficial

- Location: `relative-phase-stability.qmd`, **Measurement and uncertainty: an executable protocol**.
- Form/content: Guarded-decision intervals relative to a scalar upper limit.
- Purpose/error prevented: Separate guaranteed bound from SD and show inconclusive overlap.
- Model, labels and assumptions: Generic scalar y with declared units; bound U, limit L; no assumed coverage or compliance evidence.
- Independent check: Boundary equalities yhat+U=L and yhat−U=L; inequalities agree with text.
- Disposition: specified, not implemented or visually inspected.

## Existing assets and integration findings

- `relative-phase-reference-planes.svg`: shows common RF stimulus/fixture and LO alternatives, but omits Q and acquisition. Caption/prose acknowledge omission. V24 should expose the omitted measurement chain; assess whether the old diagram can be clarified or replaced rather than retain redundant versions. Actual legibility/sign review pending image access.
- `relative-phase-state-sequence.svg`: useful gate progression, but invalidation is only a text line. Inspect arrows/text and consider a return/gate path if needed. Do not imply settling is a fixed hardware guarantee. Retain if rendered inspection supports adequacy; no separate repeated state diagram required in Chapter 7.
- Publishing demonstration repeats the first SVG intentionally. Preserve its typography-test purpose; it does not count as another technical explanation.
- `phase_transfer_demo.py`: relevant exact/approximate delay plot currently depends on unavailable NumPy/Matplotlib and writes ignored output outside the reading path. Incorporate its scientific argument through V11 with a reproducible available implementation; do not count the unrendered example as a delivered book figure.
- No scientific photograph is needed for these idealized models. Decorative artwork is unnecessary.

## Connected progression and optional improvements

The visual sequence must progress from reference/phasor orientation to random observations, temporal weighting, coupled sources, inferential ambiguity, adequacy and signal-preserving tracking, then reuse those ideas in calibration and measurement. Cross-reference V09/V11/V13/V16 from the pilot rather than replicate generic derivations. Retain pilot-specific V23–V27 because they add architecture/measurement interfaces. Tables and prose adequately carry definitions, likelihood differentiation, regularity qualifications, source provenance and transfer instructions when connected to these figures; independent visuals for each algebraic step are unnecessary.

Optional after the specified set: animated phasor rotation, additional distribution families, alternative color styling, hardware photographs and PDF-specific layout. None replaces a missing specified explanation. Reader trials and specialist/physical validation remain separate evidence obligations.

## Gate and execution status

No illustration production until audit review and a working actual-image inspection route. Acceptance requires every indispensable item, justified dispositions of strongly beneficial items, numerical checks, technical/pedagogical separate-context review, standalone and in-HTML image inspection and correction reassessment. Image inspection failure remains blocking; parsing SVG or generating HTML cannot substitute.

## Proposed future guidance (pending remediation evidence)

Add to the existing technical-unit template: identify visual reasoning needs alongside the observable/model; specify purpose, prevented error, source equation, axes/planes, assumptions and independent checks; justify no-figure decisions where consequential.

Add to the existing technical-review template: record actual asset and rendered-page image inspection, viewport/output revision, technical and pedagogical findings separately, inaccessible images, numerical alternatives and correction reassessment.

Add a short gate to technical-authoring and verification standards: no indispensable visual gap, interpreted figures, independently checked quantitative relationships, accessible labels/captions/alt text, rendered inspection and distinct human acceptance. No figure quota. These are proposals, not evidence-based final lessons until remediation is completed.

## Required amendments from separate-context audit review

These amendments supersede narrower specifications above. They are specified corrections, not delivered images; independent reassessment remains pending.

1. **V09 (indispensable):** Add signal→complex filter→angle versus angle→phase filter. Show normalized real/imaginary impulse-response contributions to phase and amplitude, H0≠0, small perturbations and valid amplitude. Include AM-only conversion: discrete h=(1+j,−j), H0=1, A=1, α=(.1,0), φ=0 gives output 1.1+j.1, exact phase atan2(.1,1.1)=.0906599 rad and first-order .1 rad; halve perturbation to check quadratic remainder. This panel prevents unjustified use of |H|²Sφ on IQ filters.
2. **V10 (indispensable):** Explicitly plot E|C|², |E C|²=exp(−σ²), and rejected exp(−var phase-average) separately from phase RMS. At σ=1 and T/tc=10 the dimensionless values are .456410128, .367879441, .835269453; phase-average variance .180000908 rad². Preserve frozen-phase and signed two-point/Gaussian coherence comparisons.
3. **V24 (indispensable):** Add pilot-specific asymmetric fit with training and excluded held-out points, f0=1000 MHz and mean frequency 1000.166667 MHz; b0=.3 versus mean-phase .297905605 rad. Scalar carrier correction leaves 2 ns slope, +.0125664/−.0188496 rad at 999/1001.5 MHz. Cross-reference the general fit/ambiguity figures.
4. **V05 and V12 upgraded to indispensable:** Add paired synthetic records over repetitions with equal ensemble marginal variance for independent and random-constant errors. Mark record means versus ensemble mean and connect covariance sums to V06. V12 uses stationary Gaussian AR(1), ρ=−.7,0,+.7, unit marginal variance, N=1…100; compare mean SD and known-zero-mean variance-estimator SD with covariance double sums. Finite traces demonstrate neither stationarity nor ergodicity.
5. **V09/V10 (indispensable):** Include exponential covariance/Lorentzian PSD correspondence and increment comparison D(L)=2σ²(1−exp(−L/tc)) versus random-walk D(L)=qL. Choose σ=1 rad, tc=1 s, q=2 rad²/s to match initial slopes; axes L seconds and D rad². State random-walk absolute variance depends on start epoch; no stationary absolute-PSD substitution or arbitrary cutoff is justified.
6. **Existing state-sequence remediation is indispensable:** Explicit invalid-data gate and routes for failed settling/checks, amplitude/reference loss, changed state and stale calibration; require reacquisition, resolved branch, applicable calibration and independent validity evidence before use. Held-out fit checking does not independently test acquisition/instrument error. Coordinate this figure with V22 rather than duplicate it.
7. **V13 (indispensable):** Show projected support half-width sqrt(wᵀCw) for the unit covariance ellipse; a radial intersection is not that projection. State coefficient norms for (−1,1) and (−2,1) and keep their observables distinct. Rank-one covariance is a source-parameterized line, never an inverse ellipse; no automatic probability interpretation.
8. **V21 (indispensable):** Replace generic feasible shading by “meets illustrative true-residual RMS criterion,” approximately fc=28.27…134.33 Hz. No joint wanted-signal feasibility claim without a retention requirement. At fc=100 Hz a 1 Hz wanted phase has residual transfer about .01.
9. **Localized manuscript correction:** Pilot unrestricted arctangent replaced with atan2, with zero amplitude excluded. Independent check n′=−2A gives π rather than zero; nearby small-noise linearization remains unchanged. Correction awaits independent reassessment.

Revised priorities: 26 indispensable specifications and two strongly beneficial (V19, V28), plus mandatory remediation of the existing state diagram. These are needs/specifications, not a required figure count; panels and cross-references may consolidate them. Optional: improper-noise ellipse tied to signal orientation and explicit output-noise injection nodes in the endpoint architecture drawing. No new canonical treatment is authorized.


## Execution disposition — Chapters 4–6, 2026-10-30

The specifications above are the historical baseline, not a current production
status. V13–V19 are implemented in eight integrated figures. Fresh independent
scientific/graphical/pedagogical review and correction reassessment are complete;
inline mathematics and the projection derivation were corrected. Current full
page/figure pixels, hashes and findings are recorded in
[the execution record](visual-pedagogy-review.md). These chapters are checked
provisional visual drafts with optional polish and human acceptance pending.
V20–V28 and state-diagram remediation remain to be completed.


## Execution disposition — Chapter 7 and state gates, 2026-10-30

V20–V22 and mandatory existing-state-diagram remediation are implemented and
separately reviewed as checked provisional visual drafts. Author and reviewer
inspected actual standalone and integrated pixels; command/axis clarifications
passed fresh focused reassessment. [Execution/evidence](visual-pedagogy-review.md).
The pilot state integration is checked; its remaining V23–V28 work is next.
No completed Chapter 1–3 review was repeated. Human acceptance remains pending.


## Final execution dispositions

The original section ledger is closed by the following delivered mappings and
interpretive cross-links. Existing completed Chapters 1–3 reviews were preserved,
not repeated. Chapters 4–6 now have completed fresh review/correction/reassessment;
Chapter 7/state and pilot/connections have completed fresh image/mathematical review.
Earlier pending-review and usage-limit records remain historical evidence.

| Need | Delivered SVG asset(s), in book/figures | Final disposition |
|---|---|---|
| V01 | comparison-planes | Delivered/reviewed in Chapter 1; pilot connects and clarifies its own P/L/Q/O chain. |
| V02 | relative-phasors | Delivered/reviewed; geometry and reference rotation retained. |
| V03 | conversion-orientation | Delivered/reviewed; both conversion signs explicit. |
| V04 | phase-wrapping, phase-validity | Delivered/reviewed; ambiguity and amplitude-invalid gap separated. |
| V05 | ensemble-records | Delivered/reviewed with required mixture and paired repetition/record bridge. |
| V06 | averaging-floor | Delivered/reviewed; covariance-dependent improvement and persistent floor. |
| V07 | complex-distributions, circular-mean | Delivered/reviewed; propriety/circularity/joint Gaussianity and circular mean distinguished. |
| V08 | noise-phase | Delivered/reviewed; signal-frame quadratures, exact atan2 and local limit. |
| V09 | complex-filter-order, observation-weights, observation-gains | Delivered/reviewed with AM-to-PM counterexample and finite-remainder corrections/reassessment. |
| V10 | coherence-observables, covariance-increments | Delivered/reviewed with all three coherent quantities, Lorentzian correspondence and stationary/random-walk distinction. |
| V11 | shared-delay | Delivered/reviewed; common-source paths, exact gain and approximation failure. |
| V12 | finite-record-uncertainty | Delivered/reviewed with both AR(1) correlation signs and different mean/variance estimators. |
| V13 | source-covariance, covariance-projections | Delivered/reviewed; support versus radial intersection, coefficient norms and singular mapped-ball case derived and reassessed. |
| V14 | inverse-conditioning | Delivered/reviewed; response rank versus reliable inference. |
| V15 | delay-fit-precision | Delivered/reviewed; local precision, negative slope and frequency lever arm. |
| V16 | delay-ambiguity | Delivered/reviewed; wrapped branches; prose retains nuisance-delay confounding and transfer links. |
| V17 | uncertainty-sensitivity | Delivered/reviewed; observation correlation and endpoint coupling varied separately. |
| V18 | nonlinear-uncertainty | Delivered/reviewed; zero slope, finite uncertainty and opposite branches. |
| V19 (strongly beneficial) | numerical-cancellation | Delivered/reviewed; arithmetic versus model error and independent integral. |
| V20 | tracking-loop | Delivered/reviewed; actuator relation and command units clarified/reassessed. |
| V21 | tracking-transfer-budget | Delivered/reviewed; wanted transfer versus true-residual RMS criterion; no invented retention requirement. |
| V22 | tracking-nonlinear-holdover | Delivered/reviewed; equilibria, holdover and marginal latency distinct. |
| V23 | endpoint-architecture-budget | Delivered/reviewed; per-endpoint density, two-sided accounting, conditional preference and branch allocation. |
| V24 | calibration-fixed-lo, calibration-delay-fit | Delivered/reviewed with mandatory asymmetric training/held-out fit, carrier/mean intercept and residual-delay distinction. |
| V25 | calibration-maintenance | Delivered/reviewed; gate, snapshot/application epochs, held age and deterministic bound separate from SD. |
| V26 | correction-updates | Delivered/reviewed; constant rejection, changing coefficients, two-time covariance and restricted randomized-origin spectrum. |
| V27 | measurement-swaps | Delivered/reviewed; physical independent Q acquisition, conditional signs and shared-error ambiguity. |
| V28 (strongly beneficial) | guarded-decisions | Delivered/reviewed; bound versus SD, equality rules and inconclusive overlap. |
| Mandatory existing state remediation | relative-phase-state-sequence | Remediated/reviewed/reassessed; explicit invalidation bus and requalification before wanted-data use. Reused by cross-reference from Chapter 7. |
| Existing reference-plane clarification | relative-phase-reference-planes | Remediated/reviewed; Q and acquisition drawn, labels repaired. Publishing demonstration intentionally reuses the same asset. |

All 26 indispensable and two strongly beneficial specifications are satisfied in
the existing manuscript scope. Thirty-seven distinct assets support this ledger;
asset count is not the adequacy criterion. Definitions, derivations, likelihood
steps, assumptions and source provenance continue to use prose/equations/tables;
no separate decorative or algebra-per-step figure is needed. Pilot cross-links
apply the foundation figures and retain pilot-specific architecture, calibration
and measurement interfaces. Preface, references and publishing demonstration retain
their assessed roles. No reader-facing appendix has been added.

No unresolved indispensable visual gap or consequential scientific/graphical
finding remains. Optional log/tick/notation polish, narrow-view label enlargement,
richer standalone descriptions and publishing reference-word cleanup are recorded
in the execution record. PDF, offline math, full responsive/assistive-technology
behavior, specialist/reader evidence and hardware validation remain separate
limitations. The author recommends bounded HTML visual acceptance; the owner
retains the decision. K08–K10 remain outside the completed milestone.
