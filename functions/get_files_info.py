import os

def get_files_info(working_directory, directory="."):
    abs_working = os.path.abspath(working_directory)
    abs_target = os.path.abspath(os.path.join(working_directory, directory))
    if not abs_target.startswith(abs_working):
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
    elif not os.path.isdir(abs_target):
        return f'Error: "{directory}" is not a directory'
    else:
        contents = os.listdir(abs_target)
        lines = []
        for content in contents:
            item_path = os.path.join(abs_target, content)
            size = os.path.getsize(item_path)
            is_dir = os.path.isdir(item_path)
            lines.append(f'- {content}: file_size={size} bytes, is_dir={is_dir}')
        return "\n".join(lines)