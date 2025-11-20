# === final_app/src/storage/sqlite_store.py ===
import sqlite3
from storage.base import Storage


class SQLiteStore(Storage):
def __init__(self, db_file='data/state.db'):
self.db_file = db_file
self.conn = sqlite3.connect(db_file)
self._init_db()


def _init_db(self):
cursor = self.conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS notes (id TEXT PRIMARY KEY, title TEXT, body TEXT, tags TEXT, created_at TEXT)''')
cursor.execute('''CREATE TABLE IF NOT EXISTS tasks (id TEXT PRIMARY KEY, title TEXT, description TEXT, priority INTEGER, due TEXT, tags TEXT, completed INTEGER, created_at TEXT)''')
self.conn.commit()


def add_note(self, note):
cursor = self.conn.cursor()
cursor.execute('INSERT INTO notes VALUES (?,?,?,?,?)',
(note['id'], note['title'], note['body'], ','.join(note.get('tags', [])), note['created_at']))
self.conn.commit()


def get_notes(self):
cursor = self.conn.cursor()
cursor.execute('SELECT * FROM notes')
rows = cursor.fetchall()
return [{'id': r[0], 'title': r[1], 'body': r[2], 'tags': r[3].split(','), 'created_at': r[4]} for r in rows]


def add_task(self, task):
cursor = self.conn.cursor()
cursor.execute('INSERT INTO tasks VALUES (?,?,?,?,?,?,?,?)',
(task['id'], task['title'], task['description'], task['priority'], task['due'], ','.join(task.get('tags', [])), int(task['completed']), task['created_at']))
self.conn.commit()


def get_tasks(self):
cursor = self.conn.cursor()
cursor.execute('SELECT * FROM tasks')
rows = cursor.fetchall()
return [{'id': r[0], 'title': r[1], 'description': r[2], 'priority': r[3], 'due': r[4], 'tags': r[5].split(','), 'completed': bool(r[6]), 'created_at': r[7]} for r in rows]


def update_task(self, task_id, **kwargs):
cursor = self.conn.cursor()
for key, value in kwargs.items():
if key in ('title','description','priority','due','tags','completed'):
if key=='tags': value=','.join(value)
if key=='completed': value=int(value)
cursor.execute(f'UPDATE tasks SET {key}=? WHERE id=?', (value, task_id))
self.conn.commit()
