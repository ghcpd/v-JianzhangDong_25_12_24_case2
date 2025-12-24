"""api — HTTP endpoints for the task manager.

This module exposes a minimal FastAPI application used by the
project's examples and integration checks. It intentionally keeps
handlers small and delegates business logic to `tasks.TaskManager`.
"""

from fastapi import FastAPI
from tasks import Task, TaskManager

app = FastAPI()
manager = TaskManager()

@app.get("/tasks")
def get_tasks():
    """Return a list of task titles currently registered in the manager.

    Returns:
        list[str]: titles of all tasks.
    """
    return [task.title for task in manager.list_tasks()]

@app.post("/tasks")
def create_task(title: str, description: str):
    """Create a new Task and add it to the manager.

    Args:
        title (str): short title for the task (required).
        description (str): longer description for the task.

    Returns:
        dict: confirmation message.
    """
    task = Task(title, description)
    manager.add_task(task)
    return {"message": "Task added successfully"}

def internal_helper():
    """Small internal helper used by examples — not part of the public API."""
    return "This is internal"
