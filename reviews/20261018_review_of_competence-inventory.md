# Review 1

"Recommendation: defer acceptance of the inventory as the controlling input to the book’s intellectual architecture. It has strong breadth and sensible distinctions, but several essential capabilities remain sufficiently general that a future treatment could satisfy the wording without enabling consequential engineering.



Findings 1–5 are acceptance blockers. Findings 6–11 are significant corrections within the existing structure. “Missing” below generally means a missing explicit engineering outcome, rather than complete absence of the subject.



This is an AI-assisted critical review of the existing draft and selected primary-source passages. It is not independent engineering validation. No files were modified.



1\. P1 — Quantitative feasibility and incompatible requirements lack a clear engineering outcome



Affected: CAP-001, CAP-006, CAP-011, CAP-013, CAP-042; particularly CAP-011 (project/competence-inventory.md:185).



The inventory mentions information bounds, performance bounds and negotiating incompatible goals. It does not explicitly require the reader to establish whether the requested combination of performance is achievable before allocating errors.



An engineer could produce the specified trade study and budget without demonstrating that the available signal energy, bandwidth, observation duration, geometry and reference information support the required estimation performance. Local estimator precision also does not establish acquisition success or global ambiguity resolution—although CAP-006 correctly acknowledges that distinction.



Why it matters: An apparently complete budget can allocate an impossible requirement. Better components cannot resolve missing information, and longer observation may conflict with dynamics, latency or calibration validity.



Correction: Require a feasibility assessment that:



\- Connects information/estimation limits to available signals and observations.

\- Evaluates requirements jointly, including acquisition, ambiguity, tracking dynamics and latency.

\- Separates fundamental limitations, architecture/resource limitations and insufficient evidence.

\- Identifies which requirement or assumption must change when feasibility fails.



Placement: A distinct quantitative-feasibility capability, separated from architecture selection, is justified. Existing CAP-006/011/013 provide its foundations.



Acceptance consequence: Block acceptance until this responsibility has an explicit home.



2\. P1 — Blocker, nonlinear and signal-dependent impairment analysis is named but insufficiently specified



Affected: CAP-004, CAP-012–015, CAP-018, CAP-019, CAP-035, CAP-036; especially CAP-014 (project/competence-inventory.md:209).



Reciprocal mixing, compression, intermodulation and AM-to-PM conversion appear in a list. The entry does not require the calculations that turn these mechanisms into filter, gain, oscillator and converter requirements.



Counterexamples:



\- A low-noise receiver fails beside a strong blocker because LO noise is translated into the wanted band. Ordinary noise-figure characterization does not capture this additional contribution. Analog Devices’ mixer-noise discussion supports this distinction.

\- A clock allocation based on the desired signal alone fails when a large blocker reaches the ADC. Small timing errors act on the slope of the total sampled waveform; the elementary approximation is δ v≈ (dv/dt)δ t. MT-007 develops the slope dependence.

\- Gain switching prevents clipping but introduces a phase transient or invalidates calibration during the observation.



Why it matters: These interactions commonly determine whether weak coherent information survives at all. A generic covariance budget cannot substitute for the correct signal-dependent mechanism.



Correction: Require explicit outcomes for:



\- Deriving blocker-conditioned filtering, gain, headroom and LO-noise requirements.

\- Propagating relevant nonlinear products and amplitude-dependent phase errors.

\- Selecting gain-control behavior, including settling, phase continuity and data validity.

\- Recognizing limits of intercept-point, small-signal and single-tone approximations.



Placement: Strengthen existing CAP-013/014/015/018. A separate capability is unnecessary unless CAP-014 becomes unwieldy.



Acceptance consequence: Block acceptance until these calculations and decisions are explicit.



3\. P1 — The mathematical bridge from phase processes to engineering performance remains implicit



Affected: CAP-002–005, CAP-013, CAP-035–039, CAP-042; CAP-005 (project/competence-inventory.md:127) and CAP-042 (project/competence-inventory.md:175).



The inventory correctly rejects a universal coherence metric. However, it does not explicitly require deriving how the complex phase process produces integration loss, correlation changes, modulation errors or spatial-response degradation.



Counterexample: A phase offset that is random between records but constant within each record can have the same marginal variance as rapidly varying phase. The former preserves the magnitude of a within-record coherent sum; the latter need not.



For equal-amplitude samples with residual phase errors ϵₙ, the algebraic identity



\\[

\mathbb E\left|\frac1N\sum_n e^{j\epsilon_n}\right|^2

\=

\frac1{N^2}\sum\_{n,m}\mathbb E[e^{j(\epsilon_n-\epsilon_m)}]

\\]



shows why marginal RMS phase alone is insufficient. This example concerns accumulated magnitude, not every possible detection or phase-measurement objective.



Why it matters: Without this bridge, future treatments could become catalogues of PSDs and stability measures followed by application assertions.



Correction: Require the reader to formulate multiplicative phase errors, derive the relevant complex-signal statistics, and connect them to task performance. Explicitly distinguish exact relationships from small-angle, Gaussian and stationary approximations.



Placement: Extend CAP-004/005 and CAP-042; application entries should own their particular consequences.



Acceptance consequence: Block acceptance because this is central coherent-receiver reasoning.



4\. P1 — Calibration observability is strong; correction feasibility is underdeveloped



Affected: CAP-008, CAP-018, CAP-020, CAP-022–024; particularly CAP-022/023 (project/competence-inventory.md:275).



The inventory explicitly covers rank, conditioning, unobserved paths and independent residual assessment. Those are strengths. It does not equally clearly require deciding whether an identified impairment is correctable within the available hardware, noise, latency and bandwidth constraints.



Counterexample: A channel response can be measured accurately but contain a deep attenuation region. Inverting it may amplify noise excessively; a spectral null cannot be repaired by ordinary equalization. A required inverse can also be incompatible with available causal filtering and latency.



Similarly, knowing that clipping, aliasing or irreversible analog combination occurred does not restore the lost information.



Why it matters: Readers could mistake successful parameter estimation for a viable correction strategy.



Correction: Require evaluation of inverse-response noise gain, causal/stable realizability, latency, coefficient range and residual approximation error. Explicitly classify impairments as correctable, partially correctable or requiring prevention/redesign. Compare equalization with physical matching and architecture changes.



Placement: Extend CAP-022/024, using CAP-008/020. No new capability is necessary.



Acceptance consequence: Block acceptance until correction limits are explicit.



5\. P1 — Distributed coherence has insufficient committed internal depth



Affected: CAP-007, CAP-010, CAP-016, CAP-017, CAP-025, CAP-036, CAP-039; U-02.



U-02 (project/competence-inventory.md:608) correctly preserves uncertainty, but the inventory leaves too much essential distributed-reference reasoning behind that unresolved boundary.



Counterexample: A one-way timing observation combines clock offset and propagation delay. Without additional information, those contributions cannot generally be separated. A two-way exchange introduces assumptions about reciprocal delays and endpoint hardware. NIST explicitly identifies these symmetry limitations. NIST two-way time transfer.



Frequency agreement, sample-epoch alignment, RF phase relationship and transport timestamps are also distinct requirements.



Why it matters: Distributed interferometry, bistatic radar and separated apertures are already represented. Their essential synchronization reasoning cannot remain an unspecified specialist extension.



Correction: Commit internally to clock offset/rate models, delay/offset identifiability, one-/two-way reference comparisons, asymmetry, holdover, sample-time reconstruction and the distinction between timing and carrier-phase alignment. Specific protocols and specialist transfer hardware can remain external.



Placement: A dedicated distributed-reference capability is justified, complementing CAP-016’s distribution engineering and CAP-017’s state transitions.



Acceptance consequence: Block acceptance. Comprehensive protocol coverage is unnecessary; the essential internal minimum must be settled.



6\. P2 — Practical subsystem and technology selection needs more concrete evidence requirements



Affected: CAP-011, CAP-014–018, CAP-021, CAP-026, CAP-027.



Lifecycle breadth is good. However, several outcomes stop at “select,” “allocate” or “produce a rationale.” The inventory does not consistently require translating allocations into component/interface requirements and establishing which performance is guaranteed, inferred or awaiting characterization.



Counterexample: A converter and driver each meet headline specifications but fail together because input loading, settling, drive conditions or filtering differ from their characterization conditions.



Why it matters: The charter’s endpoint includes practical subsystem engineering, not just architecture and characterization planning.



Correction: Require component/technology comparisons against derived requirements, including interface compatibility, loading, operating conditions, tolerance, dissipation and missing guarantees. Make prototype characterization an explicit response to unavailable consequential data.



Placement: Incorporate into existing subsystem capabilities. Do not require transistor-level design of every component or reproduce general circuit textbooks.



Acceptance consequence: Significant strengthening before subsystem authoring; it need not prevent architecture work once the responsibility is committed.



7\. P2 — The application families are appropriate, but their walkthroughs insufficiently challenge the foundations



Affected: CAP-035–042 and §6 (project/competence-inventory.md:497).



The seven categories provide defensible breadth. Their contrasts are useful. Nevertheless, the walkthroughs often identify relevant capability numbers and then conclude that those capabilities cover the problem. That establishes routing more strongly than sufficiency.



Useful additional challenges within the existing categories include:



\- Communications: multicarrier phase variation that cannot be represented solely by a common phase correction.

\- Arrays: interference rejection/null depth rather than beam gain alone, exposing sensitivity to covariance and complex-response errors.

\- Interferometry: a weak stochastic correlation measurement rather than a split deterministic test signal.

\- Sensing: calibration or tracking that suppresses the physical change being measured.



Why it matters: A broad label can appear complete until a specific decision demands an unstated method.



Correction: For each challenge, identify the actual calculation or decision, the apparently reasonable wrong choice, and the capability outcome that discriminates between them. Qualitative symbolic cases suffice; solved designs and invented product requirements are unnecessary.



Placement: Expand existing scenario audits and affected application outcomes. No additional application category is required.



8\. P2 — Signal-preserving calibration and tracking should be explicit



Affected: CAP-006, CAP-007, CAP-010, CAP-023–025, CAP-039–041.



The inventory distinguishes unknown signal parameters from receiver defects, but does not explicitly require proving that correction preserves the desired observable.



Counterexample: A phase-tracking loop removes slow phase variation that is actually the displacement signal. In interferometry, calibration assumptions can also affect retained position information; NRAO cautions about this in its discussion of self-calibration. NRAO calibration guidance.



Why it matters: A cleaner residual can represent destruction of information rather than improvement.



Correction: Require a signal-versus-nuisance model, analysis of the desired signal’s transfer through correction/tracking, and explicit identification of reference freedoms and information intentionally surrendered. Include independent stimulus cases that test signal preservation.



Placement: Strengthen CAP-023/024/025 and application entries. No new capability is needed.



9\. P2 — Some learning prerequisites are incorrectly universal



Affected: CAP-017, CAP-022–024, CAP-030, CAP-037, CAP-041; §5.2 (project/competence-inventory.md:463).



The document says “P” denotes learning prerequisites, but some lists combine prerequisites with optional implementations and later interactions.



For example, CAP-022 requires CAP-020, which requires sampling/conversion knowledge. CAP-023 requires CAP-022, and CAP-030 requires CAP-023. Read literally, general measurement competence consequently depends on a digital multichannel processing path. CAP-041’s CAP-012–025 range similarly includes methods not necessary for every phase-sensitive instrument.



Why it matters: Analog or single-channel designs acquire artificial prerequisites, and the later learning architecture could be distorted.



Correction: Distinguish essential foundations, implementation-conditional dependencies and engineering interactions. Retain direct foundational routes to measurement and analog instruments.



Placement: Correct existing prerequisite lists and the dependency summary. No elaborate graph or new capability is warranted.



10\. P2 — Assessability is stronger for documents than for completed technical work



Affected: CAP-009, CAP-013, CAP-029–034; particularly CAP-029 (project/competence-inventory.md:333).



The six competence dimensions are well defined. Nevertheless, some evidence outcomes are specifications, plans or assessments without a minimum requirement to execute and interpret the corresponding technical work.



CAP-029, for example, could be satisfied by selecting and specifying a model without constructing it, calculating a result or discovering a consequential model failure.



Why it matters: A reader might learn to describe a sound engineering activity without becoming capable of performing it.



Correction: Add bounded performance outcomes: formulate and evaluate a model; close a budget with justified inputs; execute and interpret a measurement; evaluate calibration residuals; and assess production variation. For rare failures such as slips or restart errors, require defensible observation duration, exposure counts and confidence assumptions—without prescribing arbitrary targets.



Placement: Extend existing capabilities. This concerns what the future reader must demonstrate; it does not require developing models or executing tests during inventory authoring.



11\. P2 — “Instrument-independent measurand” is too categorical



Affected: CAP-002, CAP-005, CAP-030, CAP-041; CAP-002 (project/competence-inventory.md:103).



CAP-002 requires an instrument-independent measurand definition. That is a useful protection against confusing instrument artifacts with system behavior, but it is not universally appropriate.



A valid measurand may be defined by a specified measurement method. NIST TN 1297 explicitly allows this and requires the method dependence to be reported. NIST Appendix D.4.



Why it matters: Filtered phase residuals, finite-record stability estimates and correlation observables can depend intentionally on their observation procedure.



Correction: Require an explicit operational definition that separates the intended observation operator from unintended instrument response, corrections and uncertainty. State method dependence where it belongs to the quantity.



Placement: Correct CAP-002 and align CAP-005/030/041. No new capability is required.



The supporting source notes are appropriately restrained overall:



\| Source | Attribution assessment |

\|---|---|

\| S1 — NIST SP 1065 | The cited passages support distinct stability measures and noise-dependent limitations of ordinary variance. They do not establish application-wide coherence metrics. Examined report. |

\| S2 — NIST TN 1297 | The cited material supports measurement-process modeling, covariance and first-order uncertainty propagation. It does not establish arbitrary nonlinear phase uncertainty or compliance rules. Appendix A. |

\| S3 — Analog Devices latency article | Supports the distinction between digital framing-link latency and total converter latency. The note correctly labels the whole-receiver conclusion as an engineering inference and disclaims current-device guarantees. Article. |

\| S4 — NRAO calibration guidance | Supports differing calibration contributions and timescales in its application context. The note appropriately avoids claiming a universal calibration procedure. Guidance. |



I found no significant over-attribution in those notes. Their narrowness is acceptable for an inventory; they cannot substantiate completeness.



The exclusions of comprehensive optical/quantum coverage, exhaustive imaging or protocol algorithms, detailed radiator design and component-specific facts are defensible. They become problematic only where an essential coherent-receiver inference or interface calculation is delegated with them. Conversely, production, configuration, environmental effects and service are already represented and should not be reported as wholly missing.



Acceptance should remain pending until findings 1–5 are corrected and examined by suitable human engineering reviewers. The remaining findings can largely be resolved by sharpening existing outcomes and dependency boundaries. No new infrastructure, chapter structure or project-management process is needed."



# Review 2 

"I’m distinguishing missing engineering obligations from topics already covered that need clearer scope. My recommendation will be to withhold acceptance as an architecture input until the core gaps are corrected. Most corrections fit existing capabilities; disturbance analysis is the strongest case for a separate capability because CAP-014 currently carries too many distinct responsibilities. I recommend **withholding acceptance of the inventory as a sufficiently complete input to the book’s intellectual architecture** until findings 1–7 below are addressed. This is a recommendation for human review, not an acceptance decision.

The inventory makes a sound distinction between conceptual understanding and engineering work. Its treatment of observables, reference planes, calibration identifiability, state transitions, and evidence limitations is particularly useful. Lifecycle coverage is broad, and the seven application categories are defensible.

The principal weakness is that several consequential subjects are **named without sufficiently explicit obligations to calculate performance, determine realizability, or reject incompatible requirements**. An inventory does not need finished derivations or solved designs, but its required outcomes must make those future treatments unavoidable.

Here, **P0** means acceptance-blocking for the declared architecture-input use; **P1** means a substantive capability or scope correction; **P2** means a useful refinement that need not prevent acceptance.

1. **P0 — Feasibility is a stated responsibility, but demonstrating infeasibility is insufficiently specified.**

   **Affected:** CAP-001 (project/competence-inventory.md:95), CAP-006/011/013/018/020/037/042.

   **Deficiency:** “Negotiate incompatible goals,” “resource and performance bounds,” and “identify … feasibility limits” establish intent. They do not explicitly require the reader to derive the constraints that distinguish an impossible specification from an inadequate component choice.

   **Why it matters:** Consider a receiver whose minimum gain, set by converter noise, exceeds its maximum gain, set by blocker peaks and converter headroom. No gain setting satisfies both requirements. Digital filtering cannot repair samples already clipped. Similarly, frequency-independent phase steering cannot provide exact, frequency-independent steering at an arbitrary nonboresight angle over a continuous bandwidth.

   These are consequential rejection decisions, not merely budget adjustments. Information limits, ambiguity, physical realizability, and available-technology limits also require different remedies.

   **Correction:** Require construction of a feasible operating region under stated assumptions, including coupled gain/headroom/noise constraints, bandwidth–observation–estimation tradeoffs, spatial and waveform ambiguity, latency/settling constraints, and calibration observability. Require identification of which requirement must change when that region is empty. Avoid universal “resolution limits” detached from waveform, SNR, estimator, and ambiguity assumptions.

   **Placement:** Strengthen CAP-011 as the canonical feasibility responsibility, supported by the existing foundations and subsystem entries. **No new capability required.**
2. **P0 — Reciprocal mixing and other signal-dependent disturbances remain too close to topic labels.**

   **Affected:** CAP-014 (project/competence-inventory.md:209), CAP-004/005/013/015/016/018/036/042.

   **Deficiency:** Reciprocal mixing appears in CAP-014’s methods list, but no outcome explicitly requires calculating blocker-dependent in-band noise, deriving an LO requirement from it, or choosing where rejection must occur. Sampling jitter is similarly listed without an explicit obligation to analyze the complete input waveform.

   **Why it matters:** For illustration, assume a narrow blocker of −20 dBm at the mixer input, locally flat SSB LO phase noise of −140 dBc/Hz at the relevant offsets, and a 10 kHz equivalent noise bandwidth. The usual small-phase approximation gives approximately **−120 dBm input-referred reciprocal-mixing noise**. Excellent ordinary noise figure and a clean desired-channel output filter do not eliminate that contribution. The distinction between ordinary noise-figure measurements and blocker-induced reciprocal mixing is explicitly documented in the [manufacturer’s mixer noise discussion](https://www.analog.com/en/resources/technical-articles/wideband-lo-noise-in-passive-transmitreceive-mixer-ics.html).

   Likewise, sampling error depends locally on the slope of the **entire analog input**, approximately δ x(t)=x'(t)δ t(t), rather than only on the desired signal’s frequency. A large out-of-channel signal can dominate the resulting impairment. [Analog Devices discusses this blocker-dependent clock-noise mechanism](https://www.analog.com/en/resources/technical-articles/the-impact-of-clock-generator-performance-on-data-converters.html).

   **Correction:** Require calculation of disturbance generation and propagation from signal/blocker spectra and oscillator/clock spectra through actual filtering and sampling. Include internal LO-buffer noise, multiple interferers, applicable correlations, reference planes, and limits of flat-spectrum and small-error approximations.

   **Placement:** A **new capability for deriving physical noise and interference contributions** is justified. CAP-014 currently combines too many responsibilities; CAP-013 should assemble the resulting contributions into system budgets.
3. **P0 — Nonlinear behavior lacks an explicit engineering model and gain-control responsibility.**

   **Affected:** CAP-014/017/018/019/021/028/036.

   **Deficiency:** Compression, intermodulation, AM-to-PM conversion, switching, and recovery tests are present. Missing is a clear requirement to predict or characterize the complex, time-dependent behavior of a chain under its actual signal envelope, including gain control.

   **Why it matters:** A two-tone IP3 calculation does not establish phase fidelity near compression, during a strong pulse, or immediately afterward. A radar receiver can satisfy small-signal noise and phase specifications yet miss weak returns during limiter, amplifier, filter, or converter recovery. Independent channel gain changes can disturb an array manifold during otherwise valid operation.

   Quantization also cannot universally be treated as independent white noise; coherent inputs can produce correlated errors and spurs. The conditional role of dither is described in [ADC Input Noise](https://www.analog.com/en/resources/analog-dialogue/articles/adc-input-noise.html).

   **Correction:** Explicitly require selection of an adequate memoryless, dynamic, or measured impairment model; calculation or characterization of complex distortion versus level and history; crest-factor/headroom allocation; gain-control policy; and valid-data intervals through gain changes and overload recovery. Require recognition of where IP2/IP3 extrapolation and additive quantization-noise models fail.

   **Placement:** Expand CAP-014, with converter-specific treatment in CAP-018 and state handling in CAP-017/028. **No new capability necessary.** Exhaustive nonlinear-device theory is optional; the engineering model-selection competence is essential.
4. **P0 — Correlation mathematics is explicit, but physical multichannel noise and correlation sensitivity are not.**

   **Affected:** CAP-004/008/010/013/014/022/037/039/042.

   **Deficiency:** The inventory repeatedly requires covariance and cross-spectral propagation. It does not explicitly require deriving those quantities from antenna noise, dissipative networks, mismatch, coupled receiver noise, or stochastic source power. CAP-039 also lacks a definite correlation-sensitivity calculation.

   **Why it matters:** Knowing that output noise is w^{H}Rₙw is insufficient if the engineer assumes an unjustified diagonal Rₙ. Separate LNAs do not ensure independent channel disturbances when antenna coupling provides additional paths. This mechanism appears in the primary study [Calibration of active antenna arrays using a sky brightness model](https://agupubs.onlinelibrary.wiley.com/doi/full/10.1029/2003RS003016), particularly its mutual-coupling treatment.

   A correlator has another important trap: zero expected correlation from independent receiver noise does **not** imply zero finite-record uncertainty. Strong stochastic source power also contributes to correlation-estimator variance. Stable electronics alone cannot establish achievable sensitivity.

   **Correction:** Require conversion between available noise power, temperature, spectral density, and channel covariance under stated loading and bandwidth conditions. Include a bounded noise-wave or equivalent network treatment where coupling matters. Require derivation of correlation-estimator bias and variance, effective independent sample count, and source-dependent sensitivity.

   **Placement:** Include physical noise generation in the new capability proposed in finding 2; retain matrix foundations in CAP-004/008 and application sensitivity in CAP-037/039. **No second new capability required.**
5. **P0 — The mathematical bridge from stochastic phase to application performance is insufficiently binding.**

   **Affected:** CAP-005 (project/competence-inventory.md:127), CAP-004/007/013/015/016/036/037/039/042.

   **Deficiency:** Spectra, stability measures, covariance propagation, and coherent accumulation all have homes. What is not explicit enough is the required derivation connecting stochastic phase, observation weighting, and actual coherent performance.

   **Why it matters:** An integrated RMS phase number cannot generally determine radar pedestal shape, tracking performance, array behavior, and finite-interval integration loss. The distribution and temporal structure matter.

   A concrete algebraic example is an ideal shared oscillator observed through two paths differing only by delay τ. For phase noise with an applicable spectral description,

   \\[    \Delta\phi(t)=\phi(t)-\phi(t-\tau),\qquad    S\_{\Delta\phi}(f)=4\sin^2(\pi f\tau)S\_\phi(f).    \\]

   Thus, shared-source cancellation depends on offset frequency and delay. The inventory recognizes this qualitatively, but should explicitly require the reader to derive and use the transfer.

   **Correction:** Require derivation of phase-increment statistics, complex coherence, observation-weighted accumulation loss, and application-specific spectral consequences. State when Gaussian, stationary, small-angle, or high-SNR approximations apply. Include the additive-noise-to-phase transformation and its breakdown near low amplitude.

   **Placement:** CAP-004/005 should own the stochastic relationships; CAP-013/042 should apply them; application entries should interpret the consequences. **No new capability required.**
6. **P0 — Calibration identifiability is treated well; realizability of correction is not equally explicit.**

   **Affected:** CAP-022 (project/competence-inventory.md:275), CAP-008/019/020/023/024/035.

   **Deficiency:** Rank, conditioning, regularization, unobserved paths, and independent residual checks are present. They do not fully establish whether an identified response can be corrected by a causal, stable, finite-resource implementation within the permitted latency and noise budget.

   **Why it matters:** An accurately measured notch does not make lost information recoverable. Equalizing a deep attenuation can amplify downstream noise severely. A nonminimum-phase response can prevent exact stable causal inversion; practical correction then requires approximation and potentially additional latency. The inverse-realizability distinction is summarized in [MathWorks’ minimum-phase definition](https://www.mathworks.com/help/dsp/ref/dsp.allpassfilter.isminphase.html).

   Similarly, post-acquisition calibration cannot reconstruct clipping or recover independently required channel information discarded by analog combination. CAP-022 already recognizes correction access before combination; that principle should become a broader correction-limit obligation.

   **Correction:** Require calculation of residual error, noise enhancement, implementation length, latency, and validity limits for the proposed correction. Distinguish identifying an impairment, compensating it approximately, and restoring information.

   **Placement:** Strengthen CAP-020/022/024, supported by CAP-008/023. **No new capability required.**
7. **P0 — Distributed synchronization has an unresolved minimum internal scope.**

   **Affected:** CAP-006/007/016/017/020/025/036/039; U-02.

   **Deficiency:** Independent references and distributed systems are required contrasts, but their internally developed engineering methods remain insufficiently committed. “Distributed transfer/recovery where needed” leaves too much essential reasoning behind U-02.

   **Why it matters:** One-way observations can confound clock offset and propagation delay. Two-way transfer does not eliminate arbitrary directional asymmetry. Sample epoch, clock rate, RF carrier phase, and transport latency are separate quantities. NIST’s [two-way transfer explanation](https://tf.nist.gov/time/twoway.htm) explicitly identifies equipment-delay and propagation-asymmetry contributions.

   **Correction:** Commit to deriving representative one-way and two-way measurement equations, their reference freedoms and reciprocity assumptions, residual transfer uncertainty, holdover behavior, and the consequences of clock-rate mismatch for sample alignment and resampling. Include the bandwidth and stability consequences of delayed synchronization feedback where applicable.

   **Placement:** Strengthen CAP-016/017/020/025, using CAP-006/007 foundations. **No new capability required.** Specific protocols and specialized transfer hardware can remain external.
8. **P1 — Component and technology selection needs a more concrete internal bridge.**

   **Affected:** CAP-011/014/015/016/018/019/022/026; U-07.

   **Deficiency:** Most subsystem entries produce requirements, rationale, or characterization plans. They less clearly require turning those requirements into a realizable selection among competing technologies and checking interface compatibility.

   **Why it matters:** Selecting a low-noise mixer also requires compatible LO drive, termination, isolation, conversion response, and operating conditions. A converter selection requires an adequate driver and clock interface. A phase-shifter choice must account for insertion-loss variation, resolution, settling, and calibration consequences. Good individual specifications do not establish a compatible chain.

   **Correction:** Require comparison of representative technology alternatives using derived selection criteria and a quantitative interface budget. Include loading, stability where relevant, drive levels, bias/supply sensitivity, thermal consequences, state behavior, and the distinction between typical characterization and guaranteed performance.

   **Placement:** Expand the existing subsystem capabilities and CAP-011’s synthesis outcome. **No new capability required.** General device physics, detailed circuit recipes, current part data, and fabrication particulars can remain external.
9. **P1 — Interference rejection needs an explicit desired-signal preservation obligation.**

   **Affected:** CAP-006/008/014/019/035/037/038/042.

   **Deficiency:** Blocker tolerance, colored-noise weighting, and channel combination are included. Less explicit are estimating interference statistics, selecting rejection methods, and demonstrating that rejection preserves the desired observable.

   **Why it matters:** A spatial null formed from contaminated training data can suppress the desired signal. A cancellation reference can contain desired-signal leakage. A spectral notch may remove essential waveform information. If desired and interfering contributions occupy the same observed subspace without other distinguishing information, a linear separator cannot arbitrarily distinguish them.

   **Correction:** Require selection among spatial, spectral, temporal, and reference-assisted rejection where applicable; assessment of available degrees of freedom, training support, covariance conditioning, mismatch, and desired-signal distortion. Connect digital rejection to the analog headroom needed before it can operate.

   **Placement:** CAP-042 should own the general detection/rejection relationship; CAP-037/038/035 should develop the relevant application decisions. **No new capability required.** Exhaustive adaptive algorithms and comprehensive electronic-warfare coverage are optional.
10. **P1 — The minimum polarization and manifold scope should be fixed before architectural decomposition.**

**Affected:** CAP-010/022/023/037/038/039; U-05.

**Deficiency:** Polarization, coupling, and manifold calibration are named, but “full polarimetric inference unresolved” does not clearly separate optional specialist interpretation from indispensable receiver modeling.

**Why it matters:** Two accurately aligned receiver channels do not establish calibrated dual-polarization reception if cross-polar leakage is significant. A fixed scalar correction per channel cannot generally represent a direction-dependent vector response across an entire field of view. Similar distinctions apply to antenna reference geometry and changing element loading.

**Correction:** Commit to a minimal vector measurement model connecting incident field components, antenna/manifold response, receiver transfer, and leakage. Require identification of parameters needing external antenna or geometry information and of the conditions under which scalar channel matching suffices.

**Placement:** Strengthen CAP-010/022/023 and the application mappings. **No new capability required.** Full-wave radiator design, comprehensive polarimetric science, and specialist imaging can remain external.

11. **P1 — Some universal prerequisites unnecessarily force digital and multichannel treatments onto other receiver classes.**

**Affected:** CAP-020/022/023/024/026 and §5.2.

**Deficiency:** CAP-022 universally lists digital-processing CAP-020 as a prerequisite. CAP-023 and CAP-024 universally depend on multichannel alignment CAP-022 despite applying to all calibrated receivers. CAP-026 similarly includes multichannel alignment in its general prerequisite list.

**Why it matters:** An analog receiving array needs complex-response alignment without necessarily needing a digital downconverter. A single-channel instrument needs calibration observability without first requiring the full multichannel alignment responsibility. These dependencies could distort learning order and scope.

**Correction:** Make digital equalization and multichannel dependencies conditional. Ground general calibration in measurement equations, estimation, reference integrity, and uncertainty; add channel-alignment prerequisites when the system requires them.

Also strengthen broad work products such as CAP-013’s “budget structure”: under supplied conditions, assessment should require calculating allocations and evaluating closure, rather than merely drawing a plausible budget.

**Placement:** Revise existing prerequisite and assessment statements. **No new capability required.** The inventory already distinguishes engineering iteration from learning prerequisites; there is no need to impose an acyclic engineering workflow.

12. **P1 — The seven application categories are adequate, but their walkthroughs insufficiently test the shared foundations.**

**Affected:** CAP-035–042 and §6.

**Deficiency:** The walkthroughs identify appropriate responsibilities and useful failures, but often demonstrate that capability identifiers can be mapped to a case rather than that the required engineering decisions are covered.

**Why it matters:** The same broad phrase—“propagate errors”—can conceal substantially different methods. In particular, the current application audits do not reliably expose findings 2–6.

**Correction:** Retain the seven categories and sharpen their decision challenges:

| Category                    | Additional consequential challenge                                                                                                              |
| --------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------- |
| Communications              | Determine whether a finite burst provides sufficient observations for acquisition and ambiguity resolution before payload recovery is required. |
| Radar                       | Allocate a strong leakage/clutter-induced phase-noise pedestal against a weak target at a different delay/Doppler.                              |
| Receiving arrays            | Calculate beam sensitivity with correlated noise and evaluate pattern/null robustness under calibration error.                                  |
| DF                          | Determine what remains identifiable with coherent multipath, multiple sources, and imperfect manifold knowledge.                                |
| Interferometry              | Calculate finite-integration sensitivity, including stochastic source contribution, alignment error, and clock uncertainty.                     |
| Coherent sensing            | Determine observability and ambiguity recovery through fades while reference-path disturbances mimic the measurand.                             |
| Phase-sensitive measurement | Separate DUT behavior from level-dependent receiver error and correlated reference/fixture effects.                                             |

These can remain qualitative inventory-level challenges, with required calculations explicitly named. Complete reference designs or invented product requirements are unnecessary here.

**Placement:** Strengthen existing application entries and walkthroughs. **No new application category or capability required.**

13. **P2 — Production coverage is substantially present; quantitative yield and calibration effort would improve assessability.**

**Affected:** CAP-024/027/030/031/033/034.

**Deficiency:** CAP-033 covers unit/lot variation, fixture limitations, screening, guard bands, and escapes. Its required outcome could more clearly include estimating joint yield, calibration adjustment range, and test duration.

**Why it matters:** A prototype correction method can work technically yet require an impractical frequency × gain × temperature calibration sweep. Individual tolerance compliance also does not automatically establish joint system yield, especially with correlated variation.

**Correction:** Require a bounded estimate of production yield and calibration/test effort under declared distributions or bounds, including coefficient range/resolution and fixture uncertainty. Preserve uncertainty where production data are unavailable.

**Placement:** Strengthen CAP-033 using existing calibration and uncertainty capabilities. **No new capability required.** This is a specificity improvement, not a missing lifecycle discipline.

The scope boundaries are otherwise broadly defensible. General RF remediation, exhaustive coding and imaging methods, detailed HDL/platform implementation, full-wave antenna design, current standards, and component-specific facts can remain external. The internal book must retain the reasoning that determines whether those external inputs are adequate. Comprehensive optical/quantum coverage, every estimator family, and specialist mission processing are optional elaborations; the core corrections above are not.

The source audit found **no material overclaim in the four supporting source notes**:

| Source                                                                                                                                                                                                                                 | What the examined passages support                                                                                                    | Boundary that should remain explicit                                                                                                                                                         |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| S1, [NIST SP 1065](https://tsapps.nist.gov/publication/get_pdf.cfm?pub_id=50505), §3.3 and §§5.2.1–5.2.2                                                                                                                               | Distinct time/frequency stability measures and failure of ordinary fractional-frequency variance for some oscillator noise processes. | It does not establish a universal coherence metric or the inventory’s completeness.                                                                                                          |
| S2, [TN 1297 §5](https://www.nist.gov/pml/nist-technical-note-1297/nist-tn-1297-5-combined-standard-uncertainty) and [Appendix A](https://www.nist.gov/pml/nist-technical-note-1297/nist-tn-1297-appendix-law-propagation-uncertainty) | Measurement-process modeling, corrections, covariance, and the first-order basis of the displayed propagation law.                    | It does not justify unrestricted linear propagation through wrapped, ambiguous, or strongly nonlinear inference.                                                                             |
| S3, [Beavers’ JESD204B article](https://www.analog.com/en/resources/technical-articles/demystifying-deterministic-latency-within-jesd204b-converters.html)                                                                             | The distinction between framing-link latency, total converter latency, and additional analog-sample alignment information.            | Whole-receiver coherence is an engineering inference. The note correctly identifies that inference and does not claim direct examination of the JEDEC standard or current device guarantees. |
| S4, [NRAO Calibration Basics](https://science.nrao.edu/facilities/vla/docs/manuals/obsguide/calibration)                                                                                                                               | Distinct calibration contributions and timescales in VLA observing practice.                                                          | It does not establish a universal calibration procedure, observability proof, or transferable cadence.                                                                                       |

No source-related correction is acceptance-blocking. The limited source coverage is openly declared and should not be mistaken for support for every proposed capability. Conversely, an inventory of proposed learning requirements does not need every future textbook derivation researched before its scope can be reviewed.

I examined the inventory, charter, applicable standards, supporting notes, and the cited textual passages. No files were modified; no software tests, simulations, or physical measurements were performed. This review supplies technical criticism and recommendations, not independent physical validation or human technical acceptance."
