
from task_manager import TaskManager
from utils import print_welcome

def main():
    print_welcome()
    tm = TaskManager("memory/data.json")
    tm.run()

if __name__ == "__main__":
    main()
