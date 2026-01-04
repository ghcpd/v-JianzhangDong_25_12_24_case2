#!/bin/bash

# Test script for Linux/macOS - Verifies that all required docstrings are present

test_passed=1

echo "Testing for missing docstrings..."

# Check api.py
if ! grep -q '"""API module' api.py; then
    echo "FAIL: api.py missing module docstring"
    test_passed=0
fi

if grep -q 'def create_task' api.py && ! grep -A1 'def create_task' api.py | grep -q '"""Create'; then
    echo "FAIL: api.py - create_task missing docstring"
    test_passed=0
fi

if grep -q 'def internal_helper' api.py && ! grep -A1 'def internal_helper' api.py | grep -q '"""Internal'; then
    echo "FAIL: api.py - internal_helper missing docstring"
    test_passed=0
fi

# Check app.py
if ! grep -q '"""Main application' app.py; then
    echo "FAIL: app.py missing module docstring"
    test_passed=0
fi

# Check config.py
if ! grep -q '"""Configuration file' config.py; then
    echo "FAIL: config.py missing module docstring"
    test_passed=0
fi

# Check utils.py
if ! grep -q '"""Utility functions' utils.py; then
    echo "FAIL: utils.py missing module docstring"
    test_passed=0
fi

if grep -q 'def validate_task_title' utils.py && ! grep -A1 'def validate_task_title' utils.py | grep -q '"""Validate'; then
    echo "FAIL: utils.py - validate_task_title missing docstring"
    test_passed=0
fi

if grep -q 'def helper_function' utils.py && ! grep -A1 'def helper_function' utils.py | grep -q '"""Helper'; then
    echo "FAIL: utils.py - helper_function missing docstring"
    test_passed=0
fi

# Check tasks.py
if ! grep -q '"""Task management module' tasks.py; then
    echo "FAIL: tasks.py missing module docstring"
    test_passed=0
fi

if grep -q 'class Task:' tasks.py && ! grep -A1 'class Task:' tasks.py | grep -q '"""'; then
    echo "FAIL: tasks.py - Task class missing docstring"
    test_passed=0
fi

if grep -q 'class TaskManager:' tasks.py && ! grep -A1 'class TaskManager:' tasks.py | grep -q '"""'; then
    echo "FAIL: tasks.py - TaskManager class missing docstring"
    test_passed=0
fi

# Check for method docstrings in Task class
if grep -q 'def __init__' tasks.py && ! grep -A1 'def __init__.*Task' tasks.py | grep -q '"""Initialize'; then
    echo "FAIL: tasks.py - Task.__init__ missing docstring"
    test_passed=0
fi

if grep -q 'def mark_done' tasks.py && ! grep -A1 'def mark_done' tasks.py | grep -q '"""Mark'; then
    echo "FAIL: tasks.py - mark_done missing docstring"
    test_passed=0
fi

# Check for method docstrings in TaskManager class
if grep -q 'def add_task' tasks.py && ! grep -A1 'def add_task' tasks.py | grep -q '"""Add'; then
    echo "FAIL: tasks.py - add_task missing docstring"
    test_passed=0
fi

if grep -q 'def list_tasks' tasks.py && ! grep -A1 'def list_tasks' tasks.py | grep -q '"""Return'; then
    echo "FAIL: tasks.py - list_tasks missing docstring"
    test_passed=0
fi

if grep -q 'def remove_task' tasks.py && ! grep -A1 'def remove_task' tasks.py | grep -q '"""Remove'; then
    echo "FAIL: tasks.py - remove_task missing docstring"
    test_passed=0
fi

if [ "$test_passed" -eq 1 ]; then
    echo "All docstring checks passed!"
    exit 0
else
    echo "Some docstring checks failed!"
    exit 1
fi
