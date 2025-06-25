from src.models.task import Task
from src.db.database import Database

class TaskController:
    def __init__(self, db: Database):
        self.db = db

    def add_task(self, title, description="", user_dni=None, deadline=None, category=None, tags=None):
        cursor = self.db.conn.cursor()
        cursor.execute("""
            INSERT INTO tasks (title, description, completed, user_dni, deadline, category, tags)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        """, (title, description, 0, user_dni, deadline, category, tags))
        self.db.conn.commit()

    def get_all_tasks(self, user_dni):
        cursor = self.db.conn.cursor()
        cursor.execute("SELECT * FROM tasks WHERE user_dni=?", (user_dni,))
        rows = cursor.fetchall()
        return [
            Task(id=row[0], title=row[1], description=row[2],
                 completed=bool(row[3]), user_dni=row[4],
                 deadline=row[5], category=row[6], tags=row[7])
            for row in rows
        ]

    def update_task(self, task: Task):
        cursor = self.db.conn.cursor()
        cursor.execute("""
            UPDATE tasks SET title=?, description=?, completed=?, deadline=?, category=?, tags=?
            WHERE id=?
        """, (task.title, task.description, int(task.completed),
              task.deadline, task.category, task.tags, task.id))
        self.db.conn.commit()

    def delete_task(self, task_id: int):
        cursor = self.db.conn.cursor()
        cursor.execute("DELETE FROM tasks WHERE id=?", (task_id,))
        self.db.conn.commit()
