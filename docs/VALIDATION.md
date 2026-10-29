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
