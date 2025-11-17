from src.tasks_manager import TasksManager

def test_add_task():
    tm = TasksManager()
    t = tm.add_task("Do homework")
    assert t.title == "Do homework"
    assert t.id == 1

def test_complete_task():
    tm = TasksManager()
    tm.add_task("Clean")
    assert tm.complete_task(1)

def test_delete_task():
    tm = TasksManager()
    tm.add_task("Sleep")
    tm.delete_task(1)
    assert len(tm.list_tasks()) == 0

