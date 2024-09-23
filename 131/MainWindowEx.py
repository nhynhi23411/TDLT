from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QMessageBox

from MainWindow import Ui_MainWindow


class MainWindowEx(Ui_MainWindow):
    def __init__(self):
        pass
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow=MainWindow
        self.pushButtonSubmit.clicked.connect(self.processSubmit)
    def show(self):
        self.MainWindow.show()
    def processSubmit(self):
        str=[]
        if self.checkML.isChecked()==True:
            str.append(self.checkML.text())
        if self.checkSC.isChecked()==True:
            str.append(self.checkSC.text())
        if self.checkBox_3.isChecked()==True:
            str.append(self.heckBox_3.text())
        separator=','
        infor="Full Name = "+self.lineEditFullname.text()+"\n"
        infor+="Email = "+self.lineEditMail.text()+"\n"
        infor+="Selected courses:"+"\n"
        infor+=separator.join(str)
        self.msg=QMessageBox()
        self.msg.setWindowTitle("Selected Courses")
        self.msg.setText(infor)

        self.msg.show()