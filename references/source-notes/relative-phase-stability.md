# Relative-phase pilot: claim evidence and examination limits

Examination date: 2026-10-29. Examiner: Codex via web retrieval. Human specialist
review pending. Original derivations are in the manuscript, not certified by the
references below. No laboratory data were acquired or imported.

## taylor1994uncertainty — measurement model and covariance

Bibliographic identity: Taylor and Kuyatt, NIST TN 1297, 1994 edition; existing
canonical bibliography entry retained. Newly examined online Appendix A.1–A.3,
including equation A-3 as retrieved rendered mathematics/text:
https://www.nist.gov/pml/nist-technical-note-1297/nist-tn-1297-appendix-law-propagation-uncertainty

Supports: significant measurement-process contributions belong in the model;
first-order propagation contains covariance. Conditions: differentiable local
model; does not establish coverage, phase unwrap correctness or any instrument
budget. Translation: pilot uses degrees for the worked uncertainty example,
radians elsewhere, and explicitly separates a standard uncertainty from a bound.
No instrument, traceability chain or physical covariance was verified.

## riley2008frequency — statistic selection

Bibliographic identity: W. J. Riley, NIST SP 1065, July 2008; canonical entry
retained. Newly examined retrieved PDF text, §5.2.1, printed pp. 13–14 (PDF indices
22–23), and nearby §5.2 overview:
https://tsapps.nist.gov/publication/get_pdf.cfm?pub_id=50505

Supports only: ordinary variance is nonconvergent for some clock noise types;
choice of stability statistic matters. The pilot does not import an Allan
variance estimator or normalization. Equation extraction in this PDF is awkward;
no PDF equation is relied on for a pilot derivation. A screenshot was retrieved
but no equation-image examination is claimed. This is not evidence for the
illustrative band limits or for assuming oscillator phase is stationary.

## Discovery examined but not adopted

NIST, “Section One,” https://tf.nist.gov/phase/Properties/one.htm was opened and
its retrieved prose read. No fixed edition/revision was established. Equation
transcription is degraded and images were not inspected. No new bibliography
entry or consequential result relies on it.

## Original work and unresolved claims

The convolution-to-cross-spectrum derivation, Gaussian characteristic-function
application, observation weighting, delay fit, binomial zero-event bound and
illustrative allocations are authorial mathematical developments. They have
specific software/alternative-form checks recorded in the review; they are not
independent specialist-approved results.

The following are declared teaching inputs, not source-supported device facts:
endpoint reference pole, noise densities and independence, electrical delay
mismatch, thermal and supply sensitivities, calibration precision and uncertainty
correlation. Their hardware adequacy needs endpoint measurements and appropriate
manufacturer/implementation evidence. No part/revision guarantee is asserted.

Still needed: specialist examination of linearized endpoint phase response,
nonstationary applicability, finite-record leakage and uncertainty, calibration
identifiability and instrument-reference correlation. Primary device documents
become necessary only when actual hardware is selected. Existing S1–S9 notes
retain their previous narrow support; they are not promoted to pilot validation.

## Focused correction evidence boundary

No new source passages were examined during this correction pass. The phase
filter expansion, reference-frequency regression conversion, constant/update
calibration distinction and timing/precision calculations are authorial
derivations with the checks named in the pilot review. The 990 MHz LO,
simultaneous comb, 32 Msample/s complex acquisition and channelizer interface
are declared engineering assumptions, not examined device capabilities.
Source/fixture/acquisition/instrument identifiability is bounded by the new
measurement equation; no swap or independent comparison was executed.
