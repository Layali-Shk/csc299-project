Tasks2 — Advanced Task Manager

This is an upgraded version of the simple task manager from Tasks1.
It adds several new features to make task management more powerful and organized.

Features (compared to Tasks1)

From Tasks1:

Add tasks

List all tasks

Search tasks by keyword

Store tasks in a JSON file

New in Tasks2:

Task Priorities: Low / Medium / High

Optional Due Dates for each task

Mark tasks as done or undone

Filter search by status (done/not done) or priority

Sort tasks by priority or due date

Overdue tasks are highlighted

Cleaner terminal output with emojis for status, priority, and overdue

Class-based design (TaskManager), making it easier to extend

Setup

Navigate to the tasks2 directory:

cd tasks2


Ensure tasks.json exists (it can be empty initially):

[]


Note (Windows users):
If your version of the script writes to tasks.json in the current directory, make sure your code checks that the directory exists before calling os.makedirs().
Example fix inside the script:

dir_path = os.path.dirname(filepath)
if dir_path:  # prevents os.makedirs("") on Windows
    os.makedirs(dir_path, exist_ok=True)

Usage Examples

Add a task:

python tasks.py add "Buy groceries" Medium 2025-11-05


List tasks (sorted by priority):

python tasks.py list priority


Search tasks:

python tasks.py search "groceries" not done High


Mark task done:

python tasks.py done 1


Mark task undone:

python tasks.py undone 1


Help:

python tasks.py help
