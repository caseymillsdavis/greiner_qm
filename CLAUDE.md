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
- **Do not use `\tag{}`** for equation numbers — GitHub's MathJax renders it
  unreliably (equations collapse into a vertical stack). Instead append the
  number inline at the end of the equation, e.g. `... \qquad (1.2)`, using only
  plain characters inside the label. **Never put `$` inside a `$$...$$` block**
  (e.g. `\tag{2$\perp$}`) — the nested delimiter desyncs the parser. For symbol
  labels use bare math like `(2\parallel)`, `(2\perp)`, `(\ast)`.
- **Avoid the spacing macros `\,` `\;` `\:` `\!` inside math.** GitHub's markdown
  layer mangles backslash-punctuation, so `\,` renders as a literal comma and
  `\;` as a semicolon (e.g. `\boxed{\;x\;}` shows as `;x;`). Use a normal space,
  or `\quad`/`\qquad` (backslash-letters, which are safe). Most backslash-letter
  commands (`\frac`, `\sqrt`, `\hbar`, `\nabla`, …) are unaffected.
- **Never write literal `\{` or `\}` in math** — same backslash-punctuation
  mangling: the backslash is eaten, so `\left\{` reaches MathJax as `\left{`
  and errors with "Missing or unrecognized delimiter for \left", while bare
  `\{...\}` set braces silently disappear. Use `\lbrace` / `\rbrace` instead
  (and `\left\lbrace ... \right\rbrace` for sized delimiters).
- **`\operatorname{...}` is *not* allowed** by GitHub's MathJax subset ("The
  following macros are not allowed: operatorname"). For named operators use a
  built-in (`\nabla` for grad/div/curl, `\sin`, `\log`, …) or `\mathrm{...}`.
- **Don't write two or more paren-subscript groups like `(\hat e_i)_a (\hat e_i)_b`
  in one inline `$...$` span** — GitHub's emphasis pass pairs those underscores
  as italics markers and destroys the math span (the LaTeX shows literally,
  minus the underscores). Put such formulas on their own `$$...$$` display
  line instead. Single groups with braced subscripts, e.g. `(d\omega/dk)_{k_0}`,
  are fine.
- **Don't put inline `$...$` math inside emphasis** (`*italic*` or `**bold**`) —
  GitHub renders it raw (you see the literal `$...$`). Math sitting *next to*
  emphasis on the same line is fine; only math *inside* the `*...*` span breaks.
  So figure captions that contain math must be **plain text, not italicized**.
- **In table cells, don't wrap inline `$...$` in literal parentheses** like
  `($\vec F = \dots$)` — GitHub fails to parse the delimiters there (it works in
  ordinary body text, but not inside a `|`-delimited cell). Separate with
  punctuation instead, e.g. `...; force $\vec F = \dots$`.
- Number or label key results so they can be cross-referenced.
- When a screenshot maps to a note section, reference the source file, e.g.
  `<!-- source: source/sec-2.3-p045.png -->`.
- Favor full derivations over hand-waving; show intermediate steps.
- Add an "Intuition" or "Why this matters" aside where it aids understanding.

### Figures (cropping from the screenshots)
Diagrams from the text are cropped out of the chapter's `source/` screenshots
and saved into `figures/`. Use the helper `tools/figcrop.py` (needs Pillow:
`pip install Pillow`):

```
python3 tools/figcrop.py SRC DST LEFT TOP RIGHT BOTTOM [--scale S]
```

Workflow:
- **Find the crop box by trial.** Write a guess to `/tmp/preview.png` at full
  scale, view it, and adjust the `LEFT TOP RIGHT BOTTOM` pixel bounds. The
  figure is often lower / further right than a glance at the page suggests, and
  thin axes are easy to clip — budget a few passes.
- **Downscale the final crop with `--scale 0.333`** (~1/3) for a sensible
  display size in the notes; write it to `figures/fig-<section>-<slug>.png`.
- **Embed** with an image, a source comment, and a **plain-text** English
  caption (not italicized — captions usually contain `$math$`, which GitHub
  renders raw inside `*...*`):

  ```
  ![alt text](figures/fig-1.4-franck-hertz.png)

  <!-- figure: cropped from source/p10.jpg -->
  Caption in plain English; inline $math$ is fine in plain text.
  ```

- **Leave scan artifacts (show-through / bleed) as-is** — don't over-process.

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
