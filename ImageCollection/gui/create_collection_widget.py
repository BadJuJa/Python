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
                             QFileDialog, QMessageBox)

from gui.base.create_collection_base import Ui_CreateCollection
import common_defs as cd

class CreateCollection(QWidget, Ui_CreateCollection):
    def __init__(self):
        super(CreateCollection, self).__init__(None, QtCore.Qt.Window)
        self.setupUi(self)

        self.connect_buttons()

    def connect_buttons(self):
        self.button_open_folder.clicked.connect(self.open_folder)
        self.buttonBox_ok_cancel.accepted.connect(self.create_collection)
        self.buttonBox_ok_cancel.rejected.connect(self.close)

    def open_folder(self):
        folder = cd.OpenFolder(self)
        self.lineEdit_path.setText(folder)

    def create_collection(self):
        con = cd.Funcs.create_connection("data")
        con.cursor().execute(f""" insert into collections values ("{self.lineEdit_name.text()}", "{self.lineEdit_description.text()}", "{self.lineEdit_path.text()}")""")
        con.commit()
        con.close()
        self.close()
