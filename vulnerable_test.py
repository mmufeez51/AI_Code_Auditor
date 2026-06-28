import sqlite3

def get_user_data(username):
    # Hardcoded sensitive data (Bad Practice)
    api_key = "AIzaSyFakeKey1234567890"
    
    # Insecure SQL connection (No password, local file)
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    
    # SQL Injection Vulnerability (String formatting instead of parameterized query)
    query = f"SELECT * FROM users WHERE username = '{username}'"
    cursor.execute(query)
    
    return cursor.fetchall()

def process_data(data_string):
    # Remote Code Execution (RCE) / Eval vulnerability
    return eval(data_string)
