@echo off
if exist ".venv\Scripts\python.exe" (
  ".venv\Scripts\python.exe" run_tests.py
) else (
  python run_tests.py
)
exit /b %ERRORLEVEL%
