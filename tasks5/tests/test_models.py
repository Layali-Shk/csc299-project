from src.models import Task

def test_task_creation():
    t = Task(1, "Study")
    assert t.id == 1
    assert t.title == "Study"
    assert not t.completed

def test_task_complete():
    t = Task(1, "Study")
    t.complete()
    assert t.completed

