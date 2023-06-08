import subprocess

def git_b_create(branch_name):
    # Change the default branch name from "master" to "main"
    subprocess.Popen(['git', 'symbolic-ref', 'refs/remotes/origin/HEAD', 'refs/remotes/origin/main'])


    # git command execution
    subprocess.Popen(['git', 'branch', branch_name])

# Input branch name
branch_name = input("Enter a new branch name: ")


# branch creation function call
git_b_create(branch_name)