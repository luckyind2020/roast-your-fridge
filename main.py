#!/usr/bin/env python3
"""Roast Your Fridge — prints the one-line fridge roast from entry.txt."""
from pathlib import Path


def load_roast(path: Path) -> str:
    """Read the roast line, stripping trailing whitespace and newlines."""
    text = path.read_text(encoding="utf-8").strip()
    if not text:
        raise SystemExit("entry.txt is empty — nothing to roast.")
    return text


def main() -> None:
    here = Path(__file__).resolve().parent
    roast = load_roast(here / "entry.txt")
    print(roast)


if __name__ == "__main__":
    main()
