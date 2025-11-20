def search_notes(notes,keyword): return [n for n in notes if keyword.lower() in n['title'].lower() or keyword.lower() in n['body'].lower()]
