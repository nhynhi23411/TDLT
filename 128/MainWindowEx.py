from MainWindow import Ui_MainWindow


class MainWindowEx(Ui_MainWindow):
    def __init__(self):
        pass
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow=MainWindow
        self.pushButton.clicked.connect(self.convert)
    def convert(self):
        f = float(self.lineEditF.text())
        c = (f-32)/1.8
        self.labelC.setText(str(c))

    def show(self):
        self.MainWindow.show()