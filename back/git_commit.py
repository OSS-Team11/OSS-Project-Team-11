import subprocess

def git_commit(message):
    try:
        subprocess.check_call(['git', 'commit', '-m', message])
        return True, 'Success'
    except subprocess.CalledProcessError as e:
        error_message = e.output.strip().decode('utf-8')
        if 'nothing to commit' in error_message:
            return False, 'Error: No changes to commit.'
        elif 'not a git repository' in error_message:
            return False, 'Error: Not a git repository.'
        elif 'Changes not staged for commit' in error_message:
            return False, 'Error: Changes not staged for commit.'
        elif 'Untracked files' in error_message:
            return False, 'Error: Untracked files.'
        else:
            return False, error_message