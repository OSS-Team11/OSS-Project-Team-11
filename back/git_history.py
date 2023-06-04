import subprocess
import re

def git_history_list():
    result_lst = []
    command = ['git', 'log', '--graph', '--pretty=format:%C(auto)[%d][%s][%an]']
    result = subprocess.run(command, capture_output=True, text=True)
    output = result.stdout.strip()
    #print(output)

    for line in output.split('\n'):

        result_lst.append(line)
    print(result_lst)
    return result_lst


