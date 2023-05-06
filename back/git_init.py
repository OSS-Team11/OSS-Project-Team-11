import os

def git_init():
    result = os.popen('git init').read()
    print(result)