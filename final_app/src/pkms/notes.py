from utils import generate_id, current_time


class Note:
def __init__(self,title,body,tags=None):
self.id=generate_id(); self.title=title; self.body=body; self.tags=tags or []; self.created_at=current_time()
def to_dict(self): return vars(self)
