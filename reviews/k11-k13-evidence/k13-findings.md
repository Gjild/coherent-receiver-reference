I found **no demonstrated consequential mathematical or graphical error in the K13 allocation and revised closure**, under their stated assumptions. The 1 ms failing example and conditional 2 ms restoration are supported by independent calculations. This finding does not establish physical applicability, reader effectiveness, or human acceptance.

All **218 files listed in SHA256SUMS verified**, with no unlisted packet files apart from the manifest itself. I read requirements, relevant accepted scope/CAP-013, manuscript and source passages before examining implementation; consequential calculations preceded author code/tests. Exposure comprised packet requirements and standards, Chapter 12, Chapter 11, relevant prerequisite passages, supplied source notes/anchors, rendered HTML/SVGs, calculation code, tests, and all 21 PNGs. Original source PDFs were unavailable and were not examined. No external sources, connectors, delegation, edits, author conversation, prior reviews or history were used.

The common-source construction withstands the principal challenge. Dividing each blocker’s plane-wave response by its wanted response gives
\(v_i=\exp[j2\pi x_i(f_Bu_B-f_Ru)/c]\).
The stated direction is independently recovered as **47.1965135°**, producing phases \(0,-\pi/8,-\pi\). One proper complex source supplies two shared real quadratures; it is not three independent channel generators. Consequently, the long-comparison variance is \((1-q\cos\psi_l)/\rho\), reaching \((1+q)/\rho\) at this geometry while marginal powers remain fixed. The factor \(1/2\) in Equation 12.3 follows from proper-noise quadrature normalization.

These conclusions require the declared equal relative electronic responses, matched LO-noise transfer and selected-band properness. They do not follow from equal noise powers or identical connector spectra alone. Improper noise requires pseudocovariance as well as covariance; unequal distribution paths require frequency-dependent transfer. [§12.3.1](/tmp/k1113/k13-input/book/feasibility-architecture-allocations.qmd:461) states these restrictions. Holding total density fixed while varying its partition is a legitimate sensitivity experiment, but does not predict what changing a physical blocker or device alone will do.

Chapter 11’s restored transfer gives RF-delay sensitivity \(-2\pi f_R\) and LO-delay sensitivity \(+2\pi f_L\). Applying these independently reproduces
\(h_U=[-0.006220353,+0.006785840]\) and
\(h_V=[-0.009424778,-0.018849556]\) rad/K.
Thus ambient covariance between comparisons is negative, while the RF-only contribution is positive. Summing the two signed ambient paths before squaring gives **0.0001841905 rad²** on the long comparison; incorrectly assigning independent temperatures gives **0.0040499172 rad²**. The cancellation and misleading alternatives are physically and mathematically coherent.

The calibration ensemble is also stated correctly: uncertain intercepts remain fixed between calibrations, and the shared reference contributes to both differences. Neither calibration uncertainty nor record-constant temperature departure acquires independent-sample averaging gain. The predictive uncertainty interpretation explicitly differs from repeated-record variance with those quantities held fixed.

The complete noise floor is allocated once. I recover \(N_0=6.3095734\times10^{-19}\) W/Hz, \(k_B290=4.0038821\times10^{-21}\) W/Hz, and the allocated effective two-sided phase density **\(1.2619147\times10^{-11}\) rad²/Hz**. The synthetic partition is nonnegative across the plotted \(q\) range. Its normalization agrees with Chapter 9’s power-envelope convention; no unsupported universal conversion to \(L(f)\) is needed. Reusing an unblocked measured floor would require rebuilding this interface.

Equation 12.1 has the appropriate conjugate-transpose ordering and observation weighting. Independent perturbation/quadrature calculations reproduce the nonzero-offset cosine phase weight. Additive voltage noise and complete-waveform timing require different transfers, as the text explains. Rechecking Chapter 11’s finite-record bounds for both record lengths gives blocker transfer below **\(1.18\times10^{-10}\)** and wanted mirror/main below **\(3.304\times10^{-6}\)**.

The contamination treatment is sound within the linear-phase approximation. Dividing proper noise by each perturbed complex mean changes amplitude and projection; the triangle inequality bounds the common contribution by
\(q(\sum|w_i|)^2/(2\rho_{\min})\).
This is a bound for each task row, not a replacement covariance matrix simultaneously attained by every row.

Independent numerical results reproduce the consequential decisions:

| Quantity | Independent result |
|---|---:|
| 1 ms budget sum | 0.0123743752 rad² |
| Allowed phase variance | 0.0120258137 rad² |
| 1 ms angular envelope | 0.507194° |
| Explicit geometry, clean means | 0.506648° |
| Incorrect omission of \(V\) | 0.477180° |
| 2 ms angular envelope | 0.398732° |
| Sufficient \(\sigma_V\) limits, 1/2 ms | 1.737522 / 4.040030 K |

Crucially, [§12.3.3](/tmp/k1113/k13-input/book/feasibility-architecture-allocations.qmd:595) distinguishes failure to close a sufficient envelope from the separate constructive failing example. The budget table’s units, entries and comparison are correct.

The branch calculation retains the shared-reference cross term, thermal covariance, calibration and deterministic reductions of decision margins. I obtain approximate envelopes **\(1.81308\times10^{-4}\)** and **\(5.47621\times10^{-7}\)**. These remain Gaussian phase-tail approximations, not certified rare-event probabilities. An independent 600,000-trial nonlinear surrogate gives angular SDs approximately **0.5088°/0.3999°**, consistent with the manuscript’s numerical check within sampling variation. All 16 supplied tests subsequently passed as supporting implementation evidence.

The restoration and changed-assumption exercises remain consistent with initial feasibility. At \(q=0.2\), 2 ms gives **0.424759°**, with thermal allowance reduced to **3.663345 K**. Independent LO bands recover independent channel covariance at fixed marginals. Removing coarse information cannot be repaired by gain; narrowing the direction-cosine interval consumes prior information. The 2 W exercise correctly leaves **0.4667 W/channel**.

The 2 ms record gives 2.6 ms reporting time and 0.04° excursion, while tightening independent LO offset to **0.069444 Hz** and relative sampling-rate error to **\(3.47222\times10^{-9}\)**. Streaming traffic remains unchanged. The remaining midpoint/dynamic bias, reset mixtures, field-manifold errors, uncertain coefficients, device loading, power and processing feasibility are explicitly unresolved.

I successfully opened and inspected **all 21 actual PNGs**: three standalone assets, the complete page, and crops 00–16. The full-page image establishes continuity but is too reduced for equation reading; overlapping crops supply readable detail. Equations 12.1–12.4, budget rows, captions, signs, arrows and new figures are legible without consequential clipping. Independently decoded quantitative SVG coordinates agree with the derived curves within coordinate rounding. Canonical ownership remains coherent: Chapter 12 assembles allocations from Chapters 4, 6, 9 and 11.

**Optional polish:**

- At [line 662](/tmp/k1113/k13-input/book/feasibility-architecture-allocations.qmd:662), call 4.62 Gbit/s *framed traffic*; raw traffic is 4.2 Gbit/s.
- Identify the nonlinear check as a reduced-SNR surrogate rather than a realization of particular contamination phasors.
- The visible sidebar/next-page navigation labels the publishing demonstration “Chapter 13,” whereas the accepted TOC assigns calibration/metrology there. Distinguish scaffold navigation from canonical numbering.
- Showing the proposed 1% noise-variance sensitivity numerically would help: the 1 ms thermal threshold falls to approximately **1.64970 K**.