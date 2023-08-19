import os
import re
from os.path import join as J
from pathlib import Path

from PyQt5.Qt import Qt
from PyQt5.QtCore import QDir
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileSystemModel

import common_defs as cd
from gui.base.main_window_base import Ui_MainWindow
from gui.settings_widget import SettingsWidget
from settings import Settings


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.initiate_widgets()
        self.initiate_additional

        self.connect_buttons()
        #self.grabKeyboard()

    #region Action Handlers

    def ah_open(self):
        folder = os.path.abspath(cd.open_folder().strip())
        self.initiate_treeView(folder)
    #endregion

    #region Initiators

    def initiate_treeView(self, path):
        self.treeView_image_list.setModel(self.treeModel)
        self.treeView_image_list.setRootIndex(self.treeModel.index(path))
        for i in range(1, self.treeModel.columnCount()):
            self.treeView_image_list.header().hideSection(i)

    def initiate_widgets(self):
        self.settings = Settings()
        
        self.rename_widget = None

        self.treeModel = QFileSystemModel()
        self.treeModel.setRootPath(QDir.rootPath())
        self.treeModel.setReadOnly(False)
        
        self.treeModel.setFilter(QDir.AllDirs | QDir.NoDotAndDotDot | QDir.Files)
        self.treeModel.setNameFilters(["*.jpg", "*.png", "*.jpeg"])
        self.treeModel.setNameFilterDisables(False)

        self.treeView_image_list.setHeaderHidden(True)

    def initiate_additional(self):
        self.image_label_size = self.label_current_image_image.size()
        self.images_info = {}
        self.images_moves = {}
        self.current_collection = ""

    #endregion

    def connect_buttons(self):
        #region Collection actions
        
        #self.actionArt.triggered.connect(lambda: self.fill_list(self.settings.paths['art_path']))
        #self.actionErotics.triggered.connect(lambda: self.fill_list(self.settings.paths['ero_path']))
        #self.actionPorn.triggered.connect(lambda: self.fill_list(self.settings.paths['porn_path']))
        #self.actionRecycle_bin.triggered.connect(lambda: self.fill_list(self.settings.paths['bin_path']))

        #self.actionAll_Images.triggered.connect(lambda: self.fill_list([self.settings.paths['art_path'],
        #                                                                self.settings.paths['ero_path'],
        #                                                                self.settings.paths['porn_path'],
        #                                                                self.settings.paths['bin_path']]))
        
        #endregion
        
        # File menu
        self.actionOpen_Folder.triggered.connect(self.ah_open)
        self.actionExit.triggered.connect(QApplication.exit)
        self.actionSettings.triggered.connect(self.open_settings)

        # Triggers
        #self.listWidget_image_list.currentItemChanged.connect(self.show_image)
        self.treeView_image_list.doubleClicked.connect(lambda x: print(
            '\n========================\n',
            self.treeModel.fileName(x), 
            self.treeModel.filePath(x), 
            self.treeModel.fileInfo(x),
            self.treeModel.fileIcon(x),
            '\n========================\n',
            sep='\n'))
        
        #region Buttons

        #self.button_to_art.clicked.connect(lambda: self.prepare_to_move_image('Art'))
        #self.button_to_porn.clicked.connect(lambda: self.prepare_to_move_image('Porn'))
        #self.button_to_erotics.clicked.connect(lambda: self.prepare_to_move_image('Ero'))

        #endregion

    def open_settings(self):
        settings_widget = SettingsWidget(self.settings)
        settings_widget.show()

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
        self.listWidget_image_list.setCurrentRow(self.listWidget_image_list.currentRow() - 1)

    # events
    def keyPressEvent(self, e):
        pass