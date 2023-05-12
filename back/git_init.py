# import os

# def git_init():
#     result = os.popen('git init').read()
#     print(result)

import subprocess

def git_init():
    try:
        subprocess.check_call(["git", "init"])
        return True
    except subprocess.CalledProcessError:
        return False