# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_mainWidget(object):
    def setupUi(self, mainWidget):
        mainWidget.setObjectName("mainWidget")
        mainWidget.resize(687, 480)
        mainWidget.setStyleSheet("color: rgb(255, 255, 255);\n"
"                font: 75 13pt \"Century Gothic\";\n"
"                selection-background-color: rgb(188, 188, 188);\n"
"                selection-color: rgb(0, 0, 0);\n"
"                border-color: rgb(15, 15, 15);\n"
"                background-color: rgb(63, 63, 63);\n"
"                alternate-background-color: rgb(188, 188, 188);\n"
"\n"
"                QMenuBar::item:selected {\n"
"                background-color: rgb(188, 188, 188);\n"
"                color: rgb(0, 0, 0);\n"
"                }\n"
"            ")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(mainWidget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.widget_top = QtWidgets.QWidget(mainWidget)
        self.widget_top.setObjectName("widget_top")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget_top)
        self.horizontalLayout_2.setContentsMargins(4, 4, 4, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.listWidget_from = QtWidgets.QListWidget(self.widget_top)
        self.listWidget_from.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.listWidget_from.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.listWidget_from.setObjectName("listWidget_from")
        self.horizontalLayout_2.addWidget(self.listWidget_from)
        self.widget = QtWidgets.QWidget(self.widget_top)
        self.widget.setStyleSheet("QPushButton {\n"
"background-color: rgb(60, 60, 60);\n"
"border: 1px solid rgb(188, 188, 188);\n"
"border-radius: 25%;\n"
"font-size: 16pt;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(188, 188, 188);\n"
"color: rgb(0, 0, 0);\n"
"}\n"
"                    ")
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 179, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.button_to = QtWidgets.QPushButton(self.widget)
        self.button_to.setStyleSheet("")
        self.button_to.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/assets/arrows-right.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_to.setIcon(icon)
        self.button_to.setIconSize(QtCore.QSize(48, 48))
        self.button_to.setObjectName("button_to")
        self.verticalLayout.addWidget(self.button_to)
        self.button_from = QtWidgets.QPushButton(self.widget)
        self.button_from.setStyleSheet("")
        self.button_from.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/assets/arrows-left.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_from.setIcon(icon1)
        self.button_from.setIconSize(QtCore.QSize(48, 48))
        self.button_from.setObjectName("button_from")
        self.verticalLayout.addWidget(self.button_from)
        spacerItem1 = QtWidgets.QSpacerItem(20, 178, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.horizontalLayout_2.addWidget(self.widget)
        self.listWidget_to = QtWidgets.QListWidget(self.widget_top)
        self.listWidget_to.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.listWidget_to.setObjectName("listWidget_to")
        self.horizontalLayout_2.addWidget(self.listWidget_to)
        self.verticalLayout_2.addWidget(self.widget_top)
        self.widget_bottom = QtWidgets.QWidget(mainWidget)
        self.widget_bottom.setStyleSheet("QPushButton {\n"
"background-color: rgb(60, 60, 60);\n"
"border: 1px solid rgb(188, 188, 188);\n"
"border-radius: 10%;\n"
"font-size: 16pt;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(188, 188, 188);\n"
"color: rgb(0, 0, 0);\n"
"}\n"
"                        ")
        self.widget_bottom.setObjectName("widget_bottom")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget_bottom)
        self.horizontalLayout.setContentsMargins(4, 4, 4, 4)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem2 = QtWidgets.QSpacerItem(514, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.button_ok = QtWidgets.QPushButton(self.widget_bottom)
        self.button_ok.setStyleSheet("")
        self.button_ok.setObjectName("button_ok")
        self.horizontalLayout.addWidget(self.button_ok)
        self.button_cancel = QtWidgets.QPushButton(self.widget_bottom)
        self.button_cancel.setObjectName("button_cancel")
        self.horizontalLayout.addWidget(self.button_cancel)
        self.verticalLayout_2.addWidget(self.widget_bottom)

        self.retranslateUi(mainWidget)
        QtCore.QMetaObject.connectSlotsByName(mainWidget)

    def retranslateUi(self, mainWidget):
        _translate = QtCore.QCoreApplication.translate
        mainWidget.setWindowTitle(_translate("mainWidget", "Form"))
        self.button_ok.setText(_translate("mainWidget", "OK"))
        self.button_cancel.setText(_translate("mainWidget", "Cancel"))
import resources_rc
