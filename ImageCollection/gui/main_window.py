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

from gui.base.main_window_base import Ui_MainWindow
from gui.create_collection_widget import CreateCollection

import common_defs as cd
class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.gallery_path = ""

        self.connect_buttons()
        self.load_data()

        self.create_collection_widget = None



    def connect_buttons(self):
        self.actionOpen_Folder.triggered.connect(self.open_folder)
        self.actionNew_Collection.triggered.connect(self.create_collection)
        self.actionExit.triggered.connect(self.exit)

    def open_folder(self):
        folder = cd.OpenFolder(self)

    def create_collection(self):
        self.create_collection_widget = CreateCollection()
        self.create_collection_widget.show()

    def exit(self):
        QApplication.exit()

    def check_gallery(self):
        return True if os.path.exists(self.gallery_path) else False

    def load_data(self):
        con = cd.Funcs.create_connection("data")
        cur = con.cursor()
        collections = cur.execute(
            '''
            select * from collections
            '''
        ).fetchall()
        if len(collections) == 0:
            print("There's no collections yet. Chose your gallery and unsorted folders")
            self.gallery_path = cd.OpenFolder(self, "Chose gallery folder")
            unsorted = cd.OpenFolder(self, "Chose Unsorted folder")
            cd.Funcs.create_database("data", self.gallery_path, unsorted)
        else:
            for collection in collections:
                if collection[0] == "All":
                    self.gallery_path = collection[2]
                    break
            if self.gallery_path == "":
                os.remove("data.db")
                self.load_data()


