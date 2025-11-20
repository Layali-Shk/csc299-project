from abc import ABC, abstractmethod


class Storage(ABC):
@abstractmethod
def add_note(self, note): pass
@abstractmethod
def get_notes(self): pass
@abstractmethod
def add_task(self, task): pass
@abstractmethod
def get_tasks(self): pass
@abstractmethod
def update_task(self, task_id, **kwargs): pass
