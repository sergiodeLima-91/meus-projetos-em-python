from tkinter import Tk
from tkinter.filedialog import askopenfilename

class InitialsSelector:
    def __init__(self):
        self.root = Tk()
        self.root.withdraw()
        self.root.iconbitmap('./src/images/logo.ico')
    
    def select_initial(self):
        file_path = askopenfilename(filetypes=[("Image Files", "*.jpeg;*.jpg;*.png")])
        return file_path