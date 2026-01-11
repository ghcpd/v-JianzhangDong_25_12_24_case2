"""Utilities for task validation and small helpers.

This module provides simple helper functions used by the
application for validating task input and other tiny utilities.
"""

def validate_task_title(title):
    """Return True when `title` is a valid task title.

    A valid title is a non-empty string with length >= 3.

    Args:
        title: The task title to validate.

    Returns:
        True if the title is valid, otherwise False.
    """
    if not title or len(title) < 3:
        return False
    return True

def helper_function():
    """Placeholder helper used for internal/testing purposes.

    This function intentionally contains no operational logic and exists
    to demonstrate a documented helper.
    """
    pass
