# Visual inspection environment repair — 2026-10-30

**Historical pre-adjustment record:** current post-adjustment capability and remaining
limits are recorded in [the successful private-pipe retest](visual-inspection-retest.md).
The original failed trials below are retained as evidence.

Status: diagnosis reproduced; repair and visual acceptance incomplete. No human
technical acceptance. Illustration production and K08–K10 remain stopped.

## Observed execution environment

- Ubuntu 24.04.4 LTS, x86_64 Linux 7.0.0-28-generic; `systemd-detect-virt`
  reports `none`. Kernel has no Microsoft/WSL marker; WSL environment variables
  absent. Host process cgroup is a KDE Konsole user-session scope. These support
  a native Linux desktop host, with no detected VM/WSL/container. Codex tool
  commands themselves run in isolated mount/user/PID namespaces; this does not
  mean the host is a container. Undetectable outer virtualization is unverified.
- UID 1000, non-root, bash `/bin/bash` invoked with `-c`; inherited `SHELL=/bin/bash`.
  Parent visible as `codex-linux-sandbox`, `--apply-seccomp-then-exec`, managed
  filesystem policy: repository and `/tmp` writable; root readable; `.git`,
  `.codex`, `.agents`, `.aws` protected. Network restricted. `NoNewPrivs=1`,
  `Seccomp=2`, effective capabilities zero. Approved host diagnostic commands
  run outside that parent sandbox as the same user, not as root.
- Codex CLI 0.165.0; user configuration requests `gpt-6.1-sol`, high reasoning;
  repository trusted. Project config: workspace-write, on-request approvals,
  `network_access=false`. The active tool environment uses managed permissions
  and automatic approval review; project TOML alone does not describe it fully.
  CLI works for help/version with a read-only alias warning. Fresh CLI runtime
  initialization needs scoped host launch; reviewer shell still must be read-only.
- Browser: Brave 149.1.91.175, actual executable
  `/opt/brave.com/brave/brave`; `/usr/bin/brave-browser` resolves to its shell
  wrapper, which masks exit failures with `|| true`. The canonical smoke script
  prefers the actual executable and isolates XDG config/data as well as profile.
  `/usr/bin/firefox` is an Ubuntu Snap transition launcher, with
  `/snap/bin/firefox -> /usr/bin/snap`; `/snap/firefox/current` is mounted.
  Chromium/Google Chrome were not found on PATH. Firefox version not established.
- `DISPLAY=:0`, no WAYLAND_DISPLAY; X11 socket `/tmp/.X11-unix/X0` exists.
  `XDG_RUNTIME_DIR=/run/user/1000`, DBus address points to its bus socket.
  Presence of a socket does not demonstrate permitted display access. Headless
  mode is the intended route and requires no display service connection.
- Runtime directory is UID-owned mode 0700 but read-only in Codex sandbox;
  `~/.cache` and `~/snap` also not writable there. `/tmp` is writable, mode 1777;
  smoke output/profile/runtime/cache/config/data use private fresh directories.
  Existing personal browser profiles are not used. Sandbox inability to write
  system runtime paths is policy, not a reason to change ownership/permissions.
- Resource snapshot: open-file soft/hard limits 4096/1048576, process limit 55328,
  approximately 4.3 GB MemAvailable, 4 GB swap mostly free, 186 GB disk free.
  No OOM or process-limit error observed. Cgroup aggregate memory/PID limits were
  unavailable at the simple queried root paths; full host constraints unverified.
  Inotify max_user_instances=128, max_user_watches=65536. System file-nr was
  23534/0/9223372036854775807. No evidence for system-wide file-table exhaustion.

## Reproduction and diagnosed mechanisms

[Evidence directory](visual-inspection-evidence/) preserves exact command,
stdout/stderr and JSON results for each attempt, plus the minimal HTML and initial
hashes of pre-existing changed/untracked project files. Trials used fresh profiles
and outputs, ordinary text and an inline SVG circle; no Quarto dependencies.
Python subprocess status uses negative signal numbers; -5 is SIGTRAP (shell 133).
Timeouts terminate only the process group started by that attempt; status 124 is
the diagnostic harness timeout status.

| Execution | Status / elapsed | Stderr / outcome |
|---|---|---|
| Permitted sandbox, Brave | -5 / 0.216 s | Crashpad `setsockopt: Operation not permitted (1)`; no PNG |
| Permitted sandbox, Firefox | 46 / 0.416 s | Qt cannot connect to `:0`; cannot create `/run/user/1000/snap.firefox` (read-only); no PNG |
| Scoped approved host, Brave | 124 / 20.066 s | `inotify_init() failed: Too many open files (24)`; timeout; no PNG |
| Scoped approved host, Firefox | 124 / 20.036 s | Snap mount-namespace warnings, then headless-mode message; timeout; no PNG |

The Brave commands differ only in fresh profile/output path:

```bash
/opt/brave.com/brave/brave --headless \
  --user-data-dir=/tmp/coherent-inspection-diagnosis/permitted-brave/profile \
  --window-size=1000,700 \
  --screenshot=/tmp/coherent-inspection-diagnosis/permitted-brave/image.png \
  file:///tmp/coherent-inspection-diagnosis/minimal.html
```

Exact host and Firefox variants are in `*-command.txt`. The owner can repeat the
portable current smoke command from repository root in a normal terminal:

```bash
python3 scripts/visual_inspection.py
```

It prints an unused output location and records its exact browser invocation.
This avoids requiring the owner's terminal to reuse this session's temporary paths.

Independent minimal probes, without browser code:

```python
import ctypes, os, socket
left, right = socket.socketpair(socket.AF_UNIX, socket.SOCK_STREAM)
try:
    left.setsockopt(socket.SOL_SOCKET, socket.SO_PASSCRED, 1)
finally:
    left.close(); right.close()
libc = ctypes.CDLL(None, use_errno=True)
fd = libc.inotify_init1(os.O_CLOEXEC)
print(fd, ctypes.get_errno())
if fd >= 0:
    os.close(fd)
```

Run probes separately if the socket call raises. Sandbox socketpair creation
succeeds, but SO_PASSCRED fails EPERM for stream, datagram and seqpacket pairs;
host SO_PASSCRED succeeds. Thus a sandbox socket restriction is directly established;
seccomp is the likely enforcement layer, not independently instrumented here.
No crash-handler disabling or sandbox weakening was attempted.

Inotify creation fails EMFILE inside and outside the sandbox in a tiny process
with a few descriptors. Linux documents EMFILE for either per-user inotify-instance
exhaustion or per-process descriptor exhaustion; the latter is excluded by this
small probe and its 4096 descriptor allowance ([Linux inotify_init(2)](https://man7.org/linux/man-pages/man2/inotify_init.2.html)).
Host same-UID `/proc/*/fd` enumeration found 184 inotify **descriptors**, including
inherited duplicates, across desktop applications, editors and Codex processes.
That is not an exact count of instances and does not identify a leaking process.
Resource exhaustion is established; whether repairing it fully resolves Brave's
timeout requires the post-repair identical-command comparison. Firefox host
warnings/timeout are not assigned a proven root cause.

## Repair boundary and persistence

No system setting, software version, permission, security control or unrelated
process has been changed. The system-level proposal awaiting owner authorization
is `fs.inotify.max_user_instances=512` in a new single-purpose sysctl.d file;
rationale, risks and rollback are in [the canonical procedure](../docs/VISUAL-INSPECTION.md).
Existing policy search found only `/usr/lib/sysctl.d/30-tracker.conf` setting
max_user_watches=65536; that separate value should not be changed.

Repository work completed so far: mandatory AGENTS.md route, concise procedure,
and executable Python-standard-library smoke/capture script. The script fails
explicitly at preflight rather than retrying arbitrary flags. Ordinary sandbox
execution was exercised and exited 2 with both socket and inotify blockers.
Fresh-session scoped host execution also exited 2 at inotify preflight.
Successful captures and image inspection remain unverified. Nothing here clears the visual gate.

## Demonstration and acceptance ledger

| Required evidence | Result |
|---|---|
| Minimal local HTML/SVG screenshot | Failed in ordinary and host trials; no pixels |
| A: representative existing SVG to pixels | Pending resource repair |
| B: author examines actual raster pixels | Not demonstrated |
| C: complete Quarto page with equation/figure/labels/caption | Eleven-page scratch render passed (exit 0); pixel inspection not demonstrated |
| D: separate fresh reviewer examines attached actual pixels | Not demonstrated |
| Fresh Codex uses only repository instructions to capture and inspect | Failed acceptance: discovered/executed procedure; host preflight still blocked |
| Independent atan2 correction reassessment | Completed: no consequential defect; raw findings and hashes preserved |

The original visual audit and independent findings are preserved. Manuscript,
accepted architecture, mathematical conventions and illustrations are not edited
by this repair. No commit/push/publication/install is authorized or performed.

## Mathematics reassessment and checks

Fresh independent reviewer `01a18bdf-e8ad-7600-968d-ab4ce18c5ac6` completed its
turn and returned a final response; CLI final-output file was produced. The
original shell exit status was lost across the server restart; a `turn.completed`
event and complete final response establish completion, not a claimed OS exit code.
[Raw findings](visual-inspection-evidence/atan2-findings.md) and
[seven input hashes](visual-inspection-evidence/atan2-inputs.sha256) are preserved.
Invocation: `codex exec --ephemeral -C /tmp/coherent-atan2-reassessment
--skip-git-repo-check -m gpt-6.1-sol -c model_reasoning_effort='"high"'
-s read-only --json -o /tmp/coherent-inspection-diagnosis/atan2-review.md -`,
with frozen prompt on stdin and separate JSONL/stderr outputs. Author disposition
is appended to the original visual-pedagogy review; its original bytes remain an
unchanged prefix. Manuscript and audit hashes still match the task baseline.

Quarto 1.10.18 scratch render exited 0 and produced eleven HTML pages at
`/tmp/coherent-html-repair.wxRNwS/repo/book/_book`; render stderr/stdout are
preserved in the evidence directory. It used the canonical scratch-copy command
with temporary XDG cache; it did not verify MathJax loading or pixels.
`python3 -m py_compile scripts/visual_inspection.py`,
`python3 scripts/check_repo.py` and `git diff --check` passed. No regression suite
was needed for manuscript mathematics, which this task did not change. No pytest
execution is claimed. The smoke script's browser-success branch remains untested
on this blocked host; it is a proposed canonical capture route, not a demonstrated
permanent repair.

## Fresh-session acceptance test — completed, acceptance failed

Fresh ephemeral author-workflow context `01a18be4-443a-7d72-8024-0016e5cca85a`
was launched with GPT-6.1 Sol / high requested, `--approve-for-me`, repository
working directory and no inherited conversation. Unlike an independent technical
reviewer, this discovery test was supposed to read root AGENTS.md and active
project state. It discovered and read the canonical procedure, inspected the
script, ran `python3 scripts/visual_inspection.py` in the ordinary sandbox, and
obtained automatic approval for the identical invocation outside the parent
sandbox. Both script executions exited 2. The host retry's socket probe succeeded,
but its inotify probe still reported `Too many open files`; no capture was
attempted by the script and no image was produced or opened.

[Fresh-session final findings](visual-inspection-evidence/fresh-session-findings.md),
[prompt](visual-inspection-evidence/fresh-session-prompt.txt), both environments
and both result JSONs are preserved. The fresh CLI exited 0 after reporting the
blocker; that is successful diagnostic execution, **not successful visual
inspection**. Discovery/scoped-approval persistence is demonstrated; required
pixel-based fresh-session reproducibility is not. Workflow input hashes were
recorded before closeout status edits; no capture-code change followed the test.

## Outstanding owner action and stopping decision

The inotify resource change remains awaiting explicit owner authorization and
application in the owner's normal terminal; none was inferred from elapsed time
or from the replacement AGENTS.md. No privileged command was run. A concrete
proposed config is staged only as a temporary review artifact at
`/tmp/coherent-inspection-diagnosis/90-coherent-visual-inspection.conf`; it has
not been installed. Risks and rollback are in the canonical procedure.

After the host resource repair, rerun the original minimal browser command (fresh
profile/output) as well as the canonical smoke script. Only a successful comparison
can establish whether the known inotify failure fully accounts for the host
timeout. Then perform A–D and repeat the fresh-session pixel test. The sandbox's
socket restriction itself is not repaired; scoped approved host capture is the
proposed policy-preserving route, still unqualified. This bounded task cannot be
reported as a completed permanent repair. Visual remediation cannot safely resume
yet; no new illustrations or K08–K10 work began.
