from MainWindow import Ui_MainWindow

class MainWindowEx(Ui_MainWindow):
    def __init__(self):
        pass

    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow = MainWindow
        self.pushButton.clicked.connect(self.convert)

    def convert(self):
        # Lấy giá trị từ người dùng
        try:
            year = int(self.lineEditF.text())  # year là năm dương lịch
        except ValueError:
            self.labelResult.setText("Vui lòng nhập một số nguyên hợp lệ!")
            return

        # Mảng Thiên Can
        can = ["Canh", "Tân", "Nhâm", "Quý", "Giáp", "Ất", "Bính", "Đinh", "Mậu", "Kỷ"]

        # Mảng Địa Chi
        chi = ["Thân", "Dậu", "Tuất", "Hợi", "Tý", "Sửu", "Dần", "Mão", "Thìn", "Tỵ", "Ngọ", "Mùi"]

        # Tính toán Thiên Can và Địa Chi
        can_index = year % 10  # Lấy Thiên Can
        chi_index = year % 12  # Lấy Địa Chi

        lunar_year = f"{can[can_index]} {chi[chi_index]}"

        # Hiển thị kết quả
        self.labelC.setText(f"{lunar_year}")

    def show(self):
        self.MainWindow.show()
