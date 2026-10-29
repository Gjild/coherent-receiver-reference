# Current acceptance — bounded Chapter 1 teaching draft

**2026-10-29:** The project owner provisionally accepts the unchanged manuscript
under [ADR-0006](../project/decisions/ADR-0006-provisional-phase-comparison-acceptance.md)
as a mathematically checked, bounded textbook teaching draft for continued
development. Acceptance covers only the declared idealized signal/receiver model,
stated local conventions, checked derivations and illustrative worked example.
It is not independent specialist validation, actual reader effectiveness,
physical receiver performance or publication readiness. The accepted hash is the
same as the authorial check record below. No new technical review is asserted.

Nonblocking editorial obligations: connect ideal continuous-time extraction to
practical sampled observations in the appropriate later treatment; consider
reference-plane and conversion-orientation diagrams during visual development;
and avoid unnecessary duplication of this canonical introductory derivation.
ADR-0006 owns their disposition and reconsideration conditions. They do not
reopen this draft for speculative revision or alter the previous pilot.

**Closed for the stated use.** Next: scalar stochastic phase reasoning — selected
K02 / Chapter 2 material — **not yet started**. Historical pending-acceptance
statements below describe the delivery before this owner decision. Outstanding
specialist, reader, physical and publication evidence remains outstanding.

---

# Historical task and authorial check record

**Date:** 2026-10-29. **Author/checker:** Codex. **Human technical decision:**
pending. The owner approved the method and task, not this technical result.

## Task contract and integration

Artifact: [manuscript](../book/phase-comparison.qmd), SHA-256
`1ec0b1f401846a47e784dc928de37c694686cb7e5dddeb8cbe83d861089683d0`.
Starting HEAD: `dcce08303021b61f30e735f26777d188556b1cde` (context only; the
new file is uncommitted). Review applies to these manuscript bytes.

Develop selected K01/Chapter 1.2–1.3 responsibilities, partially exercising
CAP-002/003/012, not completing K01 or Chapter 1. From the RF phasor/calculus
baseline, enable a reader to reconstruct a voltage, calculate a port-defined
phase comparison, change conversion orientation, and reject an unsupported
input-phase or delay inference. No hidden probability/matrix/control prerequisite.

The continuous D-MET instrument supplies 1 GHz RF, 990/1010 MHz LO, port phases,
positive-IF path phases, gains, a 50-ohm load, a simultaneous 1 microsecond record
and a 25 ps added path delay. All are illustrative inputs, not component data.
Exclusions: spectra, stochastic inference, calibration algorithms, converter
selection, physical performance claims and a laboratory campaign.

The unit occupies the first developing chapter position in Quarto. Its six local
sections need not match the outline's four-section planning layout. The preface
states that it is a partial provisional chapter. Adjacent publishing/pilot pages
remain development artifacts, not the final Chapter 1-to-2 learning sequence.
The pilot's general results retain their temporary ownership: this introductory
scalar sign development does not move or supersede them. No accepted architecture,
pilot manuscript, figure, computation, test or acceptance decision is modified.

## Checks actually executed

Python 3.12.3, standard library, one-off in-memory checks (no new software module
or repository checker). Numerical agreement supports encoded mathematics only.

For N=32768 uniform points t=kT/N, T=1e-6 s, form each real product
`m=2*A*cos(2*pi*fR*t+phi)*cos(2*pi*fL*t+lambda)` and project it as
`z=(2/N)*sum(m*exp(-2j*pi*fI*t))*G*exp(1j*beta)`.
This computes from real RF/LO signals rather than the asserted envelope formula.
Integer cycles reject the sum tone and negative IF component. The grid is a
numerical quadrature, not a proposed acquisition sampling interface.
Use manuscript table values with angles converted to radians, fR=1e9,
fI=1e7 and fL=990e6 or 1010e6. Absolute assertion tolerance was 2e-10 for
angles in degrees, voltage magnitudes in V, power in W or complex differences
in their stated units; this is a numerical tolerance, not uncertainty.

Results:

| Check | Observed result |
|---|---|
| Lower-side IF phases | 12.000000000014, 52.000000000012 degrees |
| Lower-side comparison | 39.999999999998 degrees |
| Upper-side IF phases | −18.000000000010, −44.000000000008 degrees |
| Upper-side comparison | −25.999999999999 degrees |
| Added 25 ps channel-2 RF delay | Lower 31 degrees; upper −17 degrees, within tolerance |
| Equal LO phases/zero added IF phases | Lower +45 degrees; upper −45 degrees |
| Peak power | Direct real-waveform average agrees with 0.0001 W and squared envelope/100 |

Also passed: real-waveform reconstruction at six phase values and 31 epochs;
common complex-reference rotation invariance; channel-order sign reversal;
179 to −179 degree continuation gives +2 degrees; −125 ps and +875 ps give
identical 1 GHz phasors; epoch-intercept substitution with zero/100 Hz frequency
difference. Analytical authorial inspection checks volts versus volts-squared,
rad versus degree conversion, zero differential contribution limits, the
physical-delay sign, IF normalization and both input-referral equations.

The printed complex envelopes agree with the direct calculation:
`0.0978147600734+j0.0207911690818` and
`0.0615661475325+j0.0788010753607` V. Their product is
`0.00766044443119+j0.00642787609687` V². Human-readable intermediate values
and extraction derivation are in the manuscript; code is not needed to read it.

`python3 scripts/check_repo.py`: passed (13 scaffold paths; no scientific check).
`python3 -m pytest`: could not start, pytest absent; no packages installed and
no full-suite success claimed. Existing pilot code/tests were unchanged, not rerun.

`XDG_CACHE_HOME=/tmp/chapter1-quarto-cache quarto render book --to html`:
passed on five pages with Quarto 1.10.18. HTML source inspection: 39 local HTML
fragment links resolve across five pages; no duplicate IDs or unresolved `??`;
the new citation resolves to the references page; 90 manuscript mathematics
spans and MathJax loading markup are present. Structural presence does not
establish visible typesetting or layout quality.

Attempted Firefox headless screenshot of the local manuscript (20-second timeout,
1440x1100 window). It failed with exit 46: display/xcb initialization and inability
to create `/run/user/1000/snap.firefox` on a read-only filesystem. No screenshot,
pixel inspection, PDF check or offline MathJax verification is claimed.
Quarto's newly generated `book/.gitignore` was removed after inspection; root
ignore rules already cover its local cache. No publishing infrastructure changed.

## Focused authorial review and limitations

This is self-check, not independent engineer review. Checked the connections
from input planes to mixer orientation, positive-IF response, extraction and
input referral. In particular, upper-side conversion reverses RF/LO phase but
does not negate an IF phase added afterward. The counterexample retains the
same illustrative responses explicitly, without assuming real retune invariance.
A physical path insertion is distinguished from merely changing the common
complex reference; single-tone delay ambiguity is retained.

Source examination and original derivation provenance are in the
[source note](../references/source-notes/phase-comparison.md). No empirical
receiver evidence was obtained. Ideal tone/filter/gain models do not establish
image rejection, compression limits, phase fidelity, achievable endpoint phase,
real acquisition performance or settling. No numerical accuracy guarantee follows.

Reader-facing prose avoids project identifiers, status tables and review metadata.
Essential steps develop Euler decomposition, power averaging, cosine mixing and
integer-cycle extraction internally. Whether the progression is sufficiently
accessible is an authorial judgment, not an observed educational result.

No consequential defect remained identified after these checks; this is not a
claim that all defects have been found. No change to accepted pilot conclusions
was needed. Review must still challenge the definitions, signs, positive-frequency
construction, reference changes and applicability envelope.

## Completion and human decisions

Completed bounded draft with specified mathematical/numerical and HTML structural
checks. Physical applicability has been assessed for the declared idealized
model; hardware validation, independent specialist review, actual RF-engineer
reader assessment and visual publication inspection remain pending. No human
technical acceptance or publication readiness is granted.

Ask an actual reader to reconstruct the two output waveforms, recover the input
phase with known nuisance terms, change orientation/reference, and explain why a
quiet/repeated observation cannot establish input accuracy or unique delay.
Record assistance and critical errors; revise/reassess on sign/reference failures.
A mathematical/receiver reviewer must decide whether the local conventions may
be adopted more broadly. Keep ISSUE-001/002/005 and U-01–U-10 open as applicable.

Stop after this delivery. The next queue unit is not started or authorized here.

Final preservation/integration audit: all accepted architecture/decision files and
six pilot artifacts match the initial byte hashes; Git index unchanged. Among
snapshotted project files, only the authorized current-work record changed.
The manuscript hash matches this record. Forty-seven local Markdown links across
fourteen delivery files resolve; twenty-nine Markdown table rows have consistent
column counts. Final newline, whitespace and `git diff --check` checks passed.
No code, test, dependency manifest, commit, deployment or next-unit work was added.
