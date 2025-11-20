import pytest
from pkms.notes import Note


def test_note_to_dict(): n=Note('Title','Body',['tag1']); d=n.to_dict(); assert d['title']=='Title'; assert 'tag1' in d['tags']
