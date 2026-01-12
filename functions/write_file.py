import os
from google.genai import types

schema_write_file = types.FunctionDeclaration(
    name="write_file",
    description="Write or overwrite files",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        required=["file_path", "content"],
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="Path to the file to write",
            ),
            "content": types.Schema(
                type=types.Type.STRING,
                description="Content to be written to the file",
            )
        },
    ),
)


def write_file(working_directory, file_path, content):
    try:   
        abs_working = os.path.abspath(working_directory)
        abs_target = os.path.normpath(os.path.join(abs_working, file_path))

        if os.path.commonpath([abs_working, abs_target]) != abs_working:
            return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
        
        if os.path.isdir(abs_target):
            return f'Error: Cannot write to "{file_path}" as it is a directory'
        
        dir_name = os.path.dirname(abs_target)
        os.makedirs(dir_name, exist_ok=True)

        with open(abs_target, "w") as f:
            f.write(content)
        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
    except Exception as e:
        return f'Error: writing to file - {e}'