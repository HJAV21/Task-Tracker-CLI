import argparse
import json
import os
from datetime import datetime

file = 'Task.json'


def ensure_file():
    """Ensure Task.json exists and contains a valid list."""
    if not os.path.exists(file):
        with open(file, "w") as f:
            json.dump([], f, indent=4)
    else:
        # If file exists but is empty or corrupted, reset it
        try:
            with open(file, "r") as f:
                data = json.load(f)
            if not isinstance(data, list):
                raise ValueError("File does not contain a list")
        except (json.JSONDecodeError, ValueError):
            with open(file, "w") as f:
                json.dump([], f, indent=4)


def view_data():
    ensure_file()
    with open(file, "r") as f:
        temp = json.load(f)
        for idx, entry in enumerate(temp):
            print(f"Index: {idx}")
            print(f"Name of the task: {entry['Task']}")
            print(f"Creation date: {entry['Creation_Date']}")
            print(f"Progress: {entry['Progress']}")
            print("\n")


def add_Task():
    ensure_file()
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(file, "r") as f:
        temp = json.load(f)

    item_data = {
        "Task": input("Name of the Task: "),
        "Creation_Date": now,
        "Progress": input("Progress detail: ")
    }

    temp.append(item_data)

    with open(file, "w") as f:
        json.dump(temp, f, indent=4)
    print("Task added successfully.")


def delete_data():
    ensure_file()
    view_data()
    with open(file, "r") as f:
        temp = json.load(f)

    if not temp:
        print("No tasks to delete.")
        return

    data_length = len(temp) - 1
    delete_option = int(input(f"Select a number (0-{data_length}): "))

    if 0 <= delete_option <= data_length:
        removed = temp.pop(delete_option)
        with open(file, "w") as f:
            json.dump(temp, f, indent=4)
        print(f"Deleted task: {removed['Task']}")
    else:
        print("Invalid option.")


def Task_progress():
    ensure_file()
    view_data()
    with open(file, "r") as f:
        temp = json.load(f)

    if not temp:
        print("No tasks available.")
        return

    index = int(input("Enter the task index to check progress: "))
    if 0 <= index < len(temp):
        print(f"Progress of task '{temp[index]['Task']}': {temp[index]['Progress']}")
    else:
        print("Invalid index.")


def parsing():
    parser = argparse.ArgumentParser(description="Task Management")
    parser.add_argument('-add', action="store_true", help='Add to task')
    parser.add_argument('-remove', action="store_true", help="Remove Task")
    parser.add_argument('-view', action="store_true", help="View the task")
    parser.add_argument('-progress', action="store_true", help="Check Progress")
    args = parser.parse_args()

    if args.add:
        add_Task()
    elif args.remove:
        delete_data()
    elif args.view:
        view_data()
    elif args.progress:
        Task_progress()
    else:
        parser.print_help()


def main():
    parsing()


if __name__ == "__main__":
    main()





    
    



