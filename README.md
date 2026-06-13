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
│   │   └── build-book.yml          # Compiles the manuscript into a PDF on every push
│   └── pull_request_template.md    # Default checklist shown when opening a pull request
├── world/                          # Lore and worldbuilding documentation
│   ├── geography/                  # Maps, kingdoms, cities, and notable regions
│   ├── magic-system/               # Rules and mechanics of "The Source"
│   └── characters/                 # Character sheets and individual story arcs
├── manuscript/                     # The actual novel — one file per chapter
│   ├── chapter-01.md
│   ├── chapter-02.md
│   └── chapter-03.md
├── scripts/
│   └── word_counter.py             # Prints a per-chapter and total word count
├── .markdownlint.json              # Markdownlint rule configuration
└── README.md
```
