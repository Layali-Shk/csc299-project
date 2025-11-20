import json, os
from storage.base import Storage


class JSONStore(Storage):
def __init__(self, filename='data/state.json'):
self.filename = filename
os.makedirs(os.path.dirname(filename), exist_ok=True)
if not os.path.exists(filename):
with open(filename,'w') as f:
json.dump({'notes': [], 'tasks': []}, f)


def _load(self):
with open(self.filename,'r') as f: return json.load(f)
def _save(self, data):
with open(self.filename,'w') as f: json.dump(data,f,indent=2)


def add_note(self,note): data=self._load(); data['notes'].append(note); self._save(data)
def get_notes(self): return self._load()['notes']
def add_task(self,task): data=self._load(); data['tasks'].append(task); self._save(data)
def get_tasks(self): return self._load()['tasks']
def update_task(self,task_id,**kwargs):
data=self._load()
for t in data['tasks']:
if t['id']==task_id: t.update(kwargs)
self._save(data)
