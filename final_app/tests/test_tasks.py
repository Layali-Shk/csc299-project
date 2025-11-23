from tasks import TaskManager
import os

def test_add_task():
    filepath = 'data/test_tasks.json'
    if os.path.exists(filepath):
        os.remove(filepath)
    tasks = TaskManager(filepath)
    tasks.add_task("Test task")
    assert len(tasks.tasks) == 1
