import os

def git_mv(old_name, new_name):
    result = os.popen('git mv {0} {1}'.format(old_name, new_name))
    print(result)