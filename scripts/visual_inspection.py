#!/usr/bin/env python3
"""Local Chromium screenshot smoke test; private DevTools pipe, no installed packages."""
import argparse
import ctypes
import hashlib
import json
import os
from pathlib import Path
import shlex
import shutil
import signal
import socket
import struct
import subprocess
import tempfile
import time


def probes():
    facts = {}
    for name in ('DISPLAY', 'WAYLAND_DISPLAY', 'XDG_RUNTIME_DIR', 'XDG_CACHE_HOME', 'TMPDIR'):
        facts[name] = os.environ.get(name)
    for label, path in (
        ('inotify_instance_limit', '/proc/sys/fs/inotify/max_user_instances'),
        ('inotify_watch_limit', '/proc/sys/fs/inotify/max_user_watches'),
    ):
        facts[label] = Path(path).read_text().strip() if Path(path).exists() else None
    try:
        a, b = socket.socketpair()
        try:
            a.setsockopt(socket.SOL_SOCKET, socket.SO_PASSCRED, 1)
        finally:
            a.close()
            b.close()
        facts['unix_passcred'] = 'OK'
    except OSError as exc:
        facts['unix_passcred'] = str(exc)
    libc = ctypes.CDLL(None, use_errno=True)
    fd = libc.inotify_init1(os.O_CLOEXEC)
    if fd >= 0:
        os.close(fd)
        facts['inotify_init'] = 'OK'
    else:
        facts['inotify_init'] = os.strerror(ctypes.get_errno())
    return facts


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--browser', default=os.environ.get('BROWSER_BIN'))
    parser.add_argument('--backend', choices=('pipe', 'cli'), default='pipe',
                        help='private DevTools pipe (Node built-ins); cli retained for diagnosis')
    parser.add_argument('--output', type=Path, help='new evidence directory (must not exist)')
    parser.add_argument('--source', type=Path, help='trusted local HTML or SVG; default: minimal smoke page')
    parser.add_argument('--width', type=int, default=1000)
    parser.add_argument('--height', type=int, default=700)
    parser.add_argument('--timeout', type=int, default=30)
    parser.add_argument('--wait-ms', type=int, default=3000, help='page readiness budget in ms (CLI backend: virtual-time budget)')
    args = parser.parse_args()
    if min(args.width, args.height, args.timeout) <= 0 or args.wait_ms < 0:
        parser.error('dimensions/timeout must be positive and wait-ms nonnegative')
    if args.source and (not args.source.is_file() or args.source.suffix.lower() not in ('.html', '.svg')):
        parser.error('--source must be an existing local .html or .svg file')
    out = args.output.resolve() if args.output else Path(tempfile.mkdtemp(prefix='coherent-visual-'))
    if args.output:
        out.mkdir(parents=True, mode=0o700, exist_ok=False)
    facts = probes()
    candidates = ('/opt/brave.com/brave/brave', 'chromium', 'chromium-browser', 'google-chrome', 'brave-browser')
    browser = shutil.which(args.browser) if args.browser else next((shutil.which(x) for x in candidates if shutil.which(x)), None)
    facts['browser'] = browser
    facts['output'] = str(out)
    (out / 'environment.json').write_text(json.dumps(facts, indent=2) + '\n')
    print(json.dumps(facts, indent=2), flush=True)
    if facts['unix_passcred'] != 'OK' or facts['inotify_init'] != 'OK' or not browser:
        (out / 'result.json').write_text(json.dumps({'exit_status': 2, 'capture_attempted': False,
                                                    'image_exists': False, 'blockers': facts}, indent=2) + '\n')
        print('BLOCKED: see docs/VISUAL-INSPECTION.md. No screenshot attempted; no visual inspection established.')
        return 2
    source = args.source.resolve() if args.source else out / 'smoke.html'
    if not args.source:
        source.write_text('''<!doctype html><meta charset="utf-8"><title>Visual smoke test</title>
<body style="background:white;color:#111;font:24px sans-serif"><h1>Codex visual smoke test</h1>
<p>Text and SVG: a blue circle.</p><svg xmlns="http://www.w3.org/2000/svg" width="240" height="180">
<circle cx="120" cy="90" r="60" fill="#1464b4"/>
<text x="120" y="170" text-anchor="middle" font-size="20">Radius 60 px</text></svg></body>''')
    env = os.environ.copy()
    for name, directory in (('XDG_CACHE_HOME', 'cache'), ('XDG_RUNTIME_DIR', 'runtime'),
                            ('XDG_CONFIG_HOME', 'config'), ('XDG_DATA_HOME', 'data'), ('TMPDIR', 'tmp')):
        p = out / directory
        p.mkdir(mode=0o700)
        env[name] = str(p)
    profile = out / 'profile'
    profile.mkdir(mode=0o700)
    cmd = [browser, '--headless', f'--user-data-dir={profile}',
           f'--window-size={args.width},{args.height}', f'--virtual-time-budget={args.wait_ms}',
           f'--screenshot={out / "image.png"}', source.as_uri()]
    if args.backend == 'pipe':
        node = shutil.which('node')
        if not node:
            parser.error('pipe capture requires installed Node; do not install automatically')
        cmd = [node, str(Path(__file__).resolve().with_name('visual_capture.mjs')),
               browser, source.as_uri(), str(out), str(args.width), str(args.height), str(args.wait_ms)]
    (out / 'command.txt').write_text(shlex.join(cmd) + '\n')
    (out / 'browser-version.txt').write_text(subprocess.check_output([browser, '--version'], text=True, env=env, timeout=5))
    started = time.monotonic()
    timed_out = False
    with (out / 'stdout.txt').open('w') as stdout, (out / 'stderr.txt').open('w') as stderr:
        process = subprocess.Popen(cmd, env=env, stdout=stdout, stderr=stderr, start_new_session=True)
        try:
            status = process.wait(timeout=args.timeout)
        except subprocess.TimeoutExpired:
            timed_out = True
            os.killpg(process.pid, signal.SIGTERM)
            try:
                process.wait(timeout=2)
            except subprocess.TimeoutExpired:
                os.killpg(process.pid, signal.SIGKILL)
                process.wait()
            status = 124
    result = {'exit_status': status, 'timed_out': timed_out,
              'seconds': round(time.monotonic() - started, 3), 'source': str(source),
              'source_sha256': hashlib.sha256(source.read_bytes()).hexdigest(),
              'backend': args.backend, 'viewport': [args.width, args.height], 'image_exists': (out / 'image.png').is_file()}
    if result['image_exists']:
        data = (out / 'image.png').read_bytes()
        if data[:8] == b'\x89PNG\r\n\x1a\n' and len(data) >= 24:
            result['image_dimensions'] = list(struct.unpack('>II', data[16:24]))
            result['image_sha256'] = hashlib.sha256(data).hexdigest()
    (out / 'result.json').write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps(result, indent=2))
    if status or 'image_dimensions' not in result:
        print('FAILED: inspect stderr.txt; file generation is not visual inspection.')
        return 1
    print(f'CAPTURED: {out / "image.png"}; now open the actual PNG with the image tool.')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
