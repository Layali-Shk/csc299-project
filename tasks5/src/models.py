class Task:
    def __init__(self, id: int, title: str):
        self.id = id
        self.title = title
        self.completed = False

    def complete(self):
        self.completed = True

