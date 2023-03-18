import os
import pathlib

from PyQt5 import QtGui
from PyQt5.QtCore import QUrl
from PyQt5.QtGui import QPixmap
from PyQt5.QtMultimedia import QMediaPlaylist, QMediaContent
from PyQt5.QtWidgets import (QWidget, QFileDialog, QLineEdit)

import utils
from gui.base.playlist import Ui_main_widget
from gui.playlist_delete_dialog import DeleteDialog
from gui.playlist_songlist_edit import SonglistEdit


class Playlist(QWidget, Ui_main_widget):
    def __init__(self, mw_ref, new=False):
        super().__init__()
        self.main_window_ref = mw_ref
        self.new = new
        self.editMode = True if self.new else False

        self.setupUi(self)

        self.songlist_edit = None

        self.old_name = "" if self.new else self.lineEdit_name.text()
        self.old_list = [] if self.new else self.get_song_list()
        self.old_pixmap = QPixmap(":/icons/assets/no-photo.png") if self.new else self.label_image.pixmap()
        if self.new:
            self.listWidget_songs.addItems([""]*11)

        self.button_edit.setEnabled(not self.new)
        self.button_play.setEnabled(not self.new)
        self.button_shuffle.setEnabled(not self.new)

        self.backup_done = False
        self.changes_saved = False

        self.connect_signals()
        self.check_name()

    def connect_signals(self):
        if self.editMode:
            self.button_ok.clicked.connect(self.save)
            self.listWidget_songs.clicked.connect(self.open_songlist_edit)
        else:
            self.button_ok.clicked.connect(self.close)

        self.button_cancel.clicked.connect(self.close)
        self.label_image.clicked.connect(self.SetPicture)
        self.button_edit.clicked.connect(self.toggle_edit_mode)
        self.lineEdit_name.textEdited.connect(self.check_name)
        self.button_delete.clicked.connect(self.delete)
        self.button_play.clicked.connect(self.start_playlist)
        self.button_shuffle.clicked.connect(self.shuffle_playlist)

    def toggle_edit_mode(self):
        self.editMode = not self.editMode

        self.toggle_ok_button_signals_connection()
        self.toggle_songlist_signals_connection()
        self.lineEdit_name.setReadOnly(not self.editMode)
        self.button_delete.setEnabled(not self.editMode)
        self.button_play.setEnabled(not self.editMode)
        self.button_shuffle.setEnabled(not self.editMode)

        if self.editMode:
            self.changes_saved = False
            if not self.backup_done:
                self.backup()
        else:
            if not self.changes_saved:
                self.revert_changes()

    def SetPicture(self):
        if not self.editMode:
            return

        fileName = QFileDialog.getOpenFileName(self, ("Open File"),
                                               "/home",
                                               ("Images (*.png *.xpm *.jpg)"))[0]
        if fileName == '':
            return

        pixmap = QtGui.QPixmap(fileName)
        self.label_image.setPixmap(pixmap)

    def open_playlist(self, playlist_name):
        path, name, icon = self.main_window_ref.db.get_playlist(playlist_name)
        s_list = utils.CsvControl.read_from_file(path)

        if icon == '' or not pathlib.Path(icon).exists():
            pixmap = QPixmap(":/icons/assets/no-photo.png")
        else:
            pixmap = QPixmap(icon)

        self.label_image.setPixmap(pixmap)
        self.lineEdit_name.setText(name)
        self.listWidget_songs.addItems(s_list)

        self.lineEdit_name.setReadOnly(True)
        self.check_name()

    def save(self):
        playlists_folder = os.path.join(os.getcwd(), "Playlists")
        # CREATE PLAYLIST FOR SAVE
        new_playlist = QMediaPlaylist()
        ts = self.get_song_list()
        for s in ts:
            p = self.main_window_ref.db.get_song(s)
            new_playlist.addMedia(QMediaContent(QUrl.fromLocalFile(p)))

        if self.new:
            dir_ = os.path.join(playlists_folder, self.lineEdit_name.text())
            new_playlist.save(QUrl().fromLocalFile(dir_ + '.m3u'), "m3u")
            csv = utils.CsvControl.write_to_file(ts, dir_)
            image_path = os.path.join(playlists_folder, "icons", self.lineEdit_name.text())
            success = self.label_image.pixmap().save(image_path + ".png", "png")
            im_path = image_path+".png" if success else ""
            self.main_window_ref.db.add_playlist(self.lineEdit_name.text(), csv, im_path)
        else:

            old_csv = self.main_window_ref.db.get_playlist(self.old_name)[0]
            new_file_path = os.path.join(playlists_folder, self.lineEdit_name.text())

            if os.path.exists(old_csv):
                os.remove(old_csv)
            csv = utils.CsvControl.write_to_file(ts, new_file_path)

            old_m3u = os.path.join(playlists_folder, self.old_name + ".m3u")
            if os.path.exists(old_m3u):
                os.remove(old_m3u)
            new_playlist.save(QUrl().fromLocalFile(new_file_path + '.m3u'), "m3u")

            icons_path = os.path.join(playlists_folder, "icons")

            old_png = os.path.join(playlists_folder, "icons", self.old_name + ".png")
            if os.path.exists(old_png):
                os.remove(old_png)

            image_path = os.path.join(icons_path, self.lineEdit_name.text())
            #os.remove(os.path.join(icons_path, self.old_name + ".png"))
            success = self.label_image.pixmap().save(image_path + ".png", "png")
            im_path = image_path + ".png" if success else ""
            self.main_window_ref.db.update_playlist(self.old_name, self.lineEdit_name.text(), csv, im_path)

        self.main_window_ref.db.save_changes()

        self.changes_saved = True
        self.backup_done = False
        self.main_window_ref.fill_playlists_table()
        self.close()

    def open_songlist_edit(self):
        self.songlist_edit = SonglistEdit(self.main_window_ref, self.listWidget_songs)
        self.songlist_edit.listChanged.connect(self.change_list)
        self.songlist_edit.show()

    def change_list(self, new_list):
        self.listWidget_songs.clear()
        self.listWidget_songs.addItems(new_list)

    def check_name(self):
        safe = self.lineEdit_name.text().strip() != ""
        self.button_ok.setEnabled(safe)

    def backup(self):
        self.old_name = self.lineEdit_name.text()
        self.old_list = self.get_song_list()
        self.old_pixmap = self.label_image.pixmap()
        self.backup_done = True

    def revert_changes(self):

        self.lineEdit_name.setText(self.old_name.text() if isinstance(self.old_name, QLineEdit) else self.old_name)
        self.label_image.setPixmap(self.old_pixmap)
        self.listWidget_songs.clear()
        self.listWidget_songs.addItems(self.old_list)

    def toggle_songlist_signals_connection(self):
        if self.editMode:
            self.listWidget_songs.doubleClicked.connect(self.open_songlist_edit)
        else:
            self.listWidget_songs.doubleClicked.disconnect()

    def toggle_ok_button_signals_connection(self):
        self.button_ok.clicked.disconnect()
        if self.editMode:
            self.button_ok.clicked.connect(self.save)
            self.button_ok.setText("Save")
        else:
            self.button_ok.clicked.connect(self.close)
            self.button_ok.setText("OK")

    def get_song_list(self):
        return [self.listWidget_songs.item(x).text() for x in range(self.listWidget_songs.count())]

    def delete(self):
        dialog = DeleteDialog()
        dialog.show()
        result = dialog.exec()
        if result == 0:
            return

        old_csv = self.main_window_ref.db.get_playlist(self.lineEdit_name.text())[0]
        dir_ = os.path.dirname(old_csv)
        old_m3u = os.path.join(dir_, self.lineEdit_name.text() + ".m3u")
        old_png = os.path.join(dir_, "icons", self.lineEdit_name.text() + ".png")

        self.main_window_ref.db.remove_playlist(self.lineEdit_name.text())
        self.main_window_ref.db.save_changes()

        if os.path.exists(old_csv):
            os.remove(old_csv)
        if os.path.exists(old_m3u):
            os.remove(old_m3u)
        if os.path.exists(old_png):
            os.remove(old_png)

        self.close()
        self.main_window_ref.fill_playlists_table()

    def start_playlist(self):
        _ = [self.main_window_ref.db.get_song(song) for song in self.get_song_list()]
        self.main_window_ref.player.set_playlist(_)
        self.close()

    def shuffle_playlist(self):
        _ = [self.main_window_ref.db.get_song(song) for song in self.get_song_list()]
        self.main_window_ref.player.set_playlist(_, False)
        self.main_window_ref.player.shuffle()
        self.main_window_ref.player.play()
        self.close()