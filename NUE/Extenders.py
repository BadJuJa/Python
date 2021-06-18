import os

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import (QMainWindow, QApplication, QTableWidgetItem,
                             QListWidgetItem, QPushButton, QWidget, QHBoxLayout)

import sqlite3
from sqlite3 import Error
import csv
from pathlib import Path

class PlaylistWidget(QWidget):
    def __init__(self, _playlist_name, _song_list, parent=None):
        super(PlaylistWidget, self).__init__(parent)

        self.name = _playlist_name
        self.songlist = _song_list

        self.setupUI()
        self.load_table()

    def setupUI(self):
            self.verticalLayout_1 = QtWidgets.QVBoxLayout(self)
            self.verticalLayout_1.setSpacing(0)
            self.verticalLayout_1.setObjectName("verticalLayout_1")

            self.playlist_model_info_frame = QtWidgets.QFrame(self)
            self.playlist_model_info_frame.setMinimumSize(QtCore.QSize(0, 60))
            self.playlist_model_info_frame.setMaximumSize(QtCore.QSize(16777215, 64))
            self.playlist_model_info_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
            self.playlist_model_info_frame.setFrameShadow(QtWidgets.QFrame.Raised)
            self.playlist_model_info_frame.setObjectName("playlist_model_info_frame")

            self.horizontalLayout_1 = QtWidgets.QHBoxLayout(self.playlist_model_info_frame)
            self.horizontalLayout_1.setContentsMargins(0, 0, 0, 0)
            self.horizontalLayout_1.setSpacing(0)
            self.horizontalLayout_1.setObjectName("horizontalLayout_1")

            self.playlist_name_lable = QtWidgets.QLabel(self.playlist_model_info_frame)
            self.playlist_name_lable.setScaledContents(True)
            self.playlist_name_lable.setObjectName("playlist_name_lable")

            self.horizontalLayout_1.addWidget(self.playlist_name_lable)

            self.playlist_info_time_frame = QtWidgets.QFrame(self.playlist_model_info_frame)
            self.playlist_info_time_frame.setMaximumSize(QtCore.QSize(200, 16777215))
            self.playlist_info_time_frame.setFrameShape(QtWidgets.QFrame.NoFrame)
            self.playlist_info_time_frame.setFrameShadow(QtWidgets.QFrame.Raised)
            self.playlist_info_time_frame.setObjectName("playlist_info_time_frame")

            self.gridLayout = QtWidgets.QGridLayout(self.playlist_info_time_frame)
            self.gridLayout.setContentsMargins(0, 0, 0, 0)
            self.gridLayout.setSpacing(0)
            self.gridLayout.setObjectName("gridLayout")

            self.songscount_lable = QtWidgets.QLabel(self.playlist_info_time_frame)
            self.songscount_lable.setObjectName("songscount_lable")

            self.gridLayout.addWidget(self.songscount_lable, 0, 0, 1, 1)

            self.songscount_lableChange = QtWidgets.QLabel(self.playlist_info_time_frame)
            self.songscount_lableChange.setText("")
            self.songscount_lableChange.setObjectName("songscount_lableChange")

            self.gridLayout.addWidget(self.songscount_lableChange, 0, 1, 1, 1)
            self.horizontalLayout_1.addWidget(self.playlist_info_time_frame)
            self.verticalLayout_1.addWidget(self.playlist_model_info_frame)

            self.playlist_model_content_frame = QtWidgets.QFrame(self)
            self.playlist_model_content_frame.setFrameShape(QtWidgets.QFrame.NoFrame)
            self.playlist_model_content_frame.setFrameShadow(QtWidgets.QFrame.Raised)
            self.playlist_model_content_frame.setObjectName("playlist_model_content_frame")

            self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.playlist_model_content_frame)
            self.verticalLayout_2.setContentsMargins(0, 0, 0, -1)
            self.verticalLayout_2.setSpacing(0)
            self.verticalLayout_2.setObjectName("verticalLayout_2")

            self.playlist_model_buttons_frame = QtWidgets.QFrame(self.playlist_model_content_frame)
            self.playlist_model_buttons_frame.setMinimumSize(QtCore.QSize(0, 25))
            self.playlist_model_buttons_frame.setMaximumSize(QtCore.QSize(16777215, 45))
            self.playlist_model_buttons_frame.setFrameShape(QtWidgets.QFrame.NoFrame)
            self.playlist_model_buttons_frame.setFrameShadow(QtWidgets.QFrame.Raised)
            self.playlist_model_buttons_frame.setObjectName("playlist_model_buttons_frame")

            self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.playlist_model_buttons_frame)
            self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
            self.horizontalLayout_2.setSpacing(0)
            self.horizontalLayout_2.setObjectName("horizontalLayout_2")

            self.btn_playlist_play = QtWidgets.QPushButton(self.playlist_model_buttons_frame)
            self.btn_playlist_play.setMinimumSize(QtCore.QSize(100, 40))
            self.btn_playlist_play.setObjectName("btn_playlist_play")

            self.horizontalLayout_2.addWidget(self.btn_playlist_play)

            spacerItem1 = QtWidgets.QSpacerItem(858, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)

            self.horizontalLayout_2.addItem(spacerItem1)

            self.btn_playlist_shuffle = QtWidgets.QPushButton(self.playlist_model_buttons_frame)
            self.btn_playlist_shuffle.setMinimumSize(QtCore.QSize(100, 40))
            self.btn_playlist_shuffle.setObjectName("btn_playlist_shuffle")

            self.horizontalLayout_2.addWidget(self.btn_playlist_shuffle)
            self.verticalLayout_2.addWidget(self.playlist_model_buttons_frame)

            self.playlist_model_songlist_frame = QtWidgets.QFrame(self.playlist_model_content_frame)
            self.playlist_model_songlist_frame.setFrameShape(QtWidgets.QFrame.NoFrame)
            self.playlist_model_songlist_frame.setFrameShadow(QtWidgets.QFrame.Raised)
            self.playlist_model_songlist_frame.setObjectName("playlist_model_songlist_frame")

            self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.playlist_model_songlist_frame)
            self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
            self.horizontalLayout_3.setSpacing(0)
            self.horizontalLayout_3.setObjectName("horizontalLayout_3")

            self.Songlist_table = QtWidgets.QTableWidget(self.playlist_model_songlist_frame)
            self.Songlist_table.setObjectName("Songlist_table")
            self.Songlist_table.setColumnCount(2)
            self.Songlist_table.setRowCount(0)

            item = QtWidgets.QTableWidgetItem()
            self.Songlist_table.setHorizontalHeaderItem(0, item)
            item = QtWidgets.QTableWidgetItem()
            self.Songlist_table.setHorizontalHeaderItem(1, item)
            self.horizontalLayout_3.addWidget(self.Songlist_table)

            self.verticalLayout_2.addWidget(self.playlist_model_songlist_frame)
            self.verticalLayout_1.addWidget(self.playlist_model_content_frame)

            _translate = QtCore.QCoreApplication.translate
            self.playlist_name_lable.setText(_translate("MainWindow", f"{self.name}"))
            self.songscount_lable.setText(_translate("MainWindow", "Songs count:"))
            self.btn_playlist_play.setText(_translate("MainWindow", "Play"))
            self.btn_playlist_shuffle.setText(_translate("MainWindow", "Shuffle"))
            item = self.Songlist_table.horizontalHeaderItem(0)
            item.setText(_translate("MainWindow", "Name"))
            item = self.Songlist_table.horizontalHeaderItem(1)
            item.setText(_translate("MainWindow", "Author"))

    def load_table(self):
        self.Songlist_table.setRowCount(len(self.songlist))
        for i, elem in enumerate(self.songlist):
            for j, val in enumerate(elem):
                self.Songlist_table.setItem(i, j, QTableWidgetItem(str(val)))


class NewPlaylistButton(QPushButton):
    def __init__(self, name, parent=None):
        super(NewPlaylistButton, self).__init__(parent)
        self.setText(f"{name}")


class NewStackedWidgetWidget(QWidget):
    def __init__(self, parent=None):
        super(NewStackedWidgetWidget, self).__init__(parent)

        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")


class Funcs:
    @staticmethod
    def create_connection():
        connection = None
        try:
            connection = sqlite3.connect('Data.db')
        except Error as e:
            print(f"The error '{e}' occurred")

        return connection

    @staticmethod
    def read_from_file(path_to_file):
        _list = []
        with open(path_to_file, 'r', newline='') as csvFile:
            reader = csv.reader(csvFile)
            for song in reader:
                _list.append(song[0])
        return _list

    @staticmethod
    def write_to_file(_slist, _path, _name):
        if _name == "":
            return

        list_to_write = _slist
        path = _path + _name + ".csv"
        with open(path, 'w', newline='') as f:
            writer = csv.writer(f)
            for item in list_to_write:
                writer.writerow([item])

        return path

    @staticmethod
    def delete_from_path(path):
        os.remove(path)