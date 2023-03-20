# -*- coding: utf-8 -*-

from PyQt5.QtCore import pyqtSignal as Signal
from PyQt5.QtWidgets import (QWidget)

from gui.base.playlist_audio_list_edit_base import Ui_mainWidget


class audiolistEdit(QWidget, Ui_mainWidget):
    listChanged = Signal(list)

    def __init__(self, mw_ref, old_audiolist):
        super().__init__()
        self.setupUi(self)
        self.mw_ref = mw_ref
        self.fill_playlists(old_audiolist)

        self.button_cancel.clicked.connect(self.close)
        self.button_to.clicked.connect(self.to_playlist)
        self.button_from.clicked.connect(self.from_playlist)
        self.button_ok.clicked.connect(self.save)

    # Заполняет листы с аудио
    def fill_playlists(self, old_audiolist):
        audio = [x[0] for x in self.mw_ref.db.get_all_audio()]
        playlist_audio = [old_audiolist.item(i).text() for i in range(old_audiolist.count())]
        playlist_audio = list(set(playlist_audio))
        if playlist_audio.count("") > 0:
            playlist_audio.remove("")
        audio = list(set(audio) - set(playlist_audio))

        self.listWidget_from.addItems(audio)
        self.listWidget_to.addItems(playlist_audio)

        self.check_list()

    # Добавляет выбранное аудио в плейлист
    def to_playlist(self):
        if len(self.listWidget_from.selectedItems()) == 0:
            return
        item = self.listWidget_from.selectedItems()[0].text()
        self.listWidget_to.addItem(item)
        self.listWidget_from.takeItem(self.listWidget_from.currentRow())

        self.check_list()

    # Убирает аудио из плейлиста
    def from_playlist(self):
        if len(self.listWidget_to.selectedItems()) == 0:
            return
        item = self.listWidget_to.selectedItems()[0].text()
        self.listWidget_from.addItem(item)
        self.listWidget_to.takeItem(self.listWidget_to.currentRow())

        self.check_list()

    # Сохранение изменений
    def save(self):
        _ = [self.listWidget_to.item(i).text() for i in range(self.listWidget_to.count())]
        self.listChanged.emit(_)
        self.close()

    # Проверяет чтобы список аудио в плейлисте не был пуст, иначе блокирует кнопку сохранения
    def check_list(self):
        safe = self.listWidget_to.count() > 0
        self.button_ok.setEnabled(safe)
