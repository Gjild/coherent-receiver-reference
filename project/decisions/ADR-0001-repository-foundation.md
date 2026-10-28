# ADR-0001 — Initial Repository Foundation

**Status:** proposed / scaffold implemented; human adoption pending.

## Context
A long-lived textbook needs coherent manuscript source, reproducible selected calculations, source evidence and minimal Codex governance. Intellectual architecture is not yet accepted.

## Decision
Use a single Git-ready repository with a short `AGENTS.md`, stable mission and active task documents, a provisional Quarto book, Python source/tests, bibliography and evidence templates. Do not pre-populate final chapters or a knowledge graph.

## Alternatives
- LaTeX-primary book: potentially advantageous for demanding derivations; retain as a candidate pending typography pilot.
- Chapter-local scripts and bibliography: simpler initially but prone to duplicate computational results.
- Comprehensive custom knowledge database: deferred as costly without demonstrated need.

## Validation required
Quarto HTML/PDF renders, source/bibliography formatting, mathematical cross-references, Git and Codex behavior on the target workstation. All remain local-environment-dependent.

## Reversal
The manuscript backend may change without moving project governance or computational assets.
