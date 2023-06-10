import subprocess

def get_branches():
    # Run the git branch command to get a list of branches
    try:
        result = subprocess.run(['git', 'branch', '--format', '%(refname:short)'], check=True, capture_output=True, text=True)
        branch_lst = result.stdout.strip().split('\n')
        print(branch_lst)
        return True, branch_lst
    except subprocess.CalledProcessError as e:
        if e.stderr:
            error_message = e.stderr.strip().decode('utf-8')
            print(error_message)
            return False, error_message
        else:
            return False, 'Error: failed to get branch list'

def get_current_branch():
    try:
        result = subprocess.run(['git', 'rev-parse', '--abbrev-ref', 'HEAD'], capture_output=True, text=True, check=True)
        return True, result.stdout.strip()
    except subprocess.CalledProcessError as e:
        if e.stderr:
            error_message = e.stderr.strip()
            #print(error_message)
            return False, error_message
        else:
            return False, 'Error: failed to get current branch name'

def git_b_checkout(branch_name):
    # Run the git checkout command
    try:
        result = subprocess.run(['git', 'checkout', branch_name], check=True, capture_output=True, text=True)
        return True, 'Success'
    except subprocess.CalledProcessError as e:    
        if e.stderr:
            error_message = e.stderr.strip()
            print([error_message])
            return False, error_message
        else:
            return False, f'Error: failed to checkout {branch_name}'


#git_b_checkout('git_branch')
# get_branches()
# get_current_branch()
