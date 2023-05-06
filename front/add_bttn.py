from tkinter import *
import tkinter.ttk as ttk

def new_window():
	global new
	new = Toplevel()

def add_bttn():
    root = Tk()
    #git_frame = Frame(border=2, relief="groove", bg="white")
    #git_frame.pack(side="left")
    add_bttn = Button(root, text="add", font=("Arial", 12), relief="flat", bg="white", fg="black")
    restore_bttn = Button(root, text="restore", font=("Arial", 12), relief="flat", bg="white", fg="black")
    unstage_bttn = Button(root, text="unstage", font=("Arial", 12), relief="flat", bg="white", fg="black")
    commit_bttn = Button(root, text="commit", font=("Arial", 12), relief="flat", bg="white", fg="black", command=new_window)
    add_bttn.grid(column=0, row=0)
    restore_bttn.grid(column=1, row=0)
    unstage_bttn.grid(column=2, row=0)
    commit_bttn.grid(column=3, row=0)
    #add_bttn.pack()

    root.mainloop()

add_bttn();