"""
工具函数模块
"""
def validate_task_title(title):
    """
    验证任务标题
    """
    if not title or len(title) < 3:
        return False
    return True

def helper_function():
    """
    帮助函数
    """
    pass
