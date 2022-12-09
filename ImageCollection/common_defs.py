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
import sqlite3
from sqlite3 import Error
import csv


def OpenFolder(QWidget, title = "Open..."):
    folder = QFileDialog.getExistingDirectory(QWidget, title)
    return folder

class Funcs:
    @staticmethod
    def create_connection(name):
        connection = None
        try:
            connection = sqlite3.connect(f'{name}.db')
        except Error as e:
            print(f"The error '{e}' occurred")

        return connection
    @staticmethod
    def create_database(name, gallery_path, unsorted_path):
        con = Funcs.create_connection(name)
        cur = con.cursor()
        cur.execute(
            """
            CREATE TABLE IF NOT EXISTS collections (name STRING PRIMARY KEY UNIQUE, description TEXT, path STRING);
            """
        )
        cur.execute(f"""insert into collections values ("All", "All your images", "{gallery_path}");""")
        cur.execute(f"""insert into collections values ("Unsorted", "Your unsorted images", "{unsorted_path}");""")
        cur.execute(f"""CREATE TABLE images (name STRING PRIMARY KEY UNIQUE, path STRING UNIQUE, collection STRING REFERENCES collections (name))""")



        con.commit()
        con.close()



    @staticmethod
    def read_csv(path_to_file):
        _list = []
        with open(path_to_file, 'r', newline='') as csvFile:
            reader = csv.reader(csvFile)
            for song in reader:
                _list.append(song[0])
        return _list

    @staticmethod
    def write_csv(_slist, _path, _name):
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
    def scan_gallery():
        pass