import subprocess

def git_b_create(branch_name):
    # git command execution
    subprocess.Popen(['git', 'branch', branch_name])

# Input branch name
branch_name = input("Enter a new branch name: ")

# branch creation function call
git_b_create(branch_name)