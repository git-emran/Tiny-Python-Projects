import sys

from PyQt6.QtWidgets import QApplication, QInputDialog, QMainWindow, QPushButton


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Emran's Dialog")

        button1 = QPushButton("Click")
        button1.clicked.connect(self.get_an_int)

        self.setCentralWidget(button1)

    def get_an_int(self):
        my_int_value, ok = QInputDialog.getInt(self, "Get an Int", "Enter a number")
        print("Result", ok, my_int_value)


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
