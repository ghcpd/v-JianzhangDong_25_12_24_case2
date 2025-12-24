#!/usr/bin/env bash
set -euo pipefail

# Use the venv python when available
if [ -d ".venv" ] && [ -x ".venv/bin/python" ]; then
  PYTHON=.venv/bin/python
else
  PYTHON=${PYTHON:-python3}
fi

mkdir -p logs
"$PYTHON" tests/test_docstrings.py
