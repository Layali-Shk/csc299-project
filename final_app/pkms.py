import json
import os

class PKMS:
    def __init__(self, filepath):
        self.filepath = filepath
        os.makedirs(os.path.dirname(filepath), exist_ok=True)
        if not os.path.exists(filepath):
            with open(filepath, "w") as f:
                json.dump([], f)
        self._load()

    def _load(self):
        with open(self.filepath, "r") as f:
            self.notes = json.load(f)

    def _save(self):
        with open(self.filepath, "w") as f:
            json.dump(self.notes, f, indent=2)

    def add_note(self, content, tags=None, category="General"):
        tags = tags or []
        note_id = max([n.get("id",0) for n in self.notes], default=0) + 1
        self.notes.append({
            "id": note_id,
            "content": content,
            "tags": tags,
            "category": category
        })
        self._save()
        print(f"Added note {note_id}")

    def list_notes(self):
        if not self.notes:
            print("No notes found.")
            return
        for n in self.notes:
            print(f"[{n.get('id')}] {n.get('content','')} (tags: {', '.join(n.get('tags',[]))}, category: {n.get('category','General')})")

    def search_notes(self, keyword):
        results = [n for n in self.notes if keyword.lower() in n.get("content","").lower()]
        if not results:
            print("No notes found with that keyword.")
            return
        for n in results:
            print(f"[{n.get('id')}] {n.get('content','')} (tags: {', '.join(n.get('tags',[]))}, category: {n.get('category','General')})")

    def delete_note(self, note_id):
        for n in self.notes:
            if n.get("id") == note_id:
                self.notes.remove(n)
                self._save()
                print(f"Deleted note {note_id}")
                return
        print(f"Note {note_id} not found")

    def update_note(self, note_id, content=None, tags=None, category=None):
        for n in self.notes:
            if n.get("id") == note_id:
                if content is not None:
                    n["content"] = content
                if tags is not None:
                    n["tags"] = tags
                if category is not None:
                    n["category"] = category
                self._save()
                print(f"Updated note {note_id}")
                return
        print(f"Note {note_id} not found")
