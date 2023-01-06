import os
import re
from os.path import join as J
from pathlib import Path

from PyQt5.Qt import Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import (QMainWindow, QApplication)

import common_defs as cd
from gui.base.main_window_base import Ui_MainWindow
from gui.rename_widget import RenameWidget
from gui.settings_widget import SettingsWidget
from settings import Settings


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.image_label_size = self.label_current_image_image.size()
        self.connect_buttons()

        self.settings = Settings()
        self.rename_widget = None
        self.images_info = {}
        if not os.path.exists('settings.json'):
            self.settings.create_settings()
        self.fill_list(self.settings.paths['current_folder_path'])
        self.current_collection = ""
        self.grabKeyboard()

    def connect_buttons(self):
        self.actionOpen_Folder.triggered.connect(self.open_folder)
        self.actionExit.triggered.connect(QApplication.exit)
        self.actionSettings.triggered.connect(self.open_settings)
        self.actionRefresh_List.triggered.connect(lambda: self.fill_list(self.settings.paths['current_folder_path']))
        self.actionArt.triggered.connect(lambda: self.fill_list(self.settings.paths['art_path']))
        self.actionErotics.triggered.connect(lambda: self.fill_list(self.settings.paths['ero_path']))
        self.actionPorn.triggered.connect(lambda: self.fill_list(self.settings.paths['porn_path']))
        self.actionRecycle_bin.triggered.connect(lambda: self.fill_list(self.settings.paths['bin_path']))
        self.actionAll_Images.triggered.connect(lambda: self.fill_list([self.settings.paths['art_path'],
                                                                        self.settings.paths['ero_path'],
                                                                        self.settings.paths['porn_path'],
                                                                        self.settings.paths['bin_path']]))
        self.listWidget_image_list.currentItemChanged.connect(self.show_image)
        self.button_rename_image.clicked.connect(self.open_rename_widget)

    def open_folder(self):
        folder = os.path.abspath(cd.open_folder().strip())
        self.settings.paths['current_folder_path'] = folder
        self.settings.rewrite_settings()
        self.fill_list(folder)

    def open_settings(self):
        settings_widget = SettingsWidget(self.settings)
        settings_widget.show()

#    def refresh_list(self, path):
#        self.fill_list(self.current_collection)

    def fill_list(self, paths, preclear=True):
        if preclear:
            self.clearing()
        if type(paths) is not list:
            # self.current_collection = paths
            self.settings.paths['current_folder_path'] = paths
            paths = [paths]
        for path_ in paths:
            images = self.get_images_from_path(path_)
            self.listWidget_image_list.addItems(images[1])
            self.images_info.update(images[0])
        self.label_items_in_list.setText(str(self.listWidget_image_list.count()))

    def get_images_from_path(self, path_):
        images_names = []
        file_paths = cd.scan_folder(path_)
        images = {}
        for ex_path in file_paths:
            path_obj = Path(ex_path)
            name = path_obj.stem
            suffix = path_obj.suffix
            images_names.append(name)
            images[name] = {'suffix': suffix, 'directory': Path(ex_path).parents[0], 'full_path': ex_path}

        return images, images_names

    def clearing(self):
        self.listWidget_image_list.clear()
        self.label_current_image_image.clear()
        self.label_current_image_name.clear()
        self.label_current_collection_1.clear()
        self.images_info = {}

    def show_image(self):
        if self.listWidget_image_list.currentItem() is None:
            return
        current_item = self.listWidget_image_list.currentItem().text()
        image = self.images_info[current_item]['full_path']
        pixmap = self.resize_image(QPixmap(image))
        # image itself
        self.label_current_image_image.setPixmap(pixmap)
        self.update_image_info(current_item)

    def resize_image(self, pixmap):
        if pixmap.size().height() > self.image_label_size.height() or pixmap.size().width() > self.image_label_size.width():
            return pixmap.scaled(self.image_label_size, aspectRatioMode=Qt.KeepAspectRatio)
        else:
            return pixmap

    def open_rename_widget(self):
        self.rename_widget = RenameWidget(self)
        self.rename_widget.show()

    def rename_image(self, new_name):
        image_name = self.listWidget_image_list.currentItem().text()
        image_path = self.images_info[image_name]['full_path']
        image_suffix = self.images_info[image_name]['suffix']
        path_before_image = Path(image_path).parents[0]
        regex = r"(\s\(\d+\))"
        rename_arg = f'{J(path_before_image, new_name)}{image_suffix}'

        if Path(rename_arg).exists():
            new_rename_arg_base = f'{J(self.images_info[image_name]["directory"], new_name)}'
            re_search = re.search(regex, new_rename_arg_base[-4:])
            if re_search is not None:
                new_rename_arg_base = new_rename_arg_base[:-4]
            i = 2
            while True:
                new_rename_arg = f'{new_rename_arg_base} ({i}){image_suffix}'
                if Path(new_rename_arg).exists():
                    i += 1
                else:
                    rename_arg = new_rename_arg
                    break

        Path(image_path).rename(rename_arg)
        new_name = Path(rename_arg).stem
        self.images_info.pop(image_name)
        self.listWidget_image_list.currentItem().setText(new_name)
        self.images_info[new_name] = {'suffix': Path(rename_arg).suffix, 'path': rename_arg}
        self.label_current_image_name.setText(new_name)

    def update_image_info(self, current_item):
        # image name
        self.label_current_image_name.setText(current_item)
        # image collection
        image_collection = "None"
        for k, v in list(self.settings.paths.items())[:-1]:
            if self.images_info[current_item]['directory'] == Path(v):
                image_collection = k[:-5]
        self.label_current_collection_1.setText(image_collection)

    def move_to_collection(self, collection):
        if self.listWidget_image_list.currentItem() is None:
            return
        item = self.listWidget_image_list.currentItem()
        item_name = item.text()
        to = ""
        match collection:
            case "Art":
                to = self.settings.paths['art_path']
            case "Ero":
                to = self.settings.paths['ero_path']
            case "Porn":
                to = self.settings.paths['porn_path']
            case "Delete":
                to = self.settings.paths['bin_path']
        # move picture to path
        old_path = self.images_info[item_name]['full_path']
        new_path = J(to, f'{item_name}{self.images_info[item_name]["suffix"]}')
        Path(old_path).replace(new_path)
        # change image info
        self.images_info[item_name]['directory'] = Path(new_path).parents[0]
        self.images_info[item_name]['full_path'] = new_path
        self.update_image_info(item.text())

    # events
    def keyPressEvent(self, e):
        if e.key() == Qt.Key_A:
            self.listWidget_image_list.setCurrentRow(self.listWidget_image_list.currentRow()-1)
        if e.key() == Qt.Key_D:
            self.listWidget_image_list.setCurrentRow(self.listWidget_image_list.currentRow() + 1)
        if e.key() == Qt.Key_R:
            if self.listWidget_image_list.currentItem() is not None:
                self.open_rename_widget()
        if e.key() == Qt.Key_Q:
            self.move_to_collection('Art')
        if e.key() == Qt.Key_W:
            self.move_to_collection('Ero')
        if e.key() == Qt.Key_E:
            self.move_to_collection('Porn')
        if e.key() == Qt.Key_Delete:
            self.move_to_collection('Delete')
