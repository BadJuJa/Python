# IMPORTS

from PyQt5 import QtCore
from PyQt5.QtCore import QUrl, pyqtSignal as Signal
from PyQt5.QtMultimedia import QMediaPlaylist, QMediaPlayer, QMediaContent
from PyQt5.QtWidgets import (QMainWindow)


# noinspection PyUnresolvedReferences
class MediaPlayer(QMediaPlayer):
    # region SIGNALS
    signal_playlist_index_changed = Signal(int)
    # endregion

    def __init__(self, parent):
        super().__init__(parent=parent)
        self.mw_ref = parent
        self.playlist = QMediaPlaylist()
        self.playlist.currentIndexChanged.connect(self.signal_playlist_index_changed.emit)

    def set_playlist(self, song_list, start=True):
        self.stop()
        self.playlist.clear()
        self.mw_ref.listWidget_current_playlist.clear()

        if not isinstance(song_list, list):
            song_list = [song_list]

        for song in song_list:
            self.playlist.addMedia(QMediaContent(QUrl.fromLocalFile(song)))
            self.mw_ref.listWidget_current_playlist.addItem(self.mw_ref.db.get_song_name(song))

        self.setPlaylist(self.playlist)
        self.playlist.setCurrentIndex(0)
        if start:
            self.play()

    def play_pause(self):
        if self.state() == QMediaPlayer.State.PlayingState:
            self.pause()
        else:
            self.play()

    def shuffle(self):
        self.playlist.shuffle()
        _ = [self.playlist.media(i).canonicalUrl().fileName() for i in range(self.playlist.mediaCount())]
        #_ = [pathlib.Path(p).name for p in _]
        self.mw_ref.listWidget_current_playlist.clear()
        for item in _:
            self.mw_ref.listWidget_current_playlist.addItem(item)

    def setCurrentIndex(self, index):
        self.playlist.setCurrentIndex(index)
        self.play()


class MainClass(QMainWindow):
    def __init__(self):
        super(MainClass, self).__init__()
        self.setupUi(self)

        self.player = QMediaPlayer()
        self.current_playlist = []

        self.progress_bar_slider.setRange(0, 0)
        self.progress_bar_slider.sliderMoved.connect(self.set_position)

        self.sound_bar_slider.setValue(100)
        self.sound_bar_slider.setFocusPolicy(QtCore.Qt.NoFocus)
        self.addControls()

        self.update_playlists_list()
        self.on_show()

        self.selected_playlist = None
        self.new_playlist_widget = None
        self.recently_added_playlist_name = ""
        self.recently_added_playlist_slist = []
        self.artist = None

    # endregion

    # region MediaPlayer

    def durationHandler(self):
        pass

    def position_changed(self, position):
        self.progress_bar_slider.blockSignals(True)
        self.progress_bar_slider.setValue(position)
        self.progress_bar_slider.blockSignals(False)

    def duration_changed(self, duration):
        self.progress_bar_slider.setRange(0, duration)

    def set_position(self, position):
        self.player.setPosition(position)
    # endregion"""