"""
export_epub.py

Compiles the manuscript into an EPUB file using Pandoc.
Chapters are concatenated in order and passed to Pandoc with metadata.

Usage:
    python scripts/export_epub.py [--output dist/source-of-magic.epub]

Requires: pandoc (https://pandoc.org/installing.html)
"""

import argparse
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).parent.parent
MANUSCRIPT_DIR = ROOT / "manuscript"
DEFAULT_OUTPUT = ROOT / "dist" / "source-of-magic.epub"


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()

    chapters = sorted(MANUSCRIPT_DIR.glob("chapter-*.md"))
    if not chapters:
        print("No chapters found in manuscript/.")
        sys.exit(1)

    args.output.parent.mkdir(parents=True, exist_ok=True)

    with tempfile.NamedTemporaryFile(suffix=".md", mode="w", encoding="utf-8", delete=False) as tmp:
        for chapter in chapters:
            tmp.write(chapter.read_text(encoding="utf-8"))
            tmp.write("\n\n")
        tmp_path = Path(tmp.name)

    try:
        result = subprocess.run(
            [
                "pandoc", str(tmp_path),
                "--output", str(args.output),
                "--metadata", "title=Source of Magic",
                "--metadata", "author=Source of Magic Contributors",
                "--toc",
            ],
            capture_output=True,
            text=True,
        )
    finally:
        tmp_path.unlink()

    if result.returncode != 0:
        print(result.stderr)
        sys.exit(result.returncode)

    print(f"EPUB written to: {args.output.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
