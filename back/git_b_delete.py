import subprocess

def git_b_delete(branch_name):
    # Check if the branch exists
    output = subprocess.check_output(['git', 'branch', '-r', '--list', f'origin/{branch_name}']).decode('utf-8')
    if output.strip():
        # git command execution
        subprocess.run(['git', 'branch', '-D', branch_name])
        print(f"The branch '{branch_name}' has been deleted.")
    else:
        print(f"The branch '{branch_name}' does not exist.")

# Input: branch name to delete
branch_name = input("Enter the branch name to delete: ")

# branch delete function call
git_b_delete(branch_name)