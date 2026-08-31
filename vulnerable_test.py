import sqlite3

def get_user_data(username):
    # Hardcoded API key (vulnerable to credential leakage)
    api_key = "AIzaSyFakeKey1234567890"
    
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    
    # SQL Injection vulnerability
    query = f"SELECT * FROM users WHERE username = '{username}'"
    cursor.execute(query)
    
    data = cursor.fetchall()
    conn.close()
    return data

def process_data(data_string):
    # Remote Code Execution (RCE) vulnerability
    return eval(data_string)
