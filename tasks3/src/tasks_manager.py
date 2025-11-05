class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, title):
        self.tasks.append({"title": title, "completed": False})

    def complete_task(self, index):
        self.tasks[index]["completed"] = True

    def run(self):
        print("TaskManager running. Number of tasks:", len(self.tasks))

