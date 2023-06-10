import subprocess

def git_merge(branch):
    try:
        result = subprocess.run(['git', 'merge', f'{branch}'], capture_output=True, check=True, text=True)
        return True, 'Success'
    except subprocess.CalledProcessError as e:
        if e.stdout:
            error_message = e.stdout.strip()
            if e.returncode == 1 and 'Automatic merge failed' in error_message:
                unmerged_paths = get_unmerged_paths()
                print(f"Merge conflict occurred. Unmerged paths: {', '.join(unmerged_paths)}")
                return False, f"Merge conflict occurred. Unmerged paths: {', '.join(unmerged_paths)}"
            else:
                print(error_message)
                return False, error_message
        else:
            return False, 'Error: failed to merge branch'
        

def get_unmerged_paths():
    result = subprocess.run(['git', 'status', '--porcelain'], capture_output=True, text=True)
    output = result.stdout.strip()
    unmerged_paths = []
    for line in output.split('\n'):
        if line.startswith('UU'):
            path = line[3:].strip()
            unmerged_paths.append(path)
    return unmerged_paths