# Example Output

Running the auditor against `vulnerable_test.py`:

```bash
$ python auditor.py vulnerable_test.py
INFO: Analyzing vulnerable_test.py...

======================================== AUDIT REPORT ========================================

**Summary**
This code contains critical security vulnerabilities, including hardcoded secrets, SQL injection, and arbitrary code execution.

**Findings**
*   **[High] Hardcoded API Key**: Line 5 contains a hardcoded API key (`AIzaSyFakeKey1234567890`). 
*   **[High] SQL Injection**: Line 12 constructs a SQL query using string formatting. 
*   **[High] Remote Code Execution**: Line 19 uses `eval()` on untrusted input.

**Recommendations**
*   **Secrets Management**: Move the API key to environment variables (`os.environ.get('API_KEY')`).
*   **Parameterized Queries**: Use parameterized queries (`cursor.execute("SELECT * FROM users WHERE username = ?", (username,))`).
*   **Avoid eval()**: Replace `eval()` with `json.loads()` or `ast.literal_eval()`.

==============================================================================================
```
