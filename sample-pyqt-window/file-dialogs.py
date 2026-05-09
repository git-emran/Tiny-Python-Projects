import sys

from PyQt6.QtWidgets import (
    QVBoxLayout,
    QApplication,
    QMainWindow,
    QPushButton,
    QWidget,
    QFileDialog,
)


FILE_FILTERS = [
    "Portable Network Graphics files (*.png)",
    "Text files (*.txt)",
    "Comma seperated values (*.csv)",
    "All files (*)",
]


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Emran's Dialog")

        layout = QVBoxLayout()

        button1 = QPushButton("Open File")
        button1.clicked.connect(self.get_filename)
        layout.addWidget(button1)

        button2 = QPushButton("Open Files")
        button2.clicked.connect(self.get_filenames)
        layout.addWidget(button2)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def get_filename(self):
        initial_filter = FILE_FILTERS[3]
        filters = ";;"
        print("Filters are:", filters)
        print("Initial filter:", initial_filter)

        filename, selected_filter = QFileDialog.getOpenFileName(
            self, filter=filters, initialFilter=initial_filter
        )

        print("Result:", filename, selected_filter)

    def get_filenames(self):
        caption = "Open Files"
        initial_dir = ""
        initial_filter = FILE_FILTERS[1]
        dialog = QFileDialog()
        dialog.setWindowTitle(caption)
        dialog.setDirectory(initial_dir)
        dialog.setNameFilters(FILE_FILTERS)
        dialog.selectNameFilter(initial_filter)
        dialog.setFileMode(QFileDialog.FileMode.ExistingFiles)

        ok = dialog.exec()
        print(
            "Result: ",
            ok,
            dialog.selectedFiles(),
            dialog.selectNameFilter(),
        )


app = QApplication(sys.argv)

window = MainWindow()
window.show()
app.exec()
