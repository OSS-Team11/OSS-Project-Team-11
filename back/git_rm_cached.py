import os

def git_rm_cached(file_name):
    os.system('git rm --cached {0}'.format(file_name))