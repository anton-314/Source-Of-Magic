# Source of Magic 🪄💻

An open-source, community-driven epic fantasy novel engineered through Git.

---

## 📖 Project Description

**Source of Magic** is a collaborative writing experiment. It treats worldbuilding as documentation, characters as modules, and the plot as source code. By utilizing version control, this project aims to build a deeply complex, logically consistent fantasy universe where every contributor can leave their mark, propose alternative subplots via branches, and help peer-review the narrative into a seamless masterpiece.

---

## 📂 Repository Structure

```text
source-of-magic/
├── .github/                        # GitHub-specific configuration
│   ├── ISSUE_TEMPLATE/             # Templates for opening new issues
│   │   ├── plot-hole.md            # Report a logical inconsistency or plot hole
│   │   └── lore-addition.md        # Propose new lore or worldbuilding details
│   ├── workflows/                  # GitHub Actions CI/CD pipelines
│   │   ├── lint.yml                # Checks Markdown formatting on every push and PR
│   │   └── build-book.yml          # Compiles the manuscript into PDF and EPUB on every push
│   └── pull_request_template.md    # Default checklist shown when opening a pull request
├── world/                          # Lore and worldbuilding documentation
│   ├── geography/                  # Maps, kingdoms, cities, and notable regions
│   ├── magic-system/               # Rules and mechanics of "The Source"
│   └── characters/                 # Character sheets and individual story arcs
├── manuscript/                     # The actual novel — one file per chapter
│   ├── chapter-01.md
│   ├── chapter-02.md
│   └── chapter-03.md
├── scripts/                        # Developer and author utility scripts
│   ├── new_chapter.py              # Creates the next chapter file with correct numbering
│   ├── word_counter.py             # Prints a per-chapter and total word count
│   ├── character_index.py          # Shows which chapters mention each defined character
│   ├── validate_lore.py            # Checks broken links, empty world sections, placeholders
│   ├── export_md.py                # Concatenates all chapters into one Markdown file
│   ├── export_pdf.py               # Builds a PDF locally via Pandoc + XeLaTeX
│   └── export_epub.py              # Builds an EPUB locally via Pandoc
├── .markdownlint.json              # Markdownlint rule configuration
└── README.md
```

---

## 🛠 Scripts

All scripts live in `scripts/` and require Python 3.10+. Export scripts additionally require
[Pandoc](https://pandoc.org/installing.html); `export_pdf.py` also requires XeLaTeX (`texlive-xetex`).

### Authoring

| Script | Description | Usage |
|---|---|---|
| `new_chapter.py` | Creates the next `chapter-XX.md` with the correct number | `python3 scripts/new_chapter.py` |
| `new_chapter.py` | Same, but with a title in the heading | `python3 scripts/new_chapter.py "The Storm Breaks"` |
| `word_counter.py` | Prints word count per chapter and a grand total | `python3 scripts/word_counter.py` |

### Validation & Analysis

| Script | Description | Usage |
|---|---|---|
| `validate_lore.py` | Checks internal links, empty world sections, and placeholder chapters | `python3 scripts/validate_lore.py` |
| `character_index.py` | Lists which chapters mention each character defined in `world/characters/` | `python3 scripts/character_index.py` |

### Export

All export scripts write their output to `dist/` by default. Pass `--output <path>` to override.

| Script | Output | Usage |
|---|---|---|
| `export_md.py` | `dist/source-of-magic.md` — single concatenated Markdown file | `python3 scripts/export_md.py` |
| `export_pdf.py` | `dist/source-of-magic.pdf` — print-ready PDF via XeLaTeX | `python3 scripts/export_pdf.py` |
| `export_epub.py` | `dist/source-of-magic.epub` — e-reader EPUB with table of contents | `python3 scripts/export_epub.py` |

PDF and EPUB are also built automatically by CI on every push to `main` and uploaded as a
GitHub Actions artifact.
