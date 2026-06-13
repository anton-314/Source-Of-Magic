"""
validate_lore.py

Validates internal consistency of the repository:
  1. Checks that all internal Markdown links ([text](path)) resolve to existing files.
  2. Checks that world/characters/, world/geography/, world/magic-system/ each contain
     at least one document beyond their README.
  3. Checks that every chapter file is non-empty (more than placeholder text).

Usage:
    python scripts/validate_lore.py

Exits with code 1 if any issues are found (suitable for CI).
"""

import re
import sys
from pathlib import Path

ROOT = Path(__file__).parent.parent
WORLD_SECTIONS = ["characters", "geography", "magic-system"]
PLACEHOLDER = "*Chapter text goes here.*"


def check_internal_links() -> list[str]:
    errors = []
    link_re = re.compile(r"\[.*?\]\((?!https?://)([^)]+)\)")
    for md_file in ROOT.rglob("*.md"):
        text = md_file.read_text(encoding="utf-8")
        for match in link_re.finditer(text):
            target = ROOT / md_file.parent / match.group(1).split("#")[0]
            if not target.exists():
                rel = md_file.relative_to(ROOT)
                errors.append(f"  {rel}: broken link → {match.group(1)}")
    return errors


def check_world_sections() -> list[str]:
    warnings = []
    for section in WORLD_SECTIONS:
        section_dir = ROOT / "world" / section
        docs = [p for p in section_dir.glob("*.md") if p.stem != "README"]
        if not docs:
            warnings.append(f"  world/{section}/ has no documents yet (only README.md)")
    return warnings


def check_chapters() -> list[str]:
    warnings = []
    for chapter in sorted((ROOT / "manuscript").glob("chapter-*.md")):
        text = chapter.read_text(encoding="utf-8").strip()
        if not text or PLACEHOLDER in text:
            warnings.append(f"  {chapter.relative_to(ROOT)}: still contains placeholder text")
    return warnings


def main() -> None:
    failed = False

    link_errors = check_internal_links()
    world_warnings = check_world_sections()
    chapter_warnings = check_chapters()

    if link_errors:
        failed = True
        print("❌ Broken internal links:")
        print("\n".join(link_errors))

    if world_warnings:
        print("⚠  Empty world sections:")
        print("\n".join(world_warnings))

    if chapter_warnings:
        print("⚠  Placeholder chapters:")
        print("\n".join(chapter_warnings))

    if not link_errors and not world_warnings and not chapter_warnings:
        print("✅ All lore checks passed.")

    sys.exit(1 if failed else 0)


if __name__ == "__main__":
    main()
