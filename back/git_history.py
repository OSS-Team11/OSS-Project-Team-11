import subprocess

def git_history_list():
    try:
        result_lst = []
        command = ['git', 'log', '--graph', '--pretty=format:{%d}{%s}{%an}{%h}']
        result = subprocess.run(command, capture_output=True, text=True, check=True)

        if result.stdout is not None:
            output = result.stdout.strip()
            for line in output.split('\n'):
                history_detail = []
                history = line.replace('{', '^').replace('}', '^').split('^')
                cnt = 0
                for word in history:
                    cnt += 1
                    if cnt == 2 and word == '':
                        history_detail.append(word)
                    if word != '':
                        history_detail.append(word)
                print(history_detail)
                result_lst.append(history_detail)
        # print(result_lst)
        return 0, result_lst

    except subprocess.CalledProcessError as e:
        error = e.stderr.strip()
        print(e.returncode, [error])
        return e.returncode, [error]


def git_history_detail(checksum):
    try:
        result_lst = []
        command = ['git', 'show', '--stat', f'{checksum}']
        result = subprocess.run(command, capture_output=True, text=True, check=True)

        if result.stdout is not None:
            output = result.stdout.strip()
            for line in output.split('\n'):
                result_lst.append(line)

        print(result_lst)
        return 0, result_lst

    except subprocess.CalledProcessError as e:
        error = e.stderr.strip()
        print(e.returncode, [error])
        return e.returncode, [error]


git_history_list()    
# git_history_detail('e9a04c57')