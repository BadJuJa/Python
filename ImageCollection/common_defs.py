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
import sqlite3
from sqlite3 import Error
import csv


def OpenFolder(QWidget, title = "Open..."):
    folder = QFileDialog.getExistingDirectory(QWidget, title)
    return folder

class Funcs:
    @staticmethod
    def create_connection():
        connection = None
        try:
            connection = sqlite3.connect('data.db')
        except Error as e:
            print(f"The error '{e}' occurred")

        return connection
    @staticmethod
    def create_database(gallery_path, unsorted_path):
        con = Funcs.create_connection()
        cur = con.cursor()

        cur.execute("""CREATE TABLE IF NOT EXISTS collections (name STRING PRIMARY KEY UNIQUE, description TEXT, path STRING)""")
        cur.execute(
            f"""CREATE TABLE images (id INTEGER PRIMARY KEY ASC AUTOINCREMENT, name STRING, path STRING)""")

        Funcs.db_create_collection(cur, 'all')
        Funcs.db_create_collection(cur, 'unsorted')

        cur.execute(f"""insert into collections values ("all", "All your images", "{gallery_path}")""")
        cur.execute(f"""insert into collections values ("unsorted", "Your unsorted images", "{unsorted_path}")""")

        files_path = Funcs.scan_gallery(gallery_path)
        for img in files_path:
            name = img[img.rfind('\\')+1:]
            _path = img[:img.rfind('\\')]
            cur.execute(f"""insert into images values (NULL, "{name}", "{_path}")""")

        cur.execute(
            """insert into collection_all (name, path, iid) select name, path, id from images"""
        )
        cur.execute(
            """insert into collection_unsorted (name, path, iid) select name, path, id from images"""
        )

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
    def scan_gallery(g_path):
        import glob
        im_formats = ['png', 'jpg', 'jpeg']
        files_paths = []
        [files_paths.extend(glob.glob(g_path + '\**\*.' + e, recursive=True)) for e in im_formats]
        return files_paths

    @staticmethod
    def db_create_collection(cursor, collection_name):
        cursor.execute(
            f"""create table if not exists "collection_{collection_name}" (
            ciid INTEGER PRIMARY KEY AUTOINCREMENT, 
            name STRING, 
            path STRING, 
            iid INTEGER REFERENCES images(id))"""
        )

    @staticmethod
    def update_ui(main_window):
        con = Funcs.create_connection()
        fetch = con.cursor().execute(
            """ select name from collections where name not in ('all', 'unsorted') """).fetchall()
        collections = []
        collections.extend([col[0] for col in fetch])
        for collection in collections:
            Funcs.create_action(main_window.menuYour_collections, collection, lambda x: print(collection))

    @staticmethod
    def create_action(parent, name, func):
        action = QAction(parent)
        action.setText(name)
        action.setObjectName(f'action{name}')
        parent.addAction(action)
        parent.triggered.connect(func)