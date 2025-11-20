import pytest
from agents.studyagent import summarize_note, generate_questions


def test_summarize():
note = {'body':'This is the first sentence. This is the second.'}
summary = summarize_note(note)
assert summary == 'This is the first sentence.'


def test_questions():
note = {'body':'One two three four five six'}
questions = generate_questions(note)
assert len(questions) == 3
