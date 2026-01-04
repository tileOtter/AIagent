import os
import subprocess

def run_python_file(working_directory, file_path, args=None):
    try:   
        abs_working = os.path.abspath(working_directory)
        abs_target = os.path.normpath(os.path.join(abs_working, file_path))

        if os.path.commonpath([abs_working, abs_target]) != abs_working:
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
        
        if not os.path.isfile(abs_target):
            return f'Error: "{file_path}" does not exist or is not a regular file'
        
        if not os.path.basename(abs_target)[-3:] == ".py":
            return f'Error: "{file_path}" is not a Python file'
        
        command = ["python", abs_target]
        if args:        
            command.extend(args)
        
        completed_command = subprocess.run(command, capture_output=True, text=True, timeout=30, cwd=abs_working)
        output = []

        if completed_command.returncode != 0:
            output.append(f'Process exited with code {completed_command.returncode}')
        if not completed_command.stdout and not completed_command.stderr:
            output.append("No output produced")
        if completed_command.stdout:
            output.append(f'STDOUT: {completed_command.stdout}')
        if completed_command.stderr:
            output.append(f'STDERR: {completed_command.stderr}')

        return "\n".join(output)
    except Exception as e:
        return f"Error: executing Python file: {e}"
        
