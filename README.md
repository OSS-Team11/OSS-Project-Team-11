# Python file explorer

<<<<<<< Updated upstream
Tkinter version (files_new.py) works on Windows, Linux (should work on MacOS).
For Windows 10, available in "Releases" (download "files.zip", unpack and run files.exe)
=======

>>>>>>> Stashed changes

<img title="Screenshot from Windows 10" src="https://github.com/lestec-al/files/raw/main/data/pic_new_win.png" width="541" height="366"/>
<img title="Screenshot from Linux Ubuntu" src="https://github.com/lestec-al/files/raw/main/data/pic_new_linux.png" width="541" height="366"/>


<<<<<<< Updated upstream
=======

>>>>>>> Stashed changes

# Install and run as Python script
- install: Python (v3.9 or higher)
- depending on the version install: Tkinter or Kivy (+KivyMD) or PySimpleGUI
- install Send2Trash (needed for Tkinter, PySimpleGUI versions)
- download or clone this repo and in the project folder run via command line "python files_new.py" 


<<<<<<< Updated upstream
# Features
- connect to ftp servers (e.g. ftp://ftp.us.debian.org) and download files from there (tkinter, command line)
- copy/paste to/from another file manager (windows, tkinter, command line)
- catalog, files creation (tkinter, kivy, command line)
- open files by default program (tkinter, command line)
- local disks buttons (tkinter)
- keyboard navigation, copy/paste support (arrows, enter, backspace, ctrl-c/ctrl-v, tkinter)
- select multiple files/catalogs by holding Ctrl and clicking with the mouse (tkinter)
- copy, paste, rename, delete to trash (in command line ver: remove to trash, delete permanently)
- sorts by name and size
- shows hidden files
- resizability
- the command line version has navigation by typing short commands
=======
1. download or clone this repo and go to this project folder
2. run via command line `pip3 install -r requirements.txt`
3. `python3 app.py`
</aside>

# 📍Features



## 🚥 Git status

- *untracked*
    
    
    - directory
        
        ![untracked_folder.png](/readme_png/untracked_folder.png)
        
    
    - file
        
        ![untracked_file.png](/readme_png/untracked_file.png)
        

- *modified*
    
    
    - directory
        
        ![modified_folder.png](/readme_png/modified_folder.png)
        
    
    - file
        
        ![modified_file.png](/readme_png/modified_file.png)
        

- *staged*
    
    
    - directory
        
        ![staged_folder.png](/readme_png/staged_folder.png)
        
    
    - file
        
        ![staged_file.png](/readme_png/staged_file.png)
        

- *committed*
    
    
    - directory
        
        ![commited_folder.png](readme_png/commited_folder.png)
        
    
    - file
        
        ![commited_file.png](/readme_png/commited_file.png)
        
    

**→ How does one file/directory represent if it has multiple statuses (e.g. staged & untracked, staged & modified, etc.)?**

**It is expressed by setting priorities in the order of untracked > modified > staged > committed.**
>>>>>>> Stashed changes
