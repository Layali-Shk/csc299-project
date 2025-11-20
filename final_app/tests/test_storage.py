import os, tempfile, pytest
from storage.json_store import JSONStore


@pytest.fixture
def temp_json_store(): fd,path=tempfile.mkstemp(suffix='.json'); store=JSONStore(path); yield store; os.close(fd); os.remove(path)


def test_add_get_notes(temp_json_store): store=temp_json_store; note={'id':'1','title':'Test','body':'Body','tags':[],'created_at':'now'}; store.add_note(note); notes=store.get_notes(); assert len(notes)==1; assert notes[0]['title']=='Test'
