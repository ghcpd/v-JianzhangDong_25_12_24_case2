"""Task model and manager utilities."""
from typing import List

class Task:
    """
    任务类，包含任务的基本信息
    """
    def __init__(self, title: str, description: str, status: str = "pending"):
        self.title = title
        self.description = description
        self.status = status

    def mark_done(self):
        """Mark the task as done."""
        self.status = "done"

class TaskManager:
    """Manager for Task objects, supports add/list/remove operations."""
    def __init__(self):
        self.tasks: List[Task] = []

    def add_task(self, task: Task):
        """Add a Task to the internal list."""
        self.tasks.append(task)

    def list_tasks(self) -> list:
        """Return the list of tasks."""
        return self.tasks

    def remove_task(self, index: int):
        """Remove task by index if index is valid."""
        if 0 <= index < len(self.tasks):
            del self.tasks[index]
