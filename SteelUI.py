import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QFileDialog, QHBoxLayout, QTextEdit
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
import main
import output

# Removed the import main to avoid confusion, ensure to correctly import your processing logic

class SteelDefectDetector(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Steel Defect Detector')
        self.setGeometry(100, 100, 800, 600)
        self.initUI()

    def initUI(self):
        self.layout = QHBoxLayout()

        # Image display
        self.imageLabel = QLabel()
        self.imageLabel.setFixedSize(400, 500)
        self.imageLabel.setStyleSheet("background-color: white;")
        self.imageLabel.setAlignment(Qt.AlignCenter)
        self.imageLabel.setText('Upload an image of steel to start')

        # Defect data display
        self.defectDataText = QTextEdit()
        self.defectDataText.setReadOnly(True)
        self.defectDataText.setText('Defect details will appear here')


        # Upload button
        self.uploadButton = QPushButton('Upload Image')
        self.uploadButton.clicked.connect(self.uploadImage)

        # Detect button
        self.detectButton = QPushButton('Detect')
        self.detectButton.clicked.connect(self.detectDefects)  # Connecting to the slot that will handle detection

        self.layout.addWidget(self.imageLabel)
        self.layout.addWidget(self.defectDataText)
        self.layout.addWidget(self.uploadButton, alignment=Qt.AlignTop)
        self.layout.addWidget(self.detectButton, alignment=Qt.AlignTop)  # Adding the detect button to the layout

        self.setLayout(self.layout)

    def uploadImage(self):
        imagePath, _ = QFileDialog.getOpenFileName()
        global ret_text
        ret_text = main.process_image(imagePath)
        if imagePath:
            self.imagePath = imagePath  # Store the image path for later processing
            pixmap = QPixmap(imagePath)
            self.imageLabel.setPixmap(
                pixmap.scaled(self.imageLabel.width(), self.imageLabel.height(), Qt.KeepAspectRatio))

    def detectDefects(self):
        # Placeholder for your image processing logic
        # After processing, it should save the result as 'processed.png'
        # For the purpose of this example, let's assume 'processed.png' is already generated
        # and we just display it.

        # Here you would call your image processing function, e.g.,
        # processImage(self.imagePath) to generate 'processed.png'

        # Displaying the processed image
        self.defectDataText.setText('Defects: \n\n' + ret_text)
        processedPixmap = QPixmap('processed.png')

        self.imageLabel.setPixmap(
            processedPixmap.scaled(self.imageLabel.width(), self.imageLabel.height(), Qt.KeepAspectRatio))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setApplicationName('Steel Defect Detector')

    try:
        import qtmodern.styles
        import qtmodern.windows

        qtmodern.styles.dark(app)
    except ImportError:
        print("qtmodern is not installed. Proceeding with the default style.")

    mainWindow = SteelDefectDetector()

    try:
        mw = qtmodern.windows.ModernWindow(mainWindow)
        mw.show()
    except NameError:
        mainWindow.show()

    sys.exit(app.exec_())
