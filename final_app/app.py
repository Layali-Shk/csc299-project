import os, json, textwrap
from final_app.storage import JSONStorage
from final_app.pkms import PKMS
from final_app.tasks import TaskManager
from final_app.agents import AgentManager

class App:
    def __init__(self, data_dir=None):
        self.data_dir = data_dir or os.path.join(os.path.dirname(__file__), "data")
        os.makedirs(self.data_dir, exist_ok=True)
        self.storage = JSONStorage(self.data_dir)
        self.pkms = PKMS(self.storage)
        self.tasks = TaskManager(self.storage)
        self.agents = AgentManager(self.pkms, self.tasks)

    def help(self):
        print(textwrap.dedent("""        Commands (conversational or short)
        - add note
        - list notes
        - edit note <id>
        - delete note <id>
        - add task
        - list tasks
        - edit task <id>
        - delete task <id>
        - ai summarize note <id>
        - ai studyplan
        - search notes <query>
        - search tasks <query>
        - exit
        """))

    def run(self):
        print("Welcome to StudyBuddy AI (final). Say 'help' for commands.")
        while True:
            try:
                text = input("> ").strip()
            except (EOFError, KeyboardInterrupt):
                print('\nGoodbye.')
                break
            if not text:
                continue
            lower = text.lower()
            if lower in ("exit","quit"):
                print("Bye."); break
            if lower == "help":
                self.help(); continue

            # conversational handling
            if lower.startswith("add note"):
                title = input("Title: ")
                body = input("Body (end with blank line):\n")
                # simple multi-line capture
                lines = []
                while True:
                    l = input()
                    if not l.strip():
                        break
                    lines.append(l)
                body = body + "\n" + "\n".join(lines)
                note = self.pkms.add_note(title, body)
                print(f"Added note {note['id']}")
                continue

            if lower.startswith("list notes"):
                for n in self.pkms.list_notes():
                    print(f"[{n['id']}] {n['title']} (tags: {', '.join(n.get('tags',[]))})")
                continue

            if lower.startswith("search notes"):
                q = text[len("search notes"):].strip()
                if not q:
                    q = input("Query: ")
                for n in self.pkms.search(q):
                    print(f"[{n['id']}] {n['title']}")
                continue

            if lower.startswith("add task"):
                title = input("Task title: ")
                priority = input("Priority (Low/Medium/High) [Medium]: ") or "Medium"
                due = input("Due date (optional): ") or None
                t = self.tasks.add_task(title, priority, due)
                print(f"Added task {t['id']}")
                continue

            if lower.startswith("list tasks"):
                for t in self.tasks.list_tasks():
                    print(f"[{t['id']}] {t['title']} - {t['priority']} - due: {t.get('due')}")
                continue

            if lower.startswith("ai summarize note"):
                parts = text.split()
                try:
                    nid = int(parts[-1])
                except:
                    nid = int(input("Note id: "))
                note = self.pkms.get_note(nid)
                if not note:
                    print("Note not found."); continue
                print("Summarizing... (agent may need OPENAI_API_KEY)") 
                print(self.agents.summary_agent.summarize(note['body']))
                continue

            if lower.startswith("ai studyplan") or lower.startswith("ai plan") or lower.startswith("ai study plan"):
                print("Creating study plan from your notes and upcoming tasks...")
                plan = self.agents.study_agent.create_study_plan()
                print(plan)
                continue

            print("I didn't understand that. Type 'help' for commands.")

