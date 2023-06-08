import subprocess

def git_b_create(branch_name):
    # git command execution
    try:
        subprocess.run(['git', 'branch', branch_name])
        return True, 'Success'
    except subprocess.CalledProcessError as e:
        if e.stderr:
            error_message = e.stderr.strip().decode('utf-8')
            return False, error_message
        else:
            return False, 'Error: failed to commit'

# branch creation function call
# git_b_create('neww')

