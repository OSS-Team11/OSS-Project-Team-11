import subprocess
def git_mv(old_name, new_name):
    try:
        subprocess.check_call(["git", "mv", old_name, new_name])
        return True
    except subprocess.CalledProcessError:
        return False