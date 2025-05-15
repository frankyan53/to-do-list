import json
import os
from datetime import datetime


def load_tasks():
    with open("tasks.json", "r") as f:
        tasks = json.load(f)
        return tasks


def save_tasks(tasks):
    with open("tasks.json", "w") as f:
        json.dump(tasks, f, indent=2)


def load_id_counter():
    with open("id_counter.json", "r") as f:
        id_counter = json.load(f)
        return id_counter


def save_id_counter(id_counter):
    with open("id_counter.json", "w") as f:
        json.dump(id_counter, f, indent=2)


def add_task():
    tasks = load_tasks()
    id_counter = load_id_counter()
    new_task = {
        "id": id_counter,
        "task": input("Add a task: "),
        "description": input("Describe the task: "),
        "status": "to do",
        "created_at": datetime.now().strftime("%b %d, %Y at %I:%M %p")
    }
    tasks.append(new_task)
    save_tasks(tasks)
    save_id_counter(id_counter + 1)
    print("Task created successfully.")
