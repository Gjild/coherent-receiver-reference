# Repository Map and Growth Rules

| Path | Owns |
|---|---|
| `project/` | mission, scope, current task, competence and intellectual architecture, decisions |
| `standards/` | conventions, technical writing and evidence/acceptance rules |
| `book/` | human-readable Quarto manuscript (provisional tool choice) |
| `engineering/src/` | reusable, documented computational methods |
| `engineering/examples/` | reproducible illustrations |
| `tests/` | software and mathematical checks with explicit scope |
| `references/` | verified bibliography and claim-level evidence notes |
| `reviews/` | actual technical decisions and unresolved issues |
| `templates/` | optional small-format repeatable records |
| `.codex/` | local Codex runtime defaults, subject to trust and client version |
| `.agents/skills/` | add only proven recurring specialized workflows; none installed initially |

## Growth policy
1. Add chapters after the competence/dependency/architecture study; do not precommit final taxonomy.
2. Make one source of truth for each consequential engineering relationship, with explicit reuse.
3. Keep code libraries independent of chapter numbering; books may be reorganized.
4. Keep raw copyrighted references out of version control. Store permitted source notes in the repo.
5. Store generated output separately; do not report a render as fresh computational verification.
6. Keep independent human review of consequential claims distinguishable from automated checks.
7. Introduce complexity only after encountering a concrete limitation.
