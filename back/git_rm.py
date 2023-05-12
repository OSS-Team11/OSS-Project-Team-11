import subprocess
import os

def git_rm(file_path):
    if os.path.isdir(file_path):
        try:
            subprocess.run(["git", "rm", "-r", file_path], check=True)
            return True, 'Success'
        except subprocess.CalledProcessError as e:
            if e.returncode == 128:
                error_message = f"Error: {file_path} is not in the repository"
            elif e.returncode == 1:
                error_message = f"Error: {file_path} has local modifications. Use -f to force removal"
            else:
                error_message = "failed to remove file"
            return False, error_message
    else:
        try:
            subprocess.run(["git", "rm", file_path], check=True)
            return True, 'Success'
        except subprocess.CalledProcessError as e:
            if e.returncode == 128:
                error_message = f"Error: {file_path} is not in the repository"
            elif e.returncode == 1:
                error_message = f"Error: {file_path} has local modifications. Use -f to force removal"
            else:
                error_message = "Error: failed to remove file"
            return False, error_message
