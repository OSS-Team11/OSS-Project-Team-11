import os

def git_add(file_name):
    os.system('git add {0}'.format(file_name))