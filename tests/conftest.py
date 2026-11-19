"""Load the standalone scripts in this repo without packaging them.

Each topic folder is a plain directory (some with hyphens), so tests import
modules by file path instead of relying on packages.
"""
from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def load(relpath: str):
    path = ROOT / relpath
    # Sibling imports (e.g. reverse_linked_list -> singly_linked_list) need the
    # module's own folder on sys.path; it stays there, which is harmless here.
    if str(path.parent) not in sys.path:
        sys.path.insert(0, str(path.parent))
    name = relpath.replace("\\", "_").replace("/", "_").replace(".py", "")
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module
