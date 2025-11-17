# Task 5 - Knowledge & Task Manager

Single-user CLI application for managing knowledge nodes and tasks, built using GitHub's Spec-Kit.

---

## Features

- **Knowledge Nodes**: Create and manage markdown-based knowledge entries.
- **Tasks**: Create, list, and manage tasks with title and description.
- **Linking**: Connect nodes to tasks and nodes to other nodes.
- **Persistence**: Optional local JSON storage.
- **CLI Interface**: Simple command-line interface with human-readable output.

---

## Installation

1. Ensure Python 3.12+ is installed:

```bash
py --version
Create and activate a virtual environment (optional but recommended):

bash
Copy code
py -m venv .venv
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate
Install dependencies:

bash
Copy code
py -m pip install -r requirements.txt
Usage
Run the task manager CLI:

bash
Copy code
py -m src.tasks_manager
Example usage:

python
Copy code
from src import tasks_manager

tm = tasks_manager.TaskManager()
tm.add_task("Example Task", "This is a description")
print(tm.list_tasks())
Running Tests
bash
Copy code
py -m pytest
All included tests should pass.

Project Structure
bash
Copy code
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
├── specify/              # Spec-kit files
│   ├── memory/constitution.md
│   ├── scripts/bash/
│   └── templates/
├── .gitignore
├── pyproject.toml
└── README.md
Data Storage (Optional)
To persist tasks and knowledge nodes, the following JSON files are used:

data/nodes.json

data/tasks.json

data/links.json

Each file is automatically created if it does not exist.

License
MIT
