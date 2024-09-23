from MainWindowFirstDegreeEquation import Ui_MainWindow


class MainWindowFirstDegreeEquationEX(Ui_MainWindow):
    def __init__(self):
        self.pushButtonExit = None
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow=MainWindow
        self.MainWindow.setWindowTitle("Nhynhi")
        self.pushButtonExit.clicked.connect(self.process_exit)
        self.pushButtonClear.clicked.connect(self.process_clear)
        self.pushButtonSolution.clicked.connect(self.process_solution)
    def process_solution(self):
        a = float(self.lineEditInputA.text())
        b = float(self.lineEditInputB.text())
        if a==0 and b ==0:
            self.lineEditSolution.setText("Infinities solutions")
        elif a==0 and b!=0:
            self.lineEditSolution.setText("No solution")
        else:
            self.lineEditSolution.setText("X="+str(-b/a))
    def process_clear(self):
        self.lineEditInputA.setText("")
        self.lineEditInputB.setText("")
        self.lineEditSolution.setText("")
        self.lineEditInputA.setFocus()
    def process_exit(self):
        self.MainWindow.close()
    def show(self):
        self.MainWindow.show()