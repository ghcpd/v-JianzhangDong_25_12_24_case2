#!/usr/bin/env python3
"""
自动测试执行脚本
"""
import platform
import subprocess
import os
import sys
from datetime import datetime

def detect_environment():
    """检测当前环境"""
    system = platform.system()
    if system == 'Windows':
        return 'Windows'
    elif os.path.exists('/.dockerenv'):
        return 'Docker'
    else:
        return 'Linux/macOS'

def run_test_script(env):
    """运行对应的测试脚本"""
    if env == 'Windows':
        command = ['run_test.bat']
    else:
        command = ['./run_test.sh']
    
    try:
        result = subprocess.run(command, capture_output=True, text=True, cwd=os.getcwd())
        output = result.stdout + result.stderr
        return output.strip(), result.returncode == 0
    except Exception as e:
        return f"Error running test script: {str(e)}", False

def main():
    """主函数"""
    env = detect_environment()
    print(f"Detected environment: {env}")
    
    output, success = run_test_script(env)
    
    # 添加时间戳
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_content = f"[{timestamp}] Test run in {env}\n{output}\n"
    
    if success:
        log_content += "TEST PASSED\n"
    else:
        log_content += "TEST FAILED\n"
    
    # 确保logs目录存在
    os.makedirs('logs', exist_ok=True)
    
    # 写入日志
    with open('logs/test_run.log', 'w', encoding='utf-8') as f:
        f.write(log_content)
    
    print("Log saved to logs/test_run.log")
    print(log_content)

if __name__ == "__main__":
    main()