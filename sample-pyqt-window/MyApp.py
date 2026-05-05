import sys

from PyQt6.QtCore import QSize, Qt

from PyQt6.QtWidgets import (
    QApplication,
    QMainWindow,
    QPushButton,
)


class MainWindow(QMainWindow):
    def __init__(self):

        super().__init__()
        self.setWindowTitle("Emran Test")
        button = QPushButton("Click Now")

        self.setCentralWidget(button)


app = QApplication(sys.argv)

winddow = MainWindow()
winddow.show()

app.exec()
