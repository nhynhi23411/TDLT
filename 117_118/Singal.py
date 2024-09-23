from PyQt6 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(270, 20, 231, 61))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(270, 80, 231, 22))
        self.lineEdit.setObjectName("lineEdit")
        self.label_2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(270, 120, 231, 16))
        self.label_2.setObjectName("label_2")
        self.Change_color = QtWidgets.QPushButton(parent=self.centralwidget)
        self.Change_color.setGeometry(QtCore.QRect(270, 150, 93, 28))
        self.Change_color.setObjectName("Change_color")
        self.exit = QtWidgets.QPushButton(parent=self.centralwidget)
        self.exit.setGeometry(QtCore.QRect(410, 150, 93, 28))
        self.exit.setObjectName("exit")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.lineEdit.textChanged['QString'].connect(self.label_2.setText)  # type: ignore
        self.exit.clicked.connect(MainWindow.close)  # type: ignore
        self.Change_color.clicked.connect(self.changeBackground)  # Fix this connection
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.MainWindow = MainWindow

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Signals and Slots"))
        self.label_2.setText(_translate("MainWindow", "Color"))
        self.Change_color.setText(_translate("MainWindow", "Change_color"))
        self.exit.setText(_translate("MainWindow", "Exit"))

    # Correct background color change method
    def changeBackground(self):
        self.MainWindow.setStyleSheet("background-color: red;")

