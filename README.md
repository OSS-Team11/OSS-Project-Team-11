# 📌 Git Version Control for MacOS

- This program is developed based in **MacOS**.
    - It also works in **Windows**, but the UI may break or cause unexpected errors.
- The goal of this program is to provide a **simple GUI-based git repository management service**.
    
    ![example.png](/readme_png/example.png)
    
    - **Feature #1: File explorer**
        
        > The service provides a GUI for browsing files and directories on your computer.
        > 
        - The file browsing starts from the root directory of the computer of the most recently visited directory.
        - All files and directories included in the current directory are displayed with their icon, name, and extension.
        - A user can browse a directory by double clicking its icon.
    - **Feature #2: Git repository creation**
        
        > The service supports to turn any local directory into a git repository
        > 
        - It provides a menu for a git repository creation only if a current directory in the browser is not managed by git yet.
        - Once the repository creation is requested, the service creates a new git repository for the current working directory.
    - **Feature #3: Version controlling**
        
        > The service supports the version controlling of a git repository
        > 
        - Files with different status have a different mark on their icon.
        - It provides a different menu depending on the status of a selected file.
        - This program can execute the following **git command**
            - `git init`
            - `git add`
            - `git commit`
            - `git mv`
            - `git rm`
            - `git rm —cached`
            - `git restore`
            - `git restore —staged`

# ⚙️ How to execute this program

- **`Python 3.9 or later` must be installed**
- Depending on the version install: `Tkinter`
- **Please run the program in `zsh`, not bash**

<aside>
📌 Follow the instructions belows if you want to execute this program

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

