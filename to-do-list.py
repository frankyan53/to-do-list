import json
import os
from datetime import datetime


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
    print("Task created successfully.")


def update_task():
    tasks = load_current_tasks()
    task = choose_task(tasks)
    status_dict = {
        "1": "to do",
        "2": "in progress",
        "3": "completed"
    }
    status = input("""
1. to do
2. in progress
3. completed
Choose new status (1/2/3): """)
    if status in ("1", "2", "3"):
        task["status"] = status_dict.get(status)
        task["last_updated"] = datetime.now().strftime(
            "%b %d, %Y at %I:%M %p")
        save_current_tasks(tasks)
        if status == "3":
            print("Task archived successfully.")
        else:
            print("Task updated successfully.")
    if status == "3":
        archive_task(task)
    else:
        print("Invalid status choice.")


def delete_task():
    tasks = load_current_tasks()
    task = choose_task(tasks)
    tasks.remove(task)
    save_current_tasks(tasks)
    print("Task deleted successfully.")


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
    task_type = input("""
1. list current tasks
2. list to do tasks
3. list in progress tasks
4. list completed tasks
5. list archived tasks
Choose task type (1/2/3/4/5): """)
    while task_type not in task_labels_dict:
        task_type = input("Task type invalid. Try again. Enter task type: ")
    task_list = task_list_dict[task_type]
    if not task_list:
        print("No tasks listed.")
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
