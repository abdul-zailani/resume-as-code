# Resume as Code

A centralized, schema-based resume builder using the [JSON Resume Specification](https://jsonresume.org/). It features a single source of truth (`resume.json`) and an automated Python build pipeline to generate beautiful resumes in PDF, HTML, Word, and Plain Text formats.

Equipped with [AGENT.md](./AGENT.md) guidelines for AI coding assistants.

---

## 🚀 Key Features

*   🗂️ **Single Source of Truth**: All CV content is managed in a single, clean `resume.json` file.
*   🎛️ **Multi-Format Export**: Generates **5 production formats** in a single run:
    *   **PDF**: Legible, print-ready, and **exactly 2 pages** (optimized for mobile/screen viewing).
    *   **HTML**: Modern, clean web layout.
    *   **Word DOC**: Fully editable Microsoft Word document.
    *   **Plain Text (TXT)**: ATS-friendly plain text for copy-pasting.
    *   **JSON Schema**: Standard JSON resume format.
*   ⚡ **FOIT Prevention**: Headless Chrome print bugs are bypassed by stripping remote web fonts and utilizing premium, instant-loading local system font stacks.
*   📄 **Optimal Page Breaks**: Smart CSS printing layout (`page-break` optimization) that prevents individual cards from splitting awkwardly.

---

## 📂 Project Structure

```bash
├── resume.json               # Core raw resume data (JSON Resume schema)
├── build.py                  # Python build pipeline (CSS override & Chrome print)
├── AGENT.md                  # Reference guide for AI Agents / Coding Assistants
├── package.json              # NPM script configurations
├── .gitignore                # Git ignore pattern rules
├── .editorconfig             # Unified indentation and formatting rules
└── out/                      # Directory for generated outputs (PDF, HTML, DOC, TXT)
```

---

## 🛠️ Quick Start

### 1. Prerequisites
- **Node.js** (v22+)
- **Python 3**
- **Google Chrome** (installed in standard location)

### 2. Install Dependencies
```bash
npm install
```

### 3. Customize Resume
Edit `resume.json` with your personal information, work history, and skills keywords.

### 4. Compile Resume
Run the unified compilation script:
```bash
npm run build
```
This automatically compiles, applies custom patches, and outputs all pristine formats into the `out/` folder.
