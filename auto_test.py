import os
import platform
import subprocess
from datetime import datetime

LOG_DIR = os.path.join(os.path.dirname(__file__), 'logs')
LOG_FILE = os.path.join(LOG_DIR, 'test_run.log')

if not os.path.exists(LOG_DIR):
    os.makedirs(LOG_DIR)

# Detect environment
system = platform.system()
run_cmd = None
if system == 'Windows':
    run_cmd = ['cmd', '/c', 'run_test.bat']
else:
    # Detect docker by common markers
    is_docker = False
    try:
        if os.path.exists('/.dockerenv'):
            is_docker = True
        else:
            with open('/proc/1/cgroup', 'r') as f:
                if 'docker' in f.read() or 'containerd' in f.read():
                    is_docker = True
    except Exception:
        is_docker = False
    # For docker or linux/mac, run the shell script
    run_cmd = ['bash', 'run_test.sh']

# Execute the tests
start_ts = datetime.utcnow().isoformat() + 'Z'
proc = subprocess.run(run_cmd, capture_output=True, text=True)
# Write log
with open(LOG_FILE, 'a', encoding='utf-8') as f:
    f.write(f"Timestamp: {start_ts}\n")
    f.write(proc.stdout or '')
    if proc.stderr:
        f.write(proc.stderr)
    status_line = 'TEST PASSED' if proc.returncode == 0 else 'TEST FAILED'
    f.write(status_line + '\n')

# Exit with the same status
if proc.returncode != 0:
    print(status_line)
    exit(proc.returncode)
else:
    print(status_line)
    exit(0)
