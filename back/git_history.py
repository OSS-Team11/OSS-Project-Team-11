import subprocess

def git_history_list():
    try:
        result_lst = []
        command = ['git', 'log', '--graph', '--pretty=format:%C(auto)[%d][%s][%an][%h7]']
        result = subprocess.run(command, capture_output=True, text=True, check=True)

    except result.CalledProcessError as e:
        error = e.stderr.strip()
        return e.returncode, [error]
        
    output = result.stdout.strip()
    for line in output.split('\n'):
        result_lst.append(line)
    
    return 0, result_lst
    
    

def git_history_detail(checksum):
    try:
        result_lst = []
        command = ['git', 'show', '--stat', checksum]
        result = subprocess.run(command, capture_output=True, text=True, check=True)
        
    except result.CalledProcessError as e:
        error = e.stderr.strip()
        return e.returncode, [error]
        
    output = result.stdout.strip()
    for line in output.split('\n'):
        result_lst.append(line)
    
    return 0, result_lst
    
    