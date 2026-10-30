# Coherent Receiver Theory and Design

**Status: the owner provisionally accepts the Chapters 1–7 and relative-phase
pilot visual-pedagogy milestone for HTML-based analytical teaching and continued
textbook development under [ADR-0007](project/decisions/ADR-0007-provisional-html-visual-pedagogy-acceptance.md).
This does not establish publication readiness, human specialist approval, hardware
validation, educational effectiveness, PDF/offline compatibility or
assistive-technology compliance.**

This repository develops a mathematically rigorous, physically defensible and practically useful advanced textbook/reference for experienced RF engineers learning coherent receiver engineering. The book, not an autonomous design agent, is the primary deliverable.

## Start here

1. Read [`project/charter.md`](project/charter.md) for the mission and binding objectives.
2. Read [`AGENTS.md`](AGENTS.md) before using Codex.
3. Read [`project/current-work.md`](project/current-work.md) for stage status: the competence inventory is provisionally accepted for planning; the [technical coverage and knowledge-dependency architecture](project/architecture.md) is provisionally accepted for planning under [ADR-0003](project/decisions/ADR-0003-provisional-architecture-acceptance.md), subject to its review qualifications. The [book-architecture package](project/book-architecture.md) is provisionally accepted for guiding textbook development under [ADR-0004](project/decisions/ADR-0004-provisional-book-architecture-acceptance.md), subject to its review qualifications. The [corrected pilot](book/relative-phase-stability.qmd) is now accepted for
   ADR-0005's limited use; its [review record](reviews/relative-phase-pilot.md)
   preserves evidence and unresolved limits. The owner has since approved the
   [sustained authoring method](project/sustained-authoring-strategy.md). Its first
   [Chapter 1 unit](book/phase-comparison.qmd) is provisionally accepted as a
   mathematically checked, bounded teaching draft under
   [ADR-0006](project/decisions/ADR-0006-provisional-phase-comparison-acceptance.md),
   within its idealized model and stated conventions. Independent specialist
   validation, reader effectiveness, physical performance and publication readiness
   remain unestablished. K02–K04 are checked provisional teaching drafts; the
   K05–K07 batch and completed visual-pedagogy milestone are tracked in
   current-work.md. The owner has provisionally accepted the HTML visual milestone;
   K08–K10 are the next authorized autonomous batch, not started in this closeout.
4. Read [`docs/SETUP.md`](docs/SETUP.md) for installation and local checks.
5. Read [`docs/REPOSITORY-MAP.md`](docs/REPOSITORY-MAP.md) before adding files.

## Ready-to-run checks

```bash
PYTHONPATH=engineering/src python3 -m unittest discover -s tests -p test_relative_phase.py -v
PYTHONPATH=engineering/src python3 engineering/examples/relative_phase_pilot.py
python3 scripts/check_repo.py
python3 -m pytest
```

The pilot's 19 standard-library tests and example run without extra packages.
The full pytest suite additionally needs declared dependencies; pytest and NumPy
were absent at the earlier pilot closeout; pytest remains absent on the current computer. Calculations are illustrative; passing tests establish
selected mathematical/software properties, not receiver validation.

## Publication

The Quarto HTML book includes the first bounded Chapter 1 draft, publishing
demonstration, corrected pilot and developing foundational units. HTML rendering
passes under the recorded environment. The approved visual-pedagogy milestone
has completed actual browser math/layout inspection and separate-context review
for Chapters 1–7 and the pilot, within the declared models and inspected widths.
See the [visual review and acceptance limits](reviews/visual-pedagogy-review.md);
the owner has provisionally accepted this HTML milestone under ADR-0007's limits.
Every future authoring batch starts with a fresh executed and actually inspected
[visual environment smoke test](docs/VISUAL-INSPECTION.md).
With Quarto available, render from the repository root:

```bash
XDG_CACHE_HOME=/tmp/relative-phase-quarto-cache quarto render book --to html
```

The temporary cache path handles this environment's read-only default cache.
Output is in book/_book/index.html. PDF rendering requires a suitable LaTeX
installation and was not run. See [validation status](docs/VALIDATION.md).

## Authoring policy

Unreviewed material is marked draft. Human review is required for acceptance of consequential engineering results. Do not silently promote exploratory calculations to design authority. Do not add large-scale infrastructure without a demonstrated need.
