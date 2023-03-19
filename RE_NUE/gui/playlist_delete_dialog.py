# -*- coding: utf-8 -*-

from PyQt5 import QtWidgets

from gui.base.playlist_delete_dialog import Ui_dialog_delete


class DeleteDialog(QtWidgets.QDialog, Ui_dialog_delete):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.decision = None

        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)
