"""Task domain objects and an in-memory task manager used by the demo.

This module provides a minimal Task model and a light-weight TaskManager
used by the example FastAPI endpoints and unit/integration checks.
"""

from typing import List

class Task:
    """Represents a single task with title, description and status.

    Attributes:
        title (str): short title for the task.
        description (str): longer description text.
        status (str): current task status (e.g. "pending", "done").
    """
    def __init__(self, title: str, description: str, status: str = "pending"):
        self.title = title
        self.description = description
        self.status = status

    def mark_done(self):
        """Mark the task status as done."""
        self.status = "done"

class TaskManager:
    """In-memory manager for Task instances.

    This class intentionally keeps behaviour simple (append/remove/list)
    so it can be used in examples and tests without external dependencies.
    """
    def __init__(self):
        """Create an empty TaskManager."""
        self.tasks: List[Task] = []

    def add_task(self, task: Task):
        """Add a Task to the manager.

        Args:
            task (Task): task instance to add.
        """
        self.tasks.append(task)

    def list_tasks(self) -> list:
        """Return a list of managed Task objects."""
        return self.tasks

    def remove_task(self, index: int):
        """Remove a task by index if the index is valid.

        Args:
            index (int): position of the task to remove.
        """
        if 0 <= index < len(self.tasks):
            del self.tasks[index]
