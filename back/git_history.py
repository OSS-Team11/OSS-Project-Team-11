import subprocess

def git_history_list():
    try:
        result_lst = []
        command = ['git', 'log', '--graph', '--pretty=format:{%d{%s      %an{%h']
        result = subprocess.run(command, capture_output=True, text=True, check=True)

        if result.stdout is not None:
            output = result.stdout.strip()
            for line in output.split('\n'):
                history_detail = []
                history = line.replace('{', '^').replace('}', '^').split('^')
                # print(history)
                buffer = ''
                for i in range(len(history)):
                    if i == 0 or i == 3:
                        history_detail.append(history[i])
                    elif i == 1:
                        if history[1] != '':
                            buffer += history[1]
                            buffer += '      '
                    elif i == 2:
                        buffer += history[2]
                        history_detail.append(history[i])  
                        # print(buffer)
                result_lst.append(history_detail)  

        # print(result_lst)
        return 0, result_lst

    except subprocess.CalledProcessError as e:
        error = e.stderr.strip()
        return e.returncode, [error]


def git_history_detail(checksum):
    try:
        result_lst = []
        command = ['git', 'show', '--stat', f'{checksum}']
        result = subprocess.run(command, capture_output=True, text=True, check=True)

        if result.stdout is not None:
            output = result.stdout.strip()
            for line in output.split('\n'):
                if "commit" in line:
                    result_lst.append(line[7:])
                elif "Author" in line:
                    result_lst.append(line[8:])
                elif "Date" in line:
                    result_lst.append(line[8:])
                elif line == '' or ("file changed" in line and ("insertions" in line or "deletions" in line)):
                    pass
                else:
                    if "+" in line or "-" in line:
                        result_lst.append(line[1:])
                    else:
                        result_lst.append(line[4:])
        print(result_lst)
        return 0, result_lst

    except subprocess.CalledProcessError as e:
        error = e.stderr.strip()
        return e.returncode, [error]


#git_history_list()    
#git_history_detail('62d881117692eaa1c9f10003eb3aec7497e0f8c5')