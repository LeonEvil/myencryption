from tkinter import filedialog
from tkinter import *

files = [('Text Document', '*.txt')]
root = Tk()
root.focus_force()


def SelectFile():
    try:
        print("------ Select your file ------\n")
        root.filename = filedialog.askopenfilename(title="Select file", filetypes=files, defaultextension=files)
        root.withdraw()
        return root.filename
    except FileNotFoundError:
        print("\n------ File not found... ------")

        return ""
    except UnicodeDecodeError:
        print("\n------ Invalid file. Please select another file ------")
        return ""
    except TclError:
        return ""


def Read(path):
    try:
        file = open(path, 'r')
        return file.read()
    except UnicodeDecodeError:
        print("\n------ Invalid file. Please select another file ------")


def CreateFile():
    try:
        print("------ Save your file ------\n")
        root.filename = filedialog.asksaveasfile(title="Save file", filetypes=files, defaultextension=files)
        root.withdraw()
        return root.filename.name
    except TclError:
        return ""
    except AttributeError:
        return ""


def WriteFile(fileName, message):
    file = open(fileName, "w")
    file.write(message)
    file.close()
