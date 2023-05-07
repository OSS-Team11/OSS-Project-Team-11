import os
# os.walk()  >> files or directory list acquire
for curDir, dirs, files in os.walk("test"):
    for f in files:
        print(os.path.join(curDir,f))
# os.listdir() >> file or directory list check  
path='./dir' #경로 설정
flist=os.listdir(path) #flist에 os.listdir(경로) 위 경로에 있는 파일이나 디렉토리를 받음
print(flist)      
# os.path() >> file or directory existence check

# os.environ() >> 환경변수를 취득하거나, 읽어들이거나 쓰기 위해 사용한다.
os.environ["PHASE"]='staging'
print("env() " +os.environ["PHASE"])

# os.mkdir() >> 간단히 directory 작성 dir below subdir case

path='./dir/sub'
os.mkdir(path)

# os.rename() >> 지정한 파일명을 변경할 때 사용 변경 전/후 파일명 지정

path1='./dir/sample_00.txt'
path2='./dir/sample_01.txt'

os.rename(path1,path2)
print(os.path.exists(path2))

os.remove() >> 

def git_rm(file_name):
    os.system('git rr {0}'.format(file_name))