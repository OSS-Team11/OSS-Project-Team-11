import subprocess

def git_mv(old_path, new_path):
    try:
        subprocess.run(['git', 'mv', old_path, new_path], check=True)
        return True, 'Success'
    except subprocess.CalledProcessError as e:
        if e.returncode == 128:
            error_message = f"Error: {old_path} or {new_path} is not a valid file path"
        elif e.returncode == 1:
            error_message = f"Error: {old_path} or {new_path} is not found or has local modifications"
        else:
            error_message = f"Error: Failed to move {old_path} to {new_path}"
        return False, error_message
