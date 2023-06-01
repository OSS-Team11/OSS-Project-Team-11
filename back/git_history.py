import subprocess
import re

def show_git_commit_graph_with_author():
    result = subprocess.run(['git', 'log', '--graph', '--pretty=format:%h %p %an <%ae> %s'], capture_output=True, text=True)
    output = result.stdout.strip()

    # 커밋 그래프에서 커밋 정보 추출
    commit_lines = re.findall(r'(\s*\*?\s*[\w\d]+\s+[\w\s\d]+\s+[\w\s\d]+)\s+(.*)', output)
    commit_messages = {commit_line[0]: commit_line[1] for commit_line in commit_lines}

    # 그래프 출력
    for line in output.split('\n'):
        if line.strip() and not line.startswith(' '):
            print(line)
        elif line.strip():
            commit_line = line.lstrip()
            commit_hash = commit_line.split()[0]
            commit_info = commit_messages.get(commit_line, '')
            print(f"{commit_line}  {commit_info}")

show_git_commit_graph_with_author()




# import subprocess

# def get_git_commit_logs():
#     result = subprocess.run(['git', 'log'], capture_output=True, text=True)
#     output = result.stdout.strip()
#     print(output)

# get_git_commit_logs()
