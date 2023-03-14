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
    play_signal = Signal(name="PlaySong")
    pause_signal = Signal(name="PauseSong")

    def __init__(self, main_window):
        super().__init__(main_window)
        self.main_window = main_window
        self.player = QMediaPlayer()
        self.audio_output = QAudioOutput()
        self.player.setAudioOutput(self.audio_output)

        self.play_signal.connect(self.Play)
        self.pause_signal.connect(self.Pause)

        self.main_window.signal_volumeChanged.connect(self.changeVolume)
        self.main_window.signal_speedChanged.connect(self.changeSpeed)

        file_path = r"C:\Users\user\Documents\GitHub\Python\RE_NUE\music\Kelly Camelio  - Dusk on Anvil Harbor.mp3"
        self.player.audioOutput().setVolume(1)

    def Load(self, file_path):
        self.player.setSource(QUrl.fromLocalFile(Path(file_path)))

    @Slot()
    def Play(self):
        self.player.play()
        print("PLAY")

    @Slot()
    def Pause(self):
        self.player.pause()
        print("PAUSE")

    def IsPlaying(self):
        return self.player.playbackState() is QMediaPlayer.PlaybackState.PlayingState

    @Slot()
    def changeVolume(self, value):
        self.audio_output.setVolume(value/100)

    @Slot()
    def changeSpeed(self, value):
        self.player.setPlaybackRate(value/100)