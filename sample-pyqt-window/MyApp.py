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
        self.button_was_checked = True

        self.setWindowTitle("Emran Test")

        self.button = QPushButton("Click Now")
        self.button.setCheckable(True)
        self.button.released.connect(self.the_button_was_released)
        self.button.setChecked(self.button_was_checked)

        self.setCentralWidget(self.button)

    def the_button_was_released(self):
        self.button_was_checked = self.button.isChecked()
        print(self.button_was_checked)


app = QApplication(sys.argv)

winddow = MainWindow()
winddow.show()

app.exec()
