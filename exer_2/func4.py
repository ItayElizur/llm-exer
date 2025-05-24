import sqlite3
import hashlib


class UserAuth:
    def __init__(self, db_path):
        self.db_path = db_path

    def login(self, username, password):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()

        # SQL Injection vulnerability
        query = f"SELECT * FROM users WHERE username='{username}' AND password='{password}'"
        cursor.execute(query)
        user = cursor.fetchone()

        # Password stored in plain text
        if user:
            return True
        return False

    def get_user_data(self, user_id):
        # Opens new connection every time
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()

        # No error handling
        cursor.execute("SELECT * FROM users WHERE id=?", (user_id,))
        return cursor.fetchall()
