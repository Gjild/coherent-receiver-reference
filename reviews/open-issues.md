# Open Issues

- ISSUE-001: Pilot-local conventions remain explicit; book-wide convention adoption and specialist mathematical review remain open. Limited pilot acceptance under ADR-0005 does not settle them.
- ISSUE-002: Quarto HTML rendering is verified for the pilot. Browser visual mathematics/layout inspection, offline MathJax availability and PDF rendering remain unverified; earlier scaffold observations are historical.
- ISSUE-003: Locally verified codex-cli 0.165.0, configured GPT-6.1 Sol / high,
  trusted project and fresh read-only CLI review with continuation. Runtime startup
  required approved execution outside the parent sandbox; reviewer shell probe
  returned EROFS. Exact runtime model routing is not independently introspectable.
- ISSUE-004: Inventory development closed for planning use following [project-owner provisional acceptance](../project/decisions/ADR-0002-provisional-competence-baseline.md). Specialist technical review and all inventory §8 uncertainties remain open; this decision is not independent validation.
- ISSUE-005: Select tested dependency versions and generate reproducible lock/environment record.
- ISSUE-006: Architecture planning review closed with [project-owner provisional acceptance](../project/decisions/ADR-0003-provisional-architecture-acceptance.md) on 2026-10-29 following review with external AI assistance. Acceptance covers book architecture, annotated table-of-contents and intellectual-organization planning only; it does not independently validate technical results. Inventory U-01–U-10 and their [coverage §6 dispositions](../project/technical-coverage.md) remain open. Preserve the four qualifications: allow motivating examples before full quantitative prerequisites; develop K02–K07 from the declared RF-engineer baseline without hidden specialist prerequisites; further review interferometry, vector antenna/polarization models and application-processing boundaries while retaining essential coherent-receiver reasoning internally; test educational and engineering adequacy through actual textbook development, including the later dual-channel relative-phase-stability pilot. Anchor suitability, implementation/production depth, source evidence and specialist technical review remain development obligations. The subsequent book-planning stage has since closed for provisional use under [ADR-0004](../project/decisions/ADR-0004-provisional-book-architecture-acceptance.md).

- ISSUE-007: Book architecture provisionally accepted for guiding textbook development on 2026-10-29 under [ADR-0004](../project/decisions/ADR-0004-provisional-book-architecture-acceptance.md), following external AI-assisted review. Preserve early receiver relevance and consequential calculations in Chapters 1–7; continuous D-COM/ARR/RAD/MET engineering developments including justified iteration and production; flexible part/chapter/section boundaries; and all prior technical qualifications. Planning acceptance does not establish mathematical correctness, physical-model validity, educational effectiveness, experimental verification or receiver-performance compliance. The subsequent pilot development has now closed for the limited use in ADR-0005; all other scope, review and evidence qualifications remain. Existing scope, conventions, specialist-review and evidence issues remain open.


## Historical pilot implementation update — 2026-10-29

- ISSUE-001: Pilot-local conventions now explicit; book-wide adoption and human
  mathematical review remain pending. No convention approval is inferred.
- ISSUE-002: Quarto 1.10.18 HTML rendering now verified using a writable temporary
  cache. Visual browser math/layout inspection remains incomplete after failed
  browser attempts. PDF remains untested and outside this pilot.
- ISSUE-005: Python supports the dependency-free new calculations; pytest and
  NumPy are absent. Full existing suite and tested dependency-environment record
  remain pending. No lockfile or dependency installation was introduced.
- ISSUE-004/006/007 and U-01–U-10: accepted planning qualifications preserved.
  Pilot delivered with illustrative endpoint comparison, eight new checks,
  source examinations and an unexecuted measurement protocol. No physical,
  specialist or educational acceptance is inferred. See
  [pilot review](relative-phase-pilot.md) for unresolved claims and human decisions.
- No further chapters/reference designs or bench campaign begin automatically.

## Historical focused correction update

All nine requested corrections have implemented dispositions in
[the pilot review](relative-phase-pilot.md). Nineteen pilot tests and HTML
rendering pass; the full pytest suite remains blocked by absent dependencies.
Static uncertainty is excluded from the DC-rejecting band statistic, regression
references are explicit, and calibration access/timing/precision is specified.
This makes the bounded analytical pilot a candidate for provisional human
technical review, not an accepted or physically validated receiver method.
Pending: hardware envelopes/settling/alias and fixture evidence, specialist
assessment, actual reader trials and browser visual inspection.


## Current pilot acceptance and stage boundary

The owner provisionally accepts analytical teaching and technical-authoring
workflow use under [ADR-0005](../project/decisions/ADR-0005-provisional-relative-phase-pilot-acceptance.md).
Pilot development is closed; this does not close physical validation, specialist
assessment, actual reader evaluation or publishing-inspection obligations.
The accepted artifacts and reconsideration triggers are in the ADR; all nine
correction dispositions remain in [the review](relative-phase-pilot.md).

Nineteen pilot tests, the reproducible example and HTML render were rerun at
closeout. Full pytest remains unexecuted because pytest/NumPy are absent.
No physical experiment or new source examination occurred. Earlier candidate/
not-started statements above describe their recorded stages.

Historical next-stage boundary: post-pilot assessment had not started at pilot
closeout. The subsequently authorized activity is recorded below.


## First sustained-authoring unit — accepted and closed, 2026-10-29

[ADR-0006](../project/decisions/ADR-0006-provisional-phase-comparison-acceptance.md)
records owner acceptance of the unchanged Chapter 1 unit as a mathematically
checked, bounded teaching draft for continued development, within its idealized
model, conventions, checked derivations and illustrative example. The
[review](phase-comparison.md) retains evidence limits. ISSUE-001 remains open for
book-wide convention adoption and specialist examination; ISSUE-002 for visual
publication inspection; ISSUE-005 for the dependency environment/full test suite.
Independent specialist validation, actual reader effectiveness and physical
performance remain unestablished. Inventory/application adequacy issues remain.

Nonblocking editorial obligations are recorded canonically in ADR-0006: later
sampled-observation linkage, consideration of reference/orientation diagrams and
prevention of unnecessary derivation duplication. They do not reopen the unit.
Next: **scalar stochastic phase reasoning — selected K02 / Chapter 2 material —
not yet started**. Stop after administrative closeout.

## K02–K04 batch disposition — 2026-10-29

Separate AI reviews and correction reassessments completed; no unresolved critical
finding remains within the bounded teaching units. Evidence and owner decisions:
[current batch report](../project/current-work.md). AI review does not close
ISSUE-001/002/005, specialist/reader obligations or U-01–U-10. No next unit is authorized.

## K05–K07 batch boundary — 2026-10-29

Three bounded teaching drafts and connected Chapters 1–7 AI assessment completed;
[batch report](../project/current-work.md). No unresolved consequential review
finding remains in this bounded use. Reproducible baseline and unit checkpoints
are recorded there. K06's first review was replaced after historical-author-summary
exposure; final review evidence is explicitly AI-assisted. ISSUE-001/002/005,
U-01–U-10, qualified specialist/reader and physical-evidence obligations remain open.
No K08 or hardware campaign follows without owner authorization.
