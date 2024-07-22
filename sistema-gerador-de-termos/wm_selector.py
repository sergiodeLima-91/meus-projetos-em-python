from tkinter import Tk
from tkinter.filedialog import askopenfilename

class WmSelector:
    def __init__(self):
        self.root = Tk()
        self.root.withdraw()
        self.root.iconbitmap('./src/images/logo.ico')
    
    def select_pdf_file(self):
        file_path = askopenfilename(filetypes=[("Image Files", "*.jpeg;*.jpg;*.png")])
        return file_path

wm_selector = WmSelector()
wm_selector.select_pdf_file()