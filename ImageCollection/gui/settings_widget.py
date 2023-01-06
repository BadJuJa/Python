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

from gui.base.settings_base import Ui_Settings

import common_defs as cd


class SettingsWidget(QWidget, Ui_Settings):
    def __init__(self, main_window_settings):
        super().__init__()
        self.setupUi(self)
        self.connect_buttons()
        self.settings = main_window_settings
        self.paths = self.settings.get_and_validate_settings()
        self.prepare_widget()

    def connect_buttons(self):
        self.button_open_art.clicked.connect(lambda: self.change_path(self.lineEdit_art))
        self.button_open_erotic.clicked.connect(lambda: self.change_path(self.lineEdit_erotic))
        self.button_open_porn.clicked.connect(lambda: self.change_path(self.lineEdit_porn))
        self.button_save.clicked.connect(self.save)

    def change_path(self, line_edit):
        line_edit.setText(cd.open_folder(self))

    def save(self):
        self.prepare_art_path()
        self.prepare_ero_path()
        self.prepare_porn_path()

        self.settings.rewrite_settings(self.paths)
        self.close()

    def prepare_widget(self):
        self.lineEdit_art.setText(self.paths['art_path'])
        self.lineEdit_erotic.setText(self.paths['ero_path'])
        self.lineEdit_porn.setText(self.paths['porn_path'])

    def prepare_art_path(self):
        _art = self.lineEdit_art.text().strip()
        if _art != self.paths['art_path']:
            if not os.path.isdir(_art):
                os.makedirs(_art)
                self.paths['art_path'] = _art
        else:
            if _art == '':
                new_art_path = os.path.join(os.path.abspath('.'), 'Images', 'art')
                if not os.path.exists(new_art_path):
                    os.makedirs(new_art_path)
                self.paths['art_path'] = new_art_path

    def prepare_ero_path(self):
        _ero = self.lineEdit_erotic.text().strip()
        if _ero != self.paths['ero_path']:
            if not os.path.isdir(_ero):
                os.makedirs(_ero)
            self.paths['ero_path'] = _ero
        else:
            if _ero == '':
                new_ero_path = os.path.join(os.path.abspath('.'), 'Images', 'erotic')
                if not os.path.exists(new_ero_path):
                    os.makedirs(new_ero_path)
                self.paths['ero_path'] = new_ero_path

    def prepare_porn_path(self):
        _porn = self.lineEdit_porn.text().strip()
        if _porn != self.paths['porn_path']:
            if not os.path.isdir(_porn):
                os.makedirs(_porn)
            self.paths['porn_path'] = _porn
        else:
            if _porn == '':
                new_porn_path = os.path.join(os.path.abspath('.'), 'Images', 'porn')
                if not os.path.exists(new_porn_path):
                    os.makedirs(new_porn_path)
                self.paths['porn_path'] = new_porn_path

    def closeEvent(self, event):
        self.save()