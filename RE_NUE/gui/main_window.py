from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt, Signal, Slot)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QLabel,
    QLayout, QListWidget, QListWidgetItem, QMainWindow,
    QPushButton, QSizePolicy, QSpacerItem, QStatusBar,
    QTabWidget, QVBoxLayout, QWidget, QMenu, QTableWidget, QTableWidgetItem)

from gui.base.main import Ui_MainWindow
from gui.custom_grips import CustomGrip
from gui.settings_widget import SettingsWidget
from utils import *
from database import *
import pathlib
import fnmatch
from m_player import AudioPlayer


class MainWindow(QMainWindow, Ui_MainWindow):
    signal_volumeChanged = Signal(int)
    signal_speedChanged = Signal(float)

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.songs = []

        # region DATABASE
        self.db = Database('data.db')
        self.rescan_music()
        # endregion

        # region WINDOW SETUP
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground, on=True)
        self.tabWidget_main.tabBar().hide()
        self.tabWidget_song_parameters.tabBar().hide()
        self.MainMenuSetup()
        self.setup_resizeGrips()
        self.button_playlists.hide()
        self.horizontalSlider_speed.hide()
        self.label_speed_slider.hide()
        # endregion

        # region EVENT PARAMETERS
        self.mouse_press_start = QPoint(0, 0)
        self.mouse_pressed = False
        self.grip_title_bar = False
        self.maximized = False
        # endregion

        # region WIDGETS
        self.settingsWidget = None
        self.player = AudioPlayer(self)
        # endregion

        # region CONNECT SIGNALS
        self.connect_buttons()
        # endregion


    # region EVENT OVERRIDING
    def mousePressEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            if self.title_bar.geometry().top() < event.pos().y() < self.title_bar.geometry().bottom()\
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
                self.btn_max_clicked()
                x = int(event.pos().x() - self.size().width()/2)
                y = int(event.pos().y() - self.title_bar.size().height()/2)
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
        self.resize_resizeGrips()
    # endregion

    # region BUTTON METHODS
    def btn_close_clicked(self):
        self.close()

    def btn_max_clicked(self):
        if not self.maximized:
            self.showMaximized()
            self.maximized = not self.maximized
        else:
            self.showNormal()
            self.maximized = not self.maximized

    def btn_min_clicked(self):
        self.showMinimized()
    # endregion

    # region CUSTOM METHODS
    def resize_resizeGrips(self):
        self.left_grip.setGeometry(0,
                                   self.left_grip.grip_width,
                                   self.left_grip.grip_width,
                                   self.height()+self.left_grip.grip_width*2)
        self.right_grip.setGeometry(self.width() - self.right_grip.grip_width,
                                    self.right_grip.grip_width,
                                    self.right_grip.grip_width,
                                    self.height()+self.right_grip.grip_width*2)
        self.top_grip.setGeometry(0, 0, self.width(), self.top_grip.grip_width)
        self.bottom_grip.setGeometry(0, self.height() - self.bottom_grip.grip_width,
                                     self.width(), self.bottom_grip.grip_width)

    def setup_resizeGrips(self):
        self.left_grip = CustomGrip(self, Qt.LeftEdge, 3)
        self.right_grip = CustomGrip(self, Qt.RightEdge, 3)
        self.top_grip = CustomGrip(self, Qt.TopEdge, 3)
        self.bottom_grip = CustomGrip(self, Qt.BottomEdge, 3)

    def connect_buttons(self):
        self.button_menu.clicked.connect(self.qm_popup)
        self.button_minimize.clicked.connect(self.showMinimized)
        self.button_exit.clicked.connect(self.btn_close_clicked)
        self.button_maximize.clicked.connect(self.btn_max_clicked)
        self.button_all_songs.clicked.connect(lambda: self.tabWidget_main.setCurrentIndex(0))
        self.button_playlists.clicked.connect(lambda: self.tabWidget_main.setCurrentIndex(1))

        self.button_play_pause.clicked.connect(self.PlayStopMusic)
        self.tableWidget_all_songs.itemDoubleClicked.connect(self.StartSong)
        self.listWidget_current_playlist.itemDoubleClicked.connect(
            lambda x: self.player.go_to(self.listWidget_current_playlist.currentRow())
        )
        self.horizontalSlider_volume.valueChanged.connect(self.SendVolumeChange)
        self.horizontalSlider_speed.valueChanged.connect(self.SendSpeedChange)
        self.button_restore.clicked.connect(self.StartAllSongs)
        self.button_next_song.clicked.connect(self.player.next_audio)
        self.button_previous_song.clicked.connect(self.player.previous_audio)

        self.player.signal_audioIndexChanged.connect(lambda x: self.listWidget_current_playlist.setCurrentRow(x))

        self.listWidget_current_playlist.currentTextChanged.connect(lambda x: self.label_song_name.setText(x))

    def rescan_music(self):
        self.db.clear_songs_table()
        self.tableWidget_all_songs.clearContents()
        self.songs.clear()

        songs = []
        paths = self.db.get_paths()
        if len(paths) < 1:
            return

        for path in paths:
            for dirpath, _, files in os.walk(path):
                for file in files:
                    if fnmatch.fnmatch(file, '*.mp3'):
                        file_name = pathlib.Path(file).name
                        file_path = os.path.join(dirpath, file)
                        self.db.add_song(file_name, file_path)

        self.db.save_changes()
        db_songs = self.db.get_songs()

        self.tableWidget_all_songs.setRowCount(len(db_songs))

        for row in range(len(db_songs)):
            item = QTableWidgetItem(db_songs[row][0])
            self.tableWidget_all_songs.setItem(row, 0, item)
            self.songs.append(db_songs[row][1])

    def showSettingsWidget(self):
        if self.settingsWidget is None:
            self.settingsWidget = SettingsWidget(self)

        self.settingsWidget.show()

    def qm_popup(self):
        point = self.button_menu.mapToGlobal(self.button_menu.geometry().bottomLeft())
        qm_height = self.qMenu.size().height()
        offset = self.button_menu.size().height()
        if point.y() + qm_height > self.screen().size().height():
            point.setY(point.y() - (qm_height + offset))
        self.qMenu.popup(point)

    def MainMenuSetup(self):
        self.qMenu = QMenu(self.button_menu)

        aboutAction = QAction(self.qMenu)
        aboutAction.setText("About")
        aboutAction.triggered.connect(lambda: print("ABOUT"))

        settingsAction = QAction(self.qMenu)
        settingsAction.setText("Preferences")
        settingsAction.triggered.connect(self.showSettingsWidget)

        exitAction = QAction(self.qMenu)
        exitAction.setText("Exit")
        exitAction.triggered.connect(self.btn_close_clicked)

        rescanAction = QAction(self.qMenu)
        rescanAction.setText("Rescan music")
        rescanAction.triggered.connect(self.rescan_music)

        #self.qMenu.addAction(aboutAction)
        self.qMenu.addAction(settingsAction)
        self.qMenu.addSeparator()
        self.qMenu.addAction(rescanAction)
        self.qMenu.addSeparator()
        self.qMenu.addAction(exitAction)

        self.qMenu.adjustSize()

    def PlayStopMusic(self):
        if self.player.IsPlaying():
            self.player.signal_pauseAudio.emit()
        else:
            self.player.signal_playAudio.emit()

    def StartSong(self):
        row = self.tableWidget_all_songs.currentRow()
        song = self.songs[row]
        self.listWidget_current_playlist.clear()
        self.listWidget_current_playlist.addItem(self.tableWidget_all_songs.currentItem().text())
        self.player.set_playlist(song, from_index=row, instant_play=True)

    def StartAllSongs(self):
        self.listWidget_current_playlist.clear()
        self.listWidget_current_playlist.addItems([x[0] for x in self.db.get_songs()])
        self.player.set_playlist(self.songs, instant_play=True)

    def SendVolumeChange(self, value):
        self.signal_volumeChanged.emit(value)

    def SendSpeedChange(self, value):
        self.signal_speedChanged.emit(value)
    # endregion