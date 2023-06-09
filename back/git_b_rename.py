import subprocess

def git_b_rename(old_name, new_name):
    # Check current branch name
    current_branch = subprocess.check_output(['git', 'rev-parse', '--abbrev-ref', 'HEAD']).decode().strip()

    if old_name == current_branch:
        # If this is the branch you are currently working on.
        # Move HEAD with the command that creates a new branch and checks out to that branch, 
        # and deletes the branch you are working on.
        subprocess.run(['git', 'checkout', '-b', new_name])
        subprocess.run(['git', 'branch', '-D', old_name])
    else:
        # Renaming a branch directly without deleting the existing branch, 
        # if it is not the branch you are currently working on
        subprocess.run(['git', 'branch', '-m', old_name, new_name])

# Input: branch name to chage
old_name = input("Enter the branch name to change : ")
new_name = input("Enter a new branch name : ")

# branch renaming function call
#git_b_rename(old_name, new_name)