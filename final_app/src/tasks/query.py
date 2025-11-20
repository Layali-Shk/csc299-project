def search_tasks(tasks,keyword): return [t for t in tasks if keyword.lower() in t['title'].lower() or keyword.lower() in t['description'].lower()]
