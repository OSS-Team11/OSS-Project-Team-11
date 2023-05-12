import subprocess

def git_restore_staged(file_path):
    try:
        # 파일의 staged 상태를 이전 커밋 버전으로 복원합니다.
        subprocess.run(['git', 'restore', '--staged', file_path], check=True)
        return True, 'Success'
    except subprocess.CalledProcessError as e:
        # 파일이 Git 저장소에 커밋되어 있지 않은 경우
        if e.returncode == 128:
            error_message = f"{file_path} is not a tracked file in the repository"
        # 파일이 삭제된 경우
        elif e.returncode == 1 and "did not match any files" in e.output.decode():
            error_message = f"{file_path} has been deleted"
        # staged 상태를 되돌릴 수 없는 경우
        elif "unable to unlink" in e.output.decode():
            error_message = f"Could not restore staged {file_path}"
        # 그 외의 경우
        else:
            error_message = "Failed to restore staged file"
        return False, error_message