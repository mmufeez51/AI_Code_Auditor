import argparse
import os
import sys
from dotenv import load_dotenv
from google import genai

def setup_gemini():
    """Load environment variables and initialize the Gemini client."""
    # Load .env file if it exists
    load_dotenv()
    
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        print("Error: GEMINI_API_KEY environment variable not set.")
        print("Please set it in a .env file or export it.")
        print("Example (Windows): setx GEMINI_API_KEY \"your_key\"")
        sys.exit(1)
        
    client = genai.Client(api_key=api_key)
    return client

def analyze_code(client, file_path):
    """Read a file and send it to Gemini for security analysis."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            code_content = f.read()
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
        sys.exit(1)
    except Exception as e:
        print(f"Error reading file '{file_path}': {e}")
        sys.exit(1)

    print(f"Analyzing '{file_path}'...")
    
    # Construct the DevSecOps prompt
    prompt = f"""
    You are an expert DevSecOps Engineer and Code Auditor. 
    Review the following code for:
    1. Security Vulnerabilities (e.g., injection flaws, insecure logic).
    2. Hardcoded Secrets (e.g., passwords, API keys, tokens).
    3. Poor Coding Practices that could lead to security issues.
    
    Provide a structured response:
    - **Summary**: A brief overview of the code's security posture.
    - **Findings**: A bulleted list of specific issues found (if any), with their severity (High, Medium, Low).
    - **Recommendations**: Actionable advice on how to fix the findings.
    
    If the code looks perfectly secure, state that clearly.
    
    Code to review:
    ```
    {code_content}
    ```
    """

    try:
        response = client.models.generate_content(
            model='gemini-2.5-flash',
            contents=prompt,
        )
        print("\n" + "="*40 + " AUDIT REPORT " + "="*40 + "\n")
        print(response.text)
        print("\n" + "="*94 + "\n")
    except Exception as e:
        print(f"Error generating audit report: {e}")

def main():
    parser = argparse.ArgumentParser(description="AI Code Auditor - Powered by Gemini")
    parser.add_argument("file", help="Path to the file you want to audit.")
    
    args = parser.parse_args()
    
    client = setup_gemini()
    analyze_code(client, args.file)

if __name__ == "__main__":
    main()
