from .models import Task

class TasksManager:
    def __init__(self):
        self.tasks = []
        self.next_id = 1

    def add_task(self, title: str):
        task = Task(self.next_id, title)
        self.tasks.append(task)
        self.next_id += 1
        return task

    def list_tasks(self):
        return self.tasks

    def complete_task(self, id: int):
        for t in self.tasks:
            if t.id == id:
                t.complete()
                return True
        return False

    def delete_task(self, id: int):
        self.tasks = [t for t in self.tasks if t.id != id]


if __name__ == "__main__":
    tm = TasksManager()
    tm.add_task("Example task")
    print([t.title for t in tm.list_tasks()])
