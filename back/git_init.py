import subprocess

def git_init():
    try:
        result = subprocess.run(['git', 'init'], capture_output=True, check=True)
        return True, result.stdout.decode()
    except subprocess.CalledProcessError as e:
        return False, 'Error: '+e.stderr.decode()