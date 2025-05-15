import json
import os


def load_tasks():
    with open("tasks.json", "r") as f:
        tasks = json.load(f)
        return tasks


def save_tasks(tasks):
    with open("tasks.json", "w") as f:
        json.dump(tasks, f, indent=2)
