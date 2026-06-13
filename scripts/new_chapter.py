"""
new_chapter.py

Creates the next chapter file in manuscript/ with the correct zero-padded number.

Usage:
    python scripts/new_chapter.py
    python scripts/new_chapter.py "The Storm Breaks"   # optional title
"""

import sys
from pathlib import Path

MANUSCRIPT_DIR = Path(__file__).parent.parent / "manuscript"


def next_chapter_number() -> int:
    existing = sorted(MANUSCRIPT_DIR.glob("chapter-*.md"))
    if not existing:
        return 1
    last = existing[-1].stem  # e.g. "chapter-03"
    return int(last.split("-")[1]) + 1


def main() -> None:
    title = sys.argv[1] if len(sys.argv) > 1 else ""
    number = next_chapter_number()
    filename = MANUSCRIPT_DIR / f"chapter-{number:02d}.md"

    heading = f"# Chapter {number:02d}" + (f" — {title}" if title else "")
    filename.write_text(f"{heading}\n\n*Chapter text goes here.*\n", encoding="utf-8")

    print(f"Created: {filename.relative_to(Path.cwd())}")


if __name__ == "__main__":
    main()
