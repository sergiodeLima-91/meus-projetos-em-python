from tkinter import Tk
from tkinter.filedialog import askopenfilename

class SelectorPDF:
    def __init__(self):
        self.root = Tk()
        self.root.withdraw()
    
    def select_pdf_file(self):
        file_path = askopenfilename(filetypes=[("PDF Files", "*.pdf")])
        return file_path
