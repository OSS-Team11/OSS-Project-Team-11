import subprocess
import re

def show_git_commit_graph_with_author_and_branch():
    result_lst = []
    command = ['git', 'log', '--graph', '--pretty=format:%C(auto)[%d][%s][%an]']
    result = subprocess.run(command, capture_output=True, text=True)
    output = result.stdout.strip()
    print(output)

    for line in output.split('\n'):

        result_lst.append(line)
    print(result_lst)
    return result_lst

show_git_commit_graph_with_author_and_branch()
