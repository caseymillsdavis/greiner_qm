# CLAUDE.md — Study workflow for Greiner's Quantum Mechanics

This repository is a study companion for **Walter Greiner's *Quantum
Mechanics***. The owner uploads screenshots of the text and asks for each
section to be **clarified and expanded** into clean, durable notes. Treat this
as the central, indexed replacement for ephemeral chat tutoring.

## Your job

When given one or more screenshots from the text:

1. **Read carefully** — transcribe the relevant equations and identify the
   section/topic. Preserve Greiner's notation and equation numbering where
   visible (e.g. reference "Eq. (2.14)" as it appears in the text).
2. **Clarify and expand** — don't just restate. Fill in skipped algebra, give
   physical intuition, define every symbol on first use, and explain *why* each
   step follows. Aim for the level of a patient tutor walking a motivated
   student through the material.
3. **Write to the chapter's `notes.md`** in `text/chNN-slug/`, appending a new
   section rather than overwriting prior work.
4. **Update the chapter index** table in `README.md` when starting a new
   chapter or making meaningful progress.

## Conventions

### Files & folders
- One folder per chapter: `text/chNN-slug/` (zero-padded number, kebab-case
  title). Copy `text/_TEMPLATE/` to start a new chapter.
- Raw screenshots go in `source/`, named to sort in reading order
  (`p045.png`, `sec-2.3-p045.png`).
- Generated or extracted diagrams go in `figures/`.
- Expanded notes go in `notes.md`.

### Notes format (Markdown)
- Use `##` for sections, `###` for subsections; mirror the book's structure.
- **Math is LaTeX**, rendered by GitHub: `$...$` inline, `$$...$$` for display.
  Use `\hat{}` for operators, standard QM notation (`\langle\psi|\phi\rangle`,
  `\nabla^2`, `\hbar`, etc.).
- Number or label key results so they can be cross-referenced.
- When a screenshot maps to a note section, reference the source file, e.g.
  `<!-- source: source/sec-2.3-p045.png -->`.
- Favor full derivations over hand-waving; show intermediate steps.
- Add an "Intuition" or "Why this matters" aside where it aids understanding.

### Structure of each chapter's notes.md
Start from the template:
- Title + chapter heading
- One section per topic/subsection of the chapter
- Within a section: statement of the result → derivation → intuition →
  (optional) worked example or cross-references

## Git
- Develop on the branch specified for the session.
- Commit per chapter or per meaningful study session with clear messages
  (e.g. `ch02: expand the time-independent Schrödinger equation`).
- Do not open pull requests unless explicitly asked.
