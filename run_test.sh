#!/usr/bin/env bash
if [ -x ".venv/bin/python" ]; then
  .venv/bin/python run_tests.py
else
  python run_tests.py
fi
exit $?
