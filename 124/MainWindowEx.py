from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPixmap, QMovie
from MainWindow import Ui_MainWindow


class MainWindowEx(Ui_MainWindow):
    def __init__(self):
        super().__init__()  # Call the parent constructor

    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow = MainWindow

        # Connect buttons to their respective slots
        self.ChangetextpushButton.clicked.connect(self.processChangeText)
        self.FontsizepushButton.clicked.connect(self.processChangeFontSize)
        self.AlignLeftPushButton.clicked.connect(self.processAlignLeft)
        self.AlignCenterPushButton.clicked.connect(self.processAlignCenter)
        self.AlignRightPushButton.clicked.connect(self.processAlignRight)
        self.ShowPNGpushButton.clicked.connect(self.processChangePNG)
        self.ShowGIFpushButton.clicked.connect(self.processChangeGIF)

    def show(self):
        self.MainWindow.show()

    def processChangeText(self):
        self.titlelabel.setText("https://tranduythanh.com")

    def processChangeFontSize(self):
        # Get the font object
        font = self.titlelabel.font()
        # Change font properties
        font.setPointSize(20)
        font.setItalic(True)
        font.setBold(True)
        font.setFamily("Cambria")  # Corrected capitalization
        # Re-assign the modified font
        self.titlelabel.setFont(font)

    def processAlignLeft(self):
        self.titlelabel.setAlignment(Qt.AlignmentFlag.AlignLeft)

    def processAlignCenter(self):
        self.titlelabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

    def processAlignRight(self):
        self.titlelabel.setAlignment(Qt.AlignmentFlag.AlignRight)

    def processChangePNG(self):
        # Create a QPixmap instance
        pixmap = QPixmap("Image/picture.jpg")  # Ensure the path is correct
        # Set the pixmap for the label
        self.imagelabel.setPixmap(pixmap)

    def processChangeGIF(self):
        # Create a QMovie instance
        movie = QMovie("Image/bird.gif")  # Ensure the path is correct
        # Set the movie object for the label
        self.imagelabel.setMovie(movie)
        # Start the movie
        movie.start()
