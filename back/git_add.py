import tkinter as tk
from tkinter import messagebox
import subprocess

def git_add(file_path):
    try:
        # subprocess를 이용해 git 명령어 실행
        output = subprocess.check_output(['git', 'add', file_path])
        return True, 'Success'
    except subprocess.CalledProcessError as error:
        error_output = error.output.decode().strip()
        # 파일/디렉토리가 존재하지 않음
        if "did not match any files" in error_output:
            return False, 'Error: File or directory does not exist'
        # 권한 부족
        elif "Permission denied" in error_output:
            return False, 'Error: Permission denied'
        # 이미 add된 파일 재 추가 시도
        elif "already in index" in error_output:
            return False, 'Error: File is already in index'
        # add 실행 도중 파일 삭제
        elif "did not match any files" in error_output:
            return False, 'Error: File was deleted during add'
        # .gitignore 파일에 해당 파일/디렉토리 포함됨
        elif "ignored by one of your .gitignore files" in error_output:
            return False, 'Error: File is ignored by .gitignore'
        # 경로가 잘못 입력됨
        elif "Not a git repository" in error_output:
            return False, 'Error: Not a git repository'
        # 기타 다른 에러
        else:
            return False, 'Error: Unknown error'

