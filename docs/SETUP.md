# Local Setup

## Requirements
- Git and Python 3.11 or newer.
- Codex CLI installed and authenticated separately.
- Quarto CLI for book rendering; TeX distribution for PDF rendering.

Verify on your target workstation:

```bash
git --version
python --version
codex --version
quarto --version
```

## Bootstrap

```bash
cd coherent-receiver-reference
git init
python -m venv .venv
source .venv/bin/activate  # Windows PowerShell: .venv\Scripts\Activate.ps1
python -m pip install -e '.[dev]'
python -m pytest
python scripts/check_repo.py
```

These install requirements are **not locked** yet. Freeze tested dependencies in a lock file once the target development system is chosen.

## Codex

Launch from repository root with `codex`. First ask it to read `AGENTS.md`, the charter and `current-work.md`, and report the authorized next task. Check whether `.codex/config.toml` is loaded under local trust rules and verify approval/sandbox behavior in your own installation. Do not assume every file edit requests approval.

Network access is disabled in the proposed sandbox config. Research requiring external access should be explicitly authorized and its source evidence recorded. Avoid placing secrets or proprietary technical documents in the repository.

## Quarto (provisional)

```bash
cd book
quarto render --to html
quarto render --to pdf
```

PDF rendering requires a suitable TeX installation. Review equations, citations, cross-references and layout manually. Rendering does not establish physical validity.

## Engineering example

```bash
python -m pip install -e '.[dev]'
python engineering/examples/phase_transfer_demo.py
```

It generates a mathematical illustration in ignored `build/`; not a validated receiver model.
