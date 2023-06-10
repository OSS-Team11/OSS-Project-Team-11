import subprocess
import os, json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
secret_file = os.path.join(BASE_DIR, 'secrets.json')  # secrets.json 파일 위치를 명시

def create_secrets_file(file_path):
    secrets = {
        'GIT_ID': '',
        'GIT_TOKEN': '',
        # 추가적인 시크릿 설정 등
    }

    with open(file_path, 'w') as f:
        json.dump(secrets, f, indent=4)

def initialize_secrets(id, token):

    create_secrets_file(secret_file)
    secrets = get_secrets()

    if not secrets['GIT_ID']:
        update_secret('GIT_ID', id)

    if not secrets['GIT_TOKEN']:
        update_secret('GIT_TOKEN', token)

def get_secrets():
    if not os.path.exists(secret_file):
        create_secrets_file(secret_file)

    with open(secret_file) as f:
        secrets = json.load(f)

    return secrets

def update_secret(setting, value):
    secrets = get_secrets()
    secrets[setting] = value

    with open(secret_file, 'w') as f:
        json.dump(secrets, f, indent=4)
    
def git_clone(is_private, clone_url, id, token):
    if is_private == False:
        try:
            result = subprocess.run(['git', 'clone', f'{clone_url}'], capture_output=True, text=True, check=True)
            return True, result.stdout.strip()
        except subprocess.CalledProcessError as e:
            if e.stderr:
                error_message = e.stderr.strip()
                return False, error_message
            else:
                return False, 'Error: failed to clone repository'
            
    else:
        if not os.path.exists(secret_file):
            initialize_secrets(id, token)

        id = get_secrets()['GIT_ID']
        token = get_secrets()['GIT_TOKEN']

        try:
            clone_url = clone_url[8:]
            print(clone_url)
            result = subprocess.run(['git', 'clone', f'https://{id}:{token}@{clone_url}'], capture_output=True, text=True, check=True)
            return True, result.stdout.strip()
        except subprocess.CalledProcessError as e:
            if e.stderr:
                error_message = e.stderr.strip()
                print(error_message)
                return False, error_message
            else:
                print('error')
                return False, 'Error: failed to clone repository'
            
#git_clone(False, 'https://github.com/OSS-Team11/OSS-Project-Team-11.git','','')
# git_clone(True, 'https://github.com/hayeongKo/private.git', '', '')

        
        