import subprocess

# 0: untracked / 1: modified / 2: staged / 3: committed
def git_status():
    try:
        subprocess.check_output(["git", "status", "--porcelain"])
    except subprocess.CalledProcessError as e:
        if e.returncode == 128:
            return None

    result = subprocess.run(["git", "status", "--porcelain"], capture_output=True, text=True)
    output = result.stdout.strip().split("\n")
    files = {"0": [], "1": [], "2": [], "3": []}
    
    if output != ['']:
        for line in output:
            if list(line)[2] != ' ':
                line = ' ' + line
            status = line[:2]
            filename = line[3:]
            if status == "??":
                files["0"].append(filename)
            elif status == " M" or status == "MM" or status == "AM":
                files["1"].append(filename)
            elif status == "M " or status == "A ":
                files["2"].append(filename)
            elif status == "R ":
                files["2"].append(line.split(' -> ')[1])
    
    # Get list of files without changes since last commit
    result = subprocess.run(["git", "ls-files", "--full-name"], capture_output=True, text=True)
    all_files = set(result.stdout.strip().split("\n"))
    result = subprocess.run(["git", "diff", "--cached", "--name-only"], capture_output=True, text=True)
    staged_files = set(result.stdout.strip().split("\n"))
    committed_files = all_files - staged_files
    for filename in committed_files:
        if filename not in files["2"] and filename not in files["1"]:
            files["3"].append(filename)

    return files

