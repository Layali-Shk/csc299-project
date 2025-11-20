import readline
from storage.json_store import JSONStore
from cli.commands import Commands


class Shell:
def __init__(self): self.store=JSONStore(); self.cmds=Commands(self.store)
def run(self):
print("Welcome to StudyBuddy AI!")
while True:
try: line=input('> ')
except (KeyboardInterrupt,EOFError): print('\nGoodbye!'); break
if not line.strip(): continue
parts=line.strip().split(maxsplit=1); cmd=parts[0]; args=parts[1] if len(parts)>1 else ''
if cmd=='/note_add': title,body=args.split('|'); self.cmds.add_note(title.strip(),body.strip())
elif cmd=='/note_list': self.cmds.list_notes()
elif cmd=='/task_add': self.cmds.add_task(args.strip())
elif cmd=='/task_list': self.cmds.list_tasks()
elif cmd in ('exit','quit'): print('Bye!'); break
else: print('Unknown command:',cmd)
