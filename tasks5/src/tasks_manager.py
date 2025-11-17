# src/tasks_manager.py
import json
import os
from .models import Task

DATA_DIR = os.path.join(os.path.dirname(__file__), '..', 'data')
TASKS_FILE = os.path.join(DATA_DIR, 'tasks.json')

class TasksManager:
    def __init__(self):
        os.makedirs(DATA_DIR, exist_ok=True)
        if not os.path.exists(TASKS_FILE):
            with open(TASKS_FILE, 'w') as f:
                f.write("[]")
        self.tasks = self._load_tasks()
        self.next_id = max([t.id for t in self.tasks], default=0) + 1

    def _load_tasks(self):
        with open(TASKS_FILE, 'r') as f:
            data = json.load(f)
        return [Task(d['id'], d['title'], d.get('completed', False)) for d in data]

    def _save_tasks(self):
        with open(TASKS_FILE, 'w') as f:
            json.dump([t.__dict__ for t in self.tasks], f, indent=4)

    def add_task(self, title: str):
        task = Task(self.next_id, title)
        self.tasks.append(task)
        self.next_id += 1
        self._save_tasks()
        return task

    def list_tasks(self):
        return self.tasks

    def complete_task(self, id: int):
        for t in self.tasks:
            if t.id == id:
                t.complete()
                self._save_tasks()
                return True
        return False

    def delete_task(self, id: int):
        self.tasks = [t for t in self.tasks if t.id != id]
        self._save_tasks()


if __name__ == "__main__":
    tm = TasksManager()
    tm.add_task("Example task")
    print([t.title for t in tm.list_tasks()])
