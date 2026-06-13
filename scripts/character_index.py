"""
character_index.py

Scans all chapter files for mentions of characters defined in world/characters/.
Each character file's stem (filename without .md) is treated as the character's
canonical name — spaces are represented by hyphens (e.g. "aria-voss.md" → "Aria Voss").

Usage:
    python scripts/character_index.py
"""

from pathlib import Path

CHARACTERS_DIR = Path(__file__).parent.parent / "world" / "characters"
MANUSCRIPT_DIR = Path(__file__).parent.parent / "manuscript"


def name_variants(stem: str) -> list[str]:
    """Return search variants for a character name derived from its filename stem."""
    canonical = stem.replace("-", " ").title()
    parts = canonical.split()
    variants = [canonical]
    if len(parts) > 1:
        variants.append(parts[0])   # first name only
        variants.append(parts[-1])  # last name only
    return variants


def main() -> None:
    characters = [p for p in sorted(CHARACTERS_DIR.glob("*.md")) if p.stem != "README"]

    if not characters:
        print("No character files found in world/characters/ (excluding README.md).")
        return

    chapters = sorted(MANUSCRIPT_DIR.glob("chapter-*.md"))
    if not chapters:
        print("No chapters found in manuscript/.")
        return

    chapter_texts = {p.stem: p.read_text(encoding="utf-8").lower() for p in chapters}

    print()
    any_found = False
    for char_file in characters:
        variants = name_variants(char_file.stem)
        found_in = [
            stem for stem, text in chapter_texts.items()
            if any(v.lower() in text for v in variants)
        ]
        label = variants[0]
        if found_in:
            any_found = True
            print(f"{label}")
            for ch in found_in:
                print(f"  · {ch}")
        else:
            print(f"{label}")
            print(f"  · (not mentioned in any chapter)")

    if not any_found:
        print("No character mentions found — add character files to world/characters/")
    print()


if __name__ == "__main__":
    main()
