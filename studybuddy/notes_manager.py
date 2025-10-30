import json, os

class NotesManager:
    def __init__(self, filepath):
        self.filepath = filepath
        os.makedirs(os.path.dirname(filepath), exist_ok=True)
        if not os.path.exists(filepath):
            with open(filepath, "w") as f:
                json.dump([], f)

    def _load(self):
        with open(self.filepath, "r") as f:
            return json.load(f)

    def _save(self, data):
        with open(self.filepath, "w") as f:
            json.dump(data, f, indent=2)

    def add(self, title, content):
        data = self._load()
        data.append({"title": title, "content": content})
        self._save(data)

    def list_all(self):
        data = self._load()
        if not data:
            print("No notes yet.")
        else:
            for i, note in enumerate(data, 1):
                print(f"{i}. {note['title']}: {note['content'][:60]}...")

