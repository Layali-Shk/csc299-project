import os
import json
import pytest
from src.tasks_manager import TasksManager

# Path to your tasks.json file
DATA_FILE = os.path.join(os.path.dirname(__file__), '..', 'data', 'tasks.json')

# Fixture to clear tasks.json before each test
@pytest.fixture(autouse=True)
def clear_tasks_file():
    os.makedirs(os.path.dirname(DATA_FILE), exist_ok=True)
    with open(DATA_FILE, 'w') as f:
        f.write("[]")  # reset tasks
    yield
    # optional cleanup after test
    with open(DATA_FILE, 'w') as f:
        f.write("[]")

def test_add_task():
    tm = TasksManager()
    t = tm.add_task("Do homework")
    assert t.title == "Do homework"
    assert t.id == 1  # should start at 1 because file is cleared

def test_list_tasks():
    tm = TasksManager()
    tm.add_task("Read book")
    tasks = tm.list_tasks()
    assert len(tasks) == 1
    assert tasks[0].title == "Read book"

def test_complete_task():
    tm = TasksManager()
    tm.add_task("Clean")
    assert tm.complete_task(1)  # should succeed
    assert tm.list_tasks()[0].completed is True

def test_delete_task():
    tm = TasksManager()
    tm.add_task("Sleep")
    tm.delete_task(1)
    assert len(tm.list_tasks()) == 0  # file reset ensures only this task exists

def test_multiple_tasks():
    tm = TasksManager()
    tm.add_task("Task 1")
    tm.add_task("Task 2")
    tasks = tm.list_tasks()
    assert len(tasks) == 2
    assert tasks[0].id == 1
    assert tasks[1].id == 2
