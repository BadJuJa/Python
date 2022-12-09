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

from gui.base.main_window_base import Ui_MainWindow
from gui.create_collection_widget import CreateCollection
#import settings
from sqlite3 import OperationalError

import common_defs as cd
class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.gallery_path = "C:/Users/Guren/Downloads/потом разберусь/Images/Gallery"

        self.connect_buttons()
        self.load_data()
        cd.Funcs.update_ui(self)

        self.create_collection_widget = None


    #def exit_p(self):
    #    self.exit()

    def connect_buttons(self):
        self.actionOpen_Folder.triggered.connect(self.open_folder)
        self.actionNew_Collection.triggered.connect(self.create_collection)
        self.actionExit.triggered.connect(self.exit)


    def open_folder(self):
        folder = cd.OpenFolder(self)

    def create_collection(self):
        self.create_collection_widget = CreateCollection(self.gallery_path, self)
        self.create_collection_widget.show()

    def exit(self):
        QApplication.exit()

    def check_gallery(self):
        return True if os.path.exists(self.gallery_path) else False

    def load_data(self):
        if not os.path.exists("data.db"):
            if self.gallery_path == "":
                self.gallery_path = cd.OpenFolder(self, "Chose gallery folder")
            cd.Funcs.create_database(self.gallery_path, self.gallery_path + '/unsorted')
            con = cd.Funcs.create_connection()
            con.execute("""select * from images""")
            con.close()
            time.sleep(1)
            self.load_data()
        else:
            con = cd.Funcs.create_connection()
            cur = con.cursor()
            try:
                collections = cur.execute('''select * from collections''').fetchall()
                image_list = self.fetch_image_list()
            except OperationalError:
                os.remove("data.db")
                self.load_data()
            else:
                pass

    def fetch_image_list(self):
        con = cd.Funcs.create_connection()
        fetch = con.cursor().execute('''select id from images''').fetchall()
        il = []
        il.extend([iid[0] for iid in fetch])
        return il

