import ast
import os
import sys

BASE = os.path.dirname(__file__)

files_to_check_module = ["api.py", "tasks.py", "utils.py", "app.py", "config.py"]

# Functions and classes to check for docstrings
checks = {
    'api.py': {
        'functions': ['create_task', 'internal_helper'],
        'classes': []
    },
    'tasks.py': {
        'functions': [],
        'classes': [
            {
                'name': 'TaskManager',
                'methods': ['add_task', 'list_tasks', 'remove_task']
            },
            {
                'name': 'Task',
                'methods': ['mark_done']
            }
        ]
    },
    'utils.py': {
        'functions': ['validate_task_title', 'helper_function'],
        'classes': []
    },
    'app.py': {'functions': [], 'classes': []},
    'config.py': {'functions': [], 'classes': []}
}

missing = []

for fname in files_to_check_module:
    path = os.path.join(BASE, fname)
    if not os.path.exists(path):
        missing.append(f"MISSING FILE: {fname}")
        continue
    with open(path, 'r', encoding='utf-8') as f:
        src = f.read()
    try:
        tree = ast.parse(src)
    except SyntaxError as e:
        missing.append(f"SYNTAX ERROR: {fname}: {e}")
        continue
    # Module docstring
    mod_doc = ast.get_docstring(tree)
    if not mod_doc:
        missing.append(f"{fname}: Missing module docstring")
    # top-level functions
    for node in tree.body:
        if isinstance(node, ast.FunctionDef):
            if node.name in checks.get(fname, {}).get('functions', []):
                if not ast.get_docstring(node):
                    missing.append(f"{fname}: Missing function docstring for {node.name}()")
        if isinstance(node, ast.ClassDef):
            # check classes
            for clsinfo in checks.get(fname, {}).get('classes', []):
                if node.name == clsinfo['name']:
                    if not ast.get_docstring(node):
                        missing.append(f"{fname}: Missing class docstring for {node.name}")
                    # check methods
                    methods = {n.name: n for n in node.body if isinstance(n, ast.FunctionDef)}
                    for m in clsinfo.get('methods', []):
                        if m in methods:
                            if not ast.get_docstring(methods[m]):
                                missing.append(f"{fname}: Missing method docstring for {node.name}.{m}()")
                        else:
                            missing.append(f"{fname}: Missing method {node.name}.{m}() (not found)")

# Print results
if missing:
    print("TEST FAILED: Missing docstrings detected")
    for m in missing:
        print(m)
    sys.exit(2)
else:
    print("All docstrings present. TEST PASSED")
    sys.exit(0)
