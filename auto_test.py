import platform
import subprocess
import os
import datetime
import sys

LOG_DIR = "logs"
LOG_FILE = os.path.join(LOG_DIR, "test_run.log")


def detect_environment():
    system = platform.system()
    # simple Docker detection
    if system == "Linux":
        try:
            if os.path.exists("/.dockerenv"):
                return "Docker"
            with open("/proc/self/cgroup", "r") as fh:
                data = fh.read()
                if "docker" in data or "kubepods" in data:
                    return "Docker"
        except Exception:
            pass
        return "Linux"
    if system == "Darwin":
        return "Linux"
    if system == "Windows":
        return "Windows"
    return system


def run_script(command, shell=False):
    proc = subprocess.run(command, shell=shell, capture_output=True, text=True)
    return proc.returncode, proc.stdout + ("\n" + proc.stderr if proc.stderr else "")


def main():
    env = detect_environment()
    if env == "Windows":
        script = "run_test.bat"
        cmd = [script]
        use_shell = True
    else:
        script = "./run_test.sh"
        cmd = [script]
        use_shell = True

    os.makedirs(LOG_DIR, exist_ok=True)
    ts = datetime.datetime.now().isoformat()

    rc, output = run_script(cmd, shell=use_shell)

    status = "TEST PASSED" if rc == 0 else "TEST FAILED"

    with open(LOG_FILE, "a", encoding="utf-8") as fh:
        fh.write(f"[{ts}] Environment: {env}\n")
        fh.write(output)
        fh.write(f"\nFinal status: {status}\n\n")

    print(output)
    print(status)
    sys.exit(rc)


if __name__ == "__main__":
    main()
