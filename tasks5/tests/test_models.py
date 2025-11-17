# tests/test_models.py
from src.models import Task

def test_task_creation():
    t = Task(1, "Sample Task")
    assert t.id == 1
    assert t.title == "Sample Task"
    assert t.completed is False

def test_task_completion():
    t = Task(1, "Another Task")
    t.complete()
    assert t.completed is True
