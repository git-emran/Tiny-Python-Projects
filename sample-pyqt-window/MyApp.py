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
        self.button_was_checked = True

        button = QPushButton("Click Now")
        button.setCheckable(True)
        button.clicked.connect(self.button_was_toggled)
        button.setChecked(self.button_was_checked)

        self.setCentralWidget(button)

    def button_was_toggled(self, checked):
        self.button_was_checked = checked
        print(self.button_was_checked)


app = QApplication(sys.argv)

winddow = MainWindow()
winddow.show()

app.exec()
