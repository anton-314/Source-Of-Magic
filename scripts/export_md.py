"""
export_md.py

Concatenates all chapters from manuscript/ into a single Markdown file.
Useful as a quick plaintext export or as input for other tools.

Usage:
    python scripts/export_md.py [--output dist/source-of-magic.md]
"""

import argparse
from pathlib import Path

ROOT = Path(__file__).parent.parent
MANUSCRIPT_DIR = ROOT / "manuscript"
DEFAULT_OUTPUT = ROOT / "dist" / "source-of-magic.md"


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()

    chapters = sorted(MANUSCRIPT_DIR.glob("chapter-*.md"))
    if not chapters:
        print("No chapters found in manuscript/.")
        return

    args.output.parent.mkdir(parents=True, exist_ok=True)

    with args.output.open("w", encoding="utf-8") as out:
        out.write("# Source of Magic\n\n")
        for chapter in chapters:
            out.write(chapter.read_text(encoding="utf-8"))
            out.write("\n\n---\n\n")

    print(f"Markdown written to: {args.output.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
