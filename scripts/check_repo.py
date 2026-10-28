"""Small dependency-free scaffold integrity check; not a content-validity test."""
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
REQUIRED = [
    'README.md', 'AGENTS.md', '.codex/config.toml', 'project/charter.md',
    'project/current-work.md', 'project/competence-inventory.md',
    'standards/notation-and-conventions.md', 'standards/sources-and-evidence.md',
    'book/_quarto.yml', 'book/index.qmd', 'book/publishing-pilot.qmd',
    'references/references.bib', 'pyproject.toml',
]
missing = [p for p in REQUIRED if not (ROOT / p).is_file()]
if missing:
    print('Missing required files:', *missing, sep='\n- ')
    sys.exit(1)
print(f'Scaffold integrity OK: {len(REQUIRED)} required files present.')
print('This check does not assess scientific correctness, sources, or render quality.')
