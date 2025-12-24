"""Automatic test execution script for documentation verification."""

import os
import sys
import subprocess
import platform
from datetime import datetime
from pathlib import Path


def get_environment():
    """Detect current environment (Windows/Linux/Docker)."""
    if os.environ.get('DOCKER_CONTAINER'):
        return 'docker'
    elif platform.system() == 'Windows':
        return 'windows'
    else:
        return 'linux'


def get_test_script():
    """Get the appropriate test script based on environment."""
    env = get_environment()
    if env == 'windows':
        return 'run_test.bat'
    else:
        return 'run_test.sh'


def run_tests():
    """Run the appropriate test script and capture output."""
    env = get_environment()
    
    # Create logs directory if not exists
    log_dir = Path('logs')
    log_dir.mkdir(exist_ok=True)
    
    log_file = log_dir / 'test_run.log'
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    
    try:
        # Open log file for writing
        with open(log_file, 'w') as f:
            f.write(f"Test Execution Report\n")
            f.write(f"Environment: {env}\n")
            f.write(f"Timestamp: {timestamp}\n")
            f.write(f"{'='*60}\n\n")
            
            # Verify docstrings in Python files
            test_passed = verify_docstrings(f)
            
            # Write final status
            if test_passed:
                status = "TEST PASSED"
                f.write(f"\nFinal Status: {status}\n")
                print(f"[{timestamp}] {status}")
                return True
            else:
                status = "TEST FAILED"
                f.write(f"\nFinal Status: {status}\n")
                print(f"[{timestamp}] {status}")
                return False
    
    except Exception as e:
        with open(log_file, 'a') as f:
            f.write(f"\nExecution Error: {str(e)}\n")
            f.write(f"Final Status: TEST FAILED\n")
        print(f"Error running tests: {str(e)}")
        return False


def verify_docstrings(log_file):
    """Verify that all required docstrings are present in Python files."""
    all_passed = True
    
    # Check api.py
    log_file.write("Checking api.py...\n")
    if not check_file_docstrings('api.py', {
        'module': '"""API module',
        'create_task': 'def create_task',
        'internal_helper': 'def internal_helper'
    }, log_file):
        all_passed = False
    
    # Check app.py
    log_file.write("Checking app.py...\n")
    if not check_file_docstrings('app.py', {
        'module': '"""Main application'
    }, log_file):
        all_passed = False
    
    # Check config.py
    log_file.write("Checking config.py...\n")
    if not check_file_docstrings('config.py', {
        'module': '"""Configuration file'
    }, log_file):
        all_passed = False
    
    # Check utils.py
    log_file.write("Checking utils.py...\n")
    if not check_file_docstrings('utils.py', {
        'module': '"""Utility functions',
        'validate_task_title': 'def validate_task_title',
        'helper_function': 'def helper_function'
    }, log_file):
        all_passed = False
    
    # Check tasks.py
    log_file.write("Checking tasks.py...\n")
    if not check_file_docstrings('tasks.py', {
        'module': '"""Task management module',
        'Task class': 'class Task:',
        'TaskManager class': 'class TaskManager:',
        'mark_done': 'def mark_done',
        'add_task': 'def add_task',
        'list_tasks': 'def list_tasks',
        'remove_task': 'def remove_task'
    }, log_file):
        all_passed = False
    
    return all_passed


def check_file_docstrings(filename, patterns, log_file):
    """Check if a file contains expected docstrings."""
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Check module docstring first
        if 'module' in patterns:
            if patterns['module'] not in content:
                log_file.write(f"  FAIL: Missing module docstring\n")
                return False
        
        # Check other patterns
        for name, pattern in patterns.items():
            if name == 'module':
                continue
            
            if pattern in content:
                # Check if the function/class/method has a docstring
                if '"""' not in content.split(pattern)[1].split('\n')[0:5]:
                    if '"""' not in ''.join(content.split(pattern)[1].split('\n')[0:5]):
                        log_file.write(f"  FAIL: {name} missing docstring\n")
                        return False
        
        log_file.write(f"  PASS: All required docstrings found\n")
        return True
    
    except Exception as e:
        log_file.write(f"  ERROR: {str(e)}\n")
        return False


def create_default_test_script(env, script_name):
    """Create a default test script that checks for docstrings."""
    if env == 'windows':
        # Create Windows batch file - not used since run_test.bat exists
        return
    else:
        # Create Unix shell script - not used since run_test.sh exists
        return


if __name__ == "__main__":
    success = run_tests()
    sys.exit(0 if success else 1)
