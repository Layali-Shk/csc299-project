from notes_manager import NotesManager
from tasks_manager import TasksManager
from ai_agent import AIAgent

def main():
    print(" Welcome to StudyBuddy AI!")
    print("Type 'help' to see available commands.\n")

    notes = NotesManager("data/notes.json")
    tasks = TasksManager("data/tasks.json")
    ai = AIAgent(notes, tasks)

    while True:
        cmd = input(" > ").strip().lower()

        if cmd == "help":
            print("""
Commands:
  add note        - Add a new note
  list notes      - Show all notes
  add task        - Add a new task
  list tasks      - Show all tasks
  summarize note  - AI summarizes your notes
  study advice    - AI gives a study suggestion
  exit            - Quit the program
""")

        elif cmd == "add note":
            title = input("Title: ")
            content = input("Content: ")
            notes.add(title, content)
            print(" Note added.")

        elif cmd == "list notes":
            notes.list_all()

        elif cmd == "add task":
            task = input("Task description: ")
            tasks.add(task)
            print(" Task added.")

        elif cmd == "list tasks":
            tasks.list_all()

        elif cmd == "summarize note":
            ai.summarize_notes()

        elif cmd == "study advice":
            ai.study_advice()

        elif cmd == "exit":
            print(" Goodbye! Keep studying smart.")
            break

        else:
            print(" Unknown command. Type 'help' for options.")

if __name__ == "__main__":
    main()

