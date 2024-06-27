from PyQt6 import QtCore, QtGui, QtWidgets
from select_file import SelectorPDF

class Ui_Adhesion_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(990, 528)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(".\\src/images/logo.ico"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("QScrollBar:vertical{\n"
"    border: none;\n"
"    background-color: rgb(170, 255, 255);\n"
"    width:14px;\n"
"    margin: 15px 0 15px 0;\n"
"    border-radius: 0px;\n"
"}\n"
"QScrollBar::handle:vertical{\n"
"    background-color: rgb(50, 200, 255);\n"
"    mini-height: 30px;\n"
"    border-radius: 7px;\n"
"}\n"
"QScrollBar::handle:vertical:hover{\n"
"    background-color: rgb(70, 220, 255);\n"
"}\n"
"QScrollBar::handle:vertical:pressed{\n"
"    background-color: rgb(30, 180, 255);\n"
"}\n"
"QScrollBar::sub-line:vertical{\n"
"    border: none;\n"
"    background-color: rgb(50, 200, 255);\n"
"    height: 15px;\n"
"    border-top-left-radius: 7px;\n"
"    border-top-right-radius: 7px; \n"
"    subcontrol-posiiton: top;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:vertical:hover{\n"
"    background-color: rgb(70, 220, 255);\n"
"}\n"
"QScrollBar::sub-line:vertical:pressed{\n"
"    background-color: rgb(30, 180, 255);\n"
"}\n"
"QScrollBar::add-line:vertical{\n"
"    border: none;\n"
"    background-color: rgb(50, 200, 255);\n"
"    height: 15px;\n"
"    border-bottom-left-radius: 7px;\n"
"    border-botton-right-radius: 7px;\n"
"    subcontrol-posiiton: botton;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::add-line:vertical:hover{\n"
"    background-color: rgb(70, 220, 255);\n"
"}\n"
"QScrollBar::add-line:vertical:pressed{\n"
"    background-color: rgb(30, 180, 255);\n"
"}\n"
"\n"
"QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical{\n"
"    background: none;\n"
"}\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical{\n"
"    background: none;\n"
"}\n"
"\n"
"/*HORIZONTAL SCROW BAR*/\n"
"\n"
"QScrollBar:horizontal{\n"
"    border: none;\n"
"    background-color: rgb(170, 255, 255);\n"
"    heigth:14px;\n"
"    border-radius: 0px;\n"
"}\n"
"QScrollBar::handle:horizontal{\n"
"    background-color: rgb(50, 200, 255);\n"
"    mini-height: 30px;\n"
"    border-radius: 7px;\n"
"}\n"
"QScrollBar::handle:horizontal:hover{\n"
"    background-color: rgb(70, 220, 255);\n"
"}\n"
"QScrollBar::handle:horizontal:pressed{\n"
"    background-color: rgb(30, 180, 255);\n"
"}\n"
"QScrollBar::sub-line:horizontal{\n"
"    border: none;\n"
"    background-color: rgb(50, 200, 255);\n"
"    width: 15px;\n"
"    border-top-left-radius: 7px;\n"
"    border-top-right-radius: 7px; \n"
"    subcontrol-posiiton: top;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:horizontal:hover{\n"
"    background-color: rgb(70, 220, 255);\n"
"}\n"
"QScrollBar::sub-line:horizontal:pressed{\n"
"    background-color: rgb(30, 180, 255);\n"
"}\n"
"QScrollBar::add-line:horizontal{\n"
"    border: none;\n"
"    background-color: rgb(50, 200, 255);\n"
"    width: 15px;\n"
"    border-bottom-left-radius: 7px;\n"
"    border-botton-right-radius: 7px;\n"
"    subcontrol-posiiton: botton;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"")
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.scrollArea = QtWidgets.QScrollArea(parent=self.centralwidget)
        self.scrollArea.setStyleSheet("QScrollBar:vertical{\n"
"    border: none;\n"
"    background-color: rgb(170, 255, 255);\n"
"}")
        self.scrollArea.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, -172, 976, 700))
        self.scrollAreaWidgetContents.setStyleSheet("")
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.scrollAreaWidgetContents)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.frame_fill_fiedls = QtWidgets.QFrame(parent=self.scrollAreaWidgetContents)
        self.frame_fill_fiedls.setMinimumSize(QtCore.QSize(700, 700))
        self.frame_fill_fiedls.setStyleSheet("background-color: rgb(170, 255, 255);")
        self.frame_fill_fiedls.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_fill_fiedls.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_fill_fiedls.setObjectName("frame_fill_fiedls")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_fill_fiedls)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.frame_coverages_outside = QtWidgets.QFrame(parent=self.frame_fill_fiedls)
        self.frame_coverages_outside.setMinimumSize(QtCore.QSize(150, 0))
        self.frame_coverages_outside.setMaximumSize(QtCore.QSize(300, 16777215))
        self.frame_coverages_outside.setStyleSheet("background-image: url(./src/images/background-blue-1715x980.jpg);\n"
"border-radius: 8px;")
        self.frame_coverages_outside.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_coverages_outside.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_coverages_outside.setObjectName("frame_coverages_outside")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame_coverages_outside)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.frame_coverages_inside = QtWidgets.QFrame(parent=self.frame_coverages_outside)
        self.frame_coverages_inside.setMinimumSize(QtCore.QSize(50, 50))
        self.frame_coverages_inside.setStyleSheet("QFrame{\n"
"    border: 2px solid rgb(36, 183, 253);\n"
"    border-radius: 8px;\n"
"}")
        self.frame_coverages_inside.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_coverages_inside.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_coverages_inside.setObjectName("frame_coverages_inside")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame_coverages_inside)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_coverage = QtWidgets.QLabel(parent=self.frame_coverages_inside)
        self.label_coverage.setMinimumSize(QtCore.QSize(0, 0))
        self.label_coverage.setMaximumSize(QtCore.QSize(16777215, 20))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_coverage.setFont(font)
        self.label_coverage.setStyleSheet("border: no-border")
        self.label_coverage.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_coverage.setObjectName("label_coverage")
        self.verticalLayout.addWidget(self.label_coverage)
        self.checkBox_monitoring = QtWidgets.QCheckBox(parent=self.frame_coverages_inside)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setBold(True)
        font.setWeight(75)
        self.checkBox_monitoring.setFont(font)
        self.checkBox_monitoring.setStyleSheet("QCheckBox{\n"
"    background-color: rgb(92, 230, 255);\n"
"}\n"
"QCheckBox:hover{\n"
"    color: rgb(0, 0, 255);\n"
"}")
        self.checkBox_monitoring.setObjectName("checkBox_monitoring")
        self.verticalLayout.addWidget(self.checkBox_monitoring)
        self.checkBox_robbery = QtWidgets.QCheckBox(parent=self.frame_coverages_inside)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setBold(True)
        font.setWeight(75)
        self.checkBox_robbery.setFont(font)
        self.checkBox_robbery.setStyleSheet("QCheckBox{\n"
"    background-color: rgb(92, 230, 255);\n"
"}\n"
"QCheckBox:hover{\n"
"    color: rgb(0, 0, 255);\n"
"}")
        self.checkBox_robbery.setObjectName("checkBox_robbery")
        self.verticalLayout.addWidget(self.checkBox_robbery)
        self.checkBox_theft = QtWidgets.QCheckBox(parent=self.frame_coverages_inside)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setBold(True)
        font.setWeight(75)
        self.checkBox_theft.setFont(font)
        self.checkBox_theft.setStyleSheet("QCheckBox{\n"
"    background-color: rgb(92, 230, 255);\n"
"}\n"
"QCheckBox:hover{\n"
"    color: rgb(0, 0, 255);\n"
"}")
        self.checkBox_theft.setObjectName("checkBox_theft")
        self.verticalLayout.addWidget(self.checkBox_theft)
        self.checkBox_pt = QtWidgets.QCheckBox(parent=self.frame_coverages_inside)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setBold(True)
        font.setWeight(75)
        self.checkBox_pt.setFont(font)
        self.checkBox_pt.setStyleSheet("QCheckBox{\n"
"    background-color: rgb(92, 230, 255);\n"
"}\n"
"QCheckBox:hover{\n"
"    color: rgb(0, 0, 255);\n"
"}")
        self.checkBox_pt.setObjectName("checkBox_pt")
        self.verticalLayout.addWidget(self.checkBox_pt)
        self.checkBox_collision = QtWidgets.QCheckBox(parent=self.frame_coverages_inside)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setBold(True)
        font.setWeight(75)
        self.checkBox_collision.setFont(font)
        self.checkBox_collision.setStyleSheet("QCheckBox{\n"
"    background-color: rgb(92, 230, 255);\n"
"}\n"
"QCheckBox:hover{\n"
"    color: rgb(0, 0, 255);\n"
"}")
        self.checkBox_collision.setObjectName("checkBox_collision")
        self.verticalLayout.addWidget(self.checkBox_collision)
        self.checkBox_winch3 = QtWidgets.QCheckBox(parent=self.frame_coverages_inside)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setBold(True)
        font.setWeight(75)
        self.checkBox_winch3.setFont(font)
        self.checkBox_winch3.setStyleSheet("QCheckBox{\n"
"    background-color: rgb(92, 230, 255);\n"
"}\n"
"QCheckBox:hover{\n"
"    color: rgb(0, 0, 255);\n"
"}")
        self.checkBox_winch3.setObjectName("checkBox_winch3")
        self.verticalLayout.addWidget(self.checkBox_winch3)
        self.checkBox_winch6 = QtWidgets.QCheckBox(parent=self.frame_coverages_inside)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setBold(True)
        font.setWeight(75)
        self.checkBox_winch6.setFont(font)
        self.checkBox_winch6.setStyleSheet("QCheckBox{\n"
"    background-color: rgb(92, 230, 255);\n"
"}\n"
"QCheckBox:hover{\n"
"    color: rgb(0, 0, 255);\n"
"}")
        self.checkBox_winch6.setObjectName("checkBox_winch6")
        self.verticalLayout.addWidget(self.checkBox_winch6)
        self.checkBox_unlimited_winch = QtWidgets.QCheckBox(parent=self.frame_coverages_inside)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setBold(True)
        font.setWeight(75)
        self.checkBox_unlimited_winch.setFont(font)
        self.checkBox_unlimited_winch.setStyleSheet("QCheckBox{\n"
"    background-color: rgb(92, 230, 255);\n"
"}\n"
"QCheckBox:hover{\n"
"    color: rgb(0, 0, 255);\n"
"}")
        self.checkBox_unlimited_winch.setObjectName("checkBox_unlimited_winch")
        self.verticalLayout.addWidget(self.checkBox_unlimited_winch)
        self.checkBox_winch500 = QtWidgets.QCheckBox(parent=self.frame_coverages_inside)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setBold(True)
        font.setWeight(75)
        self.checkBox_winch500.setFont(font)
        self.checkBox_winch500.setStyleSheet("QCheckBox{\n"
"    background-color: rgb(92, 230, 255);\n"
"}\n"
"QCheckBox:hover{\n"
"    color: rgb(0, 0, 255);\n"
"}")
        self.checkBox_winch500.setObjectName("checkBox_winch500")
        self.verticalLayout.addWidget(self.checkBox_winch500)
        self.checkBox_glasses = QtWidgets.QCheckBox(parent=self.frame_coverages_inside)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setBold(True)
        font.setWeight(75)
        self.checkBox_glasses.setFont(font)
        self.checkBox_glasses.setStyleSheet("QCheckBox{\n"
"    background-color: rgb(92, 230, 255);\n"
"}\n"
"QCheckBox:hover{\n"
"    color: rgb(0, 0, 255);\n"
"}")
        self.checkBox_glasses.setObjectName("checkBox_glasses")
        self.verticalLayout.addWidget(self.checkBox_glasses)
        self.checkBox_others = QtWidgets.QCheckBox(parent=self.frame_coverages_inside)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setBold(True)
        font.setWeight(75)
        self.checkBox_others.setFont(font)
        self.checkBox_others.setStyleSheet("QCheckBox{\n"
"    background-color: rgb(92, 230, 255);\n"
"}\n"
"QCheckBox:hover{\n"
"    color: rgb(0, 0, 255);\n"
"}")
        self.checkBox_others.setObjectName("checkBox_others")
        self.verticalLayout.addWidget(self.checkBox_others)
        self.lineEdit_plain_type = QtWidgets.QLineEdit(parent=self.frame_coverages_inside)
        self.lineEdit_plain_type.setStyleSheet("QLineEdit{\n"
"    \n"
"    background-color: rgb(148, 148, 148);\n"
"    border: 1px solid rgb(10,10,10);\n"
"    border-radius: 5px;\n"
"    padding: 2px;\n"
"}\n"
"QLineEdit:hover{\n"
"    border: 1px solid rgb(150,150,150);\n"
"}\n"
"QLineEdit:focus{\n"
"    border: 2px solid rgb(100, 100, 255);\n"
"}")
        self.lineEdit_plain_type.setObjectName("lineEdit_plain_type")
        self.verticalLayout.addWidget(self.lineEdit_plain_type)
        self.verticalLayout_4.addWidget(self.frame_coverages_inside)
        self.horizontalLayout_3.addWidget(self.frame_coverages_outside)
        self.frame_client_data_outside = QtWidgets.QFrame(parent=self.frame_fill_fiedls)
        self.frame_client_data_outside.setMinimumSize(QtCore.QSize(150, 0))
        self.frame_client_data_outside.setMaximumSize(QtCore.QSize(300, 16777215))
        self.frame_client_data_outside.setStyleSheet("background-image: url(./src/images/background-blue-1715x980.jpg);\n"
"border-radius: 8px;")
        self.frame_client_data_outside.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_client_data_outside.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_client_data_outside.setObjectName("frame_client_data_outside")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_client_data_outside)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame_client_data_inside = QtWidgets.QFrame(parent=self.frame_client_data_outside)
        self.frame_client_data_inside.setMinimumSize(QtCore.QSize(150, 50))
        self.frame_client_data_inside.setStyleSheet("QFrame{\n"
"    border: 2px solid rgb(36, 183, 253);\n"
"    border-radius: 8px;\n"
"}")
        self.frame_client_data_inside.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_client_data_inside.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_client_data_inside.setObjectName("frame_client_data_inside")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.frame_client_data_inside)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_clientdata = QtWidgets.QLabel(parent=self.frame_client_data_inside)
        self.label_clientdata.setMinimumSize(QtCore.QSize(0, 0))
        self.label_clientdata.setMaximumSize(QtCore.QSize(16777215, 20))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_clientdata.setFont(font)
        self.label_clientdata.setStyleSheet("border:no")
        self.label_clientdata.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_clientdata.setObjectName("label_clientdata")
        self.verticalLayout_5.addWidget(self.label_clientdata)
        self.lineEdit_name = QtWidgets.QLineEdit(parent=self.frame_client_data_inside)
        self.lineEdit_name.setStyleSheet("QLineEdit{\n"
"    \n"
"    background-color: rgb(148, 148, 148);\n"
"    border: 1px solid rgb(10,10,10);\n"
"    border-radius: 5px;\n"
"    padding: 2px;\n"
"}\n"
"QLineEdit:hover{\n"
"    border: 1px solid rgb(150,150,150);\n"
"}\n"
"QLineEdit:focus{\n"
"    border: 2px solid rgb(100, 100, 255);\n"
"}")
        self.lineEdit_name.setObjectName("lineEdit_name")
        self.verticalLayout_5.addWidget(self.lineEdit_name)
        self.lineEdit_rg_3 = QtWidgets.QLineEdit(parent=self.frame_client_data_inside)
        self.lineEdit_rg_3.setStyleSheet("QLineEdit{\n"
"    \n"
"    background-color: rgb(148, 148, 148);\n"
"    border: 1px solid rgb(10,10,10);\n"
"    border-radius: 5px;\n"
"    padding: 2px;\n"
"}\n"
"QLineEdit:hover{\n"
"    border: 1px solid rgb(150,150,150);\n"
"}\n"
"QLineEdit:focus{\n"
"    border: 2px solid rgb(100, 100, 255);\n"
"}")
        self.lineEdit_rg_3.setObjectName("lineEdit_rg_3")
        self.verticalLayout_5.addWidget(self.lineEdit_rg_3)
        self.lineEdit_cpf = QtWidgets.QLineEdit(parent=self.frame_client_data_inside)
        self.lineEdit_cpf.setStyleSheet("QLineEdit{\n"
"    \n"
"    background-color: rgb(148, 148, 148);\n"
"    border: 1px solid rgb(10,10,10);\n"
"    border-radius: 5px;\n"
"    padding: 2px;\n"
"}\n"
"QLineEdit:hover{\n"
"    border: 1px solid rgb(150,150,150);\n"
"}\n"
"QLineEdit:focus{\n"
"    border: 2px solid rgb(100, 100, 255);\n"
"}")
        self.lineEdit_cpf.setObjectName("lineEdit_cpf")
        self.verticalLayout_5.addWidget(self.lineEdit_cpf)
        self.lineEdit_birth = QtWidgets.QLineEdit(parent=self.frame_client_data_inside)
        self.lineEdit_birth.setStyleSheet("QLineEdit{\n"
"    \n"
"    background-color: rgb(148, 148, 148);\n"
"    border: 1px solid rgb(10,10,10);\n"
"    border-radius: 5px;\n"
"    padding: 2px;\n"
"}\n"
"QLineEdit:hover{\n"
"    border: 1px solid rgb(150,150,150);\n"
"}\n"
"QLineEdit:focus{\n"
"    border: 2px solid rgb(100, 100, 255);\n"
"}")
        self.lineEdit_birth.setObjectName("lineEdit_birth")
        self.verticalLayout_5.addWidget(self.lineEdit_birth)
        self.lineEdit_nationality = QtWidgets.QLineEdit(parent=self.frame_client_data_inside)
        self.lineEdit_nationality.setStyleSheet("QLineEdit{\n"
"    \n"
"    background-color: rgb(148, 148, 148);\n"
"    border: 1px solid rgb(10,10,10);\n"
"    border-radius: 5px;\n"
"    padding: 2px;\n"
"}\n"
"QLineEdit:hover{\n"
"    border: 1px solid rgb(150,150,150);\n"
"}\n"
"QLineEdit:focus{\n"
"    border: 2px solid rgb(100, 100, 255);\n"
"}")
        self.lineEdit_nationality.setObjectName("lineEdit_nationality")
        self.verticalLayout_5.addWidget(self.lineEdit_nationality)
        self.lineEdit_phone1 = QtWidgets.QLineEdit(parent=self.frame_client_data_inside)
        self.lineEdit_phone1.setStyleSheet("QLineEdit{\n"
"    \n"
"    background-color: rgb(148, 148, 148);\n"
"    border: 1px solid rgb(10,10,10);\n"
"    border-radius: 5px;\n"
"    padding: 2px;\n"
"}\n"
"QLineEdit:hover{\n"
"    border: 1px solid rgb(150,150,150);\n"
"}\n"
"QLineEdit:focus{\n"
"    border: 2px solid rgb(100, 100, 255);\n"
"}")
        self.lineEdit_phone1.setObjectName("lineEdit_phone1")
        self.verticalLayout_5.addWidget(self.lineEdit_phone1)
        self.lineEdit_phone2 = QtWidgets.QLineEdit(parent=self.frame_client_data_inside)
        self.lineEdit_phone2.setStyleSheet("QLineEdit{\n"
"    \n"
"    background-color: rgb(148, 148, 148);\n"
"    border: 1px solid rgb(10,10,10);\n"
"    border-radius: 5px;\n"
"    padding: 2px;\n"
"}\n"
"QLineEdit:hover{\n"
"    border: 1px solid rgb(150,150,150);\n"
"}\n"
"QLineEdit:focus{\n"
"    border: 2px solid rgb(100, 100, 255);\n"
"}")
        self.lineEdit_phone2.setObjectName("lineEdit_phone2")
        self.verticalLayout_5.addWidget(self.lineEdit_phone2)
        self.label_adress = QtWidgets.QLabel(parent=self.frame_client_data_inside)
        self.label_adress.setMinimumSize(QtCore.QSize(0, 0))
        self.label_adress.setMaximumSize(QtCore.QSize(16777215, 20))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.label_adress.setFont(font)
        self.label_adress.setStyleSheet("border-color: rgb(36, 183, 253);")
        self.label_adress.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_adress.setObjectName("label_adress")
        self.verticalLayout_5.addWidget(self.label_adress)
        self.lineEdit_street = QtWidgets.QLineEdit(parent=self.frame_client_data_inside)
        self.lineEdit_street.setStyleSheet("QLineEdit{\n"
"    \n"
"    background-color: rgb(148, 148, 148);\n"
"    border: 1px solid rgb(10,10,10);\n"
"    border-radius: 5px;\n"
"    padding: 2px;\n"
"}\n"
"QLineEdit:hover{\n"
"    border: 1px solid rgb(150,150,150);\n"
"}\n"
"QLineEdit:focus{\n"
"    border: 2px solid rgb(100, 100, 255);\n"
"}")
        self.lineEdit_street.setObjectName("lineEdit_street")
        self.verticalLayout_5.addWidget(self.lineEdit_street)
        self.lineEdit_number = QtWidgets.QLineEdit(parent=self.frame_client_data_inside)
        self.lineEdit_number.setStyleSheet("QLineEdit{\n"
"    \n"
"    background-color: rgb(148, 148, 148);\n"
"    border: 1px solid rgb(10,10,10);\n"
"    border-radius: 5px;\n"
"    padding: 2px;\n"
"}\n"
"QLineEdit:hover{\n"
"    border: 1px solid rgb(150,150,150);\n"
"}\n"
"QLineEdit:focus{\n"
"    border: 2px solid rgb(100, 100, 255);\n"
"}")
        self.lineEdit_number.setObjectName("lineEdit_number")
        self.verticalLayout_5.addWidget(self.lineEdit_number)
        self.lineEdit_comp = QtWidgets.QLineEdit(parent=self.frame_client_data_inside)
        self.lineEdit_comp.setStyleSheet("QLineEdit{\n"
"    \n"
"    background-color: rgb(148, 148, 148);\n"
"    border: 1px solid rgb(10,10,10);\n"
"    border-radius: 5px;\n"
"    padding: 2px;\n"
"}\n"
"QLineEdit:hover{\n"
"    border: 1px solid rgb(150,150,150);\n"
"}\n"
"QLineEdit:focus{\n"
"    border: 2px solid rgb(100, 100, 255);\n"
"}")
        self.lineEdit_comp.setObjectName("lineEdit_comp")
        self.verticalLayout_5.addWidget(self.lineEdit_comp)
        self.lineEdit_neghbordhood = QtWidgets.QLineEdit(parent=self.frame_client_data_inside)
        self.lineEdit_neghbordhood.setStyleSheet("QLineEdit{\n"
"    \n"
"    background-color: rgb(148, 148, 148);\n"
"    border: 1px solid rgb(10,10,10);\n"
"    border-radius: 5px;\n"
"    padding: 2px;\n"
"}\n"
"QLineEdit:hover{\n"
"    border: 1px solid rgb(150,150,150);\n"
"}\n"
"QLineEdit:focus{\n"
"    border: 2px solid rgb(100, 100, 255);\n"
"}")
        self.lineEdit_neghbordhood.setObjectName("lineEdit_neghbordhood")
        self.verticalLayout_5.addWidget(self.lineEdit_neghbordhood)
        self.lineEdit_city = QtWidgets.QLineEdit(parent=self.frame_client_data_inside)
        self.lineEdit_city.setStyleSheet("QLineEdit{\n"
"    \n"
"    background-color: rgb(148, 148, 148);\n"
"    border: 1px solid rgb(10,10,10);\n"
"    border-radius: 5px;\n"
"    padding: 2px;\n"
"}\n"
"QLineEdit:hover{\n"
"    border: 1px solid rgb(150,150,150);\n"
"}\n"
"QLineEdit:focus{\n"
"    border: 2px solid rgb(100, 100, 255);\n"
"}")
        self.lineEdit_city.setObjectName("lineEdit_city")
        self.verticalLayout_5.addWidget(self.lineEdit_city)
        self.lineEdit_uf = QtWidgets.QLineEdit(parent=self.frame_client_data_inside)
        self.lineEdit_uf.setStyleSheet("QLineEdit{\n"
"    \n"
"    background-color: rgb(148, 148, 148);\n"
"    border: 1px solid rgb(10,10,10);\n"
"    border-radius: 5px;\n"
"    padding: 2px;\n"
"}\n"
"QLineEdit:hover{\n"
"    border: 1px solid rgb(150,150,150);\n"
"}\n"
"QLineEdit:focus{\n"
"    border: 2px solid rgb(100, 100, 255);\n"
"}")
        self.lineEdit_uf.setObjectName("lineEdit_uf")
        self.verticalLayout_5.addWidget(self.lineEdit_uf)
        self.lineEdit_cep = QtWidgets.QLineEdit(parent=self.frame_client_data_inside)
        self.lineEdit_cep.setStyleSheet("QLineEdit{\n"
"    \n"
"    background-color: rgb(148, 148, 148);\n"
"    border: 1px solid rgb(10,10,10);\n"
"    border-radius: 5px;\n"
"    padding: 2px;\n"
"}\n"
"QLineEdit:hover{\n"
"    border: 1px solid rgb(150,150,150);\n"
"}\n"
"QLineEdit:focus{\n"
"    border: 2px solid rgb(100, 100, 255);\n"
"}")
        self.lineEdit_cep.setObjectName("lineEdit_cep")
        self.verticalLayout_5.addWidget(self.lineEdit_cep)
        self.verticalLayout_2.addWidget(self.frame_client_data_inside)
        self.horizontalLayout_3.addWidget(self.frame_client_data_outside)
        self.frame_contract_outside = QtWidgets.QFrame(parent=self.frame_fill_fiedls)
        self.frame_contract_outside.setMinimumSize(QtCore.QSize(0, 0))
        self.frame_contract_outside.setMaximumSize(QtCore.QSize(300, 16777215))
        self.frame_contract_outside.setStyleSheet("background-image: url(./src/images/background-blue-1715x980.jpg);\n"
"border-radius: 8px;")
        self.frame_contract_outside.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_contract_outside.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_contract_outside.setObjectName("frame_contract_outside")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.frame_contract_outside)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.frame_vehicle_plain_data_inside = QtWidgets.QFrame(parent=self.frame_contract_outside)
        self.frame_vehicle_plain_data_inside.setMinimumSize(QtCore.QSize(150, 50))
        self.frame_vehicle_plain_data_inside.setStyleSheet("QFrame{\n"
"    border: 2px solid rgb(36, 183, 253);\n"
"    border-radius: 8px;\n"
"}")
        self.frame_vehicle_plain_data_inside.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_vehicle_plain_data_inside.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_vehicle_plain_data_inside.setObjectName("frame_vehicle_plain_data_inside")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_vehicle_plain_data_inside)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_vehicle = QtWidgets.QLabel(parent=self.frame_vehicle_plain_data_inside)
        self.label_vehicle.setMinimumSize(QtCore.QSize(0, 0))
        self.label_vehicle.setMaximumSize(QtCore.QSize(16777215, 20))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_vehicle.setFont(font)
        self.label_vehicle.setStyleSheet("border:no")
        self.label_vehicle.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_vehicle.setObjectName("label_vehicle")
        self.verticalLayout_3.addWidget(self.label_vehicle)
        self.lineEdit_assembler = QtWidgets.QLineEdit(parent=self.frame_vehicle_plain_data_inside)
        self.lineEdit_assembler.setStyleSheet("QLineEdit{\n"
"    \n"
"    background-color: rgb(148, 148, 148);\n"
"    border: 1px solid rgb(10,10,10);\n"
"    border-radius: 5px;\n"
"    padding: 2px;\n"
"}\n"
"QLineEdit:hover{\n"
"    border: 1px solid rgb(150,150,150);\n"
"}\n"
"QLineEdit:focus{\n"
"    border: 2px solid rgb(100, 100, 255);\n"
"}")
        self.lineEdit_assembler.setObjectName("lineEdit_assembler")
        self.verticalLayout_3.addWidget(self.lineEdit_assembler)
        self.lineEdit_model = QtWidgets.QLineEdit(parent=self.frame_vehicle_plain_data_inside)
        self.lineEdit_model.setStyleSheet("QLineEdit{\n"
"    \n"
"    background-color: rgb(148, 148, 148);\n"
"    border: 1px solid rgb(10,10,10);\n"
"    border-radius: 5px;\n"
"    padding: 2px;\n"
"}\n"
"QLineEdit:hover{\n"
"    border: 1px solid rgb(150,150,150);\n"
"}\n"
"QLineEdit:focus{\n"
"    border: 2px solid rgb(100, 100, 255);\n"
"}")
        self.lineEdit_model.setObjectName("lineEdit_model")
        self.verticalLayout_3.addWidget(self.lineEdit_model)
        self.lineEdit_plate = QtWidgets.QLineEdit(parent=self.frame_vehicle_plain_data_inside)
        self.lineEdit_plate.setStyleSheet("QLineEdit{\n"
"    \n"
"    background-color: rgb(148, 148, 148);\n"
"    border: 1px solid rgb(10,10,10);\n"
"    border-radius: 5px;\n"
"    padding: 2px;\n"
"}\n"
"QLineEdit:hover{\n"
"    border: 1px solid rgb(150,150,150);\n"
"}\n"
"QLineEdit:focus{\n"
"    border: 2px solid rgb(100, 100, 255);\n"
"}")
        self.lineEdit_plate.setObjectName("lineEdit_plate")
        self.verticalLayout_3.addWidget(self.lineEdit_plate)
        self.lineEdit_color = QtWidgets.QLineEdit(parent=self.frame_vehicle_plain_data_inside)
        self.lineEdit_color.setStyleSheet("QLineEdit{\n"
"    \n"
"    background-color: rgb(148, 148, 148);\n"
"    border: 1px solid rgb(10,10,10);\n"
"    border-radius: 5px;\n"
"    padding: 2px;\n"
"}\n"
"QLineEdit:hover{\n"
"    border: 1px solid rgb(150,150,150);\n"
"}\n"
"QLineEdit:focus{\n"
"    border: 2px solid rgb(100, 100, 255);\n"
"}")
        self.lineEdit_color.setObjectName("lineEdit_color")
        self.verticalLayout_3.addWidget(self.lineEdit_color)
        self.lineEdit_year = QtWidgets.QLineEdit(parent=self.frame_vehicle_plain_data_inside)
        self.lineEdit_year.setStyleSheet("QLineEdit{\n"
"    \n"
"    background-color: rgb(148, 148, 148);\n"
"    border: 1px solid rgb(10,10,10);\n"
"    border-radius: 5px;\n"
"    padding: 2px;\n"
"}\n"
"QLineEdit:hover{\n"
"    border: 1px solid rgb(150,150,150);\n"
"}\n"
"QLineEdit:focus{\n"
"    border: 2px solid rgb(100, 100, 255);\n"
"}")
        self.lineEdit_year.setObjectName("lineEdit_year")
        self.verticalLayout_3.addWidget(self.lineEdit_year)
        self.lineEdit_chassis = QtWidgets.QLineEdit(parent=self.frame_vehicle_plain_data_inside)
        self.lineEdit_chassis.setStyleSheet("QLineEdit{\n"
"    \n"
"    background-color: rgb(148, 148, 148);\n"
"    border: 1px solid rgb(10,10,10);\n"
"    border-radius: 5px;\n"
"    padding: 2px;\n"
"}\n"
"QLineEdit:hover{\n"
"    border: 1px solid rgb(150,150,150);\n"
"}\n"
"QLineEdit:focus{\n"
"    border: 2px solid rgb(100, 100, 255);\n"
"}")
        self.lineEdit_chassis.setObjectName("lineEdit_chassis")
        self.verticalLayout_3.addWidget(self.lineEdit_chassis)
        self.lineEdit_renavam = QtWidgets.QLineEdit(parent=self.frame_vehicle_plain_data_inside)
        self.lineEdit_renavam.setStyleSheet("QLineEdit{\n"
"    \n"
"    background-color: rgb(148, 148, 148);\n"
"    border: 1px solid rgb(10,10,10);\n"
"    border-radius: 5px;\n"
"    padding: 2px;\n"
"}\n"
"QLineEdit:hover{\n"
"    border: 1px solid rgb(150,150,150);\n"
"}\n"
"QLineEdit:focus{\n"
"    border: 2px solid rgb(100, 100, 255);\n"
"}")
        self.lineEdit_renavam.setObjectName("lineEdit_renavam")
        self.verticalLayout_3.addWidget(self.lineEdit_renavam)
        self.lineEdit_fipe_value = QtWidgets.QLineEdit(parent=self.frame_vehicle_plain_data_inside)
        self.lineEdit_fipe_value.setStyleSheet("QLineEdit{\n"
"    \n"
"    background-color: rgb(148, 148, 148);\n"
"    border: 1px solid rgb(10,10,10);\n"
"    border-radius: 5px;\n"
"    padding: 2px;\n"
"}\n"
"QLineEdit:hover{\n"
"    border: 1px solid rgb(150,150,150);\n"
"}\n"
"QLineEdit:focus{\n"
"    border: 2px solid rgb(100, 100, 255);\n"
"}")
        self.lineEdit_fipe_value.setObjectName("lineEdit_fipe_value")
        self.verticalLayout_3.addWidget(self.lineEdit_fipe_value)
        self.lineEdit_fipe_code = QtWidgets.QLineEdit(parent=self.frame_vehicle_plain_data_inside)
        self.lineEdit_fipe_code.setStyleSheet("QLineEdit{\n"
"    \n"
"    background-color: rgb(148, 148, 148);\n"
"    border: 1px solid rgb(10,10,10);\n"
"    border-radius: 5px;\n"
"    padding: 2px;\n"
"}\n"
"QLineEdit:hover{\n"
"    border: 1px solid rgb(150,150,150);\n"
"}\n"
"QLineEdit:focus{\n"
"    border: 2px solid rgb(100, 100, 255);\n"
"}")
        self.lineEdit_fipe_code.setObjectName("lineEdit_fipe_code")
        self.verticalLayout_3.addWidget(self.lineEdit_fipe_code)
        self.lineEdit_hora = QtWidgets.QLineEdit(parent=self.frame_vehicle_plain_data_inside)
        self.lineEdit_hora.setStyleSheet("QLineEdit{\n"
"    \n"
"    background-color: rgb(148, 148, 148);\n"
"    border: 1px solid rgb(10,10,10);\n"
"    border-radius: 5px;\n"
"    padding: 2px;\n"
"}\n"
"QLineEdit:hover{\n"
"    border: 1px solid rgb(150,150,150);\n"
"}\n"
"QLineEdit:focus{\n"
"    border: 2px solid rgb(100, 100, 255);\n"
"}")
        self.lineEdit_hora.setObjectName("lineEdit_hora")
        self.verticalLayout_3.addWidget(self.lineEdit_hora)
        self.verticalLayout_9.addWidget(self.frame_vehicle_plain_data_inside)
        self.frame_contract_inside = QtWidgets.QFrame(parent=self.frame_contract_outside)
        self.frame_contract_inside.setMinimumSize(QtCore.QSize(1, 221))
        self.frame_contract_inside.setStyleSheet("QFrame{\n"
"    border: 2px solid rgb(36, 183, 253);\n"
"    border-radius: 8px;\n"
"}")
        self.frame_contract_inside.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_contract_inside.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_contract_inside.setObjectName("frame_contract_inside")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.frame_contract_inside)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.label_textArea = QtWidgets.QLabel(parent=self.frame_contract_inside)
        self.label_textArea.setMinimumSize(QtCore.QSize(0, 0))
        self.label_textArea.setMaximumSize(QtCore.QSize(16777215, 20))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_textArea.setFont(font)
        self.label_textArea.setStyleSheet("border: no")
        self.label_textArea.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_textArea.setObjectName("label_textArea")
        self.verticalLayout_11.addWidget(self.label_textArea)
        self.pushButton_insert_file = QtWidgets.QPushButton(parent=self.frame_contract_inside)
        self.pushButton_insert_file.setStyleSheet("QPushButton{\n"
"    border: 1px solid rgb(10, 10, 10);\n"
"    border-radius: 5px;\n"
"    background-color: rgb(100, 230, 253);\n"
"    padding: 5px;\n"
"}\n"
"QPushButton:hover{\n"
"    border: 1px solid rgb(150,150,150);\n"
"     font: 12px;\n"
"}\n"
"QPushButton:pressed{\n"
"    border: 2px solid rgb(50, 50, 255);\n"
"    font: 10px;\n"
"}")
        self.pushButton_insert_file.setObjectName("pushButton_insert_file")
        self.verticalLayout_11.addWidget(self.pushButton_insert_file)
        self.verticalLayout_9.addWidget(self.frame_contract_inside)
        self.horizontalLayout_3.addWidget(self.frame_contract_outside)
        self.frame_financial_buttons_company_data = QtWidgets.QFrame(parent=self.frame_fill_fiedls)
        self.frame_financial_buttons_company_data.setMinimumSize(QtCore.QSize(0, 0))
        self.frame_financial_buttons_company_data.setMaximumSize(QtCore.QSize(300, 16777215))
        self.frame_financial_buttons_company_data.setStyleSheet("")
        self.frame_financial_buttons_company_data.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_financial_buttons_company_data.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_financial_buttons_company_data.setObjectName("frame_financial_buttons_company_data")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.frame_financial_buttons_company_data)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.frame_financial = QtWidgets.QFrame(parent=self.frame_financial_buttons_company_data)
        self.frame_financial.setMinimumSize(QtCore.QSize(161, 286))
        self.frame_financial.setMaximumSize(QtCore.QSize(300, 16777215))
        self.frame_financial.setStyleSheet("QFrame{\n"
"    background-color: rgb(139, 253, 137);\n"
"    border-radius: 8px;\n"
"}")
        self.frame_financial.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_financial.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_financial.setObjectName("frame_financial")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.frame_financial)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label_finance = QtWidgets.QLabel(parent=self.frame_financial)
        self.label_finance.setMinimumSize(QtCore.QSize(0, 0))
        self.label_finance.setMaximumSize(QtCore.QSize(16777215, 20))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_finance.setFont(font)
        self.label_finance.setStyleSheet("QLabel{\n"
"    border:no;\n"
"}")
        self.label_finance.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_finance.setObjectName("label_finance")
        self.verticalLayout_6.addWidget(self.label_finance)
        self.lineEdit_monthly_payment = QtWidgets.QLineEdit(parent=self.frame_financial)
        self.lineEdit_monthly_payment.setStyleSheet("QLineEdit{\n"
"    \n"
"    background-color: rgb(142, 216, 141);\n"
"    border: 2px solid rgb(0, 102, 52);\n"
"    border-radius: 5px;\n"
"    padding: 2px;\n"
"}\n"
"QLineEdit:hover{\n"
"    border: 2px solid rgb(100, 202, 152);\n"
"}\n"
"QLineEdit:focus{\n"
"    border: 2px solid rgb(0, 0, 255);\n"
"}")
        self.lineEdit_monthly_payment.setObjectName("lineEdit_monthly_payment")
        self.verticalLayout_6.addWidget(self.lineEdit_monthly_payment)
        self.lineEdit_membership_fee = QtWidgets.QLineEdit(parent=self.frame_financial)
        self.lineEdit_membership_fee.setStyleSheet("QLineEdit{\n"
"    \n"
"    background-color: rgb(142, 216, 141);\n"
"    border: 2px solid rgb(0, 102, 52);\n"
"    border-radius: 5px;\n"
"    padding: 2px;\n"
"}\n"
"QLineEdit:hover{\n"
"    border: 2px solid rgb(100, 202, 152);\n"
"}\n"
"QLineEdit:focus{\n"
"    border: 2px solid rgb(0, 0, 255);\n"
"}")
        self.lineEdit_membership_fee.setObjectName("lineEdit_membership_fee")
        self.verticalLayout_6.addWidget(self.lineEdit_membership_fee)
        self.lineEdit_total_payment = QtWidgets.QLineEdit(parent=self.frame_financial)
        self.lineEdit_total_payment.setStyleSheet("QLineEdit{\n"
"    \n"
"    background-color: rgb(142, 216, 141);\n"
"    border: 2px solid rgb(0, 102, 52);\n"
"    border-radius: 5px;\n"
"    padding: 2px;\n"
"}\n"
"QLineEdit:hover{\n"
"    border: 2px solid rgb(100, 202, 152);\n"
"}\n"
"QLineEdit:focus{\n"
"    border: 2px solid rgb(0, 0, 255);\n"
"}")
        self.lineEdit_total_payment.setObjectName("lineEdit_total_payment")
        self.verticalLayout_6.addWidget(self.lineEdit_total_payment)
        self.frame_playndate = QtWidgets.QFrame(parent=self.frame_financial)
        self.frame_playndate.setMaximumSize(QtCore.QSize(16777215, 142))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        self.frame_playndate.setFont(font)
        self.frame_playndate.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_playndate.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_playndate.setObjectName("frame_playndate")
        self.verticalLayout_12 = QtWidgets.QVBoxLayout(self.frame_playndate)
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.label_start = QtWidgets.QLabel(parent=self.frame_playndate)
        self.label_start.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_start.setFont(font)
        self.label_start.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label_start.setObjectName("label_start")
        self.verticalLayout_12.addWidget(self.label_start)
        self.dateEdit_start = QtWidgets.QDateEdit(parent=self.frame_playndate)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        self.dateEdit_start.setFont(font)
        self.dateEdit_start.setStyleSheet("")
        self.dateEdit_start.setObjectName("dateEdit_start")
        self.verticalLayout_12.addWidget(self.dateEdit_start)
        self.label_finish = QtWidgets.QLabel(parent=self.frame_playndate)
        self.label_finish.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setBold(True)
        font.setWeight(75)
        self.label_finish.setFont(font)
        self.label_finish.setObjectName("label_finish")
        self.verticalLayout_12.addWidget(self.label_finish)
        self.dateEdit_finish = QtWidgets.QDateEdit(parent=self.frame_playndate)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        self.dateEdit_finish.setFont(font)
        self.dateEdit_finish.setObjectName("dateEdit_finish")
        self.verticalLayout_12.addWidget(self.dateEdit_finish)
        self.verticalLayout_6.addWidget(self.frame_playndate)
        self.frame_playndate_2 = QtWidgets.QFrame(parent=self.frame_financial)
        self.frame_playndate_2.setMinimumSize(QtCore.QSize(0, 0))
        self.frame_playndate_2.setMaximumSize(QtCore.QSize(16777215, 142))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        self.frame_playndate_2.setFont(font)
        self.frame_playndate_2.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_playndate_2.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_playndate_2.setObjectName("frame_playndate_2")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.frame_playndate_2)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.label_detail_recibo = QtWidgets.QLabel(parent=self.frame_playndate_2)
        self.label_detail_recibo.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_detail_recibo.setFont(font)
        self.label_detail_recibo.setTextFormat(QtCore.Qt.TextFormat.PlainText)
        self.label_detail_recibo.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_detail_recibo.setObjectName("label_detail_recibo")
        self.verticalLayout_8.addWidget(self.label_detail_recibo)
        self.textEdit_detail_pagto_obs = QtWidgets.QTextEdit(parent=self.frame_playndate_2)
        self.textEdit_detail_pagto_obs.setMinimumSize(QtCore.QSize(0, 58))
        self.textEdit_detail_pagto_obs.setStyleSheet("QTextEdit{\n"
"    \n"
"    background-color: rgb(142, 216, 141);\n"
"    border: 2px solid rgb(0, 102, 52);\n"
"    border-radius: 5px;\n"
"    padding: 2px;\n"
"}\n"
"QTextEdit:hover{\n"
"    border: 2px solid rgb(100, 202, 152);\n"
"}\n"
"QTextEdit:focus{\n"
"    border: 2px solid rgb(0, 0, 255);\n"
"}")
        self.textEdit_detail_pagto_obs.setObjectName("textEdit_detail_pagto_obs")
        self.verticalLayout_8.addWidget(self.textEdit_detail_pagto_obs)
        self.label_formapagto = QtWidgets.QLabel(parent=self.frame_playndate_2)
        self.label_formapagto.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_formapagto.setFont(font)
        self.label_formapagto.setTextFormat(QtCore.Qt.TextFormat.PlainText)
        self.label_formapagto.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_formapagto.setObjectName("label_formapagto")
        self.verticalLayout_8.addWidget(self.label_formapagto)
        self.comboBox_formapagto = QtWidgets.QComboBox(parent=self.frame_playndate_2)
        self.comboBox_formapagto.setStyleSheet("QComboBox{\n"
"    border-radius: 2px;\n"
"}")
        self.comboBox_formapagto.setObjectName("comboBox_formapagto")
        self.verticalLayout_8.addWidget(self.comboBox_formapagto)
        self.verticalLayout_6.addWidget(self.frame_playndate_2)
        self.verticalLayout_10.addWidget(self.frame_financial)
        self.frame_company_data_outside_2 = QtWidgets.QFrame(parent=self.frame_financial_buttons_company_data)
        self.frame_company_data_outside_2.setMinimumSize(QtCore.QSize(150, 120))
        self.frame_company_data_outside_2.setMaximumSize(QtCore.QSize(300, 200))
        self.frame_company_data_outside_2.setStyleSheet("border-radius: 8px;\n"
"background-color: rgb(170, 255, 255);")
        self.frame_company_data_outside_2.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_company_data_outside_2.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_company_data_outside_2.setObjectName("frame_company_data_outside_2")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frame_company_data_outside_2)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.frame_company_data = QtWidgets.QFrame(parent=self.frame_company_data_outside_2)
        self.frame_company_data.setMinimumSize(QtCore.QSize(150, 118))
        self.frame_company_data.setStyleSheet("QFrame{\n"
"    border: 2px solid rgb(36, 183, 253);\n"
"    border-radius: 8px;\n"
"}")
        self.frame_company_data.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_company_data.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_company_data.setObjectName("frame_company_data")
        self.verticalLayout_13 = QtWidgets.QVBoxLayout(self.frame_company_data)
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.label_company_data = QtWidgets.QLabel(parent=self.frame_company_data)
        self.label_company_data.setMinimumSize(QtCore.QSize(0, 0))
        self.label_company_data.setMaximumSize(QtCore.QSize(16777215, 15))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_company_data.setFont(font)
        self.label_company_data.setStyleSheet("border:no")
        self.label_company_data.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_company_data.setObjectName("label_company_data")
        self.verticalLayout_13.addWidget(self.label_company_data)
        self.lineEdit_razao_social = QtWidgets.QLineEdit(parent=self.frame_company_data)
        self.lineEdit_razao_social.setStyleSheet("QLineEdit{\n"
"    \n"
"    background-color: rgb(103, 229, 254);\n"
"    border: 1px solid rgb(10,10,10);\n"
"    border-radius: 5px;\n"
"    padding: 2px;\n"
"}\n"
"QLineEdit:hover{\n"
"    border: 1px solid rgb(150,150,150);\n"
"}\n"
"QLineEdit:focus{\n"
"    border: 2px solid rgb(100, 100, 255);\n"
"}")
        self.lineEdit_razao_social.setObjectName("lineEdit_razao_social")
        self.verticalLayout_13.addWidget(self.lineEdit_razao_social)
        self.lineEdit_cnpj = QtWidgets.QLineEdit(parent=self.frame_company_data)
        self.lineEdit_cnpj.setStyleSheet("QLineEdit{\n"
"    \n"
"    background-color: rgb(103, 229, 254);\n"
"    border: 1px solid rgb(10,10,10);\n"
"    border-radius: 5px;\n"
"    padding: 2px;\n"
"}\n"
"QLineEdit:hover{\n"
"    border: 1px solid rgb(150,150,150);\n"
"}\n"
"QLineEdit:focus{\n"
"    border: 2px solid rgb(100, 100, 255);\n"
"}")
        self.lineEdit_cnpj.setObjectName("lineEdit_cnpj")
        self.verticalLayout_13.addWidget(self.lineEdit_cnpj)
        self.horizontalLayout_4.addWidget(self.frame_company_data)
        self.verticalLayout_10.addWidget(self.frame_company_data_outside_2)
        self.frame_buttons_observations = QtWidgets.QFrame(parent=self.frame_financial_buttons_company_data)
        self.frame_buttons_observations.setMaximumSize(QtCore.QSize(16777215, 200))
        self.frame_buttons_observations.setStyleSheet("QFrame{\n"
"    border: no\n"
"}")
        self.frame_buttons_observations.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_buttons_observations.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_buttons_observations.setObjectName("frame_buttons_observations")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.frame_buttons_observations)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.pushButton_adhesion = QtWidgets.QPushButton(parent=self.frame_buttons_observations)
        self.pushButton_adhesion.setMinimumSize(QtCore.QSize(20, 22))
        self.pushButton_adhesion.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        self.pushButton_adhesion.setFont(font)
        self.pushButton_adhesion.setStyleSheet("QPushButton{\n"
"    border: 1px solid rgb(10, 10, 10);\n"
"    border-radius: 5px;\n"
"    background-color: rgb(100, 230, 253);\n"
"}\n"
"QPushButton:hover{\n"
"    border: 1px solid rgb(150,150,150);\n"
"     font: 12px;\n"
"}\n"
"QPushButton:pressed{\n"
"    border: 2px solid rgb(50, 50, 255);\n"
"    font: 10px;\n"
"}")
        self.pushButton_adhesion.setObjectName("pushButton_adhesion")
        self.verticalLayout_7.addWidget(self.pushButton_adhesion)
        self.verticalLayout_10.addWidget(self.frame_buttons_observations)
        self.horizontalLayout_3.addWidget(self.frame_financial_buttons_company_data)
        self.horizontalLayout_2.addWidget(self.frame_fill_fiedls)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.horizontalLayout.addWidget(self.scrollArea)
        MainWindow.setCentralWidget(self.centralwidget)
        self.actionGerar_termo_de_ades_o = QtGui.QAction(parent=MainWindow)
        self.actionGerar_termo_de_ades_o.setObjectName("actionGerar_termo_de_ades_o")
        self.actionNovo = QtGui.QAction(parent=MainWindow)
        self.actionNovo.setObjectName("actionNovo")
        self.actionSalvar = QtGui.QAction(parent=MainWindow)
        self.actionSalvar.setObjectName("actionSalvar")
        self.actionGerar_Termo_em_PDF = QtGui.QAction(parent=MainWindow)
        self.actionGerar_Termo_em_PDF.setObjectName("actionGerar_Termo_em_PDF")
        self.actionImprimir_Termo = QtGui.QAction(parent=MainWindow)
        self.actionImprimir_Termo.setObjectName("actionImprimir_Termo")
        self.actionImprimir_Termo_2 = QtGui.QAction(parent=MainWindow)
        self.actionImprimir_Termo_2.setObjectName("actionImprimir_Termo_2")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # FUNCTIONS:
        self.pushButton_insert_file.clicked.connect(self.show_file_dialog)

    def show_file_dialog(self):
        self. selected = SelectorPDF()
        self.file_path = self.selected.select_pdf_file()
        return self.file_path
        

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Termo de Adesão"))
        self.label_coverage.setText(_translate("MainWindow", "COBERTURAS / PLANO"))
        self.checkBox_monitoring.setText(_translate("MainWindow", "Monitoramento e Rastreamento"))
        self.checkBox_robbery.setText(_translate("MainWindow", "Roubo"))
        self.checkBox_theft.setText(_translate("MainWindow", "Furto"))
        self.checkBox_pt.setText(_translate("MainWindow", "Perda Total"))
        self.checkBox_collision.setText(_translate("MainWindow", "Colisão do Associado"))
        self.checkBox_winch3.setText(_translate("MainWindow", "3 Reboques Gratuitos a.a."))
        self.checkBox_winch6.setText(_translate("MainWindow", "6 Reboques Gratuitos a.a."))
        self.checkBox_unlimited_winch.setText(_translate("MainWindow", "Reboque Ilimitado"))
        self.checkBox_winch500.setText(_translate("MainWindow", "Quinhentos Quilômetros de Reboque"))
        self.checkBox_glasses.setText(_translate("MainWindow", "Vidros em Geral"))
        self.checkBox_others.setText(_translate("MainWindow", "Terceiros"))
        self.lineEdit_plain_type.setPlaceholderText(_translate("MainWindow", "PLANO"))
        self.label_clientdata.setText(_translate("MainWindow", "DADOS DO CLIENTE"))
        self.lineEdit_name.setPlaceholderText(_translate("MainWindow", "NOME"))
        self.lineEdit_rg_3.setPlaceholderText(_translate("MainWindow", "RG"))
        self.lineEdit_cpf.setPlaceholderText(_translate("MainWindow", "CPF"))
        self.lineEdit_birth.setPlaceholderText(_translate("MainWindow", "DATA DE NASCIMENTO"))
        self.lineEdit_nationality.setPlaceholderText(_translate("MainWindow", "NACIONALIDADE"))
        self.lineEdit_phone1.setPlaceholderText(_translate("MainWindow", "TELEFONE 1"))
        self.lineEdit_phone2.setPlaceholderText(_translate("MainWindow", "TELEFONE 2"))
        self.label_adress.setText(_translate("MainWindow", "ENDEREÇO"))
        self.lineEdit_street.setPlaceholderText(_translate("MainWindow", "RUA/AV"))
        self.lineEdit_number.setPlaceholderText(_translate("MainWindow", "NUMERO"))
        self.lineEdit_comp.setPlaceholderText(_translate("MainWindow", "COMPLEMENTO"))
        self.lineEdit_neghbordhood.setPlaceholderText(_translate("MainWindow", "BAIRRO"))
        self.lineEdit_city.setPlaceholderText(_translate("MainWindow", "CIDADE"))
        self.lineEdit_uf.setPlaceholderText(_translate("MainWindow", "UF"))
        self.lineEdit_cep.setPlaceholderText(_translate("MainWindow", "CEP"))
        self.label_vehicle.setText(_translate("MainWindow", "DADOS DO VEÍCULO"))
        self.lineEdit_assembler.setPlaceholderText(_translate("MainWindow", "MONTADORA"))
        self.lineEdit_model.setPlaceholderText(_translate("MainWindow", "MODELO"))
        self.lineEdit_plate.setPlaceholderText(_translate("MainWindow", "PLACA"))
        self.lineEdit_color.setPlaceholderText(_translate("MainWindow", "COR"))
        self.lineEdit_year.setPlaceholderText(_translate("MainWindow", "ANO"))
        self.lineEdit_chassis.setPlaceholderText(_translate("MainWindow", "CHASSI"))
        self.lineEdit_renavam.setPlaceholderText(_translate("MainWindow", "RENAVAM"))
        self.lineEdit_fipe_value.setPlaceholderText(_translate("MainWindow", "FALOR - FIPE"))
        self.lineEdit_fipe_code.setPlaceholderText(_translate("MainWindow", "COD - FIPE"))
        self.lineEdit_hora.setPlaceholderText(_translate("MainWindow", "HORARIO DE EVENTOS"))
        self.label_textArea.setText(_translate("MainWindow", "CONTRATO"))
        self.pushButton_insert_file.setText(_translate("MainWindow", "ADICIONAR CONTRATO (PDF)"))
        self.label_finance.setText(_translate("MainWindow", "FINANCEIRO"))
        self.lineEdit_monthly_payment.setPlaceholderText(_translate("MainWindow", "MENSALIDADE"))
        self.lineEdit_membership_fee.setPlaceholderText(_translate("MainWindow", "TAXA DE ADESÃO/CANCELAMENTO"))
        self.lineEdit_total_payment.setPlaceholderText(_translate("MainWindow", "PARCELA ÚNICA (PAGTO TOTAL DE PLANO)"))
        self.label_start.setText(_translate("MainWindow", "Plano válido de:"))
        self.label_finish.setText(_translate("MainWindow", "Até"))
        self.label_detail_recibo.setText(_translate("MainWindow", "Detalhamento para Recibo"))
        self.textEdit_detail_pagto_obs.setPlaceholderText(_translate("MainWindow", "OBSERVAÇÕES"))
        self.label_formapagto.setText(_translate("MainWindow", "Forma de Pagamento"))
        self.label_company_data.setText(_translate("MainWindow", "DADOS DA EMPRESA"))
        self.lineEdit_razao_social.setPlaceholderText(_translate("MainWindow", "RAZÃO SOCIAL"))
        self.lineEdit_cnpj.setPlaceholderText(_translate("MainWindow", "CNPJ"))
        self.pushButton_adhesion.setText(_translate("MainWindow", "Gerar Termo de Adesão"))
        self.actionGerar_termo_de_ades_o.setText(_translate("MainWindow", "Gerar termo de adesão"))
        self.actionNovo.setText(_translate("MainWindow", "Novo..."))
        self.actionSalvar.setText(_translate("MainWindow", "Salvar"))
        self.actionGerar_Termo_em_PDF.setText(_translate("MainWindow", "Gerar Termo em PDF"))
        self.actionImprimir_Termo.setText(_translate("MainWindow", "Imprimir Termo"))
        self.actionImprimir_Termo_2.setText(_translate("MainWindow", "Imprimir Termo"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_Adhesion_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
