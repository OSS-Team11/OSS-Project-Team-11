import os
import subprocess

def git_rm_cached(path):
    if os.path.isfile(path):
        try:
            subprocess.check_call(['git', 'rm', '--cached', path])
            return True, 'Success'
        except subprocess.CalledProcessError as e:
            if e.returncode == 128:
                error_message = f"Error: {path} is not in the repository"
            elif e.returncode == 1 and e.stderr and "No such file or directory" in e.stderr:
                error_message = f"Error: {path} has been deleted"
            else:
                error_message = "Error: Failed to remove file from Git repository"
        return False, error_message
    elif os.path.isdir(path):
        try:
            subprocess.check_call(['git', 'rm', '-r', '--cached', path])
            return True, 'Success'
        except subprocess.CalledProcessError as e:
            if e.returncode == 128:
                error_message = f"Error: {path} is not in the repository"
            elif e.returncode == 1 and e.stderr and "No such file or directory" in e.stderr:
                error_message = f"Error: {path} has been deleted"
            else:
                error_message = "Error: Failed to remove file from Git repository"
    else:
        return False, 'Error: Path does not exist.'
