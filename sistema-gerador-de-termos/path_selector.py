from tkinter import Tk
from tkinter.filedialog import asksaveasfilename

class PathSelector:
    def __init__(self):
        self.root = Tk()
        self.root.withdraw()
        self.root.iconbitmap('./src/images/logo.ico')

    def select_path(self):
        folder_path = asksaveasfilename(defaultextension=".pdf", filetypes=[("PDF files", "*.pdf")])
        return folder_path
