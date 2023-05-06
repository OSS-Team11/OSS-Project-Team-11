import os

def cd_home():
    os.system('cd ~')

def cd_move_up():
    os.system('cd ..')

def cd_dir(dir):
    os.system('cd {0}'.format(dir))