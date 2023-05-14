import os
import subprocess

def git_rm_cached(file_path):
    if os.path.isfile(file_path):
        try:
            subprocess.check_call(['git', 'rm', '--cached', file_path])
            return True, 'Success'
        except subprocess.CalledProcessError as e:
            if e.returncode == 128:
                error_message = f"Error: {file_path} is not in the repository"
            elif e.returncode == 1 and e.stderr and "No such file or directory" in e.stderr:
                error_message = f"Error: {file_path} has been deleted"
            else:
                error_message = "Error: Failed to remove file from Git repository"
        return False, error_message
    elif os.path.isdir(file_path):
        try:
            subprocess.check_call(['git', 'rm', '-r', '--cached', file_path])
            return True, 'Success'
        except subprocess.CalledProcessError as e:
            if e.returncode == 128:
                error_message = f"Error: {file_path} is not in the repository"
            elif e.returncode == 1 and e.stderr and "No such file or directory" in e.stderr:
                error_message = f"Error: {file_path} has been deleted"
            else:
                error_message = "Error: Failed to remove file from Git repository"
    else:
        return False, 'Error: Path does not exist.'
