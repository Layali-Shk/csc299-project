# Task 5 - Knowledge & Task Manager

Single-user CLI application for managing knowledge nodes (markdown) and tasks, built using GitHub's Spec-Kit.

**Features**  
- Knowledge Nodes: Create and manage markdown-based knowledge entries.  
- Tasks: Create, list, and manage tasks with title and description.  
- Linking: Connect nodes to tasks and nodes to other nodes.  
- Persistence: Optional local JSON storage for tasks and nodes.  
- CLI Interface: Simple command-line interface with human-readable output.

**(Optional but recommended) Create and activate a virtual environment:**
py -m venv .venv
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate

# Install dependencies:
py -m pip install -r requirements.txt
# Usage
**Run the task manager CLI:**
py -m src.tasks_manager
# Example usage in Python:
from src import tasks_manager

tm = tasks_manager.TaskManager()
tm.add_task("Example Task", "This is a description")
print(tm.list_tasks())

# Running Tests
py -m test

# Project Structure
tasks5/
├── src/                  # Source code
│   └── tasks_manager.py
├── tests/                # Tests
│   ├── test_models.py
│   └── test_tasks_manager.py
├── data/                 # Optional runtime JSON storage
│   ├── nodes.json
│   ├── tasks.json
│   └── links.json
├── specify/              # Spec-Kit files
│   ├── memory/constitution.md
│   ├── scripts/bash/
│   └── templates/
├── .gitignore
├── pyproject.toml
└── README.md

**Installation**  
Ensure Python 3.12+ is installed:
```bash

py --version
