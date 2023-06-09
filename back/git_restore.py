import subprocess

def git_restore(file_path):
    try:
        # 파일의 변경 내용을 이전 커밋 버전으로 복원합니다.
        subprocess.run(['git', 'restore', file_path], check=True)
        return True, 'Success'
    except subprocess.CalledProcessError as e:
        # 파일이 Git 저장소에 커밋되어 있지 않은 경우
        if e.returncode == 128:
            error_message = f"Error: {file_path} is not a tracked file in the repository"
        # 파일이 삭제된 경우
        elif e.returncode == 1 and e.stderr and "did not match any files" in e.stderr.decode():
            error_message = f"Error: {file_path} has been deleted"
        # 변경 내용을 되돌릴 수 없는 경우
        elif e.stderr and "could not restore untracked files from stash" in e.stderr.decode():
            error_message = f"Error: Could not restore {file_path} from stash"
        # 그 외의 경우
        else:
            error_message = "Error: Failed to restore file"
        return False, error_message
