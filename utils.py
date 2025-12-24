"""Utility helpers for validating and manipulating task-related data.

Lightweight helpers kept here so they can be reused by the application
and by unit tests without pulling in additional dependencies.
"""

def validate_task_title(title):
    """Quick validation for a task title.

    Rules:
      - must be non-empty
      - must be at least 3 characters long

    Returns:
        bool: True when the title looks valid, otherwise False.
    """
    if not title or len(title) < 3:
        return False
    return True

def helper_function():
    """Placeholder helper retained for examples/tests (no-op)."""
    pass
