# Tasks2 — Advanced Task Manager

This is an upgraded version of the simple task manager from **Tasks1**.  
It adds several new features to make task management more powerful and organized.

## Features (compared to Tasks1)

**From Tasks1:**
* Add tasks
* List all tasks
* Search tasks by keyword
* Store tasks in a JSON file

**New in Tasks2:**
* **Task Priorities**: Low / Medium / High
* **Optional Due Dates** for each task
* **Mark tasks as done or undone**
* **Filter search** by status (done/not done) or priority
* **Sort tasks** by priority or due date
* **Overdue tasks are highlighted**
* **Cleaner terminal output** with emojis for status, priority, and overdue
* **Class-based design** (TaskManager), making it easier to extend

---

## Setup

1. Navigate to the tasks2 directory:
    ```bash
    cd tasks2
    ```

2. Ensure `tasks.json` exists (it can be empty initially):
    ```json
    []
    ```

**Windows note:**  
If your script writes to `tasks.json` in the current directory, make sure directory creation only happens when a directory actually exists:
    ```python
    if dir_path: 
        os.makedirs(dir_path, exist_ok=True)
    ```

---

## Usage Examples

Add a task:
    ```bash
    python tasks.py add "Buy groceries" Medium 2025-11-05
    ```

List tasks (sorted by priority):
    ```bash
    python tasks.py list priority
    ```

Search tasks:
    ```bash
    python tasks.py search "groceries" not done High
    ```

Mark task done:
    ```bash
    python tasks.py done 1
    ```

Mark task undone:
    ```bash
    python tasks.py undone 1
    ```

Help:
    ```bash
    python tasks.py help
    ```

---
