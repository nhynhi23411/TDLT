from MainWindow import Ui_MainWindow
from PyQt6 import QtWidgets, QtCore


class MainWindowEx(Ui_MainWindow):
    def __init__(self):
        pass

    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow = MainWindow

        # Connect buttons to respective functions
        self.pushButton_5.clicked.connect(self.SHBT)
        self.pushButtonHD.clicked.connect(self.HD)
        self.pushButtonKD.clicked.connect(self.KD)
        self.pushButtonSX.clicked.connect(self.SX)
        self.pushButtonTT.clicked.connect(self.TT)

    def SHBT(self):
        try:
            A = int(self.CulineEdit.text())  # Old meter reading
            B = int(self.MoilineEdit.text())  # New meter reading
            C = int(self.SoholineEdit.text())  # Number of households

            if A > B:
                self.label_7.setText("Error: Old meter reading must be less than the new meter reading!")
                return

            if C <= 0:
                self.label_7.setText("Error: Number of households must be greater than 0!")
                return

            consumption = (B - A) / C
            amount = 0

            if consumption <= 50:
                amount = consumption * 1484
            elif consumption <= 100:
                amount = (50 * 1484) + (consumption - 50) * 1533
            elif consumption <= 200:
                amount = (50 * 1484) + (50 * 1533) + (consumption - 100) * 1786
            elif consumption <= 300:
                amount = (50 * 1484) + (50 * 1533) + (100 * 1786) + (consumption - 200) * 2242
            elif consumption <= 400:
                amount = (50 * 1484) + (50 * 1533) + (100 * 1786) + (100 * 2242) + (consumption - 300) * 2503
            else:
                amount = (50 * 1484) + (50 * 1533) + (100 * 1786) + (100 * 2242) + (100 * 2503) + (
                            consumption - 400) * 2587

            self.label_7.setText(f"Amount to be paid: {amount:.0f} VND")
            self.DungineEdit.setText(str(B - A))  # Set the usage value correctly

        except ValueError:
            self.label_7.setText("Please enter valid numbers!")

    def KD(self):
        try:
            A = int(self.CulineEdit.text())
            B = int(self.MoilineEdit.text())
            if A > B:
                self.label_7.setText("Error: Old meter reading must be less than the new meter reading!")
                return
            amount = (B - A) * 2320
            self.label_7.setText(f"Amount to be paid: {amount:.0f} VND")
            self.DungineEdit.setText(str(B - A))  # Set the usage value
        except ValueError:
            self.label_7.setText("Please enter valid numbers!")

    def SX(self):
        try:
            A = int(self.CulineEdit.text())
            B = int(self.MoilineEdit.text())
            if A > B:
                self.label_7.setText("Error: Old meter reading must be less than the new meter reading!")
                return
            amount = (B - A) * 1518
            self.label_7.setText(f"Amount to be paid: {amount:.0f} VND")
            self.DungineEdit.setText(str(B - A))  # Set the usage value
        except ValueError:
            self.label_7.setText("Please enter valid numbers!")

    def TT(self):
        # Clear all inputs and labels
        self.CulineEdit.clear()
        self.MoilineEdit.clear()
        self.SoholineEdit.clear()
        self.DungineEdit.clear()
        self.label_7.clear()

        # Set focus back to old meter reading
        self.CulineEdit.setFocus()

    def HD(self):
        # Show information message
        QtWidgets.QMessageBox.information(self.MainWindow, "Guide",
                                          "This is an electricity bill calculation software, developed by: Yến Nhi")

    def show(self):
        self.MainWindow.show()

