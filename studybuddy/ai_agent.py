import random

class AIAgent:
    def __init__(self, notes_manager, tasks_manager):
        self.notes_manager = notes_manager
        self.tasks_manager = tasks_manager

    def summarize_notes(self):
        notes = self.notes_manager._load()
        if not notes:
            print("No notes to summarize.")
            return
        total_notes = len(notes)
        print(f"🧩 Summary: You have {total_notes} notes saved.")
        print("Here are the main topics:")
        for note in notes:
            print(f" - {note['title']}")
        print("🧠 Tip: Try connecting similar topics together while studying!")

    def study_advice(self):
        tips = [
            "Take short breaks every 45 minutes to refresh your brain.",
            "Summarize what you learned in your own words.",
            "Start with the hardest task first!",
            "Use active recall — test yourself, don’t just reread notes.",
            "Keep your tasks organized and prioritize deadlines."
        ]
        print("💡 Study Advice:", random.choice(tips))

