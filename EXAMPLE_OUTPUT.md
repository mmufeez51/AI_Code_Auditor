# AI Code Auditor - Example Output

Here is an example of what the AI Code Auditor outputs when analyzing the `vulnerable_test.py` file included in this repository.

```text
Analyzing 'vulnerable_test.py'...

======================================== AUDIT REPORT ========================================

**Summary**
This code contains several critical security vulnerabilities that must be addressed immediately. It includes hardcoded secrets, a severe SQL injection vulnerability, and an arbitrary code execution vulnerability.

**Findings**
*   **[High] Hardcoded API Key**: Line 5 contains a hardcoded API key (`AIzaSyFakeKey1234567890`). Hardcoding secrets in source code is a major security risk as they can be easily extracted or leaked via version control.
*   **[High] SQL Injection (SQLi)**: Line 12 constructs a SQL query using string formatting (`f"SELECT * FROM users WHERE username = '{username}'"`). This allows an attacker to inject arbitrary SQL commands by manipulating the `username` parameter.
*   **[High] Remote Code Execution (RCE) via `eval()`**: Line 19 uses the `eval()` function on untrusted user input (`data_string`). This allows an attacker to execute arbitrary Python code on the server.

**Recommendations**
*   **Remove Hardcoded Secrets**: Move the API key to an environment variable or a secure secrets management system. Use `os.environ.get('API_KEY')` to access it.
*   **Use Parameterized Queries**: Replace the string formatting in the SQL query with parameterized queries provided by `sqlite3`. 
    *   *Fix*: `cursor.execute("SELECT * FROM users WHERE username = ?", (username,))`
*   **Avoid `eval()`**: Never use `eval()` on untrusted input. If you need to parse structured data, use safe alternatives like `json.loads()` for JSON or `ast.literal_eval()` if parsing Python literals is strictly necessary.

==============================================================================================
```
