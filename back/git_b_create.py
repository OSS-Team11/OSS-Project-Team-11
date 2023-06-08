import subprocess

def create_branch(branch_name):

    # Change the default branch name from "master" to "main"
    subprocess.Popen(['git', 'symbolic-ref', 'refs/remotes/origin/HEAD', 'refs/remotes/origin/main'])

    # Create branch
    subprocess.run(["git", "branch", branch_name])


    # Print the branch list
    subprocess.run(["git", "branch", "-a"])

# Get the branch name from the user
branch_name = input("Enter the branch name: ")

# Create and configure the branch
create_branch(branch_name)