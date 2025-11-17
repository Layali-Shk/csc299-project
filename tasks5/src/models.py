import json
import os
from typing import List, Optional

DATA_DIR = os.path.join(os.path.dirname(__file__), "..", "data")
TASKS_FILE = os.path.join(DATA_DIR, "tasks.json")

class Task:
    def __init__(self, id: int, title: str, completed: bool = False):
        self.id = id
        self.title = title
        self.completed = completed

    def complete(self):
        self.completed = True

    def to_dict(self):
        return {"id": self.id, "title": self.title, "completed": self.completed}

    @classmethod
    def from_dict(cls, data: dict):
        return cls(data["id"], data["title"], data.get("completed", False))

def load_tasks() -> List[Task]:
    if not os.path.exists(DATA_DIR):
        os.makedirs(DATA_DIR)
    if not os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, "w") as f:
            json.dump([], f)
    with open(TASKS_FILE, "r") as f:
        data = json.load(f)
    return [Task.from_dict(d) for d in data]

def save_tasks(tasks: List[Task]):
    if not os.path.exists(DATA_DIR):
        os.makedirs(DATA_DIR)
    with open(TASKS_FILE, "w") as f:
        json.dump([t.to_dict() for t in tasks], f, indent=2)
