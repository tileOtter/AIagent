import os

def write_file(working_directory, file_path, content):
        try:   
            abs_working = os.path.abspath(working_directory)
            abs_target = os.path.abspath(os.path.join(working_directory, file_path))
            if not abs_target.startswith(abs_working):
                return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
            elif os.path.isdir(abs_target):
                return f'Error: Cannot write to "{file_path}" as it is a directory'
                make_dirs = os.makedirs(abs_target, exist_ok=True)
            else:
                 
                 with open(abs_target, "w") as f:
                      f.write(content)
                      return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
        except Exception as e:
            return f'Error: {e}'