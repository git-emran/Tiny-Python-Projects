import json
import os

from PyQt6 import uic
from PyQt6.QtCore import QAbstractListModel, Qt
from PyQt6.QtGui import QImage
from PyQt6.QtWidgets import QMainWindow


basedir = os.path.dirname(__file__)
ui_path = os.path.join(basedir, "mainwindow.ui")
db_path = os.path.join(basedir, "data.db")
icon_path = os.path.join(basedir, "tick.png")


MainWindowUI, _ = uic.loadUiType(ui_path)


class TodoModel(QAbstractListModel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.todos = self._load()
        self.tick = QImage(icon_path)

    def _load(self):
        try:
            with open("data.db", mode="r", encoding="utf-8") as todo_db:
                return json.load(todo_db)
        except FileNotFoundError:
            return []

    def data(self, index, role):
        if role == Qt.ItemDataRole.DisplayRole:
            _, text = self.todos[index.row()]
            return text

        if role == Qt.ItemDataRole.DecorationRole:
            status, _ = self.todos[index.row()]
            if status:
                return self.tick

    def rowCount(self, index):
        return len(self.todos)

    def add(self, todo_text):
        self.todos.append((False, todo_text))
        self._save()

    def _save(self):
        with open("data.db", mode="w", encoding="utf-8") as todo_db:
            json.dump(self.todos, todo_db)
        self.layoutChanged.emit()

    def delete(self, index):
        try:
            del self.todos[index]
        except IndexError:
            return
        self._save()

    def complete(self, index):
        try:
            self.todos[index] = (True, self.todos[index][1])
        except IndexError:
            return
        self._save()


class MainWindow(QMainWindow, MainWindowUI):
    def __init__(self):
        super().__init__()
        self.ui = MainWindowUI()
        self.ui.setupUi(self)
        self.model = TodoModel()
        self.ui.todoView.setModel(self.model)
        # Connect buttons to their respective methods
        self.ui.addButton.pressed.connect(self.add)
        self.ui.deleteButton.pressed.connect(self.delete)
        self.ui.completeButton.pressed.connect(self.complete)

    def add(self):
        if text := self.ui.todoEdit.text():
            self.model.add(text)
            self.ui.todoEdit.clear()

    def delete(self):
        if indexes := self.ui.todoView.selectedIndexes():
            index = indexes[0]
            self.model.delete(index.row())
            self.ui.todoView.clearSelection()

    def complete(self):
        if indexes := self.ui.todoView.selectedIndexes():
            index = indexes[0]
            self.model.complete(index.row())
            self.ui.todoView.clearSelection()
