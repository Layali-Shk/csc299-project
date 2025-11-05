# Example simple function
def inc(n: int) -> int:
    return n + 1

# Main PKMS entry point
from .tasks_manager import TaskManager  # only if you have this file

def main():
    print("Hello, Layali! Your PKMS tasks3 package is running.")
    # Example code: initialize task manager
    try:
        tm = TaskManager()
        tm.run()  # your main method
    except Exception:
        print("TaskManager not implemented yet.")

if __name__ == "__main__":
    main()
