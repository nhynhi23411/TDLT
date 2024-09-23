from PyQt6.QtWidgets import QApplication, QMainWindow

from MainWindowFirstDegreeEquationEx import MainWindowFirstDegreeEquationEX

app=QApplication([])
myWindow= MainWindowFirstDegreeEquationEX()
myWindow.setupUi(QMainWindow())
myWindow.show()
app.exec()