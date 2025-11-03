# Tasks2 — Advanced Task Manager

Features:
- Add tasks with priority (Low/Medium/High) and optional due date
- List all tasks (optionally sort by priority or due date)
- Search tasks by keyword, filter by status or priority
- Mark tasks as done or undone
- Overdue tasks are highlighted

## Setup

1. Navigate to the tasks2 directory:
    cd tasks2

2. Ensure tasks.json exists:
    []

## Usage Examples

Add a task:
    python tasks2.py add "Buy groceries" Medium 2025-11-05

List tasks (sorted by priority):
    python tasks2.py list priority

Search tasks:
    python tasks2.py search "groceries" not done High

Mark task done:
    python tasks2.py done 1

Mark task undone:
    python tasks2.py undone 1

Help:
    python tasks2.py help

