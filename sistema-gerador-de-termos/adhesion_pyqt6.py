from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QFileDialog, QScrollArea
from PyQt6 import QtCore, QtGui, QtWidgets

class Ui_Adhesion_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(400, 400)
        MainWindow.setMaximumSize(QtCore.QSize(400, 400))
        MainWindow.setWindowTitle("Termo de Adesão")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("./src/images/logo.ico"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        MainWindow.setWindowIcon(icon)

    def show_file_dialog(self):
        file_name, _ = QFileDialog.getOpenFileName(self, "Selecionar Arquivo", "", "PDF Files (*.pdf);;All Files (*)")
        if file_name:
            print(f"Arquivo selecionado: {file_name}")

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_Adhesion_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
