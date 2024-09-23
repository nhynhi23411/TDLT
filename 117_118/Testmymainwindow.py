from PyQt6.QtWidgets import QApplication, QMainWindow
from Helloword import Ui_MainWindow
app=QApplication([])
mw=QMainWindow()
mywindow=Ui_MainWindow()
mywindow.setupUi(mw)
mw.show()
app.exec()
