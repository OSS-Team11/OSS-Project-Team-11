import os
def cd_dir(dir):
    os.chdir('{0}'.format(dir))
    print(os.getcwd())