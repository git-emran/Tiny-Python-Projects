import sys

from PyQt6.QtWidgets import (
    QApplication,
    QInputDialog,
    QMainWindow,
    QPushButton,
    QVBoxLayout,
    QWidget,
    QLineEdit,
)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()
        self.setWindowTitle("Emran's Dialog")

        button1 = QPushButton("Integer")
        button1.clicked.connect(self.get_an_int)
        layout.addWidget(button1)

        button2 = QPushButton("Float")
        button2.clicked.connect(self.get_a_float)
        layout.addWidget(button2)

        button3 = QPushButton("Select")
        button3.clicked.connect(self.get_a_str_from_a_list)
        layout.addWidget(button3)

        button4 = QPushButton("String")
        button4.clicked.connect(self.get_a_str)
        layout.addWidget(button4)

        button5 = QPushButton("Text")
        button5.clicked.connect(self.get_a_txt)
        layout.addWidget(button5)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def get_an_int(self):
        my_int_value, ok = QInputDialog.getInt(self, "Get an Int", "Enter a number")
        print("Result", ok, my_int_value)

    def get_a_float(self):
        title = "Enter a float"
        label = "Type your float here"

        my_float_value, ok = QInputDialog.getDouble(
            self, title, label, value=0, min=5.3, max=5.7, decimals=2
        )
        print("Result:", ok, my_float_value)

    def get_a_str_from_a_list(self):
        title = "Select a String"
        label = "Select a fruit from the list"
        items = ["apple", "pear", "orange", "grape"]
        inital_selection = 2
        my_selected_str, ok = QInputDialog.getItem(
            self, title, label, items, current=inital_selection, editable=False
        )
        print("Result:", ok, my_selected_str)

    def get_a_str(self):
        title = "Enter a string"
        label = "Type your password"
        text = "My secret password"
        mode = QLineEdit.EchoMode.Password
        my_selected_str, ok = QInputDialog.getText(self, title, label, mode, text)
        print("Result:", ok, my_selected_str)

    def get_a_txt(self):
        title = "Enter Text"
        label = "Type your novel here"
        text = "Once Upon a time..."

        my_selected_str, ok = QInputDialog.getMultiLineText(self, title, label, text)
        print("Result:", ok, my_selected_str)


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
