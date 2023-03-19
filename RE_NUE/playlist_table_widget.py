# -*- coding: utf-8 -*-

import pathlib

from PyQt5.QtCore import (QSize)
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import (QWidget, QHBoxLayout, QLabel)


class TablePlaylist(QWidget):
    def __init__(self, table_parent, _name, _icon):
        super().__init__(table_parent)

        self.layout = QHBoxLayout(self)
        self.layout.setContentsMargins(0, 0, 0, 0)

        self.image = QLabel(self)
        self.image.setMinimumSize(QSize(125, 125))
        self.image.setMaximumSize(QSize(125, 125))
        self.image.setScaledContents(True)
        if _icon == '' or not pathlib.Path(_icon).exists():
            pixmap = QPixmap(":/icons/assets/no-photo.png")
        else:
            pixmap = QPixmap(_icon)
        self.image.setContentsMargins(10, 5, 10, 5)
        self.image.setPixmap(pixmap)

        self.name = QLabel(self)
        self.name.setMinimumSize(QSize(0, 100))
        self.name.setMaximumSize(QSize(16777215, 150))
        self.name.setText(_name)
        self.name.setContentsMargins(10, 10, 10, 10)
        self.name.setWordWrap(True)

        self.layout.addWidget(self.image)
        self.layout.addWidget(self.name)
