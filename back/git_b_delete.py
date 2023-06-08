import subprocess

def git_b_delete(branch_name):
    # git command execution
    subprocess.run(['git', 'branch', '-D', branch_name])

# Input: branch name to delete 
branch_name = input("Enter the branch name to delete : ")

# branch delete function call
git_b_delete(branch_name)