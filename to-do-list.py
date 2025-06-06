import json
import os
import textwrap
from datetime import datetime


def initialize_storage():
    if not os.path.exists("current_tasks.json"):
        with open("current_tasks.json", "w") as f:
            json.dump([], f)
    if not os.path.exists("archived_tasks.json"):
        with open("archived_tasks.json", "w") as f:
            json.dump([], f)
    if not os.path.exists("id_counter.json"):
        with open("id_counter.json", "w") as f:
            json.dump(1, f)


def load_current_tasks():
    with open("current_tasks.json", "r") as f:
        current_tasks = json.load(f)
        return current_tasks


def save_current_tasks(current_tasks):
    with open("current_tasks.json", "w") as f:
        json.dump(current_tasks, f, indent=2)


def load_archived_tasks():
    with open("archived_tasks.json", "r") as f:
        archived_tasks = json.load(f)
        return archived_tasks


def save_archived_tasks(archived_tasks):
    with open("archived_tasks.json", "w") as f:
        json.dump(archived_tasks, f, indent=2)


def load_id_counter():
    with open("id_counter.json", "r") as f:
        id_counter = json.load(f)
        return id_counter


def save_id_counter(id_counter):
    with open("id_counter.json", "w") as f:
        json.dump(id_counter, f, indent=2)


def choose_task(tasks):
    id = input("Enter task ID: ")
    for task in tasks:
        if str(task["id"]) == id:
            print()
            return task
    else:
        print("Task ID not found. Try again.", end=" ")
        return choose_task(tasks)


def archive_task(task):
    current_tasks = load_current_tasks()
    current_tasks.remove(task)
    save_current_tasks(current_tasks)
    archived_tasks = load_archived_tasks()
    archived_tasks.append(task)
    save_archived_tasks(archived_tasks)


def format_task_name(task_name):
    return f"{task_name[:14]}..." if len(task_name) > 17 else task_name


def add_task():
    tasks = load_current_tasks()
    id_counter = load_id_counter()
    new_task = {
        "id": id_counter,
        "task": input("Add a task: "),
        "description": input("Describe the task: "),
        "status": "to do",
        "created_at": datetime.now().strftime("%b %d, %Y at %I:%M %p")
    }
    tasks.append(new_task)
    save_current_tasks(tasks)
    save_id_counter(id_counter + 1)
    print("Task created successfully.\n")


def update_task():
    tasks = load_current_tasks()
    print("What task do you want to update?", end=" ")
    task = choose_task(tasks)
    status_dict = {
        "1": "to do",
        "2": "in progress",
        "3": "completed"
    }
    status = input("""1. to do
2. in progress
3. completed
Enter a number (1-3): """)
    while status not in ("1", "2", "3"):
        status = input(
            "Invalid status choice. Try again. Enter a number (1-3): ")
    print()
    task["status"] = status_dict.get(status)
    task["last_updated"] = datetime.now().strftime("%b %d, %Y at %I:%M %p")
    save_current_tasks(tasks)
    if status == "3":
        print("Task archived successfully.")
    else:
        print("Task updated successfully.")
    if status == "3":
        archive_task(task)
    print()


def delete_task():
    tasks = load_current_tasks()
    print("What task do you want to delete?", end=" ")
    task = choose_task(tasks)
    tasks.remove(task)
    save_current_tasks(tasks)
    print("Task deleted successfully.\n")


def view_task():
    tasks = load_current_tasks()
    print("What task do you want to view?", end=" ")
    task = choose_task(tasks)
    print("=" * 40)
    print(f"{" " * 11}DETAILED TASK VIEW{" " * 11}")
    print("=" * 40)
    print(f"ID: {task["id"]}")
    print(textwrap.fill(task["task"], 40,
          initial_indent="Task: "))
    print(textwrap.fill(task["description"], 40,
          initial_indent="Description: "))
    print(f"Status: {task["status"]}")
    print(f"Created at: {task["created_at"]}")
    if "last_updated" in task:
        print(f"Last updated: {task["last_updated"]}")
    print()


def list_tasks():
    current_tasks = load_current_tasks()
    archived_tasks = load_archived_tasks()
    task_labels_dict = {
        "1": "LIST OF CURRENT TASKS",
        "2": "LIST OF TO DO TASKS",
        "3": "LIST OF IN PROGRESS TASKS",
        "4": "LIST OF COMPLETED TASKS",
        "5": "LIST OF ARCHIVED TASKS"
    }
    task_list_dict = {
        "1": current_tasks,
        "2": [task for task in current_tasks if task["status"] == "to do"],
        "3": [task for task in current_tasks if task["status"] == "in progress"],
        "4": [task for task in archived_tasks if task["status"] == "completed"],
        "5": archived_tasks
    }
    task_type = input("""1. list current tasks
2. list to do tasks
3. list in progress tasks
4. list completed tasks
5. list archived tasks
Choose task type (1-5): """)
    print()
    while task_type not in task_labels_dict:
        task_type = input("Task type invalid. Try again. Enter task type: ")
    print()
    task_list = task_list_dict[task_type]
    if not task_list:
        print("No tasks listed.\n")
    else:
        print("=" * 40)
        print(f"{task_labels_dict[task_type]:^40}")
        print("=" * 40)
        print(f"{"ID":<5} {"Task":<20} {"Status":<12}")
        print("-" * 40)
        for task in task_list:
            print(
                f"{task["id"]:<5} {format_task_name(task["task"]):<20} {task["status"]:<12}")
        print()


def main():
    initialize_storage()
    print("This is a to-do list.")
    while True:
        action = input("""1. Add task
2. Update task
3. Delete task
4. View task
5. List tasks
6. Exit 
Enter a number (1-6): """)
        print()
        if action == "1":
            add_task()
        elif action == "2":
            update_task()
        elif action == "3":
            delete_task()
        elif action == "4":
            view_task()
        elif action == "5":
            list_tasks()
        elif action == "6":
            break
        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()
