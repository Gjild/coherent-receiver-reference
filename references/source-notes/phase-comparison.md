# Phase comparison: claim provenance

Date: 2026-10-29. Examiner: Codex. Human specialist review pending.

## Examined source

- Citation key: scipyHilbert. The SciPy community, `hilbert`, online SciPy Manual,
  page served with v1.18.0 heading; no fixed publication date asserted.
- Access: web text retrieval of
  https://docs.scipy.org/doc/scipy/reference/generated/scipy.signal.hilbert.html.
- Actual examined passages: opening definition (retrieval lines 33–35) and Notes
  (73–78), including the displayed analytic-signal expression.
- Supported claim: forming an analytic representation by retaining/doubling
  positive-frequency content, discarding negative-frequency content, and
  recovering the real input as the real part. Translation: manuscript uses j,
  peak-voltage amplitude and an explicitly chosen positive carrier.
- Boundary: documentation describes an FFT implementation; this is support for
  the representation convention, not proof of the unit's continuous-time mixer
  derivations, a finite-record hardware algorithm or real receiver accuracy.
  The manuscript handles DC separately. No implementation, SciPy installation,
  referenced book, linked code or hardware measurement was examined/executed.

## Authorial development and illustrative inputs

Euler decomposition, cosine-product mixing, positive-IF orientation, conjugate
comparison, cycle-average power, integer-cycle extraction, reference/epoch changes
and delay ambiguity are developed explicitly in the manuscript. They are authorial
mathematical derivations checked as recorded in the review, not results certified
by the source above. The unit does not rely on unexamined citations for these
steps. The pilot is a local consistency reference, not independent evidence.

All port phases, gains, frequencies, 50-ohm load, one-microsecond observation and
25 ps added delay are declared teaching assumptions. Unity-normalized mixing is
an ideal mathematical model. No part, fixture, LO phase control, path response,
settling time, accuracy, reader outcome or hardware feasibility is established.
