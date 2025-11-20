def plan_tasks(tasks): return [f"Task: {t['title']} (priority {t['priority']})" for t in sorted(tasks,key=lambda x:x['priority'])]
