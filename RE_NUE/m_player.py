# IMPORTS
import sys
import os
import fnmatch
from pathlib import Path
import time

from PySide6 import QtCore, QtGui
from PySide6.QtCore import QUrl, QDirIterator, Slot, Signal, QObject
from PySide6.QtMultimedia import (QAudio, QAudioOutput, QMediaFormat,
                                  QMediaPlayer)
from PySide6.QtWidgets import (QMainWindow, QApplication, QTableWidgetItem,
                             QListWidgetItem, QPushButton, QWidget, QHBoxLayout,
                             QFileDialog, QMessageBox)


class AudioPlayer(QObject):
    signal_playAudio = Signal()
    signal_pauseAudio = Signal()
    signal_audioIndexChanged = Signal(int)

    def __init__(self, main_window):
        super().__init__(main_window)
        self.main_window = main_window
        self.player = QMediaPlayer()
        self.audio_output = QAudioOutput()
        self.player.setAudioOutput(self.audio_output)

        self.playlist_index = 0
        self.playlist = []

        self.signal_playAudio.connect(self.Play)
        self.signal_pauseAudio.connect(self.Pause)

        self.main_window.signal_volumeChanged.connect(self.changeVolume)
        self.main_window.signal_speedChanged.connect(self.changeSpeed)

        self.player.mediaStatusChanged.connect(lambda status: self.change_audio(status))

        self.player.audioOutput().setVolume(1)

    def Load(self, file_path):
        self.player.setSource(QUrl.fromLocalFile(Path(file_path)))

    @Slot()
    def Play(self):
        print(self.playlist_index)
        self.player.play()

    @Slot()
    def Pause(self):
        self.player.pause()

    @Slot()
    def Stop(self):
        self.player.stop()

    def IsPlaying(self):
        return self.player.playbackState() is QMediaPlayer.PlaybackState.PlayingState

    @Slot()
    def changeVolume(self, value):
        self.audio_output.setVolume(value/100)

    @Slot()
    def changeSpeed(self, value):
        self.player.setPlaybackRate(value/100)

    def set_playlist(self, playlist, instant_play=False, from_index=0):
        if not isinstance(playlist, list):
            self.playlist = [playlist]
        else:
            self.playlist = playlist
        if from_index != 0:
            clamped_index = max(0, min(self.playlist_index, len(self.playlist)-1))
            self.playlist_index = from_index if from_index == clamped_index else clamped_index
        else:
            self.playlist_index = from_index

        self.signal_audioIndexChanged.emit(self.playlist_index)

        if instant_play:
            self.iterate_playlist()

    def iterate_playlist(self):
        song = self.playlist[self.playlist_index]
        self.Load(song)
        self.Play()

    def change_audio(self, status):
        if status is QMediaPlayer.MediaStatus.EndOfMedia:
            self.next_audio()

    def next_audio(self):
        if len(self.playlist) - self.playlist_index == 1:
            self.Stop()
            return
        self.playlist_index += 1
        self.iterate_playlist()
        self.signal_audioIndexChanged.emit(self.playlist_index)

    def previous_audio(self):
        if self.playlist_index == 0:
            self.Stop()
            return
        self.playlist_index -= 1
        self.iterate_playlist()
        self.signal_audioIndexChanged.emit(self.playlist_index)

    def go_to(self, index):
        self.playlist_index = index
        self.iterate_playlist()
        self.signal_audioIndexChanged.emit(self.playlist_index)