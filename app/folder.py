from tkinter import filedialog
from tkinter import *
import os

def openFile():
    root = Tk()
    root.filename =  filedialog.askopenfilename(initialdir = os.getcwd(), title = "Select file", filetypes = (("jpeg files","*.jpg"),("all files","*.*")))
    print (root.filename)