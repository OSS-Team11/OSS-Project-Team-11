# import os
# import subprocess

# def git_rm(path):
#     if os.path.isfile(path):
#         try:
#             subprocess.check_call(['git', 'rm', path])
#             return True, 'Success'
#         except subprocess.CalledProcessError as e:
#             return False, 'Error: '+ e.output.strip().decode('utf-8')
#     elif os.path.isdir(path):
#         try:
#             subprocess.check_call(['git', 'rm', '-r', path])
#             return True, None
#         except subprocess.CalledProcessError as e:
#             return False, 'Error: '+e.output.strip().decode('utf-8')
#     else:
#         return False, 'Error: Path does not exist.'

import subprocess
import os

def git_rm(file_path):
    print(file_path)
    if os.path.isdir(file_path):
        flag = "-r"
    else:
        flag = ""
    try:
        subprocess.run(["git", "rm", flag, file_path], check=True)
        return (True, None)
    except subprocess.CalledProcessError as e:
        if e.returncode == 128:
            error_message = f"{file_path} is not in the repository"
        elif e.returncode == 1:
            error_message = f"{file_path} has local modifications. Use -f to force removal"
        else:
            error_message = "failed to remove file"
        return (False, 'Error: ' + error_message)
