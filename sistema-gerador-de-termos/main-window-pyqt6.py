# Form implementation generated from reading ui file 'main-window.ui'
#
# Created by: PyQt6 UI code generator 6.7.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets
from adhesion import Ui_Adhesion_MainWindow
from declaration import Ui_Declaration_MainWindow
from cancel import Ui_Cancel_MainWindow


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(600, 600)
        MainWindow.setMaximumSize(QtCore.QSize(600, 600))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icon/src/images/logo.ico"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setMinimumSize(QtCore.QSize(0, 0))
        self.centralwidget.setMaximumSize(QtCore.QSize(600, 600))
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.scrollAreaMain = QtWidgets.QScrollArea(parent=self.centralwidget)
        self.scrollAreaMain.setMaximumSize(QtCore.QSize(600, 600))
        self.scrollAreaMain.setStyleSheet("background-color: rgb(85, 170, 255);\n"
"")
        self.scrollAreaMain.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.scrollAreaMain.setWidgetResizable(True)
        self.scrollAreaMain.setObjectName("scrollAreaMain")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 600, 600))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frameLogo = QtWidgets.QFrame(parent=self.scrollAreaWidgetContents)
        self.frameLogo.setStyleSheet("QFrame{        \n"
"    image: url(:/Logo/src/images/logo.png);\n"
"    background-repeat: no-repeat;\n"
"    \n"
"}\n"
"\n"
"\n"
"")
        self.frameLogo.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.frameLogo.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frameLogo.setObjectName("frameLogo")
        self.verticalLayout_2.addWidget(self.frameLogo)
        self.frameMenus = QtWidgets.QFrame(parent=self.scrollAreaWidgetContents)
        self.frameMenus.setStyleSheet("QFrame {\n"
"    border-color: rgb(0, 0, 0);\n"
"}")
        self.frameMenus.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frameMenus.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frameMenus.setObjectName("frameMenus")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frameMenus)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frameButtonAdesao = QtWidgets.QFrame(parent=self.frameMenus)
        self.frameButtonAdesao.setStyleSheet("QFrame {\n"
"    margin: auto;\n"
"}")
        self.frameButtonAdesao.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frameButtonAdesao.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frameButtonAdesao.setObjectName("frameButtonAdesao")
        self.pushButtonAdesao = QtWidgets.QPushButton(parent=self.frameButtonAdesao)
        self.pushButtonAdesao.setGeometry(QtCore.QRect(38, 131, 75, 23))
        self.pushButtonAdesao.setMaximumSize(QtCore.QSize(90, 16777215))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setBold(True)
        font.setWeight(75)
        self.pushButtonAdesao.setFont(font)
        self.pushButtonAdesao.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.ArrowCursor))
        self.pushButtonAdesao.setStyleSheet("background-color: rgb(150, 170, 255);\n"
"text-align: center;\n"
"\n"
"")
        self.pushButtonAdesao.setObjectName("pushButtonAdesao")
        self.horizontalLayout.addWidget(self.frameButtonAdesao)
        self.frameButtonDec = QtWidgets.QFrame(parent=self.frameMenus)
        self.frameButtonDec.setStyleSheet("QFrame {\n"
"    margin: auto;\n"
"}")
        self.frameButtonDec.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frameButtonDec.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frameButtonDec.setObjectName("frameButtonDec")
        self.pushButtonDec = QtWidgets.QPushButton(parent=self.frameButtonDec)
        self.pushButtonDec.setGeometry(QtCore.QRect(38, 131, 81, 23))
        self.pushButtonDec.setMaximumSize(QtCore.QSize(90, 16777215))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setBold(True)
        font.setWeight(75)
        self.pushButtonDec.setFont(font)
        self.pushButtonDec.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.ArrowCursor))
        self.pushButtonDec.setStyleSheet("background-color: rgb(150, 170, 255);\n"
"text-align: center;\n"
"\n"
"")
        self.pushButtonDec.setObjectName("pushButtonDec")
        self.horizontalLayout.addWidget(self.frameButtonDec)
        self.frameButtonCanc = QtWidgets.QFrame(parent=self.frameMenus)
        self.frameButtonCanc.setStyleSheet("QFrame {\n"
"    margin: auto;\n"
"}")
        self.frameButtonCanc.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frameButtonCanc.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frameButtonCanc.setObjectName("frameButtonCanc")
        self.pushButtonCanc = QtWidgets.QPushButton(parent=self.frameButtonCanc)
        self.pushButtonCanc.setGeometry(QtCore.QRect(38, 131, 100, 23))
        self.pushButtonCanc.setMinimumSize(QtCore.QSize(100, 0))
        self.pushButtonCanc.setMaximumSize(QtCore.QSize(90, 16777215))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setBold(True)
        font.setWeight(75)
        self.pushButtonCanc.setFont(font)
        self.pushButtonCanc.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.ArrowCursor))
        self.pushButtonCanc.setStyleSheet("background-color: rgb(150, 170, 255);\n"
"text-align: center;\n"
"")
        self.pushButtonCanc.setObjectName("pushButtonCanc")
        self.horizontalLayout.addWidget(self.frameButtonCanc)
        self.verticalLayout_2.addWidget(self.frameMenus)
        self.scrollAreaMain.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout.addWidget(self.scrollAreaMain)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # Connecting in to Buttons:
        self.pushButtonAdesao.clicked.connect(self.createAdhesionTerm)
        self.pushButtonDec.clicked.connect(self.createDeclarationTerm)
        self.pushButtonCanc.clicked.connect(self.createCancelTerm)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Sistema Gerador de Termos"))
        self.pushButtonAdesao.setText(_translate("MainWindow", "ADESÃO"))
        self.pushButtonDec.setText(_translate("MainWindow", "DECLARAÇÃO"))
        self.pushButtonCanc.setText(_translate("MainWindow", "CANCELAMENTO"))

        # Functions:
    def createAdhesionTerm(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_Adhesion_MainWindow()
        self.ui.setupUi(self.window)
        self.window.show()

    def createDeclarationTerm(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_Declaration_MainWindow()
        self.ui.setupUi(self.window)
        self.window.show()
    
    def createCancelTerm(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_Cancel_MainWindow()
        self.ui.setupUi(self.window)
        self.window.show()

import file_rc_mw_pyqt6

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
