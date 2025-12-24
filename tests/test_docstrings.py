"""Tests that verify the previously-reported missing docstrings are present.

This script reads `reference_link.txt` (created by the maintenance task)
and asserts that each listed module/class/function/method now has a
non-empty docstring. It uses the AST so it does not import the project
package (avoids side-effects).
"""
import ast
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REF = ROOT / "reference_link.txt"

ITEM_RE = re.compile(r"\)\s*(?P<path>[^:]+):\s*Missing\s*(?P<what>module|class|function|method)\s*docstring(?:\s*for\s*(?P<name>[\w\.()]+))?\s*\(line\s*(?P<line>\d+)\)", re.IGNORECASE)


def find_node_by_name(module_node, kind, name):
    if kind == "module":
        return module_node
    if kind == "function":
        for node in module_node.body:
            if isinstance(node, ast.FunctionDef) and node.name == name:
                return node
    if kind in ("class", "method"):
        cls_name = name.split(".")[0] if "." in name else name
        method_name = None
        if "." in name:
            _, method_name = name.split(".", 1)
        for node in module_node.body:
            if isinstance(node, ast.ClassDef) and node.name == cls_name:
                if kind == "class":
                    return node
                # method
                if method_name:
                    for child in node.body:
                        if isinstance(child, ast.FunctionDef) and child.name == method_name:
                            return child
    return None


def main():
    if not REF.exists():
        print(f"reference file not found: {REF}")
        return 2

    failures = []
    for i, line in enumerate(REF.read_text(encoding="utf-8").splitlines(), start=1):
        m = ITEM_RE.search(line)
        if not m:
            continue
        relpath = m.group("path").strip()
        what = m.group("what").lower()
        name = m.group("name")
        lineno = int(m.group("line"))

        target = ROOT / relpath
        if not target.exists():
            failures.append(f"{relpath}: file not found")
            continue
        src = target.read_text(encoding="utf-8")
        tree = ast.parse(src)
        node = find_node_by_name(tree, what, (name or "").replace("()", ""))
        doc = ast.get_docstring(node) if node is not None else None
        if not doc or not doc.strip():
            failures.append(f"{relpath}: missing {what} docstring for '{name or '<module>'}' (expected at line {lineno})")

    if failures:
        print("DOCSTRING CHECK: FAILED")
        for f in failures:
            print(" - ", f)
        return 1

    print("DOCSTRING CHECK: PASSED")
    return 0


if __name__ == "__main__":
    sys.exit(main())
