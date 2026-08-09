import sqlite3
import os
import ast

def get_user_data(username):
    # Use environment variables for sensitive data instead of hardcoding
    api_key = os.environ.get("API_KEY")
    
    # Use a context manager to ensure the database connection is closed properly
    with sqlite3.connect('users.db') as conn:
        cursor = conn.cursor()
        
        # Use parameterized queries to prevent SQL Injection
        query = "SELECT * FROM users WHERE username = ?"
        cursor.execute(query, (username,))
        
        return cursor.fetchall()

def process_data(data_string):
    # Use ast.literal_eval instead of eval to prevent Remote Code Execution (RCE)
    try:
        return ast.literal_eval(data_string)
    except (ValueError, SyntaxError):
        return None
