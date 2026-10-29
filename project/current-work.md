# Current Work: Provisional Book Architecture Stage Closed

**Closed stage:** provisional book architecture, annotated table of contents and intellectual organization. **State:** provisionally accepted by the project owner on 2026-10-29 as suitable for guiding textbook development under [ADR-0004](decisions/ADR-0004-provisional-book-architecture-acceptance.md), following external AI-assisted review. This is planning acceptance only.

**Subsequent work — not yet started:** technical authoring standards development, publishing validation and the initial dual-channel relative-phase-stability technical pilot. These are future bounded tasks requiring separate authorization; no work on them begins in this closeout.

## Accepted book-planning package

- [Book architecture](book-architecture.md): five proposed parts and 32 chapters, organizational alternatives, learning/reference routes, boundaries and review decisions.
- [Annotated contents](annotated-toc.md): chapter objectives, prerequisites, canonical ownership, 128 substantive section annotations, work/evidence expectations and technical appendices.
- [Book coverage](book-coverage.md): canonical location assignments, all 45 capability outputs/dimensions, dependency/cohesion audits, staged reference designs and seven application/five failure-probe routes.

These organize the accepted knowledge requirements into a provisionally accepted textbook plan. They do not replace the canonical architecture or constitute manuscript content. Counts describe the provisional organization; they are not quality targets, fixed boundaries or adequacy evidence. The four ADR-0003 qualifications are preserved. All substantive source research, derivations, models, solved designs and educational/engineering validation remain future work.

## Earlier baseline and accepted technical package

The [charter](charter.md) governs mission and audience. The [competence inventory](competence-inventory.md) remains the provisional 45-capability baseline governed by [ADR-0002](decisions/ADR-0002-provisional-competence-baseline.md). Historical next-stage statements in that ADR and the inventory describe their earlier closeout; this record gives subsequent status without expanding their acceptance scope.

The accepted planning package consists of:

- [Technical architecture](architecture.md): reader bridges, progression, relationships, reference routes and readiness gate.
- [Technical coverage](technical-coverage.md): canonical treatment specifications, dependencies, capability traceability and gap dispositions.
- [Reference-design plan](reference-design-plan.md): provisional design briefs, example progression and paper stress tests.

ADR-0003 records the accepted Git revision and each document's SHA-256 before administrative closeout edits. Capability definitions, canonical treatment specifications and reference-design briefs are unchanged.

## Acceptance qualifications and outstanding work

1. Learning prerequisites and application treatment requirements must allow motivating examples before full quantitative methods are taught.
2. K02–K07 mathematical bridges must be developed for the declared RF-engineer baseline without hidden specialist prerequisites.
3. Interferometry, vector antenna/polarization models and application-processing scope require further boundary review; essential coherent-receiver reasoning must remain internal.
4. Educational and engineering adequacy must be tested through actual textbook development, including the later dual-channel relative-phase-stability pilot.

Inventory U-01–U-10, technical coverage §6 dispositions, unresolved mathematical conventions, claim-level source work and specialist review obligations remain open. Planning acceptance does not independently validate any derivation, physical model, engineering method, simulation, measurement or hardware-performance claim, nor establish system compliance. No independent specialist approval or unprovided external AI review findings are asserted.

## Historical book-planning checks and evidence boundaries

Checks actually performed on 2026-10-29 for this draft:

- `python3 scripts/check_repo.py`: passed; 13 required scaffold files present.
- One-off read-only audit, kept outside the repository: 32 ordered chapter headings and 128 section headings; explicit referenced section endpoints exist; all 33 K/A treatment identifiers have canonical rows; all 45 capability rows retain the accepted dimensions and evaluated-output audit text.
- The same audit checked consistent table columns in the three new documents, local Markdown link resolution across the three documents and this record, and byte-for-byte preservation against HEAD of the competence inventory, accepted three-document package and ADR-0002/0003. All 25 local links resolve after the status update.
- `git diff --check`: passed after the status update. The one-off audit also checked the new, untracked documents for trailing whitespace and final newlines.
- Authorial inspection of prerequisite/refinement/conditional routes, canonical boundaries, analog alternatives, all seven P routes and five X probes is recorded in book coverage §3–§4. This is an editorial audit, not independent technical review or proof of learning adequacy.

No software tests or book render were run: no engineering code, manuscript or publishing configuration changed. No source passages were newly examined; no derivation, numerical allocation, engineering model, physical measurement or learner assessment was performed. Existing source evidence remains limited to its recorded claims. The new documents and this status record are the only repository changes intended by this stage.

## Historical architecture-closeout checks and evidence boundaries

The 2026-10-28 architecture pass recorded scaffold integrity, in-memory capability/dimension/treatment/link/table audits, an ordering check on a manually transcribed dependency table, authorial paper-route review and `git diff --check`. Those historical checks support planning traceability only; they were not independent technical review, calculations, physical validation or learner assessment.

Closeout checks actually performed on 2026-10-29:

- `python3 scripts/check_repo.py`: passed; 13 required scaffold files present. The initial `python` invocation could not run because that command is unavailable; the installed `python3` was used.
- One-off in-memory audit: all three accepted-package SHA-256 values match their bytes at the recorded Git revision; architecture §§1–4, technical coverage §§1–5 and reference-design plan §§1–4 are byte-for-byte unchanged; the competence inventory and ADR-0002 are unchanged in full.
- One-off in-memory audit: all 43 local Markdown links resolve and Markdown table column counts are consistent across the seven closeout files. No checker or metadata framework was added.
- `git diff --check`: passed. Diff review confirms changes are limited to acceptance/status, qualifications, issue disposition and closeout records.

These are repository consistency checks, not technical validation. Software tests and book renders were not run because no implementation or manuscript changed. No source passages are newly examined and no technical results are independently validated by this closeout.

## Book-architecture acceptance qualifications and closeout

ADR-0004 preserves four review findings: Chapters 1–7 must connect foundations to meaningful receiver questions and consequential calculations early; all four anchors must become continuous engineering developments with justified iteration and production implications; part/chapter/section boundaries remain flexible; and all earlier technical qualifications remain in force. The exact accepted pre-closeout bytes are identified by SHA-256 in that decision, because the planning files were staged additions rather than contents of the recorded HEAD revision.

Acceptance does not establish mathematical correctness, physical-model validity, educational effectiveness, experimental verification or receiver-performance compliance. No new source examination, technical review by an independent specialist, measurement or learner assessment is asserted. Existing U-01–U-10, mathematical conventions, specialist boundaries and evidence gaps remain open. No additional issue blocking this administrative stage closure has been identified; they may restrict subsequent technical uses.

Closeout checks actually performed on 2026-10-29:

- `python3 scripts/check_repo.py`: passed; 13 required scaffold files present.
- One-off read-only audit outside the repository: all three ADR-0004 hashes match both the captured pre-closeout bytes and the existing staged artifacts. The recorded HEAD is context, not a false claim that it contains those additions.
- Preservation audit: the annotated contents after its status paragraph is byte-for-byte unchanged; book architecture and book coverage §§1–4 are unchanged. Protected competence, canonical treatment, reference-design and earlier decision documents are unchanged. All 32 chapter/128 section headings, 33 K/A identifiers and 45 capability dimensions/evaluated-output targets are retained.
- Link/table/whitespace audit: all 50 local Markdown links resolve across the seven closeout files; table columns, final newlines and trailing whitespace are consistent. `git diff --check` passed.
- Scope review: changes are confined to ADR-0004 and administrative status, acceptance, qualification, issue and closeout records in the six authorized existing documents. Existing staged work was preserved; no commit, tag or index update was performed. An unrelated, initially untracked `changes.zip` disappeared during the turn; this task did not edit or remove it, and it was excluded from the final repository-file preservation audit.

These are repository and planning-consistency checks, not mathematical or physical validation. No software tests or book render were run because no engineering implementation, manuscript or publishing configuration changed. No new source passages were examined. The later authoring standards, publishing validation and technical pilot were not executed.

## Stopping boundary

The book-architecture stage is closed for the owner's stated provisional use. Stop here. Technical authoring standards, publishing validation and the initial relative-phase-stability pilot are subsequent work, not yet started. Do not begin manuscript drafting, substantial mathematical derivations, computational modeling, solved designs or publishing infrastructure. Eventual pilot assessment must test actual educational and engineering adequacy, including consequential calculations and changed assumptions, not merely coverage.
