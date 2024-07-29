from tkinter import Tk
from tkinter.filedialog import askdirectory

class PathSelector:
    def __init__(self):
        self.root = Tk()
        self.root.withdraw()
        self.root.iconbitmap('./src/images/logo.ico')

    def select_path(self):
        folder_path = askdirectory(title='Selecionar diretório')
        return folder_path
