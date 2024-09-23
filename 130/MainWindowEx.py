from MainWindow import Ui_MainWindow
from PyQt6 import QtWidgets

class MainWindowEx(Ui_MainWindow):
    def __init__(self):
        super().__init__()

    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow = MainWindow

        # Connect buttons to respective functions
        self.pushButton.clicked.connect(self.TinhKH)
        self.pushButton_2.clicked.connect(self.ChiTiet)

    def TinhKH(self):
        try:
            # Get inputs from the UI
            price = float(self.lineEditNewPrice.text())  # Asset initial price
            transport_cost = float(self.lineEditShip.text())  # Transportation cost
            install_cost = float(self.lineEditLapDat.text())  # Installation cost
            years = int(self.lineEditYear.text())  # Number of depreciation years

            # Calculate asset's total value (price + transport + installation)
            total_value = price + transport_cost + install_cost

            # Calculate annual and monthly depreciation
            annual_depreciation = total_value / years
            monthly_depreciation = annual_depreciation / 12

            # Display results in the UI
            self.lineEditNguyenGia.setText(f"{total_value:.2f}")
            self.lineEditGiaMoiNam.setText(f"{annual_depreciation:.2f}")
            self.lineEditHangThang.setText(f"{monthly_depreciation:.2f}")

        except ValueError:
            self.label.setText("Please enter valid numeric values!")

    def ChiTiet(self):
        try:
            # Get inputs from the UI again (in case they have been changed)
            price = float(self.lineEditNewPrice.text())  # Asset initial price
            transport_cost = float(self.lineEditShip.text())  # Transportation cost
            install_cost = float(self.lineEditLapDat.text())  # Installation cost
            years = int(self.lineEditYear.text())  # Number of depreciation years

            # Calculate asset's total value (price + transport + installation)
            total_value = price + transport_cost + install_cost
            annual_depreciation = total_value / years
            accumulated_depreciation = 0

            # Prepare details of depreciation
            details = "Yearly Depreciation Details:\n"
            for year in range(1, years + 1):
                total_value -= annual_depreciation
                details += f"Year {year}: {total_value:.2f} VND\n"


            # Display the detailed depreciation breakdown
            self.labelchitiet.setText(details)

        except ValueError:
            self.labelchitiet.setText("Please enter valid numeric values!")

    def show(self):
        self.MainWindow.show()
