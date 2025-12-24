"""Auto-runner for the project's documentation checks.

Detects the environment (Windows / Linux / Docker) and executes the
corresponding test runner. All output is saved to `logs/test_run.log`.
The log will include a timestamp and a final status line: TEST PASSED
or TEST FAILED.
"""
import os
import platform
import shlex
import shutil
import subprocess
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).parent
LOGS = ROOT / "logs"
LOG = LOGS / "test_run.log"


def detect_env():
    sys = platform.system().lower()
    if Path("/.dockerenv").exists() or os.environ.get("IN_DOCKER"):
        return "docker"
    if sys.startswith("windows"):
        return "windows"
    return "unix"


def get_runner(env):
    if env == "windows":
        return ["cmd.exe", "/c", "run_test.bat"]
    return ["/bin/bash", "run_test.sh"]


def main():
    LOGS.mkdir(exist_ok=True)
    env = detect_env()
    runner = get_runner(env)

    header = f"[{datetime.utcnow().isoformat()}Z] auto_test.py starting (env={env})\n"
    LOG.write_text(header, encoding="utf-8")

    try:
        proc = subprocess.run(runner, cwd=ROOT, capture_output=True, text=True, timeout=300)
        out = proc.stdout + proc.stderr
        LOG.write_text(header + out, encoding="utf-8", )
        status = "TEST PASSED" if proc.returncode == 0 else "TEST FAILED"
        with LOG.open("a", encoding="utf-8") as f:
            f.write(f"\n{datetime.utcnow().isoformat()}Z {status}\n")
        print(status)
        return proc.returncode
    except Exception as exc:
        with LOG.open("a", encoding="utf-8") as f:
            f.write(f"\nException while running tests: {exc}\n")
            f.write(f"{datetime.utcnow().isoformat()}Z TEST FAILED\n")
        print("TEST FAILED")
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
