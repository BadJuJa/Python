# -*- coding: utf-8 -*-

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class CustomGrip(QWidget):
    def __init__(self, parent, grip_width=10):
        self.grip_width = grip_width
        QWidget.__init__(self)
        self.parent = parent
        self.setParent(parent)
        self.widget = Widgets(self.grip_width)
        self.widget.setup_ui(self)
        self.setGeometry(0, self.parent.height() - self.grip_width, self.parent.width(), self.grip_width)
        self.setMaximumHeight(self.grip_width)

        # Виджет захвата
        self.bottom_right = QSizeGrip(self.widget.bottom_right)

        # Масштабирование виджета захвата при изменении размера окна
        def resize_bottom(event):
            delta = event.pos()
            height = max(self.parent.minimumHeight(), self.parent.height() + delta.y())
            self.parent.resize(self.parent.width(), height)
            event.accept()
        self.widget.bottom_right.mouseMoveEvent = resize_bottom

    # region Перезапись событий масштабирования
    def mouseReleaseEvent(self, event):
        self.mousePos = None

    def resizeEvent(self, event):
        if hasattr(self.widget, 'container_bottom'):
            self.widget.container_bottom.setGeometry(0, 0, self.width(), self.grip_width)
    # endregion


class Widgets(object):
    def __init__(self, grip_width):
        self.grip_width = grip_width

    def setup_ui(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        self.container_bottom = QFrame(Form)
        self.container_bottom.setObjectName(u"container_bottom")
        self.container_bottom.setGeometry(QRect(0, 0, 500, self.grip_width))
        self.container_bottom.setMinimumSize(QSize(0, self.grip_width))
        self.container_bottom.setMaximumSize(QSize(16777215, self.grip_width))
        self.container_bottom.setFrameShape(QFrame.NoFrame)
        self.container_bottom.setFrameShadow(QFrame.Raised)
        self.bottom_layout = QHBoxLayout(self.container_bottom)
        self.bottom_layout.setSpacing(0)
        self.bottom_layout.setObjectName(u"bottom_layout")
        self.bottom_layout.setContentsMargins(0, 0, 0, 0)
        self.bottom = QFrame(self.container_bottom)
        self.bottom.setObjectName(u"bottom")
        self.bottom.setStyleSheet(u"background-color: transparent;")
        self.bottom.setFrameShape(QFrame.NoFrame)
        self.bottom.setFrameShadow(QFrame.Raised)
        self.bottom_layout.addWidget(self.bottom)
        self.bottom_right = QFrame(self.container_bottom)
        self.bottom_right.setObjectName(u"bottom_right")
        self.bottom_right.setMinimumSize(QSize(self.grip_width, self.grip_width))
        self.bottom_right.setMaximumSize(QSize(self.grip_width, self.grip_width))
        self.bottom_right.setCursor(QCursor(Qt.SizeFDiagCursor))
        self.bottom_right.setStyleSheet(u"background-color: rgb(33, 37, 43);")
        self.bottom_right.setFrameShape(QFrame.NoFrame)
        self.bottom_right.setFrameShadow(QFrame.Raised)
        self.bottom_layout.addWidget(self.bottom_right)

