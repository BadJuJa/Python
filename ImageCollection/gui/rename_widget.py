from PyQt5.QtWidgets import (QWidget)
from PyQt5.Qt import Qt
from gui.base.rename_base import Ui_Rename


class RenameWidget(QWidget, Ui_Rename):
    def __init__(self, main_window):
        super().__init__()
        self.setupUi(self)
        self.main_window = main_window
        self.connect_buttons()

    def connect_buttons(self):
        self.button_ok.clicked.connect(self.ok)
        self.button_cancel.clicked.connect(self.cancel)

    def ok(self):
        new_name = self.lineEdit_name.text().strip()
        if new_name == '':
            new_name = 'unnamed'
        self.main_window.rename_image(new_name)
        self.close()
        self.releaseKeyboard()
        self.main_window.grabKeyboard()

    def cancel(self):
        self.close()
        self.releaseKeyboard()
        self.main_window.grabKeyboard()

    def keyPressEvent(self, e):
        if e.key() == Qt.Key_Enter:
            self.ok()
        if e.key() == Qt.Key_Escape:
            self.cancel()