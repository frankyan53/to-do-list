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
        print("Task ID not found.")
        return choose_task(tasks)


def archive_task(task):
    current_tasks = load_current_tasks()
    current_tasks.remove(task)
    save_current_tasks(current_tasks)
    archived_tasks = load_archived_tasks()
    archived_tasks.append(task)
    save_archived_tasks(archived_tasks)


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
                   1 - to do
                   2 - in progress
                   3 - completed
                   Choose new status (1/2/3):
                   """)
    if status in ("1", "2", "3"):
        task["status"] = status_dict.get(status)
        task["last_updated"] = datetime.now().strftime(
            "%b %d, %Y at %I:%M %p")
        save_current_tasks(tasks)
        print("Task updated successfully.")
    else:
        print("Invalid status choice.")


def delete_task():
    tasks = load_current_tasks()
    task = choose_task(tasks)
    tasks.remove(task)
    save_current_tasks(tasks)
