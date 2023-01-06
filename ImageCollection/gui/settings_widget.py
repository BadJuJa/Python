import os

from PyQt5.QtWidgets import (QWidget)

import common_defs as cd
from gui.base.settings_base import Ui_Settings


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
        self.prepare_path(self.lineEdit_art, 'art_path')
        self.prepare_path(self.lineEdit_erotic, 'ero_path')
        self.prepare_path(self.lineEdit_porn, 'porn_path')
        self.prepare_path(self.lineEdit_trash, 'bin_path')

        self.settings.rewrite_settings(self.paths)
        self.close()

    def prepare_widget(self):
        self.lineEdit_art.setText(self.paths['art_path'])
        self.lineEdit_erotic.setText(self.paths['ero_path'])
        self.lineEdit_porn.setText(self.paths['porn_path'])
        self.lineEdit_trash.setText(self.paths['bin_path'])

    def prepare_path(self, line_edit, paths_key):
        lE = line_edit.text().strip()
        if lE != self.paths[paths_key]:
            if not os.path.isdir(lE):
                os.makedirs(lE)
            self.paths[paths_key] = lE
        else:
            if lE == '':
                new_folder_path = os.path.join(os.path.abspath('.'), 'Images', self.get_folder_name(paths_key))
                if not os.path.exists(new_folder_path):
                    os.makedirs(new_folder_path)
                self.paths[paths_key] = new_folder_path

    def get_folder_name(self, paths_key):
        name = ""
        match paths_key:
            case "art_path":
                name = "art"
            case "ero_path":
                name = "erotic"
            case "porn_path":
                name = "porn"
            case "bin_path":
                name = "recycle_bin"
        return name

    def closeEvent(self, event):
        self.save()