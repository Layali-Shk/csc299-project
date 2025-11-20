import sqlite3
from storage.base import Storage


class SQLiteStore(Storage):
def __init__(self, db_file='data/state.db'):
self.conn=sqlite3.connect(db_file)
self._init_db()


def _init_db(self):
c=self.conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS notes (id TEXT PRIMARY KEY,title TEXT,body TEXT,tags TEXT,created_at TEXT)''')
c.execute('''CREATE TABLE IF NOT EXISTS tasks (id TEXT PRIMARY KEY,title TEXT,description TEXT,priority INTEGER,due TEXT,tags TEXT,completed INTEGER,created_at TEXT)''')
self.conn.commit()


def add_note(self,n): c=self.conn.cursor(); c.execute('INSERT INTO notes VALUES (?,?,?,?,?)',(n['id'],n['title'],n['body'],','.join(n.get('tags',[])),n['created_at'])); self.conn.commit()
def get_notes(self): c=self.conn.cursor(); c.execute('SELECT * FROM notes'); rows=c.fetchall(); return [{'id':r[0],'title':r[1],'body':r[2],'tags':r[3].split(','),'created_at':r[4]} for r in rows]
def add_task(self,t): c=self.conn.cursor(); c.execute('INSERT INTO tasks VALUES (?,?,?,?,?,?,?,?)',(t['id'],t['title'],t['description'],t['priority'],t['due'],','.join(t.get('tags',[])),int(t['completed']),t['created_at'])); self.conn.commit()
def get_tasks(self): c=self.conn.cursor(); c.execute('SELECT * FROM tasks'); rows=c.fetchall(); return [{'id':r[0],'title':r[1],'description':r[2],'priority':r[3],'due':r[4],'tags':r[5].split(','),'completed':bool(r[6]),'created_at':r[7]} for r in rows]
def update_task(self,task_id,**kwargs): c=self.conn.cursor();
for k,v in kwargs.items():
if k in ('title','description','priority','due','tags','completed'):
if k=='tags':v=','.join(v)
if k=='completed':v=int(v)
c.execute(f'UPDATE tasks SET {k}=? WHERE id=?',(v,task_id))
self.conn.commit()
