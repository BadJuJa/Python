# importing the required modules
# importing all the widgets and modules from tkinter
from tkinter import *
# importing the messagebox module from tkinter
from tkinter import messagebox as mb
# importing the filedialog module from tkinter
from tkinter import filedialog as fd
import os                               # importing the os module
import shutil                           # importing the shutil module


# ----------------- defining functions -----------------
# function to open a file
def openFile():
    # selecting the file using the askopenfilename() method of filedialog
    the_file = fd.askopenfilename(
        title="Select a file of any type",
        filetypes=[("All files", "*.*"),
                   ("Image", ["*.jpg", "*.png"]), ("Esm", "*.esm")]
    )
    # opening a file using the startfile() method of the os module
    os.startfile(os.path.abspath(the_file))


openFile()
