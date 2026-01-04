@echo off
REM Test script for Windows - Verifies that all required docstrings are present

setlocal enabledelayedexpansion

echo Testing for missing docstrings...

set "test_passed=1"

REM Function to check if a file contains required docstrings
REM We check for patterns of docstrings in each file

REM Check api.py
powershell -Command "^
$content = Get-Content api.py -Raw; ^
if ($content -match 'def create_task' -and $content -notmatch 'def create_task[^:]*:\s*\"\"\"') { ^
    Write-Host 'FAIL: api.py - create_task missing docstring'; ^
    exit 1 ^
} ^
if ($content -match 'def internal_helper' -and $content -notmatch 'def internal_helper[^:]*:\s*\"\"\"') { ^
    Write-Host 'FAIL: api.py - internal_helper missing docstring'; ^
    exit 1 ^
} ^
if ($content -notmatch '\"\"\"API module') { ^
    Write-Host 'FAIL: api.py missing module docstring'; ^
    exit 1 ^
} ^
exit 0 ^
"
if !errorlevel! neq 0 (
    set "test_passed=0"
)

REM Check app.py
powershell -Command "^
$content = Get-Content app.py -Raw; ^
if ($content -notmatch '\"\"\"Main application') { ^
    Write-Host 'FAIL: app.py missing module docstring'; ^
    exit 1 ^
} ^
exit 0 ^
"
if !errorlevel! neq 0 (
    set "test_passed=0"
)

REM Check config.py
powershell -Command "^
$content = Get-Content config.py -Raw; ^
if ($content -notmatch '\"\"\"Configuration file') { ^
    Write-Host 'FAIL: config.py missing module docstring'; ^
    exit 1 ^
} ^
exit 0 ^
"
if !errorlevel! neq 0 (
    set "test_passed=0"
)

REM Check utils.py
powershell -Command "^
$content = Get-Content utils.py -Raw; ^
if ($content -notmatch '\"\"\"Utility functions') { ^
    Write-Host 'FAIL: utils.py missing module docstring'; ^
    exit 1 ^
} ^
if ($content -match 'def validate_task_title' -and $content -notmatch 'def validate_task_title[^:]*:\s*\"\"\"') { ^
    Write-Host 'FAIL: utils.py - validate_task_title missing docstring'; ^
    exit 1 ^
} ^
if ($content -match 'def helper_function' -and $content -notmatch 'def helper_function[^:]*:\s*\"\"\"') { ^
    Write-Host 'FAIL: utils.py - helper_function missing docstring'; ^
    exit 1 ^
} ^
exit 0 ^
"
if !errorlevel! neq 0 (
    set "test_passed=0"
)

REM Check tasks.py
powershell -Command "^
$content = Get-Content tasks.py -Raw; ^
if ($content -notmatch '\"\"\"Task management module') { ^
    Write-Host 'FAIL: tasks.py missing module docstring'; ^
    exit 1 ^
} ^
if ($content -match 'class Task:' -and $content -notmatch 'class Task:\s*\"\"\"') { ^
    Write-Host 'FAIL: tasks.py - Task class missing docstring'; ^
    exit 1 ^
} ^
if ($content -match 'class TaskManager:' -and $content -notmatch 'class TaskManager:\s*\"\"\"') { ^
    Write-Host 'FAIL: tasks.py - TaskManager class missing docstring'; ^
    exit 1 ^
} ^
exit 0 ^
"
if !errorlevel! neq 0 (
    set "test_passed=0"
)

if "!test_passed!"=="1" (
    echo All docstring checks passed!
    exit /b 0
) else (
    echo Some docstring checks failed!
    exit /b 1
)
