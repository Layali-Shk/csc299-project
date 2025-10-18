import json
import os
import sys

DATA_FILE = "tasks.json"


def load_tasks():
    """Load tasks from the JSON file or return an empty list if not found."""
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, "r") as file:
        return json.load(file)


def save_tasks(tasks):
    """Save tasks to the JSON file."""
    with open(DATA_FILE, "w") as file:
        json.dump(tasks, file, indent=4)


def add_task(description):
    """Add a new task."""
    tasks = load_tasks()
    new_task = {"id": len(tasks) + 1, "description": description}
    tasks.append(new_task)
    save_tasks(tasks)
    print(f"Task added: {description}")


def list_tasks():
    """List all tasks."""
    tasks = load_tasks()
    if not tasks:
        print("📭 No tasks found.")
        return
    print(" Your Tasks:")
    for task in tasks:
        print(f"{task['id']}. {task['description']}")


def search_tasks(keyword):
    """Search tasks containing the keyword."""
    tasks = load_tasks()
    results = [t for t in tasks if keyword.lower() in t["description"].lower()]
    if results:
        print(f"🔍 Search results for '{keyword}':")
        for t in results:
            print(f"{t['id']}. {t['description']}")
    else:
        print(f"No tasks found containing '{keyword}'.")


def show_help():
    """Display help message."""
    print("""
Usage:
    python tasks.py add "task description"   → Add a new task
    python tasks.py list                     → List all tasks
    python tasks.py search "keyword"         → Search tasks
    python tasks.py help                     → Show this help message
""")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        show_help()
    else:
        command = sys.argv[1].lower()
        if command == "add" and len(sys.argv) >= 3:
            add_task(" ".join(sys.argv[2:]))
        elif command == "list":
            list_tasks()
        elif command == "search" and len(sys.argv) >= 3:
            search_tasks(" ".join(sys.argv[2:]))
        elif command == "help":
            show_help()
        else:
            print(" Invalid command. Type `python tasks.py help` for usage.")
