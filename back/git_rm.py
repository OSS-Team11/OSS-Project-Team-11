import os
import subprocess

def git_rm(path):
    if os.path.isfile(path):
        try:
            subprocess.check_call(['git', 'rm', path])
            return True, 'Success'
        except subprocess.CalledProcessError as e:
            return False, 'Error: '+ e.output.strip().decode('utf-8')
    elif os.path.isdir(path):
        try:
            subprocess.check_call(['git', 'rm', '-r', path])
            return True, None
        except subprocess.CalledProcessError as e:
            return False, 'Error: '+e.output.strip().decode('utf-8')
    else:
        return False, 'Error: Path does not exist.'
