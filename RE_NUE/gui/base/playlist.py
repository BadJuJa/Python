# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_main_widget(object):
    def setupUi(self, main_widget):
        main_widget.setObjectName("main_widget")
        main_widget.resize(800, 600)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(main_widget.sizePolicy().hasHeightForWidth())
        main_widget.setSizePolicy(sizePolicy)
        main_widget.setMinimumSize(QtCore.QSize(800, 600))
        main_widget.setMaximumSize(QtCore.QSize(800, 600))
        main_widget.setStyleSheet("color: rgb(255, 255, 255); font: 75 13pt \"Century Gothic\";\n"
"selection-background-color: rgb(188, 188, 188);\n"
"selection-color: rgb(0, 0, 0); border-color: rgb(15, 15, 15);\n"
"background-color: rgb(63, 63, 63);\n"
"alternate-background-color: rgb(188, 188, 188);\n"
"\n"
"QMenuBar::item:selected { \n"
"background-color: rgb(188, 188, 188); color: rgb(0, 0, 0);\n"
"}")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(main_widget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.widget_top = QtWidgets.QWidget(main_widget)
        self.widget_top.setObjectName("widget_top")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget_top)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(8)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_image = ClickableLabel(self.widget_top)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_image.sizePolicy().hasHeightForWidth())
        self.label_image.setSizePolicy(sizePolicy)
        self.label_image.setMinimumSize(QtCore.QSize(250, 250))
        self.label_image.setMaximumSize(QtCore.QSize(250, 250))
        self.label_image.setText("")
        self.label_image.setScaledContents(True)
        self.label_image.setObjectName("label_image")
        self.horizontalLayout_2.addWidget(self.label_image)
        self.widget_text_edits = QtWidgets.QWidget(self.widget_top)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_text_edits.sizePolicy().hasHeightForWidth())
        self.widget_text_edits.setSizePolicy(sizePolicy)
        self.widget_text_edits.setObjectName("widget_text_edits")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget_text_edits)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName("verticalLayout")
        self.lineEdit_name = QtWidgets.QLineEdit(self.widget_text_edits)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_name.sizePolicy().hasHeightForWidth())
        self.lineEdit_name.setSizePolicy(sizePolicy)
        self.lineEdit_name.setMinimumSize(QtCore.QSize(0, 30))
        self.lineEdit_name.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.lineEdit_name.setReadOnly(False)
        self.lineEdit_name.setObjectName("lineEdit_name")
        self.verticalLayout.addWidget(self.lineEdit_name)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.MinimumExpanding)
        self.verticalLayout.addItem(spacerItem)
        self.widget = QtWidgets.QWidget(self.widget_text_edits)
        self.widget.setMinimumSize(QtCore.QSize(0, 75))
        self.widget.setMaximumSize(QtCore.QSize(16777215, 75))
        self.widget.setStyleSheet("QPushButton {\n"
"background-color: rgb(60, 60, 60);\n"
"border: 1px solid rgb(188, 188, 188);\n"
"border-radius: 10%;\n"
"font-size: 16pt;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(188, 188, 188);\n"
"color: rgb(0, 0, 0);\n"
"}")
        self.widget.setObjectName("widget")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.button_play = QtWidgets.QPushButton(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_play.sizePolicy().hasHeightForWidth())
        self.button_play.setSizePolicy(sizePolicy)
        self.button_play.setStyleSheet("")
        self.button_play.setObjectName("button_play")
        self.horizontalLayout_3.addWidget(self.button_play)
        self.button_edit = QtWidgets.QPushButton(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_edit.sizePolicy().hasHeightForWidth())
        self.button_edit.setSizePolicy(sizePolicy)
        self.button_edit.setStyleSheet("")
        self.button_edit.setObjectName("button_edit")
        self.horizontalLayout_3.addWidget(self.button_edit)
        self.button_shuffle = QtWidgets.QPushButton(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_shuffle.sizePolicy().hasHeightForWidth())
        self.button_shuffle.setSizePolicy(sizePolicy)
        self.button_shuffle.setStyleSheet("")
        self.button_shuffle.setObjectName("button_shuffle")
        self.horizontalLayout_3.addWidget(self.button_shuffle)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem2)
        self.verticalLayout.addWidget(self.widget)
        self.horizontalLayout_2.addWidget(self.widget_text_edits)
        self.verticalLayout_2.addWidget(self.widget_top)
        self.listWidget_audio = QtWidgets.QListWidget(main_widget)
        self.listWidget_audio.setMouseTracking(True)
        self.listWidget_audio.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.listWidget_audio.setWordWrap(True)
        self.listWidget_audio.setObjectName("listWidget_audio")
        self.verticalLayout_2.addWidget(self.listWidget_audio)
        self.widget_buttons = QtWidgets.QWidget(main_widget)
        self.widget_buttons.setStyleSheet("QPushButton {\n"
"background-color: rgb(60, 60, 60);\n"
"border: 1px solid rgb(188, 188, 188);\n"
"border-radius: 10%;\n"
"font-size: 16pt;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(188, 188, 188);\n"
"color: rgb(0, 0, 0);\n"
"}")
        self.widget_buttons.setObjectName("widget_buttons")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget_buttons)
        self.horizontalLayout.setContentsMargins(0, 0, 5, 0)
        self.horizontalLayout.setSpacing(10)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.button_delete = QtWidgets.QPushButton(self.widget_buttons)
        self.button_delete.setMinimumSize(QtCore.QSize(26, 26))
        self.button_delete.setMaximumSize(QtCore.QSize(26, 26))
        self.button_delete.setStyleSheet("QPushButton {\n"
"border-radius: 13%;\n"
"margin: -1px;\n"
"}")
        self.button_delete.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/assets/delete.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_delete.setIcon(icon)
        self.button_delete.setIconSize(QtCore.QSize(24, 24))
        self.button_delete.setObjectName("button_delete")
        self.horizontalLayout.addWidget(self.button_delete)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.button_ok = QtWidgets.QPushButton(self.widget_buttons)
        self.button_ok.setMinimumSize(QtCore.QSize(40, 26))
        self.button_ok.setMaximumSize(QtCore.QSize(16777215, 26))
        self.button_ok.setStyleSheet("")
        self.button_ok.setObjectName("button_ok")
        self.horizontalLayout.addWidget(self.button_ok)
        self.button_cancel = QtWidgets.QPushButton(self.widget_buttons)
        self.button_cancel.setMinimumSize(QtCore.QSize(90, 26))
        self.button_cancel.setMaximumSize(QtCore.QSize(16777215, 26))
        self.button_cancel.setStyleSheet("")
        self.button_cancel.setObjectName("button_cancel")
        self.horizontalLayout.addWidget(self.button_cancel)
        self.verticalLayout_2.addWidget(self.widget_buttons)

        self.retranslateUi(main_widget)
        QtCore.QMetaObject.connectSlotsByName(main_widget)

    def retranslateUi(self, main_widget):
        _translate = QtCore.QCoreApplication.translate
        main_widget.setWindowTitle(_translate("main_widget", "Playlist"))
        self.button_play.setText(_translate("main_widget", "PLAY"))
        self.button_edit.setText(_translate("main_widget", "EDIT"))
        self.button_shuffle.setText(_translate("main_widget", "SHUFFLE"))
        self.button_ok.setText(_translate("main_widget", "OK"))
        self.button_cancel.setText(_translate("main_widget", "Cancel"))
from clickable_label import ClickableLabel
import resources_rc
