# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_dialog_delete(object):
    def setupUi(self, dialog_delete):
        dialog_delete.setObjectName("dialog_delete")
        dialog_delete.resize(400, 240)
        dialog_delete.setMinimumSize(QtCore.QSize(400, 240))
        dialog_delete.setMaximumSize(QtCore.QSize(400, 240))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        dialog_delete.setFont(font)
        dialog_delete.setStyleSheet("color: rgb(255, 255, 255);\n"
"                selection-background-color: rgb(188, 188, 188);\n"
"                selection-color: rgb(0, 0, 0);\n"
"                border-color: rgb(15, 15, 15);\n"
"                background-color: rgb(63, 63, 63);\n"
"                alternate-background-color: rgb(188, 188, 188);\n"
"            ")
        self.verticalLayout = QtWidgets.QVBoxLayout(dialog_delete)
        self.verticalLayout.setContentsMargins(0, 10, 0, 15)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(dialog_delete)
        self.label.setMinimumSize(QtCore.QSize(0, 0))
        self.label.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(17)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(dialog_delete)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.label_3 = QtWidgets.QLabel(dialog_delete)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.buttonBox = QtWidgets.QDialogButtonBox(dialog_delete)
        self.buttonBox.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.buttonBox.setStyleSheet("QPushButton {\n"
"background-color: rgb(60, 60, 60);\n"
"border: 1px solid rgb(188, 188, 188);\n"
"border-radius: 10%;\n"
"font-size: 16pt;\n"
"width: 100px;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(188, 188, 188);\n"
"color: rgb(0, 0, 0);\n"
"}\n"
"                        ")
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.No|QtWidgets.QDialogButtonBox.Yes)
        self.buttonBox.setCenterButtons(True)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(dialog_delete)
        self.buttonBox.accepted.connect(dialog_delete.accept) # type: ignore
        self.buttonBox.rejected.connect(dialog_delete.reject) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(dialog_delete)

    def retranslateUi(self, dialog_delete):
        _translate = QtCore.QCoreApplication.translate
        dialog_delete.setWindowTitle(_translate("dialog_delete", "Dialog"))
        self.label.setText(_translate("dialog_delete", "STOP RIGHT THERE, YOU, USER!"))
        self.label_2.setText(_translate("dialog_delete", "That little button you clicked\n"
" is for deleting the playlist\n"
"                        "))
        self.label_3.setText(_translate("dialog_delete", "Are you sure you know what you\'re doing?"))
