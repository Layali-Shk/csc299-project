from colorama import Fore

class StudyAgent:
    def __init__(self, client):
        self.client = client

    def summarize_note(self, pkms, note_id):
        for note in pkms.notes:
            if note.get("id") == note_id:
                content = note.get("content","")
                response = self.client.chat.completions.create(
                    model="gpt-5-mini",
                    messages=[
                        {"role": "system", "content": "You are a helpful assistant that summarizes notes."},
                        {"role": "user", "content": f"Summarize this note in one sentence: {content}"}
                    ]
                )
                summary = response.choices[0].message.content
                print(f"Summarized note {note_id}: {summary}")
                return
        print(f"Note {note_id} not found")

    def summarize_all_notes(self, pkms):
        if not pkms.notes:
            print("No notes to summarize.")
            return
        for note in pkms.notes:
            content = note.get("content","")
            response = self.client.chat.completions.create(
                model="gpt-5-mini",
                messages=[
                    {"role": "system", "content": "You are a helpful assistant that summarizes notes."},
                    {"role": "user", "content": f"Summarize this note in one sentence: {content}"}
                ]
            )
            summary = response.choices[0].message.content
            print(f"[{note.get('id')}] {summary}")

    def generate_plan(self, pkms, tasks):
        if not pkms.notes and not tasks.tasks:
            print("No notes or tasks to generate a plan.")
            return
        print("Generated study plan based on notes and tasks:")
        for note in pkms.notes:
            content = note.get("content","")
            response = self.client.chat.completions.create(
                model="gpt-5-mini",
                messages=[
                    {"role": "system", "content": "You are a helpful assistant that generates study plans."},
                    {"role": "user", "content": f"Give a short action step for this note: {content}"}
                ]
            )
            summary = response.choices[0].message.content
            print(f"- Review note [{note.get('id')}]: {summary}")

        for task in tasks.tasks:
            content = task.get("content","")
            response = self.client.chat.completions.create(
                model="gpt-5-mini",
                messages=[
                    {"role": "system", "content": "You are a helpful assistant that generates study plans."},
                    {"role": "user", "content": f"Give a short action step for this task: {content}"}
                ]
            )
            summary = response.choices[0].message.content
            print(f"- Complete task [{task.get('id')}]: {summary}")

    def suggest_task(self, tasks):
        if not tasks.tasks:
            print("No tasks to suggest.")
            return

        task_text = "\n".join(
            [f"- {t.get('content','')} (Priority: {t.get('priority','None')}, Due: {t.get('due','None')})"
             for t in tasks.tasks]
        )

        response = self.client.chat.completions.create(
            model="gpt-5-mini",
            messages=[
                {"role": "system", "content": "You are a helpful assistant that recommends which task to do next."},
                {"role": "user", "content": f"Here are my tasks:\n{task_text}\nSuggest the top 1 task I should do next and explain why."}
            ]
        )

        suggestion = response.choices[0].message.content
        print(Fore.GREEN + "AI Task Suggestion:")
        print(suggestion)
