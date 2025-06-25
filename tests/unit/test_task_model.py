import unittest
from src.models.task import Task

class TestTaskModel(unittest.TestCase):
    def test_create_task(self):
        task = Task(1, "Estudiar Python", "Repasar listas", False, user_id=42)
        self.assertEqual(task.title, "Estudiar Python")
        self.assertFalse(task.completed)
        self.assertEqual(task.user_id, 42)

if __name__ == "__main__":
    unittest.main()
