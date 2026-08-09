import argparse
import logging
import os
import sys
from dotenv import load_dotenv
from google import genai

logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')

def init_client() -> genai.Client:
    load_dotenv()
    
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        logging.error("GEMINI_API_KEY environment variable is missing.")
        sys.exit(1)
        
    return genai.Client(api_key=api_key)

def audit_file(client: genai.Client, file_path: str) -> None:
    if not os.path.exists(file_path):
        logging.error(f"File not found: {file_path}")
        sys.exit(1)
        
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            source = f.read()
    except IOError as e:
        logging.error(f"Failed to read {file_path}: {e}")
        sys.exit(1)

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
            model='gemini-2.5-flash',
            contents=prompt,
        )
        print("\n" + "="*40 + " AUDIT REPORT " + "="*40 + "\n")
        print(response.text.strip())
        print("\n" + "="*94 + "\n")
    except Exception as e:
        logging.error(f"API request failed: {e}")
        sys.exit(1)

def main() -> None:
    parser = argparse.ArgumentParser(description="Static analysis and security auditing tool.")
    parser.add_argument("file", help="Source file to audit")
    args = parser.parse_args()
    
    client = init_client()
    audit_file(client, args.file)

if __name__ == "__main__":
    main()
