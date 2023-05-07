import os
def cd_dir(dir):
    os.chdir('cd {0}'.format(dir))
    print(os.getcwd())