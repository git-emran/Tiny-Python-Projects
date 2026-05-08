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
        dialog = QInputDialog(self)
        dialog.setWindowTitle("Enter an Integer")
        dialog.setLabelText("Type your Integer here")
        dialog.setIntValue(0)
        dialog.setIntMinimum(-5)
        dialog.setIntMaximum(5)
        dialog.setIntStep(1)
        ok = dialog.exec()
        print("Result:", ok, dialog.intValue())

    def get_a_float(self):
        dialog = QInputDialog(self)
        dialog.setWindowTitle("Enter a Float")
        dialog.setLabelText("Type your float here")
        dialog.setDoubleValue(0.1)
        dialog.setDoubleMinimum(-5.3)
        dialog.setDoubleMaximum(5.7)
        dialog.setDoubleStep(1.4)
        dialog.setDoubleDecimals(2)
        ok = dialog.exec()
        print("Result:", ok, dialog.doubleValue())

    def get_a_str_from_a_list(self):
        dialog = QInputDialog(self)
        dialog.setWindowTitle("Select a string")
        dialog.setLabelText("Select a Fruit from the list")
        dialog.setComboBoxItems(["apple", "pear", "orange", "grape"])
        dialog.setComboBoxEditable(False)
        dialog.setTextValue("orange")
        ok = dialog.exec()
        print("Result:", ok, dialog.textValue())

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
