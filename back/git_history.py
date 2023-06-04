import subprocess

def git_history_list():
    result_lst = []
    command = ['git', 'log', '--graph', '--pretty=format:%C(auto)[%d][%s][%an][%h7]']
    result = subprocess.run(command, capture_output=True, text=True)
    
    ##error
    if result.returncode == 128:
        error = result.stderr.strip()
        result_lst.append(error)
    else:
        output = result.stdout.strip()   
        for line in output.split('\n'):
            result_lst.append(line)

    print(result.returncode, result_lst)
    return result.returncode, result_lst

def git_history_detail(commit_sum):
    command = ['git', 'show', '--stat', commit_sum]
    result = subprocess.run(command, capture_output=True, text=True)
