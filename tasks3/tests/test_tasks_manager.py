from tasks3.tasks_manager import TaskManager

def test_add_task():
    tm = TaskManager()
    tm.add_task("Finish homework")
    assert len(tm.tasks) == 1
    assert tm.tasks[0]["title"] == "Finish homework"

def test_complete_task():
    tm = TaskManager()
    tm.add_task("Submit assignment")
    tm.complete_task(0)
    assert tm.tasks[0]["completed"] is True
