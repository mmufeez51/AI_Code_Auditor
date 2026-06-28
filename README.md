# AI Code Auditor 🛡️🤖

AI Code Auditor is a command-line tool powered by the Gemini AI model that analyzes your source code for security vulnerabilities, hardcoded secrets, and poor coding practices.

## Features
- **Security Vulnerability Detection**: Identifies issues like SQL injections, XSS, and RCE.
- **Secret Scanning**: Detects hardcoded passwords, API keys, and tokens.
- **Actionable Recommendations**: Provides structured advice on how to fix identified issues.

## Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/mmufeez51/AI_Code_Auditor.git
   cd AI_Code_Auditor
   ```
2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Set up your environment variables:
   Create a `.env` file in the root directory and add your Gemini API Key:
   ```env
   GEMINI_API_KEY="your_api_key_here"
   ```

## Usage

Simply pass the file you want to audit as an argument:
```bash
python auditor.py path/to/your/file.py
```

## Example Output
Curious about what the analysis looks like? We ran the auditor against a deliberately vulnerable file (`vulnerable_test.py`). 

👉 **[View Example Audit Report (https://github.com/mmufeez51/AI_Code_Auditor/blob/main/EXAMPLE_OUTPUT.md)](https://github.com/mmufeez51/AI_Code_Auditor/blob/main/EXAMPLE_OUTPUT.md)**
