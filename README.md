# code-auditor

A lightweight, LLM-driven static analysis and security auditing tool. It scans source code for vulnerabilities, exposed secrets, and insecure patterns using Google's Gemini API.

## Features
- Detects common security flaws (SQLi, XSS, RCE, etc.)
- Scans for hardcoded secrets and credentials
- Provides actionable remediation steps

## Installation

```bash
git clone https://github.com/mmufeez51/AI_Code_Auditor.git
cd AI_Code_Auditor
pip install -r requirements.txt
```

## Configuration

Set your Gemini API key in the environment. You can use a `.env` file in the project root:

```env
GEMINI_API_KEY=your_api_key_here
```

## Usage

```bash
# Scan a single file
python auditor.py <file_path>

# Scan an entire directory
python auditor.py <directory_path>

# Specify a different Gemini model
python auditor.py <target> --model gemini-2.5-flash

# Save the report to a Markdown file
python auditor.py <target> --output report.md
```

See [EXAMPLE_OUTPUT.md](EXAMPLE_OUTPUT.md) for a sample audit report.
