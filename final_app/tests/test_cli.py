import pytest
from storage.json_store import JSONStore
from cli.commands import Commands


def test_add_list_notes(tmp_path): store=JSONStore(tmp_path/'state.json'); cmds=Commands(store); cmds.add_note('Note1','Body1'); notes=store.get_notes(); assert notes[0]['title']=='Note1'
