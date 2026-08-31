import argparse
import logging
import os
import sys
from pathlib import Path
from dotenv import load_dotenv
from google import genai

logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')

SUPPORTED_EXTENSIONS = {'.py', '.js', '.ts', '.java', '.c', '.cpp', '.cs', '.go', '.rb', '.php'}

def init_client() -> genai.Client:
    load_dotenv()
    
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        logging.error("GEMINI_API_KEY environment variable is missing.")
        sys.exit(1)
        
    return genai.Client(api_key=api_key)

def audit_file(client: genai.Client, file_path: str, model_name: str) -> str:
    if not os.path.exists(file_path):
        logging.error(f"File not found: {file_path}")
        return ""
        
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            source = f.read()
    except IOError as e:
        logging.error(f"Failed to read {file_path}: {e}")
        return ""

    logging.info(f"Analyzing {file_path}...")
    
    prompt = (
        "You are a DevSecOps Engineer. Review the following code for:\n"
        "1. Security Vulnerabilities (e.g., injection flaws, insecure logic).\n"
        "2. Hardcoded Secrets (e.g., passwords, API keys).\n"
        "3. Poor Coding Practices.\n\n"
        "Provide a structured response containing a Summary, Findings (with severity), "
        "and Recommendations.\n\n"
        f"Code:\n```\n{source}\n```"
    )

    try:
        response = client.models.generate_content(
            model=model_name,
            contents=prompt,
        )
        report = f"## Audit Report for `{file_path}`\n\n"
        report += response.text.strip() + "\n\n"
        return report
    except Exception as e:
        logging.error(f"API request failed for {file_path}: {e}")
        return ""

def scan_target(client: genai.Client, target_path: str, model_name: str) -> str:
    full_report = ""
    path = Path(target_path)
    
    if path.is_file():
        return audit_file(client, str(path), model_name)
    elif path.is_dir():
        logging.info(f"Scanning directory: {target_path}")
        for root, _, files in os.walk(path):
            # Skip hidden directories like .git
            if '/.' in root.replace('\\', '/') or '\\.' in root:
                continue
                
            for file in files:
                file_path = Path(root) / file
                if file_path.suffix in SUPPORTED_EXTENSIONS:
                    report = audit_file(client, str(file_path), model_name)
                    if report:
                        full_report += report + "---\n\n"
        return full_report
    else:
        logging.error(f"Target path not found or invalid: {target_path}")
        return ""

def main() -> None:
    parser = argparse.ArgumentParser(description="Static analysis and security auditing tool.")
    parser.add_argument("target", help="Source file or directory to audit")
    parser.add_argument("--model", default="gemini-3.5-flash", help="Gemini model to use (default: gemini-3.5-flash)")
    parser.add_argument("-o", "--output", help="Save the audit report to a Markdown file")
    
    args = parser.parse_args()
    
    client = init_client()
    report = scan_target(client, args.target, args.model)
    
    if not report.strip():
        logging.warning("No audit report was generated.")
        return
        
    if args.output:
        try:
            with open(args.output, 'w', encoding='utf-8') as f:
                f.write(f"# AI Code Auditor Report\n\n{report}")
            logging.info(f"Report saved successfully to {args.output}")
        except IOError as e:
            logging.error(f"Failed to write output to {args.output}: {e}")
    else:
        print("\n" + "="*40 + " AUDIT REPORT " + "="*40 + "\n")
        print(report)
        print("="*94 + "\n")

if __name__ == "__main__":
    main()
