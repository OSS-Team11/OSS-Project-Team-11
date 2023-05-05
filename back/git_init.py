import os

def git_init(trace):
    os.system('cd {0}'.format(trace))
    result = os.popen('git init').read()
    print(result)