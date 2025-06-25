import sqlite3

class Database:
    def __init__(self, db_name="tasks.db"):
        self.conn = sqlite3.connect(db_name)
        self.create_table()

    def create_table(self):
        self.conn.execute("""
        CREATE TABLE IF NOT EXISTS users (
            dni TEXT PRIMARY KEY,
            username TEXT NOT NULL,
            password TEXT NOT NULL,
            email TEXT,
            phone TEXT,
            age INTEGER
        )
        """)
        
        self.conn.execute("""
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            description TEXT,
            completed INTEGER DEFAULT 0,
            user_dni TEXT,
            deadline TEXT,
            category TEXT,
            tags TEXT
        )
        """)
        self.conn.commit()

    def close(self):
        self.conn.close()
