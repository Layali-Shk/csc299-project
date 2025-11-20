def summarize_note(note): return note['body'].split('.')[0]+'.'


def generate_questions(note): words=note['body'].split(); return [f"What is {' '.join(words[:i+3])}?" for i in range(min(3,len(words)-3))]



