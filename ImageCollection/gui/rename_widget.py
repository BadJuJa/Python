import sys
import os
import fnmatch
from pathlib import Path
import time

from PyQt5 import QtCore, QtGui
from PyQt5.QtCore import QUrl, QDirIterator
from PyQt5.QtMultimedia import QMediaPlaylist, QMediaPlayer, QMediaContent
from PyQt5.QtWidgets import (QMainWindow, QApplication, QTableWidgetItem,
                             QListWidgetItem, QPushButton, QWidget, QHBoxLayout,
                             QFileDialog, QMessageBox, QAction)

from gui.base.rename_base import Ui_Rename

import common_defs as cd


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

    def cancel(self):
        self.close()
