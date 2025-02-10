import os
import importlib.util
import sys

def handler(event):
    """
    Dynamically load and execute the code.py file as a script.
    """
    # print current pythin version
    print(f"Python version: {sys.version}")
    code_file = "code.py"
    
    # Check if the file exists
    if os.path.exists(code_file):
        # Dynamically import the file
        spec = importlib.util.spec_from_file_location("code", code_file)
        code = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(code)
    else:
        print(f"File {code_file} not found. Please ensure it exists.")
