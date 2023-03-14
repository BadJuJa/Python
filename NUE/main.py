# IMPORTS
import sys
import os
import fnmatch
from pathlib import Path
import time

from PyQt5 import QtCore, QtGui
from PyQt5.QtCore import QUrl, QDirIterator
from PyQt5.QtMultimedia import QMediaPlaylist, QMediaPlayer, QMediaContent
from PyQt5.QtWidgets import (QMainWindow, QApplication, QTableWidgetItem,
                             QListWidgetItem, QPushButton, QWidget, QHBoxLayout,
                             QFileDialog, QMessageBox)

import ui
import Extenders
import changePath
import newPlaylist
import artist
import playlist

"""
class PathsEditWidget(QWidget, changePath.Ui_EditPathsWidget):
    def __init__(self, parent=None):
        super(PathsEditWidget, self).__init__(parent, QtCore.Qt.Window)
        self.setupUi(self)
        self.update_paths_list()
        self.enable_buttons()

    def enable_buttons(self):
        self.btn_addPath.clicked.connect(self.add_path)
        self.btn_deletePath.clicked.connect(self.delete_path)
        self.btn_OKPathChange.clicked.connect(self.close)

    def update_paths_list(self):
        self.path_list.clear()

        con = Extenders.Funcs.create_connection()
        cur = con.cursor()

        paths = cur.execute('''SELECT Path FROM ScanPaths''').fetchall()

        if len(paths) != 0:
            for path in paths:
                self.path_list.addItem(path[0])
        con.close()

    def add_path(self):
        path = QFileDialog.getExistingDirectory(self, 'Get Path', '/home')

        con = Extenders.Funcs.create_connection()
        cur = con.cursor()

        cur.execute(
            f'''
                    INSERT INTO ScanPaths (Path)
                    VALUES("{path}")
                    '''
        )
        con.commit()
        con.close()

        self.path_list.addItem(path)

    def delete_path(self):
        path_to_delete = ""
        
        selectedPath = self.path_list.selectedItems()
        
        if not selectedPath:
            return
        for p in selectedPath:
            path_to_delete = self.path_list.item(self.path_list.row(p)).text()
            self.path_list.takeItem(self.path_list.row(p))

        con = Extenders.Funcs.create_connection()
        cur = con.cursor()

        cur.execute(f'''DELETE FROM Songs WHERE path LIKE "%{path_to_delete}%"''')

        cur.execute(f'''DELETE FROM ScanPaths WHERE Path == "{path_to_delete}"''')
        con.commit()
        con.close()


class PlaylistWidget(QWidget, playlist.Ui_Form):
    play_playlist_signal = QtCore.pyqtSignal()
    shuffle_playlist_signal = QtCore.pyqtSignal()

    def __init__(self, _name, parent=None):
        super(PlaylistWidget, self).__init__(parent, QtCore.Qt.Window)
        self.name = _name
        self.songlist = []
        self.setupUi(self)
        self.enable_buttons()
        self.playlist_name_lable.setText(self.name)
        self.get_songlist()

    def enable_buttons(self):
        self.btn_back_2.clicked.connect(self.close)
        self.btn_play_2.clicked.connect(self.emit_signal_play)
        self.btn_shuffle_2.clicked.connect(self.emit_signal_shuffle)

    def update_list(self):
        con = Extenders.Funcs.create_connection()
        cur = con.cursor()

        res = cur.execute(f'''SELECT SonglistPath FROM Playlists WHERE Name == "{self.name}"''').fetchall()
        songsList = res[0][0]

        songs = Extenders.Funcs.read_from_file(songsList)

        for song in songs:
            self.listWidget_2.addItem(song)

        con.close()

    def get_songlist(self):
        con = Extenders.Funcs.create_connection()
        cur = con.cursor()
        res = cur.execute(f'''SELECT SonglistPath FROM Playlists WHERE Name == "{self.name}"''').fetchall()

        self.songlist = Extenders.Funcs.read_from_file(res[0][0])

    def emit_signal_shuffle(self):
        self.shuffle_playlist_signal.emit()
        self.close()

    def emit_signal_play(self):
        self.play_playlist_signal.emit()
        self.close()

    def showEvent(self, a0: QtGui.QShowEvent) -> None:
        self.update_list()

    def closeEvent(self, a0: QtGui.QCloseEvent) -> None:
        self.listWidget_2.clear()


class NewPlaylist(QWidget, newPlaylist.Ui_Playlist_add_form):
    create_widget_signal = QtCore.pyqtSignal()

    def __init__(self, parent=None):
        super(NewPlaylist, self).__init__(parent, QtCore.Qt.Window)
        self.setupUi(self)
        self.enable_buttons()

        self.playlist_name = ""
        self.slist = []
        self.path_to_list = ""
        self.to_save = []

    def enable_buttons(self):
        # BUTTONS
        self.btn_cancel.clicked.connect(self.close)
        self.btn_save.clicked.connect(self.gotcha)

    def gotcha(self):
        self.prepare_song_list()
        self.playlist_name = self.new_playlist_name_line.text().strip()
        self.path_to_list = Extenders.Funcs.write_to_file(self.slist, os.getcwd() + "/Playlists/",
                                                          self.playlist_name.strip())
        self.send_to_db()
        self.create_widget_signal.emit()
        self.close()

    def prepare_song_list(self):
        if len(self.songlist.selectedItems()) == 0:
            return

        _songlist = self.songlist.selectedItems()

        for item in range(0, len(self.songlist.selectedItems()), 2):
            self.slist.append(_songlist[item].text())
            self.to_save.append((_songlist[item].text(), _songlist[item+1].text()))

    def load_table(self):
        con = Extenders.Funcs.create_connection()
        cur = con.cursor()
        
        songs = cur.execute('''SELECT Name, Author FROM Songs''').fetchall()

        self.songlist.setRowCount(len(songs))

        for i, elem in enumerate(songs):
            for j, val in enumerate(elem):
                self.songlist.setItem(i, j, QTableWidgetItem(str(val)))

        con.close()

    def send_to_db(self):
        if (self.new_playlist_name_line.text().strip() == ""
                or self.path_to_list == ""
                or len(self.slist) == 0):
            return

        con = Extenders.Funcs.create_connection()
        cur = con.cursor()

        cur.execute(
            f'''
            INSERT INTO Playlists (Name, SonglistPath)
            VALUES ("{self.playlist_name}","{self.path_to_list}")
            '''
        )

        con.commit()
        con.close()

    def showEvent(self, a0: QtGui.QShowEvent) -> None:
        self.load_table()

    def closeEvent(self, a0: QtGui.QCloseEvent):
        if self.new_playlist_name_line.text().strip() == "":
            answer = QMessageBox.question(
                self,
                "Stop right there!",
                "Your playlist won't be saved!\nAre you sure you want to quit?",
                QMessageBox.Yes,
                QMessageBox.No
            )
            if answer == QMessageBox.Yes:
                a0.accept()
            else:
                a0.ignore()


class Artist(QWidget, artist.Ui_Form):
    play_artist_signal = QtCore.pyqtSignal()
    shuffle_artist_signal = QtCore.pyqtSignal()

    def __init__(self, name, parent=None):
        super(Artist, self).__init__(parent, QtCore.Qt.Window)
        self.setupUi(self)
        
        self.artist_name = name
        self.enable_buttons()

    def enable_buttons(self):
        self.btn_back.clicked.connect(self.close)
        self.btn_shuffle.clicked.connect(self.emit_signal_shuffle)
        self.btn_play.clicked.connect(self.emit_signal_play)

    def update_songlist(self):
        con = Extenders.Funcs.create_connection()
        cur = con.cursor()
        
        songs = cur.execute(f'''SELECT Name FROM Songs WHERE Author == "{self.artist_name}"''').fetchall()

        for song in songs:
            self.listWidget.addItem(song[0])

        con.close()

        self.Name.setText(self.artist_name)

    def emit_signal_shuffle(self):
        self.shuffle_artist_signal.emit()
        self.close()

    def emit_signal_play(self):
        self.shuffle_artist_signal.emit()
        self.close()

    def showEvent(self, a0: QtGui.QShowEvent) -> None:
        self.update_songlist()

    def closeEvent(self, a0: QtGui.QCloseEvent) -> None:
        self.listWidget.clear()

"""

class MainClass(QMainWindow, ui.Ui_MainWindow):
    def __init__(self):
        super(MainClass, self).__init__()
        self.setupUi(self)

        self.player = QMediaPlayer()
        self.playlist = QMediaPlaylist()
        self.userAction = -1  # 0- stopped, 1- playing 2-paused
        self.isPlaying = False
        self.current_playlist = []

        self.progress_bar_slider.setRange(0, 0)
        self.progress_bar_slider.sliderMoved.connect(self.set_position)

        self.sound_bar_slider.setValue(100)
        self.sound_bar_slider.setFocusPolicy(QtCore.Qt.NoFocus)
        self.addControls()

        self.maxPlaylistsInList = 10
        self.artists_container = []

        self.enable_buttons()
        self.btn_songs_clicked()
        self.update_playlists_list()
        self.on_show()

        self.paths_widget = None

        self.selected_playlist = None
        self.new_playlist_widget = None
        self.recently_added_playlist_name = ""
        self.recently_added_playlist_slist = []
        self.artist = None

    # region MainFuncs
    def open_paths(self):
        if not self.paths_widget:
            self.paths_widget = PathsEditWidget()
        self.paths_widget.show()

    def open_selected_playlist(self, playlist_name):
        self.selected_playlist = PlaylistWidget(playlist_name)
        self.selected_playlist.play_playlist_signal.connect(self.selected_pl_play)
        self.selected_playlist.shuffle_playlist_signal.connect(self.selected_pl_shuffle)
        self.selected_playlist.show()

    def add_new_playlist(self):
        self.new_playlist_widget = NewPlaylist()

        self.new_playlist_widget.create_widget_signal.connect(self.t1)
        self.new_playlist_widget.show()

    def t1(self):
        time.sleep(0.1)
        self.recently_added_playlist_name = self.new_playlist_widget.playlist_name
        self.recently_added_playlist_slist = self.new_playlist_widget.to_save

        self.playlists_list.addItem(self.recently_added_playlist_name)
        self.update_playlists_list()

    def open_artist(self, name):
        self.artist = Artist(name)
        #self.artist.play_artist_signal.connect()
        #self.artist.shuffle_artist_signal.connect()
        self.artist.show()

    def enable_buttons(self):
        # BUTTONS
        self.btn_songs.clicked.connect(self.btn_songs_clicked)
        self.btn_playlist_create.clicked.connect(self.add_new_playlist)
        self.btn_artists.clicked.connect(lambda: self.Content_pages.setCurrentWidget(self.page_artists))
        self.btn_delete.clicked.connect(self.delete_playlist)

        self.btn_all_songs_play.clicked.connect(self.all_songs_play)
        self.btn_all_songs_shuffle.clicked.connect(self.shuffle_and_play)

        # ACTIONS
        self.actionEdit_paths.triggered.connect(self.open_paths)
        self.artistsListWidget.itemDoubleClicked.connect(
            lambda: self.open_artist(self.artistsListWidget.currentItem().text())
        )
        self.artist_search_line.textChanged.connect(self.find_artist)

        self.playlists_list.itemDoubleClicked.connect(
            lambda: self.open_selected_playlist(self.playlists_list.currentItem().text())
        )

    def selected_pl_play(self):
        self.iterator(self.selected_playlist.songlist)
        self.playhandler()

    def selected_pl_shuffle(self):
        self.iterator(self.selected_playlist.songlist)
        self.shufflelist()
        self.playhandler()

    def all_songs_play(self):
        self.iterator()
        self.playhandler()

    def shuffle_and_play(self):
        self.iterator()
        self.shufflelist()

    def update_playlists_list(self):
        self.playlists_list.clear()
        con = Extenders.Funcs.create_connection()
        cur = con.cursor()
        res = cur.execute('''SELECT Name FROM Playlists''').fetchall()
        for pl in res:
            self.playlists_list.addItem(pl[0])
        con.close()

    def delete_playlist(self):
        answer = QMessageBox.question(
            self,
            "Stop right there!",
            "You're going to delete playlist!\nAre you sure you wanna do this?",
            QMessageBox.Yes,
            QMessageBox.No
        )
        if answer == QMessageBox.Yes:
            Extenders.Funcs.delete_from_path(
                os.getcwd() + "/Playlists/" + self.playlists_list.currentItem().text() + ".csv"
            )

            con = Extenders.Funcs.create_connection()
            cur = con.cursor()
            cur.execute(
                f'''
                DELETE FROM Playlists 
                WHERE Name == "{self.playlists_list.currentItem().text()}"
            ''')
            con.commit()
            con.close()

            self.playlists_list.takeItem(self.playlists_list.currentRow())
        else:
            return

    def save_what_played_last(self):
        path = Extenders.Funcs.write_to_file(self.current_playlist, os.getcwd() + "/", "lastPlayed")
        if Path(os.getcwd() + "/lastPlayed.csv").exists():
            con = Extenders.Funcs.create_connection()
            cur = con.cursor()
            cur.execute(f'''UPDATE LastPlaylist set path = "{path}" WHERE Name == "Last"''')
            con.commit()
            con.close()

    def update_database(self):
        con = Extenders.Funcs.create_connection()
        cur = con.cursor()

        name = ""
        author = ""
        file_path = ""

        paths = cur.execute('''SELECT Path FROM ScanPaths''').fetchall()
        if len(paths) < 1:
            return

        for path in paths:
            for dirpath, _, files in os.walk(path[0]):
                for file in files:
                    if fnmatch.fnmatch(file, '*.mp3'):
                        if file.count(" - ") > 0:
                            author = file[:file.find(" - ")].strip()
                            name = file[file.find(" - ") + 3:-4].strip()
                            file_path = os.path.join(dirpath, file)

                        cur.execute(
                            f'''
                            INSERT INTO Songs (Name,Author, path) 
                            VALUES ("{name}","{author}","{file_path}")
                            '''
                        )

            songs = cur.execute('''SELECT Name, Author FROM Songs''').fetchall()

            self.all_songs_table.setRowCount(len(songs))

            for i, elem in enumerate(songs):
                for j, val in enumerate(elem):
                    self.all_songs_table.setItem(i, j, QTableWidgetItem(str(val)))

        con.commit()
        con.close()

    def btn_songs_clicked(self):
        self.update_database()
        self.Content_pages.setCurrentIndex(1)
        self.update_artists()
        self.filling_visible_artists(self.artists_container)

    def find_artist(self):
        search = self.artist_search_line.text()
        if search.strip() == "":
            self.filling_visible_artists(self.artists_container)
        else:
            container = []
            results = self._artistsListWidget.findItems(search, QtCore.Qt.MatchContains)
            for res in results:
                container.append(res.text())
            self.filling_visible_artists(container)

    def filling_visible_artists(self, container):
        self.artistsListWidget.clear()
        for name in container:
            self.artistsListWidget.addItem(name)

    def update_artists(self):
        self.artistsListWidget.clear()

        con = Extenders.Funcs.create_connection()
        cur = con.cursor()
        
        authors = cur.execute('''SELECT DISTINCT Author FROM Songs''').fetchall()

        buffer = []
        for author in authors:
            self._artistsListWidget.addItem(author[0])
            buffer.append(author[0])

        self.artists_container = buffer
        con.close()

    def on_show(self):
        for it in self.current_playlist:
            self.playlist.addMedia(QMediaContent(QUrl.fromLocalFile(it)))

    def showEvent(self, a0: QtGui.QShowEvent) -> None:
        Path(os.getcwd() + "/Playlists").mkdir(parents=True, exist_ok=True)
        if Path(os.getcwd() + "/lastPlayed.csv").exists():
            self.current_playlist = Extenders.Funcs.read_from_file(os.getcwd() + "/lastPlayed.csv")

    def closeEvent(self, a0: QtGui.QCloseEvent) -> None:
        self.save_what_played_last()

    # endregion

    # region MediaPlayer
    def is_playing_switch(self):
        self.isPlaying = not self.isPlaying

        if self.isPlaying:
            self.playhandler()
        else:
            self.pausehandler()

    def addControls(self):
        self.btn_play_stop.clicked.connect(self.is_playing_switch)
        self.btn_prev_song.clicked.connect(self.prevSong)
        self.btn_next_song.clicked.connect(self.nextSong)
        self.btn_shuffle.clicked.connect(self.shufflelist)
        self.sound_bar_slider.valueChanged[int].connect(self.changeVolume)
        self.player.durationChanged.connect(self.duration_changed)
        self.player.positionChanged.connect(self.position_changed)

        self.statusBar()
        self.playlist.currentMediaChanged.connect(self.songChanged)

    def iterator(self, *paths_list):
        self.playlist.clear()
        self.current_playlist.clear()
        _buf = paths_list
        _list1 = []
        con = Extenders.Funcs.create_connection()
        cur = con.cursor()

        if len(_buf) == 0:
            songs_path = cur.execute('''SELECT path FROM Songs''').fetchall()

            for it in songs_path:
                _list1.append(it[0])
                self.current_playlist.append(it[0])
        else:
            for s in _buf:
                for pth in s:
                    path = cur.execute(f'''SELECT path FROM Songs WHERE Name == "{pth}"''').fetchall()
                    _list1.append(path[0][0])
                    self.current_playlist.append(path[0][0])

        for it in _list1:
            self.playlist.addMedia(QMediaContent(QUrl.fromLocalFile(it)))

        self.player.setPlaylist(self.playlist)
        self.player.playlist().setCurrentIndex(0)

        con.close()

    def playhandler(self):
        if self.playlist.mediaCount() != 0:
            self.player.play()
            self.userAction = 1

    def pausehandler(self):
        self.userAction = 2
        self.player.pause()

    def prevSong(self):
        if self.playlist.mediaCount() != 0:
            self.player.playlist().previous()

    def nextSong(self):
        if self.playlist.mediaCount() != 0:
            self.player.playlist().next()
            print(self.current_playlist)

    def shufflelist(self):
        self.playlist.shuffle()

    def changeVolume(self, value):
        self.player.setVolume(value)

    def songChanged(self, media):
        if not media.isNull():
            url = media.canonicalUrl()
            self.statusBar().showMessage(url.fileName())

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
    # endregion

def main():
    app = QApplication(sys.argv)
    window = MainClass()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()
