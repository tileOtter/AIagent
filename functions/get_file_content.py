import os
from config import MAX_CHARS

def get_file_content(working_directory, file_path):
    try:   
        abs_working = os.path.abspath(working_directory)
        abs_target = os.path.abspath(os.path.join(working_directory, file_path))
        if not abs_target.startswith(abs_working):
            return f'Error: Cannot list "{file_path}" as it is outside the permitted working directory'
        elif os.path.isdir(abs_target):
            return f'Error: "{file_path}" is not a file'
        else:
            with open(abs_target, "r") as f:
                file_content_string = f.read(MAX_CHARS)
                if f.read(1) != None:
                    file_content_string += f'[...File "{file_path}" truncated at {MAX_CHARS} characters]'
                return file_content_string
    except Exception as e:
        return f'Error: {e}'