# Visual inspection

Canonical route for manuscript figures and rendered pages. Capture is distinct
from inspecting pixels; neither establishes physical validity or human acceptance.

**Different-computer retest (2026-10-30):** the existing pipe helper captures the
smoke image with `/usr/bin/node` v26.12.1 and `/usr/bin/brave` 156.1.98.62.
Select this browser with `--browser /usr/bin/brave`; the default discovery list
does not include that executable name. Ordinary sandbox preflight denies
`SO_PASSCRED`; the scoped host invocation succeeds with browser sandboxing retained.
The observed inotify instance limit is already 1024 and allocation succeeds;
no limit adjustment is indicated. Earlier machine paths and resource findings
below are historical, not setup instructions for this computer. Author inspected
the actual smoke PNG; group correction review receives that PNG separately.

**Post-adjustment status (2026-10-30):** live inotify limit 512; allocation succeeds.
The installed Brave CLI `--screenshot` route still times out. Private DevTools-pipe
capture through the same browser now produces inspectable SVG and complete-page
PNGs. Author pixel inspection, fresh read-only reviewer raster inspection and
fresh repository-only capture/inspection succeeded; results are recorded in the [retest record](../reviews/visual-inspection-retest.md).
These capability tests do not accept existing illustrations or authorize remediation.

## Batch-start obligation

At the start of **every future authoring batch**, execute a new smoke capture and
inspect its actual PNG before manuscript/figure development, even on a previously
qualified computer. Record paths/versions, command, exit, image dimensions/hash
and concrete visible content in the batch review record. Supply this batch's smoke
PNG to its first fresh read-only technical/visual reviewer alongside actual figure
and full-page/crop images. Prior successes remain historical evidence.

Use the existing pipe backend and a fresh short output path. Where the ordinary
sandbox denial is already established, use the documented scoped host invocation;
do not repeat the original host investigation or weaken browser sandboxing.
Diagnose changed dependencies/permissions precisely if capture fails and preserve
the blocked visual gate. Do not infer success from metadata or source parsing.

Develop, mathematically/graphically check, render, inspect and separately review
indispensable figures alongside each bounded unit's physical argument. Freeze
manuscript/model/code, requirements/source passages and PNGs; correct consequential
findings in dependent material and obtain fresh targeted reassessment. Retain
durable hashes and supplied images when temporary directories may disappear.
[ADR-0007](../project/decisions/ADR-0007-provisional-html-visual-pedagogy-acceptance.md)
records the completed HTML milestone's scoped owner acceptance and outstanding
format/accessibility/reader-evidence limits. This adds a routine workflow obligation;
it does not change the capture helper or require repeating its original qualification.

## Environment and smoke test

Required: Linux, Python 3 with its standard library, installed Node.js (24.14.0
tested; built-in modules only), an installed Chromium-family browser, Codex with image viewing/attachment support, and Quarto for HTML checks.
No browser automation package, network debugging port, desktop display or personal browser profile
is required. This route must be requalified on another OS/browser/version.

From repository root, in an ordinary terminal or a Codex execution tool:

```bash
python3 scripts/visual_inspection.py
```

The script prints its unique evidence directory. To select the installed binary
and a new output directory explicitly:

```bash
BROWSER_BIN=/opt/brave.com/brave/brave python3 scripts/visual_inspection.py \
  --output "$PWD/build/visual-smoke"
```

`BROWSER_BIN` is configurable; the path above is this workstation's installed
binary, not a portable requirement. The output directory must not already exist;
use a fresh name on every run. Outputs include `environment.json`, `command.txt`,
`browser-version.txt`, `stdout.txt`, `stderr.txt`, `result.json` and `image.png`.
The command and result record exact arguments, status, elapsed time, timeout,
source/image hashes and PNG dimensions. The default private-pipe backend uses
`scripts/visual_capture.mjs`; `browser-command.json` records the actual browser
arguments. `page.json` records document/font/image readiness, viewport, full content
rectangle and Chromium protocol version; `browser-exit.json` records browser exit.
No raster data is fabricated from DOM/source. The browser itself supplies the PNG. Browser profile, cache, config, data,
runtime and temporary directories are private to that run. Never use a personal
profile. Exit 2 means preflight blocked; exit 1 means capture failed; exit 0 means
a valid PNG was captured, **not** that visual inspection passed.

On a new environment, run the smoke test in the ordinary permitted Codex context
first. Preflight stops before browser launch if `unix_passcred` is denied. This
restriction is already established on this workstation: use a scoped approved
execution of the same script command as the ordinary host user, or have the owner
run it in a normal terminal. Do not repeatedly launch a browser inside the known
incompatible sandbox. The script's read-only probes may be rerun safely.

Keep the repository sandbox enabled. Approval covers only the bounded capture
invocation, not an unrestricted shell. The browser retains its own security
sandbox; the helper communicates through inherited private pipes, not a listening
port. Do not add `--no-sandbox`, disable seccomp, change permissions, run as root,
or change global Codex policy. A denied approval remains a blocker. The script
never escalates itself. This is the least-privileged route **demonstrated here**;
it does not establish that no other policy-preserving configuration exists.

Open the returned `image.png` with Codex's actual image-viewing tool (`view_image`
in this environment; tool names vary). The expected 1000 × 700 image has a heading
“Codex visual smoke test”, a text line, a blue circle and “Radius 60 px”. Record
what you can actually see. An image filename, XML parse, dimensions/hash, OCR,
HTML source or tool success without returned pixels does not satisfy inspection.

## SVG and rendered HTML

Capture a trusted existing figure at a declared viewport:

```bash
python3 scripts/visual_inspection.py \
  --source book/figures/relative-phase-reference-planes.svg \
  --width 1400 --height 600 --output build/visual-svg
```

Open the PNG, check original aspect ratio/content coverage, then inspect labels
at readable scale. Record clipping, line/arrow visibility, contrast, units,
reference planes, signal direction and agreement with the declared model. A
screenshot can include white margins. It is not an AI-generated replacement asset.

Render a scratch copy to preserve the working tree (set `VISUAL_WORK` to a new,
absolute, writable location):

```bash
VISUAL_WORK=$(mktemp -d "${TMPDIR:-/tmp}/coherent-html.XXXXXX")
mkdir "$VISUAL_WORK/repo"
cp -a book references "$VISUAL_WORK/repo/"
XDG_CACHE_HOME="$VISUAL_WORK/cache" quarto render "$VISUAL_WORK/repo/book" --to html
python3 scripts/visual_inspection.py \
  --source "$VISUAL_WORK/repo/book/_book/publishing-pilot.html" \
  --width 1440 --height 2200 --wait-ms 10000 --timeout 40 \
  --output "$VISUAL_WORK/page"
```

The pipe backend waits for document completion, MathJax startup when present,
fonts and images, then captures the measured full content rectangle.
Inspect the **complete page** PNG and readable detail views. The publishing pilot
contains an equation, aligned derivation, symbol table, existing technical figure,
labels, caption and page navigation. Verify the last content and bottom navigation are in
frame. Compare the full content rectangle in `page.json` to PNG dimensions;
independently check coverage in pixels. CLI-backend viewport captures are not
automatically full-page. For long chapters capture sufficient height and inspect overlapping
readable crops covering all content; retain the original full image. Do not infer
unseen content from a thumbnail. Record viewport and output dimensions.

The existing HTML uses externally hosted MathJax. Confirm typeset equations in
pixels; readiness metadata alone cannot prove correct visible equations. Network
failure, raw TeX, blank equations or missing assets blocks that page check. Do not
silently change math renderer to make the acceptance test pass. This procedure
does not establish offline math, PDF layout, responsive behavior, all chapters,
accessibility or scientific adequacy of the existing figures.

## Separate-context image review

Freeze manuscript, source SVG, rendered HTML/assets and actual PNGs in a new
review packet; hash those bytes with `sha256sum`. Supply accepted requirement
files, model equations and necessary source passages, without author verdicts,
conversation, current-work, status summaries or previous review dispositions.
Use a minimal packet `AGENTS.md` specifying read-only review and no delegation or
connectors. Keep author dispositions separate from reviewer findings.

Launch a **new** reviewer (never `resume`/`fork`), e.g. from a normal terminal:

```bash
codex exec --ephemeral --skip-git-repo-check -C "$REVIEW_PACKET" \
  -m gpt-6.1-sol -c 'model_reasoning_effort="high"' -s read-only \
  -i "$REVIEW_PACKET/figure.png" -i "$REVIEW_PACKET/page.png" \
  --json -o "$REVIEW_OUTPUT/findings.md" - \
  < "$REVIEW_OUTPUT/prompt.txt" > "$REVIEW_OUTPUT/events.jsonl" \
  2> "$REVIEW_OUTPUT/stderr.txt"
```

Set `REVIEW_PACKET`/`REVIEW_OUTPUT` to separate absolute directories first. Supply
readable crops as additional `-i` attachments if full-page text is reduced. Ask
for pixel-specific observations, dimensions, legibility, labels, clipping,
contrast, captions and agreement with the physical/mathematical model. Require
an explicit account of images actually visible, unreadable areas and exposure.
CLI `--image` attachment and `--sandbox` are documented in the
[official Codex CLI reference](https://learn.chatgpt.com/docs/cli/reference).

Codex initialization can require writes outside the parent sandbox even with a
read-only reviewer shell. Request scoped launch approval; **retain `-s read-only`**.
Record invocation/exit, requested model/effort, input hashes and returned findings.
Do not claim independently verified backend routing. A failed invocation, image
attachment failure or source-only review is incomplete review.

## Safe diagnosis

Inspect `environment.json`, then `stderr.txt`/`result.json`. The smoke test probes
local Unix socket credentials and one inotify instance without changing limits.
On this workstation (Ubuntu 24.04, Codex 0.165.0, Brave 149.1.91.175):

- Sandbox: `SO_PASSCRED` gets EPERM; the same host probe succeeds. Use only a
  scoped approved host capture; no security-control changes are prescribed.
- Before adjustment: `inotify_init1()` got EMFILE at instance limit 128 with few
  open descriptors. Owner temporarily raised the live limit to 512; allocation
  now succeeds. The prior failure indicated exhausted per-user instances, not a
  need for
  arbitrary browser flags or a higher `ulimit -n`. Descriptor counts across
  processes can include duplicates. No process leak has been established.
- Firefox `/usr/bin/firefox` is a Snap launcher, not a tested alternative route;
  its runtime-directory failure inside the sandbox is separate from Brave.
- DISPLAY is inherited but unnecessary for headless mode. Writable private XDG
  paths do not remove socket restrictions or repair host resource exhaustion.

The CLI screenshot path still timed out after the resource adjustment, including
a hypothesis-driven `--disable-gpu` test. Direct private-pipe capture works, even
when a successful capture logs the same transient GPU diagnostic. GPU errors
alone therefore do not identify a capture failure. The upstream CLI hang remains
unresolved; do not keep trying arbitrary flags. `--backend cli` preserves the
old route for explicit diagnosis; the supported default is `--backend pipe`.

**Minimum proposed persistent resource configuration (owner-controlled):** live
512 is verified; reboot persistence is not. If the owner elects to retain the
resource allowance, create a new `/etc/sysctl.d/90-coherent-visual-inspection.conf`
containing only `fs.inotify.max_user_instances = 512`, and apply that single file
with `sudo sysctl -p /etc/sysctl.d/90-coherent-visual-inspection.conf` in the owner's
normal terminal. Do not overwrite an existing file without preserving it.
This raises permitted watcher-instance memory use and does not change browser or
Codex security controls. Roll back by removing the new file (or restoring previous
contents) and running `sudo sysctl -w fs.inotify.max_user_instances=128`, the
previous live value. Do not change max_user_watches, ulimit, permissions or security
settings. The resource increase was necessary to clear the measured allocation
failure but was insufficient to repair the CLI screenshot path.
Owner may instead close their own unneeded watcher-heavy applications to diagnose
usage; Codex must not terminate unrelated processes. Re-run the probes and the
canonical pipe smoke test after a host/browser change. The same CLI command
comparison has already shown that inotify exhaustion was not the sole failure.

## Evidence and fresh-session gate

Success requires all of: capture exit/dimensions/hashes; actual author pixel
inspection with concrete observations; complete Quarto page coverage and readable
math/figure/caption; a fresh reviewer examining attached pixels; correction and
reassessment where needed. AI findings never grant human Reviewed/Accepted status.
Record failures and unverified aspects explicitly.

After modifying the capture implementation or execution route (not merely updating
acceptance records or batch guidance), start a new Codex session at repository root,
without this conversation, and ask only: “Use repository instructions to execute the
visual-inspection smoke test and inspect its actual image; report evidence and
blockers. Do not author manuscript or figures.” Record whether it discovers this
file through root AGENTS.md, executes the procedure, obtains and opens the image,
and respects scoped approvals. Merely discovering a blocked route is useful
failure evidence, not fresh-session acceptance. Stop if any required gate fails.
