#!/usr/bin/env python3
"""Search the skill reference files for one or more keywords."""

from __future__ import annotations

import argparse
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
REF_DIR = ROOT / "references"


def make_pattern(terms: list[str]) -> re.Pattern[str]:
    escaped = [re.escape(term) for term in terms if term.strip()]
    if not escaped:
        raise ValueError("Provide at least one non-empty search term.")
    return re.compile("|".join(escaped), re.IGNORECASE)


def iter_matches(pattern: re.Pattern[str]) -> list[tuple[Path, int, str]]:
    matches: list[tuple[Path, int, str]] = []
    for path in sorted(REF_DIR.glob("*.md")):
        for lineno, line in enumerate(path.read_text(encoding="utf-8").splitlines(), start=1):
            if pattern.search(line):
                matches.append((path, lineno, line.strip()))
    return matches


def main() -> int:
    parser = argparse.ArgumentParser(description="Search markdown references for keywords.")
    parser.add_argument("terms", nargs="+", help="One or more keywords to search for")
    args = parser.parse_args()

    pattern = make_pattern(args.terms)
    matches = iter_matches(pattern)

    if not matches:
        print("No matches found.")
        return 1

    for path, lineno, line in matches:
        rel_path = path.relative_to(ROOT)
        print(f"{rel_path}:{lineno}: {line}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
