import json
import os
from datetime import datetime

class TaskManager:
    def __init__(self, filepath):
        self.filepath = filepath
        os.makedirs(os.path.dirname(filepath), exist_ok=True)
        if not os.path.exists(filepath):
            with open(filepath, "w") as f:
                json.dump([], f)
        self._load()

    def _load(self):
        with open(self.filepath, "r") as f:
            self.tasks = json.load(f)

    def _save(self):
        with open(self.filepath, "w") as f:
            json.dump(self.tasks, f, indent=2)

    def add_task(self, content, tags=None, priority="None", due="None", recurrence=None):
        tags = tags or []
        task_id = max([t.get("id",0) for t in self.tasks], default=0) + 1
        self.tasks.append({
            "id": task_id,
            "content": content,
            "tags": tags,
            "priority": priority,
            "due": due,
            "recurrence": recurrence,
            "done": False,
            "created": datetime.now().isoformat()
        })
        self._save()
        print(f"Added task {task_id}")

    def list_tasks(self, sort_by=None):
        if not self.tasks:
            print("No tasks found.")
            return
        tasks = self.tasks.copy()
        if sort_by == "priority":
            tasks.sort(key=lambda t: {"None":0,"Low":1,"Medium":2,"High":3}.get(t.get("priority","None"),0), reverse=True)
        elif sort_by == "due":
            tasks.sort(key=lambda t: t.get("due","9999-12-31"))
        for t in tasks:
            status = "✔" if t.get("done") else "✗"
            print(f"[{t.get('id')}] {t.get('content','')} (tags: {', '.join(t.get('tags',[]))}, priority: {t.get('priority')}, due: {t.get('due')}, recurrence: {t.get('recurrence')}, done: {status})")

    def filter_tasks(self, keyword=None, tag=None):
        results = self.tasks
        if keyword:
            results = [t for t in results if keyword.lower() in t.get("content","").lower()]
        if tag:
            results = [t for t in results if tag in t.get("tags",[])]
        if not results:
            print("No tasks match the filter.")
            return
        for t in results:
            status = "✔" if t.get("done") else "✗"
            print(f"[{t.get('id')}] {t.get('content','')} (tags: {', '.join(t.get('tags',[]))}, priority: {t.get('priority')}, due: {t.get('due')}, recurrence: {t.get('recurrence')}, done: {status})")

    def delete_task(self, task_id):
        for t in self.tasks:
            if t.get("id") == task_id:
                self.tasks.remove(t)
                self._save()
                print(f"Deleted task {task_id}")
                return
        print(f"Task {task_id} not found")

    def mark_done(self, task_id):
        for t in self.tasks:
            if t.get("id") == task_id:
                t["done"] = True
                self._save()
                print(f"Task {task_id} marked as done")
                return
        print(f"Task {task_id} not found")

    def upcoming_alerts(self):
        now = datetime.now().date()
        for t in self.tasks:
            if t.get("due") and t.get("due") != "None":
                due_date = datetime.fromisoformat(t["due"]).date()
                if due_date <= now:
                    print(f"⚠ Task [{t['id']}] '{t['content']}' is due soon or overdue!")
