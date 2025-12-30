"""
任务管理模块
"""
from typing import List

class Task:
    """
    任务类，包含任务的基本信息
    """
    def __init__(self, title: str, description: str, status: str = "pending"):
        """
        初始化任务
        """
        self.title = title
        self.description = description
        self.status = status

    def mark_done(self):
        """
        标记任务为完成
        """
        self.status = "done"

class TaskManager:
    """
    任务管理器类
    """
    def __init__(self):
        """
        初始化任务管理器
        """
        self.tasks: List[Task] = []

    def add_task(self, task: Task):
        """
        添加任务
        """
        self.tasks.append(task)

    def list_tasks(self) -> list:
        """
        列出所有任务
        """
        return self.tasks

    def remove_task(self, index: int):
        """
        根据索引移除任务
        """
        if 0 <= index < len(self.tasks):
            del self.tasks[index]
