import os

def git_restore(file_name):
    os.system('git restore {0}'.format(file_name))