#!/usr/bin/env python3
"""
检查文档字符串的脚本
"""
import os
import sys
import ast
import importlib.util

def has_docstring(node):
    """检查节点是否有文档字符串"""
    return ast.get_docstring(node) is not None

def check_file(file_path):
    """检查文件中的文档字符串"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        tree = ast.parse(content, filename=file_path)
        
        issues = []
        
        # 检查模块文档字符串
        if not has_docstring(tree):
            issues.append(f"Missing module docstring in {file_path}")
        
        for node in ast.walk(tree):
            if isinstance(node, ast.ClassDef):
                if not has_docstring(node):
                    issues.append(f"Missing class docstring for {node.name} in {file_path}")
            elif isinstance(node, ast.FunctionDef):
                if not has_docstring(node):
                    class_name = ""
                    for parent in ast.walk(tree):
                        if isinstance(parent, ast.ClassDef) and node in parent.body:
                            class_name = parent.name
                            break
                    if class_name:
                        issues.append(f"Missing function docstring for {node.name}() in {class_name} in {file_path}")
                    else:
                        issues.append(f"Missing function docstring for {node.name}() in {file_path}")
        
        return issues
    except Exception as e:
        return [f"Error checking {file_path}: {str(e)}"]

def main():
    """主函数"""
    workspace = os.getcwd()
    py_files = [f for f in os.listdir(workspace) if f.endswith('.py')]
    
    all_issues = []
    for file in py_files:
        file_path = os.path.join(workspace, file)
        issues = check_file(file_path)
        all_issues.extend(issues)
    
    if all_issues:
        print("TEST FAILED")
        for issue in all_issues:
            print(issue)
        return 1
    else:
        print("TEST PASSED")
        return 0

if __name__ == "__main__":
    sys.exit(main())