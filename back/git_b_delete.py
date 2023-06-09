import subprocess

def git_b_delete(branch_name):
    # git command execution
    try:
        subprocess.run(['git', 'branch', '-D', branch_name], check=True, capture_output=True, text=True)
        return True, 'Success'
    except subprocess.CalledProcessError as e:
        if e.stderr:
            error_message = e.stderr.strip()
            #print(error_message)
            return False, error_message
        else:
            return False, 'Error: failed to delete branch'

# git_b_delete('neww')