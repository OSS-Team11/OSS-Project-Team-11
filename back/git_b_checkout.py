import subprocess

def get_branches():
    # Run the git branch command to get a list of branches
    result = subprocess.run(['git', 'branch', '--format', '%(refname:short)'], capture_output=True, text=True)
    
    if result.returncode == 0:
        # return branch list
        branches = result.stdout.strip().split('\n')
        return branches
    else:
        # Return None on error
        return None

def git_b_checkout(branch_name):
    # Run the git checkout command
    result = subprocess.run(['git', 'checkout', branch_name], capture_output=True, text=True)
    
    if result.returncode == 0:
        print(f"Branch '{branch_name}'Checked out.")
    else:
         # Handle different error scenarios
        error_message = result.stderr.strip()

        if "pathspec" in error_message:
            print(f"Error: Invalid branch name '{branch_name}'.")
        elif "did not match any file(s) known to git" in error_message:
            print(f"Error: The branch '{branch_name}' does not exist.")
        elif "You are in 'detached HEAD' state" in error_message:
            print("Error: If you manually select a commit instead of a branch with 'checkout', the branch will be in a detached HEAD state. It's better to create a new commit or move to an existing branch.")
        elif "Switched to a new branch" in error_message:
            print(f"Error: Failed to switch to the branch '{branch_name}'.")
        elif "error: Your local changes to the following files would be overwritten by checkout" in error_message:
            print("Error: You have local changes that would be overwritten by checkout. Please commit or stash your changes before switching branches.")
        elif "error: The following untracked working tree files would be overwritten by checkout" in error_message:
            print("Error: The following untracked working tree files would be overwritten by checkout. Please execute 'checkout' after committing or backing up the changed files.")
        else:
            print(f"Error occurred: {error_message}")
    return 0

# Get branch list
branches = get_branches()

if branches is not None:
    # Print a list of exposed branches
    print("Branch list :")
    for index, branch in enumerate(branches, start=1):
        print(f"{index}. {branch}")
    
    
    # Input: the selected branch number
   
    branch_info = (input("Enter the branch number to check out: "))
    try:
        branch_number=int(branch_info)
        if 1 <= branch_number <= len(branches):
        # Checkout to the selected branch
            selected_branch = branches[branch_number - 1]
            git_b_checkout(selected_branch)
        else:
            print("Please enter a valid branch number.")
        
       
    except:
        git_b_checkout(branch_info)


    
    
else:
    print("Failed to get branch list.")

