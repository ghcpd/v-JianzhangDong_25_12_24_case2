from typing import List

class Task:
    """
    任务类，包含任务的基本信息
    """
    def __init__(self, title: str, description: str, status: str = "pending"):
        """Initialize a Task instance.

        Args:
            title: Task title.
            description: Task description.
            status: Optional task status (default: "pending").
        """
        self.title = title
        self.description = description
        self.status = status

    def mark_done(self):
        """Mark the task as completed by setting status to "done"."""
        self.status = "done"

class TaskManager:
    """Container object that manages a list of Task instances."""
    def __init__(self):
        """Create an empty TaskManager."""
        self.tasks: List[Task] = []

    def add_task(self, task: Task):
        """Add a Task instance to the internal task list.

        Args:
            task: Task to add.
        """
        self.tasks.append(task)

    def list_tasks(self) -> list:
        """Return the list of managed Task instances."""
        return self.tasks

    def remove_task(self, index: int):
        """Remove a Task by its index if the index is valid.

        Args:
            index: Position of the task to remove.
        """
        if 0 <= index < len(self.tasks):
            del self.tasks[index]
