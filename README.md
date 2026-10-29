# Coherent Receiver Theory and Design

**Status: provisional book-architecture stage closed with planning acceptance for guiding textbook development. Subsequent authoring standards, publishing validation and initial technical pilot work have not started. No textbook chapter or engineering capability has been technically accepted.**

This repository develops a mathematically rigorous, physically defensible and practically useful advanced textbook/reference for experienced RF engineers learning coherent receiver engineering. The book, not an autonomous design agent, is the primary deliverable.

## Start here

1. Read [`project/charter.md`](project/charter.md) for the mission and binding objectives.
2. Read [`AGENTS.md`](AGENTS.md) before using Codex.
3. Read [`project/current-work.md`](project/current-work.md) for stage status: the competence inventory is provisionally accepted for planning; the [technical coverage and knowledge-dependency architecture](project/architecture.md) is provisionally accepted for planning under [ADR-0003](project/decisions/ADR-0003-provisional-architecture-acceptance.md), subject to its review qualifications. The [book-architecture package](project/book-architecture.md) is provisionally accepted for guiding textbook development under [ADR-0004](project/decisions/ADR-0004-provisional-book-architecture-acceptance.md), subject to its review qualifications. Technical authoring standards, publishing validation and the initial technical pilot are subsequent work, not yet started. These acceptances do not establish technical or educational adequacy.
4. Read [`docs/SETUP.md`](docs/SETUP.md) for installation and local checks.
5. Read [`docs/REPOSITORY-MAP.md`](docs/REPOSITORY-MAP.md) before adding files.

## Ready-to-run checks

```bash
python -m pytest
python scripts/check_repo.py
```

The current computational example is **illustrative, not a validated receiver model**. Tests establish mathematical and implementation properties only.

## Publication

A *provisional* Quarto book skeleton is included for future proof-of-concept testing. With Quarto and a suitable LaTeX installation, run:

```bash
cd book
quarto render --to html
quarto render --to pdf
```

Neither render was executed in the environment that packaged this scaffold; see `docs/VALIDATION.md`.

## Authoring policy

Unreviewed material is marked draft. Human review is required for acceptance of consequential engineering results. Do not silently promote exploratory calculations to design authority. Do not add large-scale infrastructure without a demonstrated need.
