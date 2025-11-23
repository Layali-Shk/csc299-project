import os
from tasks import TaskManager
from pkms import PKMS
from agents import StudyAgent
from openai import OpenAI
from colorama import init, Fore

init(autoreset=True)

def main():
    tasks_file = os.path.join("data", "tasks.json")
    notes_file = os.path.join("data", "notes.json")
    os.makedirs("data", exist_ok=True)

    tasks = TaskManager(tasks_file)
    pkms = PKMS(notes_file)
    client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))
    study_agent = StudyAgent(client)

    tasks.upcoming_alerts()

    print(Fore.CYAN + "Welcome to StudyBuddy AI (Enhanced). Type 'help' for commands.")

    while True:
        command = input(Fore.MAGENTA + "> ").strip().lower()

        if command == "help":
            print(Fore.CYAN + """
StudyBuddy AI - Commands Guide

Notes Management:
  - add note         : Add a new note with optional tags and category.
  - list notes       : List all notes (can filter by category).
  - search notes     : Search notes by keyword and/or tag.
  - update note      : Update a note's content, tags, or category.
  - delete note      : Delete a note by its ID.

Tasks Management:
  - add task         : Add a new task with optional tags, priority, due date, and recurrence.
  - list tasks       : List all tasks, optionally sorted by priority or due date.
  - filter tasks     : Filter tasks by keyword and/or tag.
  - mark done        : Mark a task as completed.
  - delete task      : Delete a task by its ID.

AI Agents:
  - ai summarize note : Summarize a specific note using AI.
  - ai summarize all  : Summarize all notes using AI.
  - ai studyplan      : Generate a prioritized study plan from notes and tasks.

Other:
  - help             : Show this help menu.
  - exit             : Exit the program.
""")

        elif command == "exit":
            print(Fore.CYAN + "Goodbye!")
            break

        # PKMS commands
        elif command.startswith("add note"):
            content = input("Enter note content: ")
            tags = [t.strip() for t in input("Enter comma-separated tags (optional): ").split(",") if t.strip()]
            category = input("Enter category (optional): ") or "General"
            pkms.add_note(content, tags, category)

        elif command.startswith("list notes"):
            pkms.list_notes()

        elif command.startswith("search notes"):
            keyword = input("Enter keyword to search: ")
            pkms.search_notes(keyword)

        elif command.startswith("delete note"):
            pkms.delete_note(int(input("Enter note ID: ")))

        elif command.startswith("update note"):
            note_id = int(input("Enter note ID: "))
            content = input("New content (blank to skip): ")
            tags = input("New tags (comma-separated, blank to skip): ").split(",")
            tags = [t.strip() for t in tags if t.strip()] or None
            category = input("New category (blank to skip): ") or None
            pkms.update_note(note_id, content or None, tags, category)

        # Task commands
        elif command.startswith("add task"):
            content = input("Enter task content: ")
            tags = [t.strip() for t in input("Enter comma-separated tags (optional): ").split(",") if t.strip()]
            priority = input("Enter priority (Low/Medium/High, default None): ").capitalize() or "None"
            due = input("Enter due date (YYYY-MM-DD, optional): ") or "None"
            recurrence = input("Enter recurrence (daily/weekly/monthly, optional): ") or None
            tasks.add_task(content, tags, priority, due, recurrence)

        elif command.startswith("list tasks"):
            sort_by = input("Sort by (priority/due/none): ").lower()
            tasks.list_tasks(sort_by if sort_by in ["priority","due"] else None)

        elif command.startswith("filter tasks"):
            keyword = input("Keyword (optional): ") or None
            tag = input("Tag (optional): ") or None
            tasks.filter_tasks(keyword, tag)

        elif command.startswith("delete task"):
            tasks.delete_task(int(input("Enter task ID: ")))

        elif command.startswith("mark done"):
            tasks.mark_done(int(input("Enter task ID: ")))

        # AI commands
        elif command.startswith("ai summarize note"):
            note_id = int(input("Enter note ID: "))
            study_agent.summarize_note(pkms, note_id)

        elif command.startswith("ai summarize all"):
            study_agent.summarize_all_notes(pkms)

        elif command.startswith("ai studyplan"):
            study_agent.generate_plan(pkms, tasks)

        else:
            print(Fore.RED + "Unknown command. Type 'help' for a list of commands.")

if __name__ == "__main__":
    main()
