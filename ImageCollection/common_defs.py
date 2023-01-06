import sys
import os
import fnmatch
from pathlib import Path
import time
import glob
from PyQt5 import QtCore, QtGui
from PyQt5.QtCore import QUrl, QDirIterator
from PyQt5.QtMultimedia import QMediaPlaylist, QMediaPlayer, QMediaContent
from PyQt5.QtWidgets import (QMainWindow, QApplication, QTableWidgetItem,
                             QListWidgetItem, QPushButton, QWidget, QHBoxLayout,
                             QFileDialog, QMessageBox, QAction)
import sqlite3
from sqlite3 import Error
import csv
import json


def open_folder(parent=None, title="Open..."):
    folder = QFileDialog.getExistingDirectory(parent, title, os.getcwd())
    if folder == "":
        folder = os.getcwd()
    return folder


def scan_folder(path):
    im_formats = ['png', 'jpg', 'jpeg']
    files_paths = []
    [files_paths.extend(glob.glob(path + '\**\*.' + e, recursive=True)) for e in im_formats]
    return files_paths
