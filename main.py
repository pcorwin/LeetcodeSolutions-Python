import os
import importlib.util


def run_function(module_path, function_name):
    spec = importlib.util.spec_from_file_location("", module_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)

    if hasattr(module, function_name):
        function = getattr(module, function_name)
        function()
    else:
        print(f"Function '{function_name}' not found in '{module_path}'")


def process_directory(directory, function_name):
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".py"):
                module_path = os.path.join(root, file)
                run_function(module_path, function_name)


# Replace "directory_path" with the path to your folder containing Python files
directory_path = "Easy"
# Replace "your_function_name" with the actual name of the function you want to execute
function_name = "solve"

process_directory(directory_path, function_name)