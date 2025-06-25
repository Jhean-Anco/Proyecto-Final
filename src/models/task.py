class Task:
    def __init__(self, id, title, description="", completed=False,
                 user_dni=None, deadline=None, category=None, tags=None):
        self.id = id
        self.title = title
        self.description = description
        self.completed = completed
        self.user_dni = user_dni
        self.deadline = deadline
        self.category = category
        self.tags = tags

    def __repr__(self):
        return (f"Task({self.id}, {self.title}, {self.description}, {self.completed}, "
                f"{self.user_dni}, {self.deadline}, {self.category}, {self.tags})")
