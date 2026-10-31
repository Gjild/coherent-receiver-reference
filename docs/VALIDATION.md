# K11–K13 bounded authoring and integration checks — 2026-10-31

Three bounded treatments and11new figures are integrated in canonical Chapters1,
11 and12. [Development, findings and connected assessment](../reviews/k11-k13-development.md)
records sources, calculations, frozen inputs, separate read-only AI scrutiny,
author corrections and reassessments. These are checked provisional teaching
drafts, not complete chapters, human acceptance or demonstrated hardware.

- Fresh private-pipe batch smoke succeeded before authoring; actual PNG opened.
  Browser sandbox and established SVG/capture helpers remain unchanged.
- `python3 -m unittest discover -s tests -p '*stdlib.py'`:73pass, including rerun
  after relative-tolerance corrections. `PYTHONPATH=engineering/src python3 -m
  unittest discover -s tests -p 'test_relative_phase.py'`:19pass.92selected total.
  `python3 -m pytest` fails: no pytest module. No installation; SciPy unavailable.
- All58SVGs regenerate byte-identically; all47prior figures preserved. Independent
  K11/K12/K13 curve checks:1928+1446+1837=5211vertices, rounding≤0.000501px.
  Distinct real-waveform/source/covariance/observation/budget/state calculations
  and seeded nonlinear surrogates support mathematical consistency only.
- Final Quarto1.10.19 local HTML render succeeds:16pages,535local links,59image
  uses; no missing targets/fragments, duplicate IDs, unresolved markers or absent
  image alternatives. Actual assets/full pages and overlapping readable crops
  were inspected. Final preface/Chapter1/11/12 captures are1440×2200,
  1425×11164,1425×11286,1425×24953. Prior unit reviewers inspected all new assets;
  final reviewer inspected14representative/complete/transition PNGs, with detailed
  readability conclusions restricted to supplied crops.
- Fresh read-only Sol/high unit reviews and consequential targeted reassessments
  are archived separately from author dispositions. Connected review verifies146
  frozen hashes and independently reproduces gain/aperture conflicts, transfer
  orientation, correlated allocations, sensitivity and restoring decisions.
  Missing prerequisite test/fixture packet evidence was supplied in fresh targeted
  contexts. Final18-file numerical review passes all19physical-model tests;
  zero/large-scale-error probes reject after normalized-comparison corrections.
  Earlier omitted-fixture failure and usage-limit failure remain recorded.
- Repository integrity:13required paths;75protected baseline files match. Prior
  Chapter1 prefix, K11 feasibility body, standards, accepted architecture and
  canonical prerequisite derivations remain preserved. Development supplements
  are grouped/explained without changing accepted chapter/appendix ownership.
- Reviewers disclose incidental metadata/status text embedded in accepted planning
  requirements or standards; no separate author conversation/current-work/prior
  review records were supplied. Source access boundaries and exposure are recorded
  per invocation. Same-model scrutiny retains correlated failure risks; requested
  model/effort is not backend attestation. No human Reviewed/Accepted state granted.

Unit checkpoints: `cd2b802` (K11), `74400a1` (completed K12), `c2bd3cb` (K13), with
final connected closeout checkpointed separately. Hardware feasibility, source/
thermal/state parameters, Gaussian-tail adequacy, reader effectiveness, specialist
review, PDF/offline mathematics and exhaustive responsive/assistive inspection
remain conditional or unperformed. No owner decision blocks bounded draft closure.
**Stop after K13/integration; no K14, push or external publication.**

---

# K08–K10 bounded authoring checks — 2026-10-31

Three provisional units and ten reproducible figures are developed in canonical
Chapters 8–10. [Development, findings and integration assessment](../reviews/k08-k10-development.md)
separates author dispositions from frozen read-only AI reviewer outputs. No
human technical acceptance, hardware confirmation or reader-trial evidence is
claimed. ADR-0007's earlier scoped acceptance is preserved without extension.

- Fresh batch-start private-pipe smoke succeeded after the recorded sandbox and
  socket-length diagnostics; its actual PNG was inspected before authoring.
  The capture helper/route and browser sandbox are unchanged.
- `python3 -m unittest discover -s tests -p '*_stdlib.py' -v`: 57 pass.
  `PYTHONPATH=engineering/src python3 -m unittest discover -s tests -p 'test_relative_phase.py' -v`:
  19 pass. Total available selected regressions: 76.
- `python3 -m pytest --version`: fails because pytest is absent. SciPy comparison
  also cannot run; SciPy is absent. No installation. Independent analytical,
  source-draw, quadrature, covariance-inverse and stored-curve checks are recorded;
  these establish mathematical/software consistency, not hardware validity.
- All 47 SVGs regenerate byte-identically, including the ten new batch figures.
  Actual standalone assets, complete unit HTML pages and readable crops were
  inspected by the author and separately contextualized read-only AI reviewers.
- Scratch `quarto render …/book --to html` with XDG cache under /tmp: 14 pages,
  no reported warnings. All 421 local links/fragments resolve; no duplicate IDs
  or unresolved markers; 48 image uses have alt text. Final actual captures and
  21 readable final unit-page crops include the new interface derivation,
  probability table, exercises and Chapter 7→8→9→10 navigation.
- `python3 scripts/check_repo.py`: all 13 required paths present. Whitespace
  passes. All 62 protected baseline files match: prior technical manuscripts,
  37 figures, graphical helper, accepted standards, architecture and plans.
  The preface, authoring configuration and current-work are authorized exclusions.
- Review packets preserve SHA-256 manifests, actual PNGs and supplied inputs;
  raw findings/events remain separate from author records. Earlier metadata
  exposure and targeted replacement contexts are disclosed. Same-model contexts
  retain correlated failure risks; requested model/effort is not backend identity
  attestation. AI review confers no human Reviewed/Accepted state.

Desktop HTML analytical use is the tested format. Full pytest, PDF/offline math,
exhaustive responsive/assistive-technology assessment, qualified specialist review,
reader effectiveness and empirical receiver/source-path evidence remain open.
The K08–K10 stopping boundary applies; K11 is not authorized by these checks.

Earlier records below retain their historical dates and limitations.

---

# HTML visual acceptance — administrative closeout, 2026-10-30

The owner provisionally accepts the completed Chapters 1–7/pilot visual milestone
for HTML-based analytical teaching and continued textbook development under
[ADR-0007](../project/decisions/ADR-0007-provisional-html-visual-pedagogy-acceptance.md),
identifying artifact/evidence revision `b6d7fe68c60edf35baf7c54518e2c07c7821df1f`.
This records owner acceptance; it adds no human specialist approval or empirical
validation. The [appended closeout](../reviews/visual-pedagogy-review.md#owner-acceptance-and-administrative-closeout-2026-10-30)
keeps the decision distinct from earlier AI findings and author dispositions.

Administrative repository, local-link/fragment, whitespace and SHA-256 preservation
checks are recorded in [the closeout evidence](../reviews/visual-pedagogy-evidence/visual-acceptance-closeout-checks.json).
All book manuscripts and 37 SVGs, generating/mathematical code and tests, accepted
architecture/conventions, frozen evidence and prior decision bytes are preserved.
This documentation-only closeout does not rerun the 57 selected tests, SVG
regeneration, Quarto rendering, smoke capture or independent image/technical reviews;
the successful earlier checks below retain their original execution provenance.
The capture implementation/route is unchanged. Every future authoring batch must
execute and inspect a fresh smoke PNG before manuscript/figure development.

Nonblocking obligations remain: presentation/secondary-label/description polish,
broader responsive and assistive-technology checks, PDF/offline math, actual reader
evaluation, qualified specialist review, empirical hardware evidence and the full
pytest suite when dependencies are available. Acceptance establishes none of those
outcomes or final publication readiness. Existing scientific and local-convention
boundaries remain in force. K08–K10 are the next authorized autonomous batch;
no manuscript work on them begins in this closeout. Stop after its local checkpoint.

Earlier records below retain their historical dates, pending decisions and checks.

---

# Visual-pedagogy milestone checks — 2026-10-30

The [execution/final assessment](../reviews/visual-pedagogy-review.md) records
completed independent review/corrections, actual PNG/page inspection and limits.
Chapters 1–3 completed evidence and bytes are preserved. Chapters 4–6, Chapter 7
and pilot groups now have successful fresh read-only reviews; the historical
usage-limit invocation is not counted as completed review.

- Node `/usr/bin/node` v26.12.1 and Brave `/usr/bin/brave` 156.1.98.62 verified.
  The documented private-pipe smoke and figure/full-page capture work with scoped
  host execution and browser sandbox retained. No host-policy/helper changes.
- `python3 -m unittest discover -s tests -p '*stdlib.py'`: 38 pass.
- `PYTHONPATH=engineering/src python3 -m unittest discover -s tests -p 'test_relative_phase.py'`:
  19 pass. Total available selected regressions: 57.
- `python3 -m pytest`: cannot start, pytest absent. Full suite unperformed;
  no installation. Mathematical alternatives do not establish physical validation.
- `python3 scripts/check_repo.py`: 13 required paths present; whitespace passes.
- Scratch SVG regeneration: all 37 byte-identical. Chapters 1–3 manuscripts and
  17 illustrations match clean resume baseline `2d2e4df`.
- Quarto 1.10.19/Python 3.14.7: all 11 HTML pages render. All 285 local HTML
  links/fragments resolve; no duplicate IDs/unresolved markers; 38 figure uses
  have alt text. Capture hashes match the reviewed/rendered inputs.
- Actual standalone and full-page pixels/readable crops inspected by author
  and separate reviewers. Pilot current captures are 1425×25846 and 945×27670;
  supplementary narrow Chapters 4–7 checks are recorded. Meaningful captions,
  alt text and line styles supplement colors. Minor narrow-layout/label polish
  and generic standalone descriptions remain documented.

Recommend bounded HTML visual acceptance; the owner decides. No human acceptance,
qualified specialist validation, reader trials, hardware evidence, PDF/offline math,
exhaustive responsive/assistive-technology testing or publication readiness follows.
Stop before K08–K10. Earlier records retain their historical dates and limitations.

---

# K05–K07 reproducibility and checks — 2026-10-29

- Reconciled inspected 15-file staged set unchanged into `3b669a7`; no unstaged
  or unrelated files were present. ADR-0006 manuscript hash matches. Clean Git
  archive baseline rendered successfully. History preserved; no destructive Git.
- Clean Git archive of `94b434a`: Python 3.12.3; Quarto 1.10.18;
  codex-cli 0.165.0 observed. No installation or dependency-lock claim.
- `PYTHONPATH=engineering/src python3 -m unittest discover -s tests -p '*stdlib.py' -q`:
  24 passed (13 prior foundations + 11 new-batch).
- `PYTHONPATH=engineering/src python3 -m unittest discover -s tests -p test_relative_phase.py -q`:
  19 passed. These are mathematical/software checks, not physical validation.
- `python3 scripts/check_repo.py`: passed (13 required paths).
- Clean archive Quarto HTML render with XDG_CACHE_HOME in /tmp: passed, 11 pages.
  Parsed HTML: 247 local links/fragments resolve; no duplicate IDs or ?? markers.
- `python3 -m pytest --version`: failed; pytest absent. Full suite unperformed.
- Separate read-only AI reviews/corrections and connected progression assessment
  completed. Records disclose replaced K06 history-exposed context, source/image
  access limits, and serialization correction during final reread.
- Sixty-three pre-existing artifacts outside explicitly updated integration/workflow
  files retain starting hashes. No manuscript change to Chapter 1, pilot or K02–K04;
  no acceptance, convention or intellectual-architecture promotion.
- Markdown links and whitespace checked at closeout. Browser pixel inspection,
  PDF/offline mathematics, reader/specialist review and physical experiments absent.

Earlier records below retain their historical dates, evidence and boundaries.

---

# K02–K04 batch checks — 2026-10-29

- `python3 -m unittest discover -s tests -p test_foundation_units_stdlib.py -v`:
  13 passed. Analytical/numerical consistency only, not physical validation.
- `PYTHONPATH=engineering/src python3 -m unittest discover -s tests -p test_relative_phase.py -v`:
  19 passed; preserved pilot regression checks.
- `python3 scripts/check_repo.py`: passed, 13 required scaffold paths.
- `XDG_CACHE_HOME=/tmp/coherent-batch-audit/cache quarto render book --to html`:
  passed, eight HTML pages. Initial default-cache and QUARTO_CACHE_DIR attempts
  failed on the read-only home cache; XDG_CACHE_HOME resolved that failure.
- `python3 -m pytest --version`: failed, pytest absent. No installation.
- Separate reviewer smoke: first runtime initialization failed EROFS; approved
  retry succeeded. Exclusive-create probe inside reviewer shell returned EROFS;
  no probe file was created. Requested model/effort gpt-6.1-sol / high; runtime
  model identity was not independently exposed.
- K02–K04 review records preserve input hashes, findings, source access,
  correction propagation, reassessments and unavailable checks. Initial K02 test
  expected-value transcription was corrected after failure. Reviewer NumPy/SciPy
  attempts failed; reviewers used standard-library alternatives and recorded limits.
- Mechanical Markdown link, HTML ID/fragment, whitespace and baseline-preservation
  checks passed: 8 HTML pages / 152 local links and fragments, 52 Markdown
  links, 16 protected baseline artifacts unchanged, unrelated index entries
  preserved. The first Markdown audit exposed absolute reviewer line-links;
  these were normalized to portable relative manuscript links and the audit rerun. No pixel-level browser inspection,
  PDF render, reader trial, qualified specialist review or physical test occurred.

Earlier records below retain their dates and qualifications.

---

# Administrative closeout: first Chapter 1 unit — 2026-10-29

Owner acceptance is recorded in
[ADR-0006](../project/decisions/ADR-0006-provisional-phase-comparison-acceptance.md)
for the unchanged mathematically checked, bounded teaching draft, within its
idealized model, stated conventions, checked derivations and illustrative example.
Independent specialist validation, actual reader effectiveness, physical receiver
performance and publication readiness are not established.

Closeout checks are repository consistency checks only; earlier mathematics,
rendering, source examination and failed browser/full-suite attempts below retain
their original dates and limitations. No new numerical tests, render, browser
inspection, source examination, human specialist review, reader trial or physical
measurement was performed. No dependencies were installed. Next: scalar stochastic
phase reasoning — selected K02 / Chapter 2 material — not yet started.

Checks actually executed at closeout:

- `python3 scripts/check_repo.py`: passed, 13 required scaffold paths.
- One-off read-only audit: accepted manuscript hash matches ADR-0006; manuscript,
  accepted architecture/previous decisions, pilot and all other snapshotted files
  outside the five administrative updates are byte-for-byte preserved. Git index
  unchanged. Only ADR-0006 is newly added by this task.
- All 55 local Markdown links resolve across the six closeout files; nine table
  rows have consistent column counts. Final newline and whitespace checks pass.
- `git diff --check`: passed. No manuscript, source, standard, computational,
  publishing-configuration or dependency changes were needed.

---

# Current validation: first Chapter 1 unit — 2026-10-29

[The unit review](../reviews/phase-comparison.md) owns actual mathematical checks,
numerical results, manuscript hash and publishing limitations. Direct real-waveform
checks and five-page Quarto HTML generation/structure checks passed. Full pytest
could not start (pytest absent). Firefox screenshot failed on display/runtime
access; no browser visual, PDF, offline typesetting, specialist, learner or physical
validation is asserted. No dependency installation or software changes occurred.
Earlier records below describe their historical artifacts and environments.

---

# Pilot closeout validation — 2026-10-29

Owner acceptance is recorded in
[ADR-0005](../project/decisions/ADR-0005-provisional-relative-phase-pilot-acceptance.md)
for analytical teaching and technical-authoring workflow development only.
Closeout reran the 19 pilot unittest checks, reproducible example, scaffold
integrity and four-page HTML render successfully. Full pytest was attempted but
could not start (pytest absent); NumPy import failed too. No tools were installed.
Browser pixel inspection and PDF rendering were not performed at closeout; prior
visual-inspection limitations remain. No new source examination, specialist
review, reader trial or physical measurement is asserted.

The final audit passed: six accepted SHA-256 values match the unchanged artifacts;
52 local Markdown links and 27 table rows were checked across seven closeout
files; four HTML pages have 32 resolving internal fragment links, no duplicate
IDs and no unresolved cross-references. Both SVGs parse. Eleven protected
planning/decision files are unchanged, as is the Git index. Whitespace checks pass.
The owner's removals of changes.patch/changes.zip are preserved; this task edits
only six existing administrative files and creates ADR-0005.

Accepted artifact hashes and scope are recorded in ADR-0005 and current work. Correction-stage results below remain evidence for the same
unchanged manuscript/computational bytes; they are not new physical proof.

---

# Current validation: relative-phase pilot (2026-10-29)

See [the executed check/review record](../reviews/relative-phase-pilot.md),
including finding-by-finding disposition of the focused correction pass.
The corrected example recalculates asymmetric regression, absolute vs band
uncertainty and snapshot precision/age. pytest was retried and remains unavailable.
No new specialist/reader/measurement evidence is asserted.
Nineteen dependency-free pilot unittest checks pass; the supporting example executes.
Quarto 1.10.18 renders four HTML pages with
`XDG_CACHE_HOME=/tmp/relative-phase-quarto-cache quarto render book --to html`.
Scaffold integrity, protected-file preservation, internal fragment references,
SVG parsing and whitespace checks pass. The final correction audit resolves
32 internal fragment links on four pages, finds no duplicate IDs or unresolved
cross-references, and confirms 11 protected planning documents and pre-existing
archives unchanged from the correction-start snapshot. Exactly ten existing
pilot/support/record files were modified; their inventory is in the review.
HTML output is in `book/_book/index.html`.

The first render failed on a read-only cache. pytest/NumPy are absent, preventing
the complete pre-existing suite; no dependencies were installed. Browser pixel
inspection failed under local display/resource constraints, so visual math and
layout inspection remains pending. Existing MathJax CDN access is required for
browser typesetting. No PDF render, laboratory measurement, independent human
technical review or learner trial is claimed.

The bibliography is populated; two existing entries were re-examined for the
pilot's narrow claims. Historical “empty bibliography/not installed” notes below
are retained as earlier observations, not current statements.

---

# Validation Status for Initial Scaffold

This file must be updated with **actual** executed checks before delivery or use. It is not an engineering acceptance record.

- Project content: proposed/unreviewed.
- Source bibliography: intentionally empty.
- Quarto HTML/PDF render: not verified in scaffold environment.
- Codex project config: based on documented fields; not executed against user's installation.
- Engineering example: mathematical pure-delay identity only; no physical receiver validation.

No hardware measurements, independent engineering reviews, or textbook chapter acceptances have occurred.

## Packaging environment checks (2026-10-28)

- `python -m pytest -q`: **4 passed**.
- `python scripts/check_repo.py`: **passed**, 13 expected paths present.
- `PYTHONPATH=engineering/src python engineering/examples/phase_transfer_demo.py`: **executed**, generated illustrative plot in ignored `build/figures/`.
- Quarto CLI: **not installed**; HTML/PDF not rendered.
- Codex CLI: **not installed**; Codex config not runtime-tested.
- No human technical acceptance, external source examination, or physical measurements performed.
