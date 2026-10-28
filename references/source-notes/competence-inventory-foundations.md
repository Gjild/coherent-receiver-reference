# Selected evidence for the foundational competence inventory

**Status:** selected passage examinations recorded; no human technical review or acceptance. **Examination date:** 2026-10-28. **Examiner:** Codex, using the web tool's retrieved text. No local full-text copies or rendered-figure inspections were made. Bibliographic verification and passage examination below do not imply exhaustive source review.

This note supports only the named distinctions in `project/competence-inventory.md`. Capability selection, granularity, depth and completeness remain proposed engineering/editorial judgements. Source labels S1–S9 correspond to that document; citation keys resolve in `references/references.bib`.

## S1 — riley2008frequency

- **Bibliographic verification:** report title page identifies W. J. Riley, NIST SP 1065, July 2008. The NIST landing-page metadata also lists David A. Howe; the canonical entry follows the report's title page and preserves this discrepancy here.
- **Access / passage examined:** [report PDF text](https://tsapps.nist.gov/publication/get_pdf.cfm?pub_id=50505), §3.3, printed p. 6 (PDF page index 15), and §§5.2.1–5.2.2, printed pp. 13–15 (PDF indices 22–24). Title-page text also examined.
- **Supported distinction:** Frequency stability has distinct time- and frequency-domain measures. Ordinary variance can fail to converge for some oscillator noise types; choice of statistic matters.
- **Use:** CAP-005 and §9 justify an internal capability for selecting and interpreting observation-dependent measures.
- **Limits / conventions:** This is oscillator stability context, not evidence for one universal coherence metric. The report uses time-error and fractional-frequency variables; no report normalization or PSD convention is silently adopted. Only the named passages were checked; no derivation or estimator implementation was independently verified.

## S2 — taylor1994uncertainty

- **Bibliographic verification:** [online cover](https://www.nist.gov/pml/nist-technical-note-1297/nist-guidelines-evaluating-and-expressing-uncertainty-nist-measurement) identifies Barry N. Taylor and Chris E. Kuyatt, NIST TN 1297, September 1994, 1994 edition.
- **Access / passage examined:** [§5.1–5.2](https://www.nist.gov/pml/nist-technical-note-1297/nist-tn-1297-5-combined-standard-uncertainty) and [Appendix A.1–A.3, equations A-1 through A-3](https://www.nist.gov/pml/nist-technical-note-1297/nist-tn-1297-appendix-law-propagation-uncertainty), online text and equation transcription.
- **Supported distinction:** The measurement model includes significant uncertainty contributors and corrections. Combined uncertainty includes covariance; the displayed propagation law uses a first-order Taylor approximation.
- **Use:** CAP-009/030 and §9 support retaining correlated uncertainty and applicability limits.
- **Limits / conventions:** Not a blanket justification for linear propagation in nonlinear, ambiguous or phase-wrapped problems; not an instrument-specific uncertainty budget or a compliance decision rule. The broader document was not exhaustively examined.

## S3 — beavers2014latency

- **Bibliographic verification:** [article](https://www.analog.com/en/resources/technical-articles/demystifying-deterministic-latency-within-jesd204b-converters.html) identifies Ian Beavers, February 1, 2014, Analog Devices.
- **Access / passage examined:** first, fourth and sixth question/answer blocks: framing-link definition, comparison with total converter latency, and additional requirements for analog-sample alignment.
- **Supported distinction:** Framing-link latency excludes additional converter processing; analog-sample alignment needs additional device-specific knowledge.
- **Use:** CAP-017, P-MET and §9 support separating link timing from the complete receiver phase/time path. The system-level requirement to check the whole path is an engineering inference.
- **Limits / conventions:** A vendor explanation of JESD204B, not direct examination of the JEDEC specification. No current part, revision, timing guarantee or measured performance was checked. The inventory does not adopt numerical link constraints from the article.

## S4 — nraoCalibration

- **Bibliographic verification:** [NRAO page](https://science.nrao.edu/facilities/vla/docs/manuals/obsguide/calibration) is titled “Calibration” under the VLA observing guide. The examined passage gives no fixed publication date or revision; the access date is retained instead.
- **Access / passage examined:** “Calibration Basics,” opening explanation and list distinguishing instrument, current observing conditions and result calibration.
- **Supported distinction:** Interferometric calibration includes different physical contributions and update timescales; instrument calibration alone is insufficient for every observing effect.
- **Use:** CAP-024/039, P-INT and §9 support retaining these distinctions in the coverage requirements.
- **Limits / conventions:** VLA-specific observational guidance does not establish a general calibration procedure for communications, radar, arrays, DF or instruments. No fixed observing cadence is imported, and no measurement equation or imaging method was independently checked.

## Revision examinations — 2026-10-28

These are additional passage examinations during consolidation. Earlier S1–S4 records remain limited to their original examinations. Access used retrieved text; no equation-image or figure inspection, hardware measurement or independent derivation verification is claimed.

### S2 extension — taylor1994uncertainty

- **New passage:** [Appendix D.4.1](https://www.nist.gov/pml/nist-technical-note-1297/nist-tn-1297-appendix-d4-measurand-defined-measurement-method), opening paragraphs.
- **Support / use:** A measurand may be defined by a measurement method; reporting should identify that dependence. Supports the CAP-002/030 correction. Does not establish any particular phase/filter observable or its uncertainty.

## S5 — nistTwoWayTransfer

- **Metadata / access:** NIST, [Two Way Time Transfer](https://tf.nist.gov/time/twoway.htm); publication date/revision not established. Opening half/full-duplex explanation, reciprocity paragraph, equations (1)/(2) and the subsequent clock-difference/delay discussion examined as retrieved text.
- **Support / use:** Two-way cancellation depends on directional symmetry and endpoint delays; equipment and propagation asymmetry remain. Supports CAP-045's reciprocity/uncertainty obligation.
- **Limits:** No current protocol performance, numerical accuracy guarantee or complete distributed phase model is established. CAP-045's wider requirements are engineering scope decisions, not all claims from this page.

## S6 — adi2005widebandLO

- **Metadata / access:** Analog Devices, [Wideband LO Noise in Passive Transmit-Receive Mixer ICs](https://www.analog.com/en/resources/technical-articles/wideband-lo-noise-in-passive-transmitreceive-mixer-ics.html), page dated September 23, 2005. Introduction on internal LO buffers and subsection Mixer Noise Model prose examined.
- **Support / use:** Blockers mix with effective LO noise, adding wanted-band noise not represented by ordinary noise-figure characterization; internal LO-buffer noise matters. Supports CAP-044 and oscillator/chain selection outcomes.
- **Limits:** Equation images not inspected; no numerical reciprocal-mixing result adopted. Flat-noise and independence assumptions in the example are not universal. No current part guarantee checked.

## S7 — kester2008aperture

- **Metadata / access:** Walt Kester, [MT-007](https://www.analog.com/media/en/training-seminars/tutorials/MT-007.pdf), Revision A, 10/08, verified in PDF text. Printed pp. 3–4, aperture-jitter slope explanation and sine-input SNR assumptions examined.
- **Support / use:** Small timing error produces input-slope-dependent amplitude error; the tutorial's simple SNR calculation assumes a sine input and jitter as the sole impairment. Supports CAP-018/044's waveform-aware timing analysis.
- **Limits:** Generalization to complete wanted/blocker waveforms is an engineering model requirement; correlated sources need explicit covariance, not unconditional RSS combination. No modern converter specifications or broadband model validated.

## S8 — rogers2004arrayCalibration

- **Metadata / access:** Alan E. E. Rogers, Preethi Pratap, Eric Kratzenberg and Marcos A. Diaz, Radio Science 39(2), April 27, 2004, [doi:10.1029/2003RS003016](https://agupubs.onlinelibrary.wiley.com/doi/full/10.1029/2003RS003016). Section 6, especially paragraphs [18]–[21], examined as HTML prose.
- **Support / use:** Mutual coupling supplies paths for amplifier noise to enter other channels and affects correlation/calibration in the studied array. Supports CAP-044's requirement for physically grounded covariance.
- **Limits:** Equation images were not examined; no paper-specific numerical magnitude, Gaussian derivation or general noise-wave model is verified here. The paper's simplified assumptions cannot establish all array geometries/loading or correlation sensitivity.

## S9 — adiADCInputNoise

- **Metadata / access:** Analog Devices / Analog Dialogue, [ADC Input Noise](https://www.analog.com/en/resources/analog-dialogue/articles/adc-input-noise.html). Title/provider verified; individual byline, publication date and revision not established. Subsection on dither and spurious-free dynamic range, especially opening paragraphs and concluding limitations, examined as text.
- **Support / use:** Quantization error can correlate with coherent input; dither effectiveness depends on conditions and does not remove front-end distortion. Supports CAP-018's model-limit requirement.
- **Limits:** No device-specific measured or simulated improvement is adopted; no universal dither amplitude, independence or white-noise guarantee is inferred. Equation/plot images not inspected.

## Evidence gaps

No claim of comprehensive literature coverage follows from these examinations. Application metrics, detection/estimation and loop methods, spatial models, nonlinear impairments, physical design and production methods still require targeted primary-source study as their treatments are developed. Human review must challenge the proposed inventory itself; these sources cannot certify its completeness.
