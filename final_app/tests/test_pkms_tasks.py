from pkms import PKMS
import os

def test_add_note():
    filepath = 'data/test_notes.json'
    if os.path.exists(filepath):
        os.remove(filepath)
    pkms = PKMS(filepath)
    pkms.add_note("Test note")
    assert len(pkms.notes) == 1
