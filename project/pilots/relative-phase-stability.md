# Dual-channel relative-phase-stability development pilot

**Status:** development completed and provisionally accepted by the project owner
on 2026-10-29 for **analytical teaching and technical-authoring workflow
development** under [ADR-0005](../decisions/ADR-0005-provisional-relative-phase-pilot-acceptance.md).
Its hashes identify the accepted manuscript, figures and computational artifacts.
No physical/hardware, experimental, educational-effectiveness, general-design
or compliance acceptance follows.

## Boundary and deliverables

The manuscript is `book/relative-phase-stability.qmd`. The supporting module,
example and tests use the standard library because the environment lacks NumPy
and pytest. No dependencies were installed or changed. The pure-delay scaffold
retains its existing illustrative qualification.

Two colocated heterodyne channels, common calibration stimulus, narrowband phase
comparison and selected nearby calibration frequencies. Compare shared LO and
local reference-locked synthesis using full endpoint transfer/covariance first,
then declared illustrative envelopes. Include one linked allocation, preference
reversal, calibration/thermal revision, state validity and measurement protocol.
No full receiver, antenna model, distributed synchronization, new bench campaign,
production-yield calculation or subsequent chapter development.

## Ownership and exercised outcomes

| Responsibility | Canonical destination | Selected capability outcomes |
|---|---|---|
| Representations/observable/phase signs | K01/K12, Chapters 1/11 | CAP-002/003/012 |
| Stochastic bridge, observation, covariance and inference | K02–K05/K07, Chapters 2–6 | CAP-004–006/008/009 |
| Physical source/path and conditional allocation | K09/K11/K13/K15b, Chapters 9/12/15 | CAP-001/013/016/043/044 |
| Identifiability, correction and continued validity | K20/K21a–c, Chapters 13/20/23 | CAP-022–025 |
| State, environment and diagnosis | K23/K24, Chapters 21/22 | CAP-017/026/027/032 |
| Models, measurement and bounded evidence | K07/K22/K25/A41, Chapters 6/13/24/32 | CAP-029–031/041 |

These are partial exercises, not completion of all competence dimensions.
Hardware I/V outcomes without executed evidence remain pending. General results
have one temporary home here; future chapter development must move/reuse them.
This does not complete D-MET or replace any accepted treatment specification.

## Focused correction pass

The current manuscript distinguishes constant absolute calibration uncertainty
from DC-rejecting phase noise, identifies fixed-LO combined RF/IF/fixture delay,
and specifies simultaneous-comb access through 32 Msample/s complex acquisition.
Snapshot precision requires 10 ms for compact shared LO or 50 ms for local
synthesis under the declared envelopes. A 2 s center period includes explicit
settling, measurement, latency and invalid-data timing. Nineteen pilot tests pass.
See the [review record](../../reviews/relative-phase-pilot.md) for all nine
finding dispositions and the limited owner acceptance.
Hardware/learner/experimental adequacy is not established.

## Outcomes, limitations and stopping boundary

The integrated development distinguishes observation-specific statistics,
preserves full endpoint transfer/correlation before special cases, demonstrates
a conditional architecture preference reversal, and connects calibration
identifiability to a specified fixed-LO simultaneous-comb acquisition interface.
Snapshot precision changes the local-synthesis procedure from 10 ms to 50 ms;
settling, age and invalid-data timing are explicit. Nineteen checked calculations/
regressions support the conditional analytical argument, not hardware guarantees.

[The review record](../../reviews/relative-phase-pilot.md) preserves outstanding
specialist, physical and learner questions. Fixture slopes, endpoint spectra,
thermal/settling envelopes, acquisition omissions and remaining snapshot
uncertainty need evidence before hardware use. The measurement protocol is
unexecuted. Actual reader effectiveness and browser pixel inspection remain
unverified. Pilot-local conventions and broader standards remain provisional
outside the accepted use; ADR-0002–0004 qualifications remain active.

The development stage is closed for ADR-0005's limited use. Next is **post-pilot
development-method assessment and sustained authoring preparation, not yet
started**. Do not begin that activity, subsequent chapters, reference designs
or laboratory work automatically.
