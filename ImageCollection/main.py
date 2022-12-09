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

from gui.main_window import MainWindow
def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()