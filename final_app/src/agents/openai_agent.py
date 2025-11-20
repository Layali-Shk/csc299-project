import os
try: import openai
except ImportError: openai=None


class OpenAIAgent:
def __init__(self,api_key=None):
self.api_key=api_key or os.getenv('OPENAI_API_KEY')
if openai and self.api_key: openai.api_key=self.api_key
def summarize_text(self,text):
if not openai or not self.api_key: return text[:100]+'...'
resp=openai.ChatCompletion.create(model='gpt-5-mini',messages=[{'role':'user','content':f'Summarize this text: {text}'}])
return resp.choices[0].message.content.strip()


# === final_app/src/cli/commands.py ===
from pkms.notes import Note
from tasks.tasks import Task


class Commands:
def __init__(self,store): self.store=store
def add_note(self,title,body,tags=None): n=Note(title,body,tags); self.store.add_note(n.to_dict()); print(f"Note '{title}' added.")
def list_notes(self): [print(f"[{n['id']}] {n['title']}") for n in self.store.get_notes()]
def add_task(self,title,description='',priority=3): t=Task(title,description,priority); self.store.add_task(t.to_dict()); print(f"Task '{title}' added.")
def list_tasks(self):
for t in self.store.get_tasks(): status='Done' if t['completed'] else 'Pending'; print(f"[{t['id']}] {t['title']} ({status})")
