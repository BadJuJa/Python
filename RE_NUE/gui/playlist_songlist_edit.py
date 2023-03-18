from PyQt5.QtCore import pyqtSignal as Signal
from PyQt5.QtCore import pyqtSignal as Signal
from PyQt5.QtWidgets import (QWidget)

from gui.base.playlist_songlist_edit import Ui_mainWidget


class SonglistEdit(QWidget, Ui_mainWidget):
    listChanged = Signal(list)

    def __init__(self, mw_ref, old_songlist):
        super().__init__()
        self.setupUi(self)
        self.mw_ref = mw_ref
        self.fill_playlists(old_songlist)

        self.button_cancel.clicked.connect(self.close)
        self.button_to.clicked.connect(self.to_playlist)
        self.button_from.clicked.connect(self.from_playlist)
        self.button_ok.clicked.connect(self.save)

    def fill_playlists(self, old_songlist):
        songs = [x[0] for x in self.mw_ref.db.get_songs()]
        playlist_songs = [old_songlist.item(i).text() for i in range(old_songlist.count())]
        playlist_songs = list(set(playlist_songs))
        if playlist_songs.count("") > 0:
            playlist_songs.remove("")
        songs = list(set(songs) - set(playlist_songs))

        self.listWidget_from.addItems(songs)
        self.listWidget_to.addItems(playlist_songs)

        self.control_ok_button()

    def to_playlist(self):
        if len(self.listWidget_from.selectedItems()) == 0:
            return
        item = self.listWidget_from.selectedItems()[0].text()
        self.listWidget_to.addItem(item)
        self.listWidget_from.takeItem(self.listWidget_from.currentRow())

        self.control_ok_button()

    def from_playlist(self):
        if len(self.listWidget_to.selectedItems()) == 0:
            return
        item = self.listWidget_to.selectedItems()[0].text()
        self.listWidget_from.addItem(item)
        self.listWidget_to.takeItem(self.listWidget_to.currentRow())

        self.control_ok_button()

    def save(self):
        _ = []
        for i in range(self.listWidget_to.count()):
            _.append(self.listWidget_to.item(i).text())
        self.listChanged.emit(_)
        self.close()

    def control_ok_button(self):
        safe = self.listWidget_to.count() > 0
        self.button_ok.setEnabled(safe)