# readme 최종본

완료: No

# 📌 Git Version Control

---

- This program is developed based in **MacOS**.
    - It also works in **Windows**, but the UI may break or cause unexpected errors.
- The goal of this program is to provide a **simple GUI-based git repository management service**.
    
    ![스크린샷 2023-05-14 오전 2.05.49.png](readme%20%E1%84%8E%E1%85%AC%E1%84%8C%E1%85%A9%E1%86%BC%E1%84%87%E1%85%A9%E1%86%AB%2025873be4872e4ae7b4385183c5e5a965/%25E1%2584%2589%25E1%2585%25B3%25E1%2584%258F%25E1%2585%25B3%25E1%2584%2585%25E1%2585%25B5%25E1%2586%25AB%25E1%2584%2589%25E1%2585%25A3%25E1%2586%25BA_2023-05-14_%25E1%2584%258B%25E1%2585%25A9%25E1%2584%258C%25E1%2585%25A5%25E1%2586%25AB_2.05.49.png)
    
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

---

- `**Python 3.9 or later` must be installed**
- Depending on the version install: `Tkinter`

<aside>
📌 Follow the instructions belows if you want to execute this program

1. download or clone this repo and go to this project folder
2. run via command line `pip3 install -r requirements.txt`
3. `python3 app.py`
</aside>

# 📍Features

---

## 🚥 Git status

- *untracked*
    
    
    - directory
        
        ![untracked_folder.png](readme%20%E1%84%8E%E1%85%AC%E1%84%8C%E1%85%A9%E1%86%BC%E1%84%87%E1%85%A9%E1%86%AB%2025873be4872e4ae7b4385183c5e5a965/untracked_folder.png)
        
    
    - file
        
        ![untracked_file.png](readme%20%E1%84%8E%E1%85%AC%E1%84%8C%E1%85%A9%E1%86%BC%E1%84%87%E1%85%A9%E1%86%AB%2025873be4872e4ae7b4385183c5e5a965/untracked_file.png)
        

- *modified*
    
    
    - directory
        
        ![modified_folder.png](readme%20%E1%84%8E%E1%85%AC%E1%84%8C%E1%85%A9%E1%86%BC%E1%84%87%E1%85%A9%E1%86%AB%2025873be4872e4ae7b4385183c5e5a965/modified_folder.png)
        
    
    - file
        
        ![modified_file.png](readme%20%E1%84%8E%E1%85%AC%E1%84%8C%E1%85%A9%E1%86%BC%E1%84%87%E1%85%A9%E1%86%AB%2025873be4872e4ae7b4385183c5e5a965/modified_file.png)
        

- *staged*
    
    
    - directory
        
        ![staged_folder.png](readme%20%E1%84%8E%E1%85%AC%E1%84%8C%E1%85%A9%E1%86%BC%E1%84%87%E1%85%A9%E1%86%AB%2025873be4872e4ae7b4385183c5e5a965/staged_folder.png)
        
    
    - file
        
        ![staged_file.png](readme%20%E1%84%8E%E1%85%AC%E1%84%8C%E1%85%A9%E1%86%BC%E1%84%87%E1%85%A9%E1%86%AB%2025873be4872e4ae7b4385183c5e5a965/staged_file.png)
        

- *committed*
    
    
    - directory
        
        ![commited_folder.png](readme%20%E1%84%8E%E1%85%AC%E1%84%8C%E1%85%A9%E1%86%BC%E1%84%87%E1%85%A9%E1%86%AB%2025873be4872e4ae7b4385183c5e5a965/commited_folder.png)
        
    
    - file
        
        ![commited_file.png](readme%20%E1%84%8E%E1%85%AC%E1%84%8C%E1%85%A9%E1%86%BC%E1%84%87%E1%85%A9%E1%86%AB%2025873be4872e4ae7b4385183c5e5a965/commited_file.png)
        
    

**→ How does one file/directory represent if it has multiple statuses (e.g. staged & untracked, staged & modified, etc.)?**

**It is expressed by setting priorities in the order of untracked > modified > staged > committed.**