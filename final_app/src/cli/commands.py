from pkms.notes import Note
from tasks.tasks import Task


class Commands:
def __init__(self,store): self.store=store
def add_note(self,title,body,tags=None): n=Note(title,body,tags); self.store.add_note(n.to_dict()); print(f"Note '{title}' added.")
def list_notes(self): [print(f"[{n['id']}] {n['title']}") for n in self.store.get_notes()]
def add_task(self,title,description='',priority=3): t=Task(title,description,priority); self.store.add_task(t.to_dict()); print(f"Task '{title}' added.")
def list_tasks(self):
for t in self.store.get_tasks(): status='Done' if t['completed'] else 'Pending'; print(f"[{t['id']}] {t['title']} ({status})")


