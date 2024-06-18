from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QFileDialog

class Adhesion_MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Campo de Arquivos")
        self.setGeometry(100, 100, 400, 200)

        button = QPushButton("Selecionar Arquivo", self)
        button.clicked.connect(self.show_file_dialog)

    def show_file_dialog(self):
        file_name, _ = QFileDialog.getOpenFileName(self, "Selecionar Arquivo", "", "PDF Files (*.pdf);;All Files (*)")
        if file_name:
            print(f"Arquivo selecionado: {file_name}")

if __name__ == "__main__":
    app = QApplication([])
    window = Adhesion_MainWindow()
    window.show()
    app.exec()
