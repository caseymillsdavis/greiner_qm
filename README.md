# Greiner — Quantum Mechanics: Study Notes

A personal study companion for working through **Walter Greiner's *Quantum
Mechanics*** (Greiner physics series). Screenshots of the text are uploaded
here, and each section is clarified and expanded into clean, math-rich notes.

The goal: a centralized, indexed, and durable replacement for ephemeral chat
sessions — easy to browse on phone or desktop, easy to pick back up.

## How it works

1. **Capture** — screenshots of the text go into a chapter's `source/` folder.
2. **Expand** — each section is clarified and expanded into `notes.md`, with
   full derivations, intuition, and worked steps.
3. **Review** — everything renders directly on GitHub (math included), so it's
   readable anywhere without a build step.

## Organization

```
text/
├── _TEMPLATE/          # copy this to start a new chapter
│   ├── source/         # raw screenshots (the inputs)
│   ├── figures/        # optional extracted/generated diagrams
│   └── notes.md        # the expanded analysis (the output)
└── chNN-slug/          # one folder per chapter, e.g. ch01-wave-particle-dualism
    ├── source/
    ├── figures/
    └── notes.md
papers/
└── slug/               # section-by-section notes on an original paper,
    └── notes.md        # e.g. einstein-1905-photoelectric
```

- **One folder per chapter** under `text/`, named `chNN-slug` (zero-padded
  number + short kebab-case title) so chapters sort correctly.
- **Inputs and outputs live together** — each chapter folder is self-contained.
- **Screenshots** are named so they sort in reading order, e.g.
  `p045.png` or `sec-2.3-p045.png`.

## Format

Notes are **Markdown** with LaTeX math (`$...$` inline, `$$...$$` block), which
GitHub renders automatically. Markdown keeps everything diffable and readable
in-place, and stays open to later export (Quarto / Pandoc / MkDocs) to HTML or
PDF if a polished build is ever wanted.

## Chapter index

| Chapter | Title | Status |
|---------|-------|--------|
| [1](text/ch01-quantization-of-physical-quantities/notes.md) | The Quantization of Physical Quantities | Notes complete (pp. 1–11), figures included |
| [2](text/ch02-radiation-laws/notes.md) | Radiation Laws (*Strahlungsgesetze*) | Notes complete (pp. 12–36); figures pending |
| [3](text/ch03-wave-aspect-of-matter/notes.md) | The Wave Aspect of Matter (*Der Wellenaspekt der Materie*) | Notes complete (pp. 37–83), figures included |

## Papers

Side quests: original papers dissected section by section, as companions to
the chapters.

| Paper | Related chapters | Status |
|-------|------------------|--------|
| [Einstein (1905) — On a Heuristic Point of View about the Creation and Conversion of Light](papers/einstein-1905-photoelectric/notes.md) | Ch. 1 (light quanta), Ch. 2 (radiation laws) | Notes complete, all nine sections + intro |

## Working with Claude

See [`CLAUDE.md`](CLAUDE.md) for the standing workflow and conventions used
when processing screenshots into notes.
