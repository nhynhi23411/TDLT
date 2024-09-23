from PyQt6.QtWidgets import QMessageBox, QMainWindow
from MyQMainWindow import Ui_MainWindow
from SecondWindow import SecondWindow
import webbrowser

class MyQMainWindowExt(Ui_MainWindow):
    # Override setupUi to define MainWindow attribute for reuse
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow = MainWindow
        self.secondWindow = None
        self.processSignalAndSlot()  # Ensure signals and slots are connected

    # Define methods for assigning Signals and Slots
    def processSignalAndSlot(self):
        self.push_exit.clicked.connect(self.processExit)
        self.push_visit.clicked.connect(self.openMyBlog)
        self.push_sent.clicked.connect(self.openSecondWindow)

    # Define slot to exit window
    def processExit(self):
        dlg = QMessageBox(self.MainWindow)
        dlg.setWindowTitle("Exit Confirmation")
        dlg.setText("Are you sure you want to Exit?")
        dlg.setStandardButtons(
            QMessageBox.StandardButton.Yes
            | QMessageBox.StandardButton.No
        )
        dlg.setIcon(QMessageBox.Icon.Question)
        button = dlg.exec()
        button = QMessageBox.StandardButton(button)
        if button == QMessageBox.StandardButton.Yes:
            self.MainWindow.close()

    def openMyBlog(self):
        try:
            webbrowser.open('https://tranduythanh.com/')
        except Exception as e:
            QMessageBox.critical(self.MainWindow, "Error", f"Failed to open browser: {str(e)}")

    def openSecondWindow(self):
        if self.secondWindow is None or not self.qmainWindow.isVisible():
            self.qmainWindow = QMainWindow()  # Ensure QMainWindow is initialized
            self.secondWindow = SecondWindow(self)
            self.secondWindow.setupUi(self.qmainWindow)
            self.qmainWindow.show()

    def changeRedColor(self):
        self.MainWindow.setStyleSheet("background-color: red;")

    def changeYellowColor(self):
        self.MainWindow.setStyleSheet("background-color: yellow;")
