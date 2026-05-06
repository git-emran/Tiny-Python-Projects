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
        self.button = QPushButton("Click Me")
        self.button.clicked.connect(self.the_button_was_clicked)

        self.setCentralWidget(self.button)

    def the_button_was_clicked(self):
        self.button.setText("I have been clicked too many Times!")
        self.button.setEnabled(False)

        self.setWindowTitle("My OneShot app")


app = QApplication(sys.argv)

winddow = MainWindow()
winddow.show()

app.exec()
