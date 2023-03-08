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
        self.images_moves = {}
        if not os.path.exists('settings.json'):
            self.settings.create_settings()
        self.fill_list(self.settings.paths['current_folder_path'])
        self.current_collection = ""
        self.grabKeyboard()

    def connect_buttons(self):
        # Collections
        self.actionArt.triggered.connect(lambda: self.fill_list(self.settings.paths['art_path']))
        self.actionErotics.triggered.connect(lambda: self.fill_list(self.settings.paths['ero_path']))
        self.actionPorn.triggered.connect(lambda: self.fill_list(self.settings.paths['porn_path']))
        self.actionRecycle_bin.triggered.connect(lambda: self.fill_list(self.settings.paths['bin_path']))
        self.actionMove_Images.triggered.connect(lambda: self.move_images())

        # All images
        self.actionAll_Images.triggered.connect(lambda: self.fill_list([self.settings.paths['art_path'],
                                                                        self.settings.paths['ero_path'],
                                                                        self.settings.paths['porn_path'],
                                                                        self.settings.paths['bin_path']]))

        # File menu
        self.actionOpen_Folder.triggered.connect(self.open_folder)
        self.actionExit.triggered.connect(QApplication.exit)
        self.actionSettings.triggered.connect(self.open_settings)
        self.actionRefresh_List.triggered.connect(lambda: self.fill_list(self.settings.paths['current_folder_path']))

        # Triggers
        self.listWidget_image_list.currentItemChanged.connect(self.show_image)

        # Current image
        self.button_rename_image.clicked.connect(self.open_rename_widget)
        self.button_to_art.clicked.connect(lambda: self.prepare_to_move_image('Art'))
        self.button_to_porn.clicked.connect(lambda: self.prepare_to_move_image('Porn'))
        self.button_to_erotics.clicked.connect(lambda: self.prepare_to_move_image('Ero'))
        self.button_delete_image.clicked.connect(lambda: self.prepare_to_move_image('Delete'))

        self.button_next_image.clicked.connect(self.select_next_image)
        self.button_previous_image.clicked.connect(self.select_prev_image)

    def open_folder(self):
        folder = os.path.abspath(cd.open_folder().strip())
        self.settings.paths['current_folder_path'] = folder
        self.settings.rewrite_settings()
        self.fill_list(folder)

    def open_settings(self):
        settings_widget = SettingsWidget(self.settings)
        settings_widget.show()

    def fill_list(self, paths, preclear=True):
        if preclear:
            self.clearing()
        if type(paths) is not list:
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

            if name in list(images.keys()):
                name = f"_{name}"

            images_names.append(name)
            images[name] = {'suffix': suffix, 'directory': Path(ex_path).parents[0], 'full_path': ex_path}

        return images, images_names

    def clearing(self):
        self.listWidget_image_list.clear()
        self.label_current_image_image.clear()
        self.label_current_image_name.clear()
        self.label_collection_1.clear()
        self.label_collection_moveto_1.clear()
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
        self.releaseKeyboard()

    def rename_image(self, new_name, new_path=None):
        image_name = self.listWidget_image_list.currentItem().text()
        image_path = self.images_info[image_name]['full_path']
        image_suffix = self.images_info[image_name]['suffix']
        if new_path is None:
            path_before_image = Path(image_path).parents[0]
        else:
            path_before_image = Path(new_path).parents[0]
        regex = r"(\s\(\d+\))"
        rename_arg = f'{J(path_before_image, new_name)}{image_suffix}'
        if Path(rename_arg).exists():
            new_rename_arg_base = f'{J(path_before_image, new_name)}'
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
        old = self.images_info.pop(image_name)
        self.images_info[new_name] = {
            'suffix': Path(rename_arg).suffix,
            'directory': Path(rename_arg).parents[0].__str__(),
            'full_path': Path(rename_arg).__str__()
        }

        self.listWidget_image_list.currentItem().setText(new_name)
        self.label_current_image_name.setText(new_name)

        return new_name

    def update_image_info(self, current_item):
        # image name
        self.label_current_image_name.setText(current_item)
        # image collection
        image_collection = "None"
        for k, v in list(self.settings.paths.items())[:-1]:
            if self.images_info[current_item]['directory'] == Path(v):
                image_collection = k[:-5]
        self.label_collection_moveto_1.setText(self.images_moves.get(current_item))
        self.label_collection_1.setText(image_collection)

    def prepare_to_move_image(self, collection):
        if self.listWidget_image_list.currentItem() is None:
            return
        item = self.listWidget_image_list.currentItem()
        item_name = item.text()

        self.images_moves[item_name] = collection
        self.label_collection_moveto_1.setText(collection)

    def move_images(self):
        self.listWidget_image_list.clearSelection()
        self.label_current_image_image.clear()
        self.label_current_image_name.clear()
        self.label_collection_1.clear()
        self.label_collection_moveto_1.clear()
        for im in list(self.images_moves.keys()):
            to = ""
            match self.images_moves[im]:
                case "Art":
                    to = self.settings.paths['art_path']
                case "Ero":
                    to = self.settings.paths['ero_path']
                case "Porn":
                    to = self.settings.paths['porn_path']
                case "Delete":
                    to = self.settings.paths['bin_path']
            old_path = self.images_info[im]['full_path']
            new_path = J(to, f'{im}{self.images_info[im]["suffix"]}')
            if old_path == new_path:
                continue
            if Path(new_path).exists():
                new_name = self.rename_image(im, new_path)
                self.images_info[new_name]['directory'] = Path(new_path).parents[0]
                new_full_path = J(Path(new_path).parents[0], f"{new_name}{self.images_info[new_name]['suffix']}")
                self.images_info[new_name]['full_path'] = new_full_path
            else:
                Path(old_path).replace(new_path)
                self.images_info[im]['directory'] = Path(new_path).parents[0]
                self.images_info[im]['full_path'] = new_path

            self.update_image_info(im)
        self.images_moves.clear()

    def select_next_image(self):
        self.listWidget_image_list.setCurrentRow(self.listWidget_image_list.currentRow() + 1)

    def select_prev_image(self):
        self.listWidget_image_list.setCurrentRow(self.listWidget_image_list.currentRow() - 1)

    # events
    def keyPressEvent(self, e):
        if e.key() == Qt.Key_A:
            self.select_prev_image()
        if e.key() == Qt.Key_D:
            self.select_next_image()
        if e.key() == Qt.Key_R:
            if self.listWidget_image_list.currentItem() is not None:
                self.open_rename_widget()
        if e.key() == Qt.Key_Q:
            self.prepare_to_move_image('Art')
        if e.key() == Qt.Key_W:
            self.prepare_to_move_image('Ero')
        if e.key() == Qt.Key_E:
            self.prepare_to_move_image('Porn')
        if e.key() == Qt.Key_Delete:
            self.prepare_to_move_image('Delete')
        if e.key() == Qt.Key_F12:
            self.move_images()