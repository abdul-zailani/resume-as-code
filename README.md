# Resume as Code

A centralized, schema-based resume builder using the [JSON Resume Specification](https://jsonresume.org/). It features a single source of truth (`resume.json`) and an automated Python build pipeline to generate beautiful resumes in PDF, HTML, Word, and Plain Text formats.

Equipped with [AGENT.md](./AGENT.md) guidelines for AI coding assistants.

---

## 🚀 Key Features

*   🗂 **Single Source of Truth**: All CV content is managed in a single, clean `resume.json` file.
*   🎮 **Interactive Live Playground**: Open `index.html` directly in any web browser to edit your raw JSON schema with a real-time validating editor and a live, pixel-perfect A4 print preview.
*   🎛 **Multi-Format Export**: Generates **5 production formats** in a single run:
    *   **PDF**: Legible, print-ready, and highly optimized for mobile/screen viewing.
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
├── index.html                # 🎮 Live JSON Editor & Real-Time Print Preview Web App
├── build.py                  # Python build pipeline (CSS override & Chrome print)
├── AGENT.md                  # Reference guide for AI Agents / Coding Assistants
├── package.json              # NPM script configurations
├── .gitignore                # Git ignore pattern rules
├── .editorconfig             # Unified indentation and formatting rules
└── out/                      # Directory for generated outputs (PDF, HTML, DOC, TXT)
```

---

## 🛠️ Quick Start

### Option A: The No-Setup Playground (Highly Recommended)
1. Open **`index.html`** directly in any web browser (no installation or terminal required!).
2. Edit the raw JSON schema in the live IDE-style editor on the left pane. The built-in validator will check your JSON syntax in real-time.
3. Watch the styled resume update instantly in the right-pane preview canvas.
4. Click **Print to PDF** to download your premium print layout, or **Save JSON Code** to download your validated `resume.json` to commit to Git!

### Option B: The Automated CLI Pipeline
If you prefer managing everything via terminal commands:
1. **Prerequisites**: Ensure you have Node.js (v22+), Python 3, and Google Chrome installed.
2. **Install Dependencies**:
   ```bash
   npm install
   ```
3. **Customize Resume**: Edit `resume.json` with your career details.
4. **Compile Resume**: Run the unified compilation script:
   ```bash
   npm run build
   ```
   This automatically compiles, applies custom patches, and outputs all pristine formats into the `out/` folder.

---

## 🤖 Too Lazy to Edit JSON? Let AI Do It For You!

If you only have a finished `.pdf` resume (e.g., from Canva, Word, or LinkedIn) and do not want to edit `resume.json` manually, you can leverage any modern AI coding assistant (like Claude, ChatGPT, or Gemini) to migrate it for you instantly!

### How to do it:
1. Open a chat with your favorite AI assistant in this workspace.
2. **Upload/Attach your existing PDF resume**.
3. Paste the following prompt:
   > *"Here is my current PDF resume. Please read it and convert all my career history, skills, and contact details into the `resume.json` schema of this repository. Once done, run the `npm run build` script to generate my new premium print PDF, HTML website, Word document, and ATS-friendly text resume!"*
   
The AI will automatically parse your PDF, write the JSON data, and compile all your stunning new resume formats in seconds—**zero manual coding required!**
