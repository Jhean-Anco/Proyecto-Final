from src.models.user import User
from src.db.database import Database

class AuthController:
    def __init__(self, db: Database):
        self.db = db

    def register_user(self, dni, username, password, email, phone, age):
        cursor = self.db.conn.cursor()
        cursor.execute("SELECT * FROM users WHERE dni = ?", (dni,))
        if cursor.fetchone():
            return False

        cursor.execute(
            "INSERT INTO users (dni, username, password, email, phone, age) VALUES (?, ?, ?, ?, ?, ?)",
            (dni, username, password, email, phone, age)
        )
        self.db.conn.commit()
        print("[DEBUG] Usuario registrado:", dni)
        return True

    def login_user(self, dni, password):
        cursor = self.db.conn.cursor()
        print("[DEBUG] Intentando login:", dni, password)
        cursor.execute("SELECT * FROM users WHERE dni = ? AND password = ?", (dni, password))
        row = cursor.fetchone()
        if row:
            return User(dni=row[0], username=row[1], password=row[2],
                        email=row[3], phone=row[4], age=row[5])
        return None

