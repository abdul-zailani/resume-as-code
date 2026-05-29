# AI Agent Guidelines: Resume Builder Workspace

Welcome, Agent! Use these concise guidelines to maintain and compile this workspace.

---

## 📂 Core Architecture

*   `resume.json` — Raw source of truth (JSON Resume specification).
*   `build.py` — Automated post-processing and PDF compilation pipeline.
*   `out/` — Output folder containing generated formats (HTML, PDF, DOC, TXT).

---

## ⚡ Compilation Workflow

1.  Make content updates directly in `resume.json`.
2.  Compile all formats by running:
    ```bash
    npm run build
    ```
    *Note: This executes `python3 build.py` which compiles the HTML, overrides custom print styles, and launches headless Google Chrome to print the exactly 2-page A4 `cv.pdf`.*

---

## 🛑 Strict Rendering Constraints

You **MUST** respect the following rules during compilation:

### 1. 🔠 Legibility & Text Visibility (FOIT Prevention)
*   **The Bug**: Headless Chrome prints the page before remote Google Fonts or CDNs load, causing all text in the PDF to render as blank/invisible (locked in FOIT state).
*   **Constraint**: Do NOT load remote Google Fonts or FontAwesome CDN links in the HTML styles. Always fall back to local premium system font stacks:
    `font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;`

### 2. 📄 Strict 2-Page Fit
*   **The Bug**: Setting `section { page-break-inside: avoid; }` in print CSS forces the entire 5-job Employment section onto Page 2, creating massive gaps and overflowing the CV to Page 3.
*   **Constraint**:
    *   Set `section { page-break-inside: auto !important; }` in print CSS.
    *   Set `page-break-inside: avoid !important;` strictly for individual job cards (`.card-nested` and `section > div`) to prevent awkward splits.
    *   Keep page margin set to `@page { size: A4; margin: 0.5cm 0.7cm; }`.
    *   The generated PDF must fit **exactly 2 pages** with a body font size of `12px` to `12.5px`.

---

## 🛠️ Verification Commands

Verify your modifications by compiling and checking PDF details:
```bash
npm run build
pdfinfo out/cv.pdf
```
Ensure that `pdfinfo` reports:
*   `Pages: 2`
*   `Page size: 594.96 x 841.92 pts (A4)`
