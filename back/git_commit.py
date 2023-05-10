import os

def git_commit(message):
    result = os.popen('git commit -m "{0}'.format(message))
    print(result)