# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui/ui/create_collection.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_CreateCollection(object):
    def setupUi(self, CreateCollection):
        CreateCollection.setObjectName("CreateCollection")
        CreateCollection.resize(533, 163)
        self.gridFrame = QtWidgets.QFrame(CreateCollection)
        self.gridFrame.setGeometry(QtCore.QRect(5, 5, 521, 151))
        self.gridFrame.setObjectName("gridFrame")
        self.gridLayout = QtWidgets.QGridLayout(self.gridFrame)
        self.gridLayout.setObjectName("gridLayout")
        self.label_path = QtWidgets.QLabel(self.gridFrame)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_path.setFont(font)
        self.label_path.setObjectName("label_path")
        self.gridLayout.addWidget(self.label_path, 5, 0, 1, 1)
        self.buttonBox_ok_cancel = QtWidgets.QDialogButtonBox(self.gridFrame)
        self.buttonBox_ok_cancel.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox_ok_cancel.setObjectName("buttonBox_ok_cancel")
        self.gridLayout.addWidget(self.buttonBox_ok_cancel, 6, 1, 1, 1)
        self.label_description = QtWidgets.QLabel(self.gridFrame)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_description.setFont(font)
        self.label_description.setObjectName("label_description")
        self.gridLayout.addWidget(self.label_description, 3, 0, 1, 1)
        self.label_name = QtWidgets.QLabel(self.gridFrame)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_name.setFont(font)
        self.label_name.setObjectName("label_name")
        self.gridLayout.addWidget(self.label_name, 1, 0, 1, 1)
        self.horizontalFrame = QtWidgets.QFrame(self.gridFrame)
        self.horizontalFrame.setObjectName("horizontalFrame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalFrame)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lineEdit_path = QtWidgets.QLineEdit(self.horizontalFrame)
        self.lineEdit_path.setObjectName("lineEdit_path")
        self.horizontalLayout.addWidget(self.lineEdit_path)
        self.button_open_folder = QtWidgets.QPushButton(self.horizontalFrame)
        self.button_open_folder.setObjectName("button_open_folder")
        self.horizontalLayout.addWidget(self.button_open_folder)
        self.gridLayout.addWidget(self.horizontalFrame, 5, 1, 1, 1)
        self.lineEdit_description = QtWidgets.QLineEdit(self.gridFrame)
        self.lineEdit_description.setObjectName("lineEdit_description")
        self.gridLayout.addWidget(self.lineEdit_description, 3, 1, 1, 1)
        self.lineEdit_name = QtWidgets.QLineEdit(self.gridFrame)
        self.lineEdit_name.setObjectName("lineEdit_name")
        self.gridLayout.addWidget(self.lineEdit_name, 1, 1, 1, 1)

        self.retranslateUi(CreateCollection)
        QtCore.QMetaObject.connectSlotsByName(CreateCollection)

    def retranslateUi(self, CreateCollection):
        _translate = QtCore.QCoreApplication.translate
        CreateCollection.setWindowTitle(_translate("CreateCollection", "Form"))
        self.label_path.setText(_translate("CreateCollection", "Path"))
        self.label_description.setText(_translate("CreateCollection", "Description"))
        self.label_name.setText(_translate("CreateCollection", "Name"))
        self.button_open_folder.setText(_translate("CreateCollection", "Open..."))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    CreateCollection = QtWidgets.QWidget()
    ui = Ui_CreateCollection()
    ui.setupUi(CreateCollection)
    CreateCollection.show()
    sys.exit(app.exec_())
