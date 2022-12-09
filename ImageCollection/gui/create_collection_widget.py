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

from gui.base.create_collection_base import Ui_CreateCollection
#import settings
import common_defs as cd

class CreateCollection(QWidget, Ui_CreateCollection):
    def __init__(self, gallery_path, mw):
        super(CreateCollection, self).__init__(None, QtCore.Qt.Window)
        self.setupUi(self)
        self.gp = gallery_path
        self.connect_buttons()
        self.mw = mw

    def connect_buttons(self):
        self.button_open_folder.clicked.connect(self.open_folder)
        self.buttonBox_ok_cancel.accepted.connect(self.create_collection)
        self.buttonBox_ok_cancel.rejected.connect(self.close)

    def open_folder(self):
        folder = cd.OpenFolder(self)
        self.lineEdit_path.setText(folder)

    def create_collection(self):
        if self.lineEdit_name.text() == "":
            self.lineEdit_name.setText("unnamed")

        if self.lineEdit_path.text() == "":
            self.lineEdit_path.setText(os.path.join(self.gp, self.lineEdit_name.text()))

        if not os.path.split(self.lineEdit_path.text())[1] == self.lineEdit_name.text():
            os.mkdir(os.path.join(self.lineEdit_path.text(), self.lineEdit_name.text()))

        con = cd.Funcs.create_connection()
        con.cursor().execute(f"""insert or REPLACE into collections values ("{self.lineEdit_name.text()}", "{self.lineEdit_description.text()}", "{self.lineEdit_path.text()}")""")
        cd.Funcs.db_create_collection(con.cursor(), self.lineEdit_name.text())

        cd.Funcs.create_action(self.mw.menuYour_collections, self.lineEdit_name.text(), lambda x: print(self.lineEdit_name.text()))

        con.commit()
        con.close()
        self.close()
