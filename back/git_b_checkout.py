import subprocess

def get_branches():
    # Run the git branch command to get a list of branches
    try:
        result = subprocess.run(['git', 'branch', '--format', '%(refname:short)'], capture_output=True, text=True)
        branch_lst = result.stdout.strip().split('\n')
        return True, branch_lst
    except subprocess.CalledProcessError as e:
        if e.stderr:
            error_message = e.stderr.strip().decode('utf-8')
            print(error_message)
            return False, error_message
        else:
            return False, 'Error: failed to get branch list'

def git_b_checkout(branch_name):
    # Run the git checkout command
    result = subprocess.run(['git', 'checkout', branch_name], capture_output=True, text=True)
    error_message = result.stderr.strip()
    
    if result.returncode == 0:
        if "You are in 'detached HEAD' state" in error_message:
            print("The detached HEAD site has been changed.")
        else:
            print(f"Branch '{branch_name}'Checked out.")
    else:
         # Handle different error scenarios

        if "pathspec" in error_message:
            print(f"Error: Invalid branch name '{branch_name}'.")
        elif "did not match any file(s) known to git" in error_message:
            print(f"Error: The branch '{branch_name}' does not exist.")
        elif "error: Your local changes to the following files would be overwritten by checkout" in error_message:
            print("Error: You have local changes that would be overwritten by checkout. Please commit or stash your changes before switching branches.")
        else:
            print(f"Error occurred: {error_message}")
    return 0

# Get branch list
#get_branches()

