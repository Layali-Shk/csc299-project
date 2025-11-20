from utils import generate_id,current_time


class Task:
def __init__(self,title,description='',priority=3,due=None,tags=None,subtasks=None):
self.id=generate_id(); self.title=title; self.description=description; self.priority=priority; self.due=due; self.tags=tags or [];
self.subtasks=subtasks or []; self.completed=False; self.created_at=current_time()
def to_dict(self): return vars(self)
