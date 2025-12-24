"""HTTP API endpoints for the task manager application.

This module exposes a minimal FastAPI application used by the
project's example endpoints.
"""

from fastapi import FastAPI
from tasks import Task, TaskManager

app = FastAPI()
manager = TaskManager()

@app.get("/tasks")
def get_tasks():
    """Return the list of task titles.

    Response is a plain list of task.title strings.
    """
    return [task.title for task in manager.list_tasks()]

@app.post("/tasks")
def create_task(title: str, description: str):
    """Create a new Task and add it to the manager.

    Args:
        title: The task title.
        description: The task description.

    Returns:
        A dict containing a success message.
    """
    task = Task(title, description)
    manager.add_task(task)
    return {"message": "Task added successfully"}

def internal_helper():
    """Small internal helper used by the module (not part of the API).

    Returns a static string for internal use.
    """
    return "This is internal"
