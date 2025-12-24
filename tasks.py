"""Task management module with Task and TaskManager classes."""
from typing import List

class Task:
    """
    任务类，包含任务的基本信息
    """
    def __init__(self, title: str, description: str, status: str = "pending"):
        """Initialize a Task with title, description, and optional status."""
        self.title = title
        self.description = description
        self.status = status

    def mark_done(self):
        """Mark the task as completed."""
        self.status = "done"

class TaskManager:
    """Manager class for handling task operations."""
    def __init__(self):
        """Initialize TaskManager with an empty task list."""
        self.tasks: List[Task] = []

    def add_task(self, task: Task):
        """Add a task to the task list."""
        self.tasks.append(task)

    def list_tasks(self) -> list:
        """Return the list of all tasks."""
        return self.tasks

    def remove_task(self, index: int):
        """Remove a task from the task list by index."""
        if 0 <= index < len(self.tasks):
            del self.tasks[index]
