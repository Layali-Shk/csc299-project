# src/models.py
class Task:
    def __init__(self, id, title, completed=False):
        self.id = id
        self.title = title
        self.completed = completed

    def complete(self):
        self.completed = True
