import subprocess
import re

def get_branches_containing_commit(commit_hash):
    result = subprocess.run(['git', 'branch', '-a', '--contains', commit_hash], capture_output=True, text=True)
    output = result.stdout.strip()

    branches = []
    # for line in output.split('\n'):
    #     branch_name = line.strip()
    #     if branch_name.startswith('*'):
    #         branch_name = branch_name[1:].strip()
    #     if branch_name:
    #         branches.append(branch_name)

    for line in output.split('\n'):
        branch_name = line.strip()
        if branch_name.startswith('*'):
            branch_name = branch_name[1:].strip()
        if branch_name and not branch_name.startswith('remotes/origin/') and not branch_name.startswith('remotes/'):
            branches.append(branch_name)

    return branches

def show_git_commit_graph_with_author_and_branch():
    result_lst = []
    result = subprocess.run(['git', 'log', '--graph', '--pretty=format:%H %p %an <%ae> %s'], capture_output=True, text=True)
    output = result.stdout.strip()

    commit_lines = re.findall(r'(\s*\*?\s*[\w\d]+\s+[\w\s\d]+\s+[\w\s\d]+)\s+(.*)', output)
    commit_messages = {commit_line[0]: commit_line[1] for commit_line in commit_lines}

    for line in output.split('\n'):
        if line.strip():
            commit_line = line.lstrip()
            commit_hash = commit_line.replace('|', ' ').replace('*', ' ').replace('\\', ' ').replace('/', ' ').split()
            commit_info = commit_messages.get(commit_line, '')
            # print('commit_hash',commit_hash, end='\n')
            if commit_hash != []:
                branch_names = get_branches_containing_commit(commit_hash[0])
                if not branch_names:
                    branch_names = ['No Branch']

            result_lst.append(f"{commit_line}  {commit_info}  ({', '.join(branch_names)})")
    print(result_lst)
    return result_lst

# show_git_commit_graph_with_author_and_branch()
