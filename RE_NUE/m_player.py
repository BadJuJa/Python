# -*- coding: utf-8 -*-

from PyQt5.QtCore import QUrl, pyqtSignal as Signal
from PyQt5.QtMultimedia import QMediaPlaylist, QMediaPlayer, QMediaContent


class MediaPlayer(QMediaPlayer):
    signal_playlist_index_changed = Signal(int)

    def __init__(self, parent):
        super().__init__(parent=parent)
        self.mw_ref = parent
        self.playlist = QMediaPlaylist()
        self.playlist.currentIndexChanged.connect(self.signal_playlist_index_changed.emit)

        self.repeat = 0

    # Установка списка воспроизведения
    def set_playlist(self, audio_list, start=True):
        self.stop()
        self.playlist.clear()
        self.mw_ref.listWidget_current_playlist.clear()

        if not isinstance(audio_list, list):
            audio_list = [audio_list]

        for audio in audio_list:
            self.playlist.addMedia(QMediaContent(QUrl.fromLocalFile(audio)))
            self.mw_ref.listWidget_current_playlist.addItem(self.mw_ref.db.get_audio_name(audio))

        self.setPlaylist(self.playlist)
        self.playlist.setCurrentIndex(0)
        if start:
            self.play()

    # Переключение воспроизведения/паузы
    def play_pause(self):
        if self.state() == QMediaPlayer.State.PlayingState:
            self.pause()
        else:
            self.play()

    # Перемешивание плейлиста
    def shuffle(self):
        self.playlist.shuffle()
        _ = [self.playlist.media(i).canonicalUrl().fileName() for i in range(self.playlist.mediaCount())]
        self.mw_ref.listWidget_current_playlist.clear()
        for item in _:
            self.mw_ref.listWidget_current_playlist.addItem(item)
        self.playlist.setCurrentIndex(0)

    # Переключение текущего трека на
    def setCurrentIndex(self, index):
        self.playlist.setCurrentIndex(index)
        self.play()

    # Переключение режимов повтора аудио
    def repeat_toggle(self):
        match self.repeat:
            case 0:
                self.playlist.setPlaybackMode(QMediaPlaylist.PlaybackMode.Loop)
                self.repeat = 1
            case 1:
                self.playlist.setPlaybackMode(QMediaPlaylist.PlaybackMode.CurrentItemInLoop)
                self.repeat = 2
            case 2:
                self.playlist.setPlaybackMode(QMediaPlaylist.PlaybackMode.Sequential)
                self.repeat = 0