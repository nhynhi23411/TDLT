from PyQt6.QtWidgets import QApplication, QDialog
from Helloword import Ui_MainWindow

app=QApplication([])
dialog=QDialog()
window = Ui_MainWindow()
window.setupUi(dialog)
dialog.show()
app.exec()