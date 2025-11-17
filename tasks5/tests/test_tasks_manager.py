# tests/test_tasks_manager.py
import os
import json
import pytest
from src.tasks_manager import TasksManager, DATA_DIR, TASKS_FILE

# Ensure a clean JSON file for each test
@pytest.fixture(autouse=True)
def reset_tasks_file():
    os.makedirs(DATA_DIR, exist_ok=True)
    with open(TASKS_FILE, 'w') as f:
        f.write("[]")
    yield
    # Clean up after test
    with open(TASKS_FILE, 'w') as f:
        f.write("[]")

def test_add_task():
    tm = TasksManager()
    t = tm.add_task("Do homework")
    assert t.title == "Do homework"
    assert t.id == 1

def test_complete_task():
    tm = TasksManager()
    t = tm.add_task("Clean")
    assert tm.complete_task(1)
    assert tm.list_tasks()[0].completed is True

def test_delete_task():
    tm = TasksManager()
    tm.add_task("Sleep")
    tm.delete_task(1)
    assert len(tm.list_tasks()) == 0
