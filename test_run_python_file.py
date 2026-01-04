from functions.run_python_file import run_python_file

print(f"Result for calculator and main.py:\n{run_python_file("calculator", "main.py")}")
print(f"Result for calculator and main.py with args:\n{run_python_file("calculator", "main.py", ["3 + 5"])}")
print(f"Result for calculator and tests.py:\n{run_python_file("calculator", "tests.py")}")
print(f"Result for calculator and main.py in separate directory:\n{run_python_file("calculator", "../main.py")}")
print(f"Result for calculator and nonexistant.py:\n{run_python_file("calculator", "nonexistent.py")}")
print(f"Result for calculator and lorem.txt:\n{run_python_file("calculator", "lorem.txt")}")
