import subprocess

def git_b_rename(old_name, new_name):
    # Check current branch name
    try:
        subprocess.run(['git', 'branch', '-m', old_name, new_name], capture_output=True, text=True, check=True)
        return True, 'Success'
    except subprocess.CalledProcessError as e:
        if e.stderr:
            error_message = e.stderr.strip()
            print(error_message)
            return False, error_message
        else:
            return False, 'Error: failed to rename current branch'


# Input: branch name to chage

# branch renaming function call
# git_b_rename('old', 'new')