import pytest
from tasks.tasks import Task


@pytest.fixture
def sample_task():
return Task('Test task','Desc')


def test_task_to_dict(sample_task):
d = sample_task.to_dict()
assert d['title'] == 'Test task'
assert d['completed'] == False
