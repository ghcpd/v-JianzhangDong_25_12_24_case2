@echo off
REM Use venv python when available
if exist ".venv\Scripts\python.exe" (
  set "PYTHON=.venv\Scripts\python.exe"
) else (
  if defined PYTHON (
    set "PYTHON=%PYTHON%"
  ) else (
    set "PYTHON=python"
  )
)
if not exist logs mkdir logs
"%PYTHON%" tests\test_docstrings.py
exit /b %ERRORLEVEL%