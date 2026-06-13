"""
word_counter.py

Counts the total word count of the manuscript by reading all chapter-XX.md files
from the manuscript/ directory in order and summing up their word counts.

Intended usage:
    python scripts/word_counter.py

Expected output:
    A per-chapter breakdown of word counts and a grand total for the full manuscript.

This script is meant to give contributors and the author a quick overview of the
current length of the novel without having to open each chapter individually.
"""

import re
import sys
from pathlib import Path

MANUSCRIPT_DIR = Path(__file__).parent.parent / "manuscript"


def strip_markdown(text: str) -> str:
    text = re.sub(r"^#{1,6}\s+", "", text, flags=re.MULTILINE)
    text = re.sub(r"[*_~`]+", "", text)
    text = re.sub(r"!?\[.*?\]\(.*?\)", "", text)
    text = re.sub(r"<!--.*?-->", "", text, flags=re.DOTALL)
    return text


def count_words(text: str) -> int:
    return len(strip_markdown(text).split())


def main() -> None:
    chapters = sorted(MANUSCRIPT_DIR.glob("chapter-*.md"))

    if not chapters:
        print("No chapters found in manuscript/.")
        sys.exit(1)

    total = 0
    rows = []

    for path in chapters:
        words = count_words(path.read_text(encoding="utf-8"))
        total += words
        rows.append((path.stem, words))

    width = max(len(name) for name, _ in rows)
    print(f"\n{'Chapter':<{width}}  Words")
    print("-" * (width + 8))
    for name, words in rows:
        print(f"{name:<{width}}  {words:>6,}")
    print("-" * (width + 8))
    print(f"{'TOTAL':<{width}}  {total:>6,}\n")


if __name__ == "__main__":
    main()
