
import json
import os

class TaskManager:
    def __init__(self, filepath):
        self.filepath = filepath
        os.makedirs(os.path.dirname(filepath), exist_ok=True)
        if not os.path.exists(filepath):
            with open(filepath, "w") as f:
                json.dump([], f)

    def load_tasks(self):
        with open(self.filepath, "r") as f:
            return json.load(f)

    def save_tasks(self, tasks):
        with open(self.filepath, "w") as f:
            json.dump(tasks, f, indent=4)

    def run(self):
        tasks = self.load_tasks()
        print("Current tasks:", tasks)
        # You can add more functionality: add, update, delete tasks
