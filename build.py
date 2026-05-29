#!/usr/bin/env python3
import os
import subprocess
import sys
import re

CUSTOM_CSS = """
            * {
              box-sizing: border-box;
            }
            
            main {
              display: block;
            }
            
            body {
              font-size: 12.5px;
              color: #333;
              line-height: 1.35;
              background-color: #F0F0F0;
              margin: 0;
              padding: 0;
              font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
            }
            
            body.pdf {
              background-color: #FFFFFF;
            }
            
            #main {
              background-color: #FFF;
              margin: 0;
              padding: 15px;
              border: none;
            }
            
            body.pdf > #main {
              border: none;
            }
            
            #container > header {
              padding-top: 10px;
              padding-bottom: 5px;
            }
            
            body.pdf #container > header {
              padding: 0;
            }
            
            #main > #container > section {
              margin-left: 0;
              position: relative;
              display: block;
            }
            
            section > div {
              margin-bottom: 8px;
              page-break-inside: avoid;
            }
            
            span.fa
            {
              display: none;
            }
            
            hr {
              margin-top: 6px;
              margin-bottom: 6px;
              border: 0;
              border-top: 1px solid #EEE;
            }
            
            .tenure, .keywords {
              font-size: 85%;
            }
            
            h1 {
              margin: 0;
              font-size: 26px;
              color: #1a4367;
              display: inline-block;
            }
            
            h2 {
              font-size: 14px;
              color: #4376a2;
              text-transform: uppercase;
              font-weight: bold;
              padding-top: 3px;
              margin-top: 2px;
              margin-bottom: 6px;
              border-bottom: 2px solid #4376a2;
              padding-bottom: 2px;
            }
            
            h3 {
              margin-bottom: 1px;
              font-size: 13px;
              font-weight: bold;
            }
            
            a, a:visited {
              color: #428BCA;
              text-decoration: none;
              font-weight: bold;
            }
            
            a:hover {
              text-decoration: underline;
            }
            
            .defunct {
              color: #989898;
              font-weight: bold;
            }
            
            #summary {
              font-size: 100%;
              margin-left: 0;
              padding: 2px 0;
            }
            
            #summary > p > strong {
              font-size: 1.1em;
            }
            
            #contact {
              float: right;
              text-align: right;
            }
            
            #summary > header > .fa-info {
              display: none;
            }
            
            #summary h2 {
              display: block;
            }
            
            .label-keyword {
              display: inline-block;
              background-color: #e8f4ff !important;
              color: #1a4367 !important;
              font-size: 0.85em;
              padding: 2px 6px;
              border: 1px solid #bce0fd;
              border-radius: 4px;
              margin-top: 2px;
              margin-right: 2px;
              font-weight: 600;
              text-align: center;
              -webkit-print-color-adjust: exact !important;
              print-color-adjust: exact !important;
            }
            
            .label-keyword span, .label-keyword span.kw {
              color: #1a4367 !important;
              font-weight: 600 !important;
              -webkit-print-color-adjust: exact !important;
              print-color-adjust: exact !important;
            }
            
            .notes {
              font-size: 9px;
              display: block;
              font-weight: normal;
              text-transform: uppercase;
            }
            
            .card-skills {
                position: relative;
            }
            .card-nested {
                min-height: 0;
                margin-bottom: 4px;
                border-width: 0;
            }
            .card {
                background: #FFF;
                border-radius: 0;
                padding: 0;
                border: none;
            }
            
            .skill-level {
              display: none;
            }
            
            .skill-info {
              margin-left: 0;
            }
            @media (max-width: 480px) {
              .skill-info {
                margin-left: 0;
              }
            }
            .skill-info > strong {
              font-weight: 700;
              font-size: 13px;
              color: #1a4367;
              line-height: 18px;
            }
            
            .list-unstyled {
              padding-left: 0;
              list-style: none;
            }
            
            .space-top {
                margin-top: 1px;
            }
            
            #container {
              max-width: 800px;
              margin: 0 auto;
            }
            
            .res-label {
              font-style: italic;
            }
            
            @media print {
              html, body, main {
                padding: 0;
                margin: 0;
                width: 100%;
                background-color: #FFFFFF;
              }
              @page {
                size: A4;
                margin: 0.5cm 0.7cm;
              }
              section {
                page-break-inside: auto !important;
              }
              .card-nested, section > div {
                page-break-inside: avoid !important;
              }
              li {
                margin-bottom: 1px;
              }
            }
"""

def main():
    print("🚀 Starting Resume compilation pipeline...")

    # Define paths
    base_dir = os.path.dirname(os.path.abspath(__file__))
    resume_json = os.path.join(base_dir, "resume.json")
    out_dir = os.path.join(base_dir, "out")
    cv_html = os.path.join(out_dir, "cv.html")
    cv_txt = os.path.join(out_dir, "cv.txt")
    cv_json = os.path.join(out_dir, "cv.json")
    cv_doc = os.path.join(out_dir, "cv.doc")
    cv_pdf = os.path.join(out_dir, "cv.pdf")

    # 1. Compile formats using HackMyResume
    print("📦 Step 1: Compiling formats (HTML, TXT, JSON, DOC) via HackMyResume...")
    hmr_cmd = [
        "npx", "hackmyresume", "build", 
        resume_json, "TO", 
        cv_html, cv_txt, cv_json, cv_doc
    ]
    try:
        subprocess.run(hmr_cmd, check=True, cwd=base_dir)
        print("✅ HackMyResume compilation successful.")
    except subprocess.CalledProcessError as e:
        print(f"❌ HackMyResume compilation failed: {e}")
        sys.exit(1)

    # 2. Patch HTML for high-fidelity rendering
    print("🔧 Step 2: Injecting styling patches (legible system fonts, 2-page print layout, and no-FOIT fix)...")
    if not os.path.exists(cv_html):
        print(f"❌ HTML file not found: {cv_html}")
        sys.exit(1)

    with open(cv_html, "r", encoding="utf-8") as f:
        html_content = f.read()

    # A. Inject SEO Meta Tags inside <head>
    print("   - Injecting SEO Meta Tags (description, keywords, author, viewport)...")
    seo_meta = """
        <meta name="description" content="Senior SRE & DevOps Engineer Resume - Abdul Aziz Zailani. Expert in cloud migration, Kubernetes orchestration (EKS/GKE), Jenkins-as-Code (JCasC), and high-availability container platforms.">
        <meta name="keywords" content="Site Reliability Engineer, SRE, DevOps, Cloud Migration, Kubernetes, EKS, Terraform, Ansible, Jenkins, JCasC, Grafana, Resume-as-Code">
        <meta name="author" content="Abdul Aziz Zailani">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
    """
    html_content = html_content.replace("<head>", f"<head>{seo_meta}")

    # B. Remove external font and CSS links to prevent invisible text FOIT
    print("   - Removing external font and FontAwesome link tags...")
    html_content = re.sub(
        r"<link href='https://fonts\.googleapis\.com/css\?family=Open\+Sans:.*?'\s*rel='stylesheet'\s*type='text/css'>",
        "",
        html_content,
        flags=re.DOTALL
    )
    html_content = re.sub(
        r"<link rel=\"stylesheet\" href=\"https://maxcdn\.bootstrapcdn\.com/font-awesome/.*?\">",
        "",
        html_content,
        flags=re.DOTALL
    )

    # C. Replace the entire <style>...</style> block with our custom CSS
    print("   - Injecting pixel-perfect CSS styling override...")
    style_regex = r"<style>.*?</style>"
    html_content = re.sub(
        style_regex,
        f"<style>{CUSTOM_CSS}</style>",
        html_content,
        flags=re.DOTALL
    )

    with open(cv_html, "w", encoding="utf-8") as f:
        f.write(html_content)
    print("✅ Styling patches successfully applied to cv.html.")

    # 3. Print PDF using headless Chrome
    print("🖨️ Step 3: Compiling PDF via Headless Google Chrome...")
    chrome_path = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
    if not os.path.exists(chrome_path):
        print(f"❌ Google Chrome executable not found at: {chrome_path}")
        sys.exit(1)

    chrome_cmd = [
        chrome_path,
        "--headless",
        "--disable-gpu",
        "--print-to-pdf-no-header",
        f"--print-to-pdf={cv_pdf}",
        cv_html
    ]
    try:
        subprocess.run(chrome_cmd, check=True)
        # Verify page count
        try:
            pdfinfo_output = subprocess.check_output(["pdfinfo", cv_pdf]).decode("utf-8")
            pages_match = re.search(r"Pages:\s+(\d+)", pdfinfo_output)
            if pages_match:
                pages = int(pages_match.group(1))
                print(f"🎉 SUCCESS! Legible, {pages}-page PDF compiled: {cv_pdf}")
        except Exception:
            print(f"🎉 SUCCESS! PDF compiled: {cv_pdf}")
    except subprocess.CalledProcessError as e:
        print(f"❌ Google Chrome PDF compilation failed: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
