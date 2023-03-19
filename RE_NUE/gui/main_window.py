import fnmatch
import pathlib

from PyQt5.QtCore import (QPoint, Qt, pyqtSignal as Signal)
from PyQt5.QtWidgets import (QAction, QMainWindow, QMenu, QTableWidgetItem)

import utils
from database import *
from gui.base.main import Ui_MainWindow
from gui.custom_grips import CustomGrip
from gui.playlist import Playlist
from gui.settings_widget import SettingsWidget
from m_player import MediaPlayer
from playlist_table_widget import TablePlaylist


class MainWindow(QMainWindow, Ui_MainWindow):
    signal_volumeChanged = Signal(int)
    signal_speedChanged = Signal(float)

    def __init__(self):
        super().__init__()
        utils.create_subfolders()
        self.setupUi(self)
        self.audio_paths = []
        # region ����������� ���� ������
        self.db = Database('data.db')
        self.player = MediaPlayer(self)
        self.scan_audio()
        # endregion

        # region �������������� ��������� ����������
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground, on=True)
        self.tabWidget_main.tabBar().hide()
        self.tabWidget_audio_parameters.tabBar().hide()
        self.main_menu_setup()
        self.button_add_playlist.setHidden(1)
        self.tableWidget_playlists_table.setColumnCount(1)
        self.tableWidget_playlists_table.setRowCount(1)
        self.tableWidget_playlists_table.horizontalHeader().hide()
        self.tableWidget_playlists_table.verticalHeader().hide()
        self.bottom_grip = CustomGrip(self, 5)
        # endregion

        # region ���� ��� �������
        self.mouse_press_start = QPoint(0, 0)
        self.mouse_pressed = False
        self.grip_title_bar = False
        self.maximized = False
        # endregion

        # region �������
        self.settingsWidget = None
        self.playlistWidget = None

        # endregion

        self.fill_playlists_table()
        self.connect_signals()

    # region ���������� �������
    def mousePressEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            if self.title_bar.geometry().top() < event.pos().y() < self.title_bar.geometry().bottom() \
                    and self.title_bar.geometry().left() < event.pos().x() < self.title_bar.geometry().right():
                self.grip_title_bar = True

                self.mouse_press_start = self.mapToGlobal(event.pos())
                self.mouse_pressed = True

    def mouseMoveEvent(self, event):
        end = QPoint(0, 0)
        movement = QPoint(0, 0)
        if self.mouse_pressed:
            end = self.mapToGlobal(event.pos())
            movement = end - self.mouse_press_start
        if movement.manhattanLength() > 10:
            if self.maximized:
                self.toggle_maximize()
                x = int(event.pos().x() - self.size().width() / 2)
                y = int(event.pos().y() - self.title_bar.size().height() / 2)
                self.move(x, y)
            if self.grip_title_bar:
                self.setGeometry(self.mapToGlobal(movement).x(),
                                 self.mapToGlobal(movement).y(),
                                 self.width(),
                                 self.height())
                self.mouse_press_start = end

    def mouseReleaseEvent(self, QMouseEvent):
        self.mouse_pressed = False

    def resizeEvent(self, event):
        self.bottom_grip.setGeometry(0, self.height() - self.bottom_grip.grip_width,
                                     self.width(), self.bottom_grip.grip_width)

    def closeEvent(self, event):
        self.db.connection_close()
    # endregion

    # ������������ � ������������� �����
    def toggle_maximize(self):
        if not self.maximized:
            self.showMaximized()
            self.maximized = not self.maximized
        else:
            self.showNormal()
            self.maximized = not self.maximized

    # ����������� ��������
    def connect_signals(self):
        # ������� ������
        self.button_menu.clicked.connect(self.qm_popup)
        self.button_minimize.clicked.connect(self.showMinimized)
        self.button_exit.clicked.connect(self.close)
        self.button_maximize.clicked.connect(self.toggle_maximize)
        self.button_all_audio.clicked.connect(lambda: self.tabWidget_main.setCurrentIndex(0))
        self.button_playlists.clicked.connect(lambda: self.tabWidget_main.setCurrentIndex(1))
        self.button_play_pause.clicked.connect(self.player.play_pause)
        self.button_next_audio.clicked.connect(self.player.playlist.next)
        self.button_previous_audio.clicked.connect(self.player.playlist.previous)
        self.button_shuffle.clicked.connect(self.player.shuffle)
        self.button_add_playlist.clicked.connect(self.create_playlist)
        self.button_repeat.clicked.connect(self.player.repeat_toggle)
        self.button_stop.clicked.connect(self.player.stop)

        # ��������� ��������
        self.tabWidget_main.currentChanged.connect(lambda x: self.button_add_playlist.setHidden(not x))
        self.horizontalSlider_volume.valueChanged.connect(self.player.setVolume)
        self.listWidget_current_playlist.currentTextChanged.connect(lambda x: self.label_audio_name.setText(x))
        self.player.signal_playlist_index_changed.connect(lambda x: self.listWidget_current_playlist.setCurrentRow(x))

        # ������� ������� �� ������� ������/�������
        self.tableWidget_all_audio.itemDoubleClicked.connect(self.play_audio)
        self.listWidget_current_playlist.itemDoubleClicked.connect(
            lambda x: self.player.setCurrentIndex(self.listWidget_current_playlist.currentRow())
        )
        self.tableWidget_playlists_table.cellDoubleClicked.connect(self.show_playlist_widget)

    # ������������ ����� � ������, ��������� � ����������
    def scan_audio(self):
        self.db.clear_audio_table()
        self.tableWidget_all_audio.clearContents()
        self.audio_paths.clear()

        paths = self.db.get_paths()
        if len(paths) < 1:
            return

        for path in paths:
            for dirpath, _, files in os.walk(path):
                for file in files:
                    if fnmatch.fnmatch(file, '*.mp3'):
                        file_name = pathlib.Path(file).name
                        file_path = os.path.join(dirpath, file)
                        self.db.add_audio(file_name, file_path)

        self.db.save_changes()
        db_audio = self.db.get_all_audio()

        self.tableWidget_all_audio.setRowCount(len(db_audio))

        for row in range(len(db_audio)):
            item = QTableWidgetItem(db_audio[row][0])
            self.tableWidget_all_audio.setItem(row, 0, item)
            self.audio_paths.append(db_audio[row][1])

    # �������� ������� ��������
    def showSettingsWidget(self):
        if self.settingsWidget is None:
            self.settingsWidget = SettingsWidget(self)

        self.settingsWidget.show()

    # �������� ������� ������������� ���������
    def show_playlist_widget(self, index):
        name = self.tableWidget_playlists_table.cellWidget(index, 0).name.text()
        self.playlistWidget = Playlist(self)
        self.playlistWidget.load_playlist(name)
        self.playlistWidget.show()

    # �������� ���������
    def create_playlist(self):
        self.playlistWidget = Playlist(self, True)
        self.playlistWidget.show()

    # ��������� ���� ��� �������
    def qm_popup(self):
        point = self.button_menu.mapToGlobal(self.button_menu.geometry().bottomLeft())
        qm_height = self.qMenu.size().height()
        offset = self.button_menu.size().height()
        if point.y() + qm_height > self.screen().size().height():
            point.setY(point.y() - (qm_height + offset))
        self.qMenu.popup(point)

    # ����������� ������������ ����
    def main_menu_setup(self):
        self.qMenu = QMenu(self.button_menu)

        settingsAction = QAction(self.qMenu)
        settingsAction.setText("Preferences")
        settingsAction.triggered.connect(self.showSettingsWidget)

        exitAction = QAction(self.qMenu)
        exitAction.setText("Exit")
        exitAction.triggered.connect(self.close)

        rescanAction = QAction(self.qMenu)
        rescanAction.setText("Rescan Audio")
        rescanAction.triggered.connect(self.scan_audio)

        self.qMenu.addAction(settingsAction)
        self.qMenu.addSeparator()
        self.qMenu.addAction(rescanAction)
        self.qMenu.addSeparator()
        self.qMenu.addAction(exitAction)

        self.qMenu.adjustSize()

    # ���������������� ���������� �����
    def play_audio(self):
        row = self.tableWidget_all_audio.currentRow()
        audio = self.audio_paths[row]
        self.player.set_playlist(audio)

    # ���������� ������� � �����������
    def fill_playlists_table(self):
        # ���������� ��������� � �������
        def add_playlist(playlist_name, row_):
            # �������� ������� �������
            _path, _name, _icon = self.db.get_playlist(playlist_name)
            pl_item = TablePlaylist(self.tableWidget_playlists_table, _name, _icon)

            # ���������� ������� � �������
            self.tableWidget_playlists_table.setCellWidget(row_, 0, pl_item)

            # ��������������� ������� ��� ����������
            self.tableWidget_playlists_table.resizeRowsToContents()
            self.tableWidget_playlists_table.resizeColumnsToContents()

        # ������� �������
        self.tableWidget_playlists_table.clear()

        # ��������� ������ ���������� � ���������� �� � �������
        p_list = self.db.get_playlists()
        rows = len(p_list)
        self.tableWidget_playlists_table.setRowCount(len(p_list))

        for row in range(rows):
            add_playlist(p_list[row], row)
    # endregion