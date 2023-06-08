import subprocess

def git_b_delete(branch_name):
    # git command execution
    try:
        subprocess.run(['git', 'branch', '-D', branch_name])
        return True, 'Success'
    except subprocess.CalledProcessError as e:
        if e.stderr:
            error_message = e.stderr.strip().decode('utf-8')
            print(error_message)
            return False, error_message
        else:
            return False, 'Error: failed to delete branch'
