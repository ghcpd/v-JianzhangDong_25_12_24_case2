import ast
import re
import sys

REF_FILE = "reference_link.txt"


def parse_reference_lines(path):
    entries = []
    with open(path, "r", encoding="utf-8") as fh:
        for line in fh:
            m = re.match(r"\(\d+\)\s+([^:]+):\s+(.+)\(line\s+(\d+)\)", line.strip())
            if m:
                filepath = m.group(1).strip()
                desc = m.group(2).strip()
                lineno = int(m.group(3))
                entries.append((filepath, desc, lineno))
    return entries


def has_module_docstring(tree):
    return ast.get_docstring(tree) is not None


def find_node_at_line(tree, lineno):
    for node in ast.walk(tree):
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)):
            if getattr(node, "lineno", None) == lineno:
                return node
    return None


def check_entry(root_dir, filepath, desc, lineno):
    fullpath = filepath
    try:
        with open(fullpath, "r", encoding="utf-8") as fh:
            src = fh.read()
    except FileNotFoundError:
        return False, f"{filepath}: file not found"

    tree = ast.parse(src)

    # module-level docstring check
    if "module" in desc:
        ok = has_module_docstring(tree)
        return ok, None if ok else f"{filepath}: missing module docstring"

    # try to extract a symbol name from the description (function/class/method)
    name_match = re.search(r"for\s+([A-Za-z_][A-Za-z0-9_]*)\b(?:\(\))?", desc)
    if name_match:
        symbol = name_match.group(1)
        # search AST for matching FunctionDef or ClassDef by name
        for node in ast.walk(tree):
            if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)) and node.name == symbol:
                ds = ast.get_docstring(node)
                return (True, None) if ds else (False, f"{filepath}: missing docstring for function '{symbol}'")
            if isinstance(node, ast.ClassDef) and node.name == symbol:
                ds = ast.get_docstring(node)
                return (True, None) if ds else (False, f"{filepath}: missing docstring for class '{symbol}'")

    # fallback: try locate node at given lineno
    node = find_node_at_line(tree, lineno)
    if node is None:
        return False, f"{filepath}: no definition found at line {lineno}"

    ds = ast.get_docstring(node)
    if ds:
        return True, None
    return False, f"{filepath}: missing docstring for {node.__class__.__name__} '{getattr(node, 'name', '')}' (line {lineno})"


def main():
    entries = parse_reference_lines(REF_FILE)
    failures = []
    for fp, desc, ln in entries:
        ok, msg = check_entry(".", fp, desc, ln)
        if not ok:
            failures.append(msg)
            print("FAIL:", msg)
        else:
            print("OK:", fp, "->", desc)

    if failures:
        print(f"\n{len(failures)} docstring check(s) failed")
        sys.exit(1)
    print("All documented items are present.")
    sys.exit(0)


if __name__ == "__main__":
    main()
