import os

def git_restore_staged(file_name):
    os.system('git restore --staged {0}'.format(file_name))