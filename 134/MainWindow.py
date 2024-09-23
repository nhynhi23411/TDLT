# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created by: PyQt6 UI code generator 6.7.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(parent=self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(30, 30, 581, 161))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.groupBox.setFont(font)
        self.groupBox.setStyleSheet("background-color:rgb(255, 0, 0)")
        self.groupBox.setObjectName("groupBox")
        self.label = QtWidgets.QLabel(parent=self.groupBox)
        self.label.setGeometry(QtCore.QRect(20, 30, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.lineEditFullname = QtWidgets.QLineEdit(parent=self.groupBox)
        self.lineEditFullname.setGeometry(QtCore.QRect(110, 30, 271, 21))
        self.lineEditFullname.setObjectName("lineEditFullname")
        self.lineEditEmail = QtWidgets.QLineEdit(parent=self.groupBox)
        self.lineEditEmail.setGeometry(QtCore.QRect(110, 60, 271, 21))
        self.lineEditEmail.setObjectName("lineEditEmail")
        self.label_2 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(20, 60, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(20, 100, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.radWomen = QtWidgets.QRadioButton(parent=self.groupBox)
        self.radWomen.setGeometry(QtCore.QRect(110, 100, 95, 20))
        self.radWomen.setChecked(True)
        self.radWomen.setObjectName("radWomen")
        self.radMan = QtWidgets.QRadioButton(parent=self.groupBox)
        self.radMan.setGeometry(QtCore.QRect(230, 100, 95, 20))
        self.radMan.setObjectName("radMan")
        self.groupBox_2 = QtWidgets.QGroupBox(parent=self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(30, 220, 581, 161))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.groupBox_2.setObjectName("groupBox_2")
        self.lineEditAdress = QtWidgets.QLineEdit(parent=self.groupBox_2)
        self.lineEditAdress.setGeometry(QtCore.QRect(110, 30, 271, 21))
        self.lineEditAdress.setObjectName("lineEditAdress")
        self.label_7 = QtWidgets.QLabel(parent=self.groupBox_2)
        self.label_7.setGeometry(QtCore.QRect(20, 30, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(parent=self.groupBox_2)
        self.label_8.setGeometry(QtCore.QRect(20, 60, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.radBachelor = QtWidgets.QRadioButton(parent=self.groupBox_2)
        self.radBachelor.setGeometry(QtCore.QRect(130, 60, 95, 20))
        self.radBachelor.setObjectName("radBachelor")
        self.radMaster = QtWidgets.QRadioButton(parent=self.groupBox_2)
        self.radMaster.setGeometry(QtCore.QRect(130, 90, 95, 20))
        self.radMaster.setObjectName("radMaster")
        self.radDoctoral = QtWidgets.QRadioButton(parent=self.groupBox_2)
        self.radDoctoral.setGeometry(QtCore.QRect(130, 120, 95, 20))
        self.radDoctoral.setChecked(True)
        self.radDoctoral.setObjectName("radDoctoral")
        self.pushButtonSendData = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButtonSendData.setGeometry(QtCore.QRect(200, 390, 201, 51))
        self.pushButtonSendData.setObjectName("pushButtonSendData")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox.setTitle(_translate("MainWindow", "Personal Information"))
        self.label.setText(_translate("MainWindow", "Full Name:"))
        self.label_2.setText(_translate("MainWindow", "Email"))
        self.label_3.setText(_translate("MainWindow", "Gender"))
        self.radWomen.setText(_translate("MainWindow", "Woman"))
        self.radMan.setText(_translate("MainWindow", "Man"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Other Information"))
        self.label_7.setText(_translate("MainWindow", "Address"))
        self.label_8.setText(_translate("MainWindow", "Education"))
        self.radBachelor.setText(_translate("MainWindow", "Bachelor"))
        self.radMaster.setText(_translate("MainWindow", "Master"))
        self.radDoctoral.setText(_translate("MainWindow", "Doctoral"))
        self.pushButtonSendData.setText(_translate("MainWindow", "Send Data"))
