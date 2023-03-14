# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QDial, QFrame,
    QGridLayout, QHBoxLayout, QHeaderView, QLabel,
    QLayout, QListWidget, QListWidgetItem, QMainWindow,
    QPushButton, QSizePolicy, QSlider, QSpacerItem,
    QStatusBar, QTabWidget, QTableWidget, QTableWidgetItem,
    QVBoxLayout, QWidget)
import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setWindowModality(Qt.NonModal)
        MainWindow.resize(988, 557)
        MainWindow.setMinimumSize(QSize(900, 550))
        MainWindow.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 75 13pt \"Century Gothic\";\n"
"selection-background-color: rgb(188, 188, 188);\n"
"selection-color: rgb(0, 0, 0);\n"
"border-color: rgb(15, 15, 15);\n"
"background-color: rgb(63, 63, 63);\n"
"alternate-background-color: rgb(188, 188, 188);\n"
"\n"
"QMenuBar::item:selected {\n"
"	background-color: rgb(188, 188, 188);\n"
"	color: rgb(0, 0, 0);\n"
"}")
        MainWindow.setDockNestingEnabled(True)
        MainWindow.setDockOptions(QMainWindow.AllowNestedDocks|QMainWindow.AllowTabbedDocks|QMainWindow.AnimatedDocks)
        self.action1 = QAction(MainWindow)
        self.action1.setObjectName(u"action1")
        self.action2 = QAction(MainWindow)
        self.action2.setObjectName(u"action2")
        self._centralwidget = QWidget(MainWindow)
        self._centralwidget.setObjectName(u"_centralwidget")
        self._central_widget_gridLayout = QGridLayout(self._centralwidget)
        self._central_widget_gridLayout.setSpacing(0)
        self._central_widget_gridLayout.setObjectName(u"_central_widget_gridLayout")
        self._central_widget_gridLayout.setSizeConstraint(QLayout.SetNoConstraint)
        self._central_widget_gridLayout.setContentsMargins(0, 0, 0, 0)
        self._centralwidget_grips = QWidget(self._centralwidget)
        self._centralwidget_grips.setObjectName(u"_centralwidget_grips")
        self._centralwidget_grips.setAutoFillBackground(False)
        self._centralwidget_grips_gridLayout = QGridLayout(self._centralwidget_grips)
        self._centralwidget_grips_gridLayout.setSpacing(0)
        self._centralwidget_grips_gridLayout.setObjectName(u"_centralwidget_grips_gridLayout")
        self._centralwidget_grips_gridLayout.setSizeConstraint(QLayout.SetNoConstraint)
        self._centralwidget_grips_gridLayout.setContentsMargins(0, 0, 0, 0)
        self.centralwidget = QWidget(self._centralwidget_grips)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setAutoFillBackground(False)
        self.centralwidget_gridLayout = QGridLayout(self.centralwidget)
        self.centralwidget_gridLayout.setSpacing(0)
        self.centralwidget_gridLayout.setObjectName(u"centralwidget_gridLayout")
        self.centralwidget_gridLayout.setContentsMargins(0, 0, 0, 0)
        self.widget_timeline = QWidget(self.centralwidget)
        self.widget_timeline.setObjectName(u"widget_timeline")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_timeline.sizePolicy().hasHeightForWidth())
        self.widget_timeline.setSizePolicy(sizePolicy)
        self.widget_timeline.setMinimumSize(QSize(0, 35))
        self.widget_timeline.setMaximumSize(QSize(16777215, 35))

        self.centralwidget_gridLayout.addWidget(self.widget_timeline, 2, 0, 1, 1)

        self.title_bar = QWidget(self.centralwidget)
        self.title_bar.setObjectName(u"title_bar")
        sizePolicy.setHeightForWidth(self.title_bar.sizePolicy().hasHeightForWidth())
        self.title_bar.setSizePolicy(sizePolicy)
        self.title_bar_horizontalLayout = QHBoxLayout(self.title_bar)
        self.title_bar_horizontalLayout.setSpacing(0)
        self.title_bar_horizontalLayout.setObjectName(u"title_bar_horizontalLayout")
        self.title_bar_horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.button_menu = QPushButton(self.title_bar)
        self.button_menu.setObjectName(u"button_menu")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.MinimumExpanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.button_menu.sizePolicy().hasHeightForWidth())
        self.button_menu.setSizePolicy(sizePolicy1)
        self.button_menu.setMinimumSize(QSize(100, 30))
        self.button_menu.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(60, 60, 60);\n"
"	border-bottom-right-radius: 10%;\n"
"    border: 1px solid rgb(188, 188, 188);\n"
"	font-size: 16pt;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(188, 188, 188);\n"
"	color: rgb(0, 0, 0);\n"
"}")

        self.title_bar_horizontalLayout.addWidget(self.button_menu)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.title_bar_horizontalLayout.addItem(self.horizontalSpacer)

        self.widget_header_buttons = QWidget(self.title_bar)
        self.widget_header_buttons.setObjectName(u"widget_header_buttons")
        self.widget_header_buttons.setMinimumSize(QSize(90, 30))
        self.widget_header_buttons.setMaximumSize(QSize(30, 30))
        self.widget_header_buttons.setLayoutDirection(Qt.LeftToRight)
        self.widget_header_buttons_horizontalLayout = QHBoxLayout(self.widget_header_buttons)
        self.widget_header_buttons_horizontalLayout.setSpacing(0)
        self.widget_header_buttons_horizontalLayout.setObjectName(u"widget_header_buttons_horizontalLayout")
        self.widget_header_buttons_horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.button_minimize = QPushButton(self.widget_header_buttons)
        self.button_minimize.setObjectName(u"button_minimize")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.MinimumExpanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.button_minimize.sizePolicy().hasHeightForWidth())
        self.button_minimize.setSizePolicy(sizePolicy2)
        self.button_minimize.setMinimumSize(QSize(30, 30))
        self.button_minimize.setMaximumSize(QSize(30, 30))
        self.button_minimize.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(60, 60, 60);\n"
"	border-bottom-left-radius: 10%;\n"
"	border-bottom-right-radius: 10%;\n"
"    border: 0px solid rgb(188, 188, 188);\n"
"	font-size: 16pt;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(188, 188, 188);\n"
"	color: rgb(0, 0, 0);\n"
"}")
        icon = QIcon()
        icon.addFile(u":/icons/assets/mini.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.button_minimize.setIcon(icon)
        self.button_minimize.setIconSize(QSize(24, 24))

        self.widget_header_buttons_horizontalLayout.addWidget(self.button_minimize)

        self.button_maximize = QPushButton(self.widget_header_buttons)
        self.button_maximize.setObjectName(u"button_maximize")
        sizePolicy2.setHeightForWidth(self.button_maximize.sizePolicy().hasHeightForWidth())
        self.button_maximize.setSizePolicy(sizePolicy2)
        self.button_maximize.setMinimumSize(QSize(30, 30))
        self.button_maximize.setMaximumSize(QSize(30, 30))
        self.button_maximize.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(60, 60, 60);\n"
"	border-bottom-left-radius: 10%;\n"
"	border-bottom-right-radius: 10%;\n"
"    border: 0px solid rgb(188, 188, 188);\n"
"	font-size: 16pt;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(188, 188, 188);\n"
"	color: rgb(0, 0, 0);\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u":/icons/assets/full_screen.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.button_maximize.setIcon(icon1)
        self.button_maximize.setIconSize(QSize(24, 24))

        self.widget_header_buttons_horizontalLayout.addWidget(self.button_maximize)

        self.button_exit = QPushButton(self.widget_header_buttons)
        self.button_exit.setObjectName(u"button_exit")
        sizePolicy2.setHeightForWidth(self.button_exit.sizePolicy().hasHeightForWidth())
        self.button_exit.setSizePolicy(sizePolicy2)
        self.button_exit.setMinimumSize(QSize(30, 30))
        self.button_exit.setMaximumSize(QSize(30, 30))
        self.button_exit.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(60, 60, 60);\n"
"	border-bottom-left-radius: 10%;\n"
"    border: 0px solid rgb(188, 188, 188);\n"
"	font-size: 16pt;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(188, 188, 188);\n"
"	color: rgb(0, 0, 0);\n"
"}")
        icon2 = QIcon()
        icon2.addFile(u":/icons/assets/close.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.button_exit.setIcon(icon2)
        self.button_exit.setIconSize(QSize(24, 24))

        self.widget_header_buttons_horizontalLayout.addWidget(self.button_exit)


        self.title_bar_horizontalLayout.addWidget(self.widget_header_buttons)


        self.centralwidget_gridLayout.addWidget(self.title_bar, 0, 0, 1, 1)

        self.widget_bottom = QWidget(self.centralwidget)
        self.widget_bottom.setObjectName(u"widget_bottom")
        self.widget_bottom_horizontalLayout = QHBoxLayout(self.widget_bottom)
        self.widget_bottom_horizontalLayout.setSpacing(0)
        self.widget_bottom_horizontalLayout.setObjectName(u"widget_bottom_horizontalLayout")
        self.widget_bottom_horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.widget_tabs = QWidget(self.widget_bottom)
        self.widget_tabs.setObjectName(u"widget_tabs")
        sizePolicy3 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.widget_tabs.sizePolicy().hasHeightForWidth())
        self.widget_tabs.setSizePolicy(sizePolicy3)
        self.widget_tabs.setMinimumSize(QSize(500, 200))
        self.widget_tabs_horizontalLayout = QHBoxLayout(self.widget_tabs)
        self.widget_tabs_horizontalLayout.setSpacing(4)
        self.widget_tabs_horizontalLayout.setObjectName(u"widget_tabs_horizontalLayout")
        self.widget_tabs_horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.widget_left_buttons = QWidget(self.widget_tabs)
        self.widget_left_buttons.setObjectName(u"widget_left_buttons")
        sizePolicy4 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Expanding)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.widget_left_buttons.sizePolicy().hasHeightForWidth())
        self.widget_left_buttons.setSizePolicy(sizePolicy4)
        self.widget_left_buttons.setMinimumSize(QSize(120, 0))
        self.widget_left_buttons.setMaximumSize(QSize(120, 16777215))
        self.widget_left_buttons.setLayoutDirection(Qt.LeftToRight)
        self.widget_left_buttons_verticalLayout = QVBoxLayout(self.widget_left_buttons)
        self.widget_left_buttons_verticalLayout.setSpacing(5)
        self.widget_left_buttons_verticalLayout.setObjectName(u"widget_left_buttons_verticalLayout")
        self.widget_left_buttons_verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.button_all_songs = QPushButton(self.widget_left_buttons)
        self.button_all_songs.setObjectName(u"button_all_songs")
        sizePolicy.setHeightForWidth(self.button_all_songs.sizePolicy().hasHeightForWidth())
        self.button_all_songs.setSizePolicy(sizePolicy)
        self.button_all_songs.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(60, 60, 60);\n"
"    border: 1px solid rgb(188, 188, 188);\n"
"	border-left: 0px solid;\n"
"	border-top-right-radius: 10%;\n"
"	border-bottom-right-radius: 10%;\n"
"	font-size: 16pt;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(188, 188, 188);\n"
"	color: rgb(0, 0, 0);\n"
"}")
        self.button_all_songs.setCheckable(False)
        self.button_all_songs.setAutoExclusive(False)
        self.button_all_songs.setAutoDefault(False)

        self.widget_left_buttons_verticalLayout.addWidget(self.button_all_songs)

        self.button_playlists = QPushButton(self.widget_left_buttons)
        self.button_playlists.setObjectName(u"button_playlists")
        sizePolicy.setHeightForWidth(self.button_playlists.sizePolicy().hasHeightForWidth())
        self.button_playlists.setSizePolicy(sizePolicy)
        self.button_playlists.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(60, 60, 60);\n"
"    border: 1px solid rgb(188, 188, 188);\n"
"	border-left: 0px solid;\n"
"	border-top-right-radius: 10%;\n"
"	border-bottom-right-radius: 10%;\n"
"	font-size: 16pt;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(188, 188, 188);\n"
"	color: rgb(0, 0, 0);\n"
"}")

        self.widget_left_buttons_verticalLayout.addWidget(self.button_playlists)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.widget_left_buttons_verticalLayout.addItem(self.verticalSpacer)


        self.widget_tabs_horizontalLayout.addWidget(self.widget_left_buttons)

        self.tabWidget_main = QTabWidget(self.widget_tabs)
        self.tabWidget_main.setObjectName(u"tabWidget_main")
        self.tabWidget_main.setStyleSheet(u"QTabBar {\n"
"	font: 13pt \"Century Gothic\";\n"
"	border: 0px solid;\n"
"	width: 1px;\n"
"}\n"
"\n"
"QTabBar:tab {\n"
"	font: 13pt \"Century Gothic\";\n"
"	background-color: rgb(63, 63, 63);\n"
"	width: 0px;\n"
"\n"
"}\n"
"QTabBar:tab:hover {\n"
"	background-color: rgb(188, 188, 188);\n"
"	color: rgb(0, 0, 0)\n"
"}\n"
"QTabBar:tab:selected {\n"
"	background-color: rgb(160, 160, 160);\n"
"	color: rgb(12, 12, 12);\n"
"}\n"
"\n"
"QTabWidget::pane {}")
        self.tabWidget_main.setTabPosition(QTabWidget.West)
        self.tabWidget_main.setTabShape(QTabWidget.Rounded)
        self.tabWidget_main.setIconSize(QSize(0, 0))
        self.tabWidget_main.setUsesScrollButtons(False)
        self.tab_all_songs = QWidget()
        self.tab_all_songs.setObjectName(u"tab_all_songs")
        self.tab_all_songs_gridLayout = QGridLayout(self.tab_all_songs)
        self.tab_all_songs_gridLayout.setSpacing(0)
        self.tab_all_songs_gridLayout.setObjectName(u"tab_all_songs_gridLayout")
        self.tab_all_songs_gridLayout.setContentsMargins(0, 0, 0, 0)
        self.tableWidget_all_songs = QTableWidget(self.tab_all_songs)
        if (self.tableWidget_all_songs.columnCount() < 1):
            self.tableWidget_all_songs.setColumnCount(1)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget_all_songs.setHorizontalHeaderItem(0, __qtablewidgetitem)
        self.tableWidget_all_songs.setObjectName(u"tableWidget_all_songs")
        self.tableWidget_all_songs.setMinimumSize(QSize(501, 0))
        self.tableWidget_all_songs.setStyleSheet(u"QHeaderView {\n"
"	background: transparent;\n"
"	border: 0px solid;\n"
"}\n"
"\n"
"QHeaderView::section {\n"
"	background-color: rgb(63, 63, 63);\n"
"	color: white;\n"
"	border: 0px solid;\n"
"}\n"
"\n"
"QTableCornerButton::section {\n"
"	background-color: rgb(63,63, 63);\n"
"	border: 0px solid;\n"
"}")
        self.tableWidget_all_songs.setFrameShape(QFrame.StyledPanel)
        self.tableWidget_all_songs.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.tableWidget_all_songs.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.tableWidget_all_songs.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableWidget_all_songs.setTabKeyNavigation(False)
        self.tableWidget_all_songs.setDragDropOverwriteMode(False)
        self.tableWidget_all_songs.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tableWidget_all_songs.setShowGrid(False)
        self.tableWidget_all_songs.setSortingEnabled(True)
        self.tableWidget_all_songs.horizontalHeader().setVisible(True)
        self.tableWidget_all_songs.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget_all_songs.horizontalHeader().setProperty("showSortIndicator", True)
        self.tableWidget_all_songs.horizontalHeader().setStretchLastSection(True)
        self.tableWidget_all_songs.verticalHeader().setVisible(False)
        self.tableWidget_all_songs.verticalHeader().setHighlightSections(False)

        self.tab_all_songs_gridLayout.addWidget(self.tableWidget_all_songs, 0, 0, 1, 1)

        self.tabWidget_main.addTab(self.tab_all_songs, "")
        self.tab_all_playlists = QWidget()
        self.tab_all_playlists.setObjectName(u"tab_all_playlists")
        self.tabWidget_main.addTab(self.tab_all_playlists, "")

        self.widget_tabs_horizontalLayout.addWidget(self.tabWidget_main)


        self.widget_bottom_horizontalLayout.addWidget(self.widget_tabs)

        self.widget_current_playlist = QWidget(self.widget_bottom)
        self.widget_current_playlist.setObjectName(u"widget_current_playlist")
        sizePolicy4.setHeightForWidth(self.widget_current_playlist.sizePolicy().hasHeightForWidth())
        self.widget_current_playlist.setSizePolicy(sizePolicy4)
        self.widget_current_playlist.setMinimumSize(QSize(250, 0))
        self.widget_current_playlist_verticalLayout = QVBoxLayout(self.widget_current_playlist)
        self.widget_current_playlist_verticalLayout.setSpacing(0)
        self.widget_current_playlist_verticalLayout.setObjectName(u"widget_current_playlist_verticalLayout")
        self.widget_current_playlist_verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.label_currently_playing = QLabel(self.widget_current_playlist)
        self.label_currently_playing.setObjectName(u"label_currently_playing")
        sizePolicy5 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.label_currently_playing.sizePolicy().hasHeightForWidth())
        self.label_currently_playing.setSizePolicy(sizePolicy5)
        self.label_currently_playing.setMinimumSize(QSize(250, 30))
        self.label_currently_playing.setMaximumSize(QSize(250, 30))
        font = QFont()
        font.setFamilies([u"Century Gothic"])
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setStrikeOut(False)
        font.setKerning(True)
        font.setStyleStrategy(QFont.PreferDefault)
        self.label_currently_playing.setFont(font)
        self.label_currently_playing.setStyleSheet(u"QLabel {\n"
"	background-color: rgb(60, 60, 60);\n"
"    border: 1px solid rgb(188, 188, 188);\n"
"	border-left: 2px solid rgb(188, 188, 188);\n"
"	font-size: 16pt;\n"
"}")
        self.label_currently_playing.setAlignment(Qt.AlignCenter)

        self.widget_current_playlist_verticalLayout.addWidget(self.label_currently_playing)

        self.listWidget = QListWidget(self.widget_current_playlist)
        self.listWidget.setObjectName(u"listWidget")
        sizePolicy4.setHeightForWidth(self.listWidget.sizePolicy().hasHeightForWidth())
        self.listWidget.setSizePolicy(sizePolicy4)
        self.listWidget.setMaximumSize(QSize(250, 16777215))

        self.widget_current_playlist_verticalLayout.addWidget(self.listWidget)


        self.widget_bottom_horizontalLayout.addWidget(self.widget_current_playlist)


        self.centralwidget_gridLayout.addWidget(self.widget_bottom, 3, 0, 1, 1)

        self.widget_player = QWidget(self.centralwidget)
        self.widget_player.setObjectName(u"widget_player")
        sizePolicy.setHeightForWidth(self.widget_player.sizePolicy().hasHeightForWidth())
        self.widget_player.setSizePolicy(sizePolicy)
        self.widget_player.setMinimumSize(QSize(0, 90))
        self.widget_player.setMaximumSize(QSize(16777215, 90))
        self.widget_player_gridLayout = QGridLayout(self.widget_player)
        self.widget_player_gridLayout.setSpacing(0)
        self.widget_player_gridLayout.setObjectName(u"widget_player_gridLayout")
        self.widget_player_gridLayout.setContentsMargins(0, 0, 0, 0)
        self.widget_song_info = QWidget(self.widget_player)
        self.widget_song_info.setObjectName(u"widget_song_info")
        sizePolicy6 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.widget_song_info.sizePolicy().hasHeightForWidth())
        self.widget_song_info.setSizePolicy(sizePolicy6)
        self.widget_song_info.setMinimumSize(QSize(350, 90))
        self.widget_song_info.setMaximumSize(QSize(16777215, 90))
        self.widget_song_info_horizontalLayout = QHBoxLayout(self.widget_song_info)
        self.widget_song_info_horizontalLayout.setSpacing(10)
        self.widget_song_info_horizontalLayout.setObjectName(u"widget_song_info_horizontalLayout")
        self.widget_song_info_horizontalLayout.setContentsMargins(5, 5, 5, 5)
        self.label_song_icon = QLabel(self.widget_song_info)
        self.label_song_icon.setObjectName(u"label_song_icon")
        self.label_song_icon.setMinimumSize(QSize(80, 80))
        self.label_song_icon.setMaximumSize(QSize(80, 80))

        self.widget_song_info_horizontalLayout.addWidget(self.label_song_icon)

        self.label_song_name = QLabel(self.widget_song_info)
        self.label_song_name.setObjectName(u"label_song_name")
        self.label_song_name.setMinimumSize(QSize(0, 80))
        self.label_song_name.setMaximumSize(QSize(16777215, 80))
        self.label_song_name.setWordWrap(True)

        self.widget_song_info_horizontalLayout.addWidget(self.label_song_name)


        self.widget_player_gridLayout.addWidget(self.widget_song_info, 0, 0, 1, 1)

        self.widget_song_parameters = QWidget(self.widget_player)
        self.widget_song_parameters.setObjectName(u"widget_song_parameters")
        sizePolicy7 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.widget_song_parameters.sizePolicy().hasHeightForWidth())
        self.widget_song_parameters.setSizePolicy(sizePolicy7)
        self.widget_song_parameters.setMinimumSize(QSize(350, 90))
        self.widget_song_parameters.setMaximumSize(QSize(16777215, 90))
        self.widget_song_parameters.setStyleSheet(u"border: 0px solid")
        self.widget_song_parameters_horizontalLayout = QHBoxLayout(self.widget_song_parameters)
        self.widget_song_parameters_horizontalLayout.setSpacing(0)
        self.widget_song_parameters_horizontalLayout.setObjectName(u"widget_song_parameters_horizontalLayout")
        self.widget_song_parameters_horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.widget_song_parameters_horizontalLayout.addItem(self.horizontalSpacer_2)

        self.tabWidget_song_parameters = QTabWidget(self.widget_song_parameters)
        self.tabWidget_song_parameters.setObjectName(u"tabWidget_song_parameters")
        self.tabWidget_song_parameters.setMinimumSize(QSize(350, 90))
        self.tabWidget_song_parameters.setMaximumSize(QSize(350, 90))
        self.tabWidget_song_parameters.setLayoutDirection(Qt.LeftToRight)
        self.tabWidget_song_parameters.setStyleSheet(u"QTabBar {\n"
"	font: 13pt \"Century Gothic\";\n"
"	border: 0px solid;\n"
"}\n"
"\n"
"QTabBar:tab {\n"
"	font: 13pt \"Century Gothic\";\n"
"	background-color: rgb(63, 63, 63);\n"
"	height: 0px;\n"
"\n"
"}\n"
"QTabBar:tab:hover {\n"
"	background-color: rgb(188, 188, 188);\n"
"	color: rgb(0, 0, 0)\n"
"}\n"
"QTabBar:tab:selected {\n"
"	background-color: rgb(160, 160, 160);\n"
"	color: rgb(12, 12, 12);\n"
"}\n"
"\n"
"QTabWidget::pane {}")
        self.tabWidget_song_parameters.setIconSize(QSize(0, 0))
        self.tabWidget_song_parameters.setUsesScrollButtons(False)
        self.tab_song_parameters_dials = QWidget()
        self.tab_song_parameters_dials.setObjectName(u"tab_song_parameters_dials")
        self.tab_song_parameters_dials_gridLayout = QGridLayout(self.tab_song_parameters_dials)
        self.tab_song_parameters_dials_gridLayout.setSpacing(0)
        self.tab_song_parameters_dials_gridLayout.setObjectName(u"tab_song_parameters_dials_gridLayout")
        self.tab_song_parameters_dials_gridLayout.setContentsMargins(0, 0, 0, 0)
        self.widget_dial_volume = QWidget(self.tab_song_parameters_dials)
        self.widget_dial_volume.setObjectName(u"widget_dial_volume")
        self.widget_dial_volume.setMinimumSize(QSize(175, 0))
        self.widget_dial_volume_gridLayout = QGridLayout(self.widget_dial_volume)
        self.widget_dial_volume_gridLayout.setSpacing(0)
        self.widget_dial_volume_gridLayout.setObjectName(u"widget_dial_volume_gridLayout")
        self.widget_dial_volume_gridLayout.setContentsMargins(0, 0, 0, 0)
        self.label_volume_dial = QLabel(self.widget_dial_volume)
        self.label_volume_dial.setObjectName(u"label_volume_dial")
        sizePolicy6.setHeightForWidth(self.label_volume_dial.sizePolicy().hasHeightForWidth())
        self.label_volume_dial.setSizePolicy(sizePolicy6)
        self.label_volume_dial.setMinimumSize(QSize(60, 0))
        self.label_volume_dial.setMaximumSize(QSize(100, 80))
        font1 = QFont()
        font1.setFamilies([u"Century Gothic"])
        font1.setPointSize(13)
        font1.setBold(False)
        font1.setItalic(False)
        self.label_volume_dial.setFont(font1)
        self.label_volume_dial.setScaledContents(False)
        self.label_volume_dial.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_volume_dial.setMargin(0)

        self.widget_dial_volume_gridLayout.addWidget(self.label_volume_dial, 0, 0, 1, 1)

        self.dial_volume = QDial(self.widget_dial_volume)
        self.dial_volume.setObjectName(u"dial_volume")
        self.dial_volume.setMinimumSize(QSize(60, 60))
        self.dial_volume.setMaximumSize(QSize(80, 80))
        self.dial_volume.setMaximum(100)
        self.dial_volume.setValue(100)
        self.dial_volume.setTracking(True)
        self.dial_volume.setOrientation(Qt.Horizontal)
        self.dial_volume.setInvertedAppearance(False)
        self.dial_volume.setInvertedControls(False)
        self.dial_volume.setWrapping(False)
        self.dial_volume.setNotchesVisible(True)

        self.widget_dial_volume_gridLayout.addWidget(self.dial_volume, 0, 1, 1, 1)


        self.tab_song_parameters_dials_gridLayout.addWidget(self.widget_dial_volume, 0, 0, 1, 1)

        self.widget_dial_speed = QWidget(self.tab_song_parameters_dials)
        self.widget_dial_speed.setObjectName(u"widget_dial_speed")
        self.widget_dial_speed.setMinimumSize(QSize(175, 0))
        self.widget_dial_speed_gridLayout = QGridLayout(self.widget_dial_speed)
        self.widget_dial_speed_gridLayout.setSpacing(0)
        self.widget_dial_speed_gridLayout.setObjectName(u"widget_dial_speed_gridLayout")
        self.widget_dial_speed_gridLayout.setContentsMargins(0, 0, 0, 0)
        self.dial_speed = QDial(self.widget_dial_speed)
        self.dial_speed.setObjectName(u"dial_speed")
        self.dial_speed.setMinimumSize(QSize(60, 60))
        self.dial_speed.setMaximumSize(QSize(90, 90))
        self.dial_speed.setMaximum(100)
        self.dial_speed.setValue(100)
        self.dial_speed.setTracking(True)
        self.dial_speed.setOrientation(Qt.Horizontal)
        self.dial_speed.setInvertedAppearance(False)
        self.dial_speed.setWrapping(False)
        self.dial_speed.setNotchesVisible(True)

        self.widget_dial_speed_gridLayout.addWidget(self.dial_speed, 0, 0, 1, 1)

        self.label_speed_dial = QLabel(self.widget_dial_speed)
        self.label_speed_dial.setObjectName(u"label_speed_dial")
        sizePolicy6.setHeightForWidth(self.label_speed_dial.sizePolicy().hasHeightForWidth())
        self.label_speed_dial.setSizePolicy(sizePolicy6)
        self.label_speed_dial.setMinimumSize(QSize(100, 0))
        self.label_speed_dial.setMaximumSize(QSize(16777215, 80))
        self.label_speed_dial.setFont(font1)
        self.label_speed_dial.setLayoutDirection(Qt.LeftToRight)
        self.label_speed_dial.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.widget_dial_speed_gridLayout.addWidget(self.label_speed_dial, 0, 1, 1, 2)


        self.tab_song_parameters_dials_gridLayout.addWidget(self.widget_dial_speed, 0, 1, 1, 1)

        self.tabWidget_song_parameters.addTab(self.tab_song_parameters_dials, "")
        self.tab_song_parameters_sliders = QWidget()
        self.tab_song_parameters_sliders.setObjectName(u"tab_song_parameters_sliders")
        self.tab_song_parameters_sliders.setStyleSheet(u"border: 0px solid;")
        self.tab_song_parameters_sliders_gridLayout = QGridLayout(self.tab_song_parameters_sliders)
        self.tab_song_parameters_sliders_gridLayout.setObjectName(u"tab_song_parameters_sliders_gridLayout")
        self.tab_song_parameters_sliders_gridLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.tab_song_parameters_sliders_gridLayout.setHorizontalSpacing(5)
        self.tab_song_parameters_sliders_gridLayout.setVerticalSpacing(0)
        self.tab_song_parameters_sliders_gridLayout.setContentsMargins(2, 0, 5, 0)
        self.label_speed_slider = QLabel(self.tab_song_parameters_sliders)
        self.label_speed_slider.setObjectName(u"label_speed_slider")
        self.label_speed_slider.setMinimumSize(QSize(0, 40))
        self.label_speed_slider.setMaximumSize(QSize(16777215, 45))
        self.label_speed_slider.setFont(font1)
        self.label_speed_slider.setStyleSheet(u"QLabel {\n"
"	background-color: rgb(60, 60, 60);\n"
"}")

        self.tab_song_parameters_sliders_gridLayout.addWidget(self.label_speed_slider, 1, 1, 1, 1)

        self.label_volume_slider = QLabel(self.tab_song_parameters_sliders)
        self.label_volume_slider.setObjectName(u"label_volume_slider")
        self.label_volume_slider.setMinimumSize(QSize(0, 40))
        self.label_volume_slider.setMaximumSize(QSize(16777215, 45))
        self.label_volume_slider.setFont(font1)
        self.label_volume_slider.setStyleSheet(u"QLabel {\n"
"	background-color: rgb(60, 60, 60);\n"
"}")

        self.tab_song_parameters_sliders_gridLayout.addWidget(self.label_volume_slider, 0, 1, 1, 1)

        self.horizontalSlider_volume = QSlider(self.tab_song_parameters_sliders)
        self.horizontalSlider_volume.setObjectName(u"horizontalSlider_volume")
        self.horizontalSlider_volume.setMinimumSize(QSize(0, 40))
        self.horizontalSlider_volume.setMaximumSize(QSize(16777215, 45))
        self.horizontalSlider_volume.setFont(font1)
        self.horizontalSlider_volume.setMaximum(100)
        self.horizontalSlider_volume.setValue(100)
        self.horizontalSlider_volume.setOrientation(Qt.Horizontal)
        self.horizontalSlider_volume.setInvertedControls(False)
        self.horizontalSlider_volume.setTickPosition(QSlider.TicksAbove)
        self.horizontalSlider_volume.setTickInterval(10)

        self.tab_song_parameters_sliders_gridLayout.addWidget(self.horizontalSlider_volume, 0, 0, 1, 1)

        self.horizontalSlider_speed = QSlider(self.tab_song_parameters_sliders)
        self.horizontalSlider_speed.setObjectName(u"horizontalSlider_speed")
        self.horizontalSlider_speed.setEnabled(False)
        self.horizontalSlider_speed.setMinimumSize(QSize(0, 40))
        self.horizontalSlider_speed.setMaximumSize(QSize(16777215, 45))
        self.horizontalSlider_speed.setMinimum(25)
        self.horizontalSlider_speed.setMaximum(200)
        self.horizontalSlider_speed.setSingleStep(25)
        self.horizontalSlider_speed.setPageStep(0)
        self.horizontalSlider_speed.setValue(100)
        self.horizontalSlider_speed.setSliderPosition(100)
        self.horizontalSlider_speed.setTracking(True)
        self.horizontalSlider_speed.setOrientation(Qt.Horizontal)
        self.horizontalSlider_speed.setTickPosition(QSlider.TicksBelow)
        self.horizontalSlider_speed.setTickInterval(25)

        self.tab_song_parameters_sliders_gridLayout.addWidget(self.horizontalSlider_speed, 1, 0, 1, 1)

        self.tab_song_parameters_sliders_gridLayout.setRowStretch(0, 1)
        self.tab_song_parameters_sliders_gridLayout.setRowStretch(1, 1)
        self.tabWidget_song_parameters.addTab(self.tab_song_parameters_sliders, "")

        self.widget_song_parameters_horizontalLayout.addWidget(self.tabWidget_song_parameters)


        self.widget_player_gridLayout.addWidget(self.widget_song_parameters, 0, 2, 1, 1)

        self.song_control_buttons = QWidget(self.widget_player)
        self.song_control_buttons.setObjectName(u"song_control_buttons")
        sizePolicy8 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy8.setHorizontalStretch(0)
        sizePolicy8.setVerticalStretch(0)
        sizePolicy8.setHeightForWidth(self.song_control_buttons.sizePolicy().hasHeightForWidth())
        self.song_control_buttons.setSizePolicy(sizePolicy8)
        self.song_control_buttons.setMinimumSize(QSize(200, 90))
        self.song_control_buttons.setMaximumSize(QSize(200, 90))
        self.song_control_buttons_gridLayout = QGridLayout(self.song_control_buttons)
        self.song_control_buttons_gridLayout.setObjectName(u"song_control_buttons_gridLayout")
        self.song_control_buttons_gridLayout.setHorizontalSpacing(10)
        self.song_control_buttons_gridLayout.setVerticalSpacing(0)
        self.song_control_buttons_gridLayout.setContentsMargins(0, 0, 0, 0)
        self.widget_restore_repeat_shuffle = QWidget(self.song_control_buttons)
        self.widget_restore_repeat_shuffle.setObjectName(u"widget_restore_repeat_shuffle")
        sizePolicy8.setHeightForWidth(self.widget_restore_repeat_shuffle.sizePolicy().hasHeightForWidth())
        self.widget_restore_repeat_shuffle.setSizePolicy(sizePolicy8)
        self.widget_restore_repeat_shuffle.setMinimumSize(QSize(0, 40))
        self.widget_restore_repeat_shuffle.setMaximumSize(QSize(16777215, 40))
        self.gridLayout_2 = QGridLayout(self.widget_restore_repeat_shuffle)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setHorizontalSpacing(17)
        self.gridLayout_2.setVerticalSpacing(0)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.button_restore = QPushButton(self.widget_restore_repeat_shuffle)
        self.button_restore.setObjectName(u"button_restore")
        self.button_restore.setMaximumSize(QSize(30, 30))
        self.button_restore.setCursor(QCursor(Qt.PointingHandCursor))
        self.button_restore.setStyleSheet(u"QPushButton {\n"
"	background-color: rgba(255, 255, 255, 0);\n"
"}")
        icon3 = QIcon()
        icon3.addFile(u":/icons/assets/reset.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.button_restore.setIcon(icon3)
        self.button_restore.setIconSize(QSize(30, 30))

        self.gridLayout_2.addWidget(self.button_restore, 0, 0, 1, 1)

        self.button_repeat = QPushButton(self.widget_restore_repeat_shuffle)
        self.button_repeat.setObjectName(u"button_repeat")
        self.button_repeat.setMaximumSize(QSize(30, 30))
        self.button_repeat.setCursor(QCursor(Qt.PointingHandCursor))
        self.button_repeat.setStyleSheet(u"QPushButton {\n"
"	background-color: rgba(255, 255, 255, 0);\n"
"}")
        icon4 = QIcon()
        icon4.addFile(u":/icons/assets/repeat.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.button_repeat.setIcon(icon4)
        self.button_repeat.setIconSize(QSize(30, 30))

        self.gridLayout_2.addWidget(self.button_repeat, 0, 1, 1, 1)

        self.button_shuffle = QPushButton(self.widget_restore_repeat_shuffle)
        self.button_shuffle.setObjectName(u"button_shuffle")
        self.button_shuffle.setMaximumSize(QSize(30, 30))
        self.button_shuffle.setCursor(QCursor(Qt.PointingHandCursor))
        self.button_shuffle.setStyleSheet(u"QPushButton {\n"
"	background-color: rgba(255, 255, 255, 0);\n"
"}")

        self.gridLayout_2.addWidget(self.button_shuffle, 0, 2, 1, 1)


        self.song_control_buttons_gridLayout.addWidget(self.widget_restore_repeat_shuffle, 1, 0, 1, 2)

        self.widget_prev_play_next = QWidget(self.song_control_buttons)
        self.widget_prev_play_next.setObjectName(u"widget_prev_play_next")
        sizePolicy8.setHeightForWidth(self.widget_prev_play_next.sizePolicy().hasHeightForWidth())
        self.widget_prev_play_next.setSizePolicy(sizePolicy8)
        self.widget_prev_play_next.setMinimumSize(QSize(0, 50))
        self.widget_prev_play_next.setMaximumSize(QSize(16777215, 50))
        self.gridLayout = QGridLayout(self.widget_prev_play_next)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setHorizontalSpacing(10)
        self.gridLayout.setVerticalSpacing(0)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.button_previous_song = QPushButton(self.widget_prev_play_next)
        self.button_previous_song.setObjectName(u"button_previous_song")
        sizePolicy5.setHeightForWidth(self.button_previous_song.sizePolicy().hasHeightForWidth())
        self.button_previous_song.setSizePolicy(sizePolicy5)
        self.button_previous_song.setMinimumSize(QSize(40, 40))
        self.button_previous_song.setMaximumSize(QSize(40, 40))
        self.button_previous_song.setCursor(QCursor(Qt.PointingHandCursor))
        self.button_previous_song.setStyleSheet(u"QPushButton {\n"
"	background-color: rgba(255, 255, 255, 0);\n"
"}")
        icon5 = QIcon()
        icon5.addFile(u":/icons/assets/backward.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.button_previous_song.setIcon(icon5)
        self.button_previous_song.setIconSize(QSize(50, 50))

        self.gridLayout.addWidget(self.button_previous_song, 0, 0, 1, 1)

        self.button_play_pause = QPushButton(self.widget_prev_play_next)
        self.button_play_pause.setObjectName(u"button_play_pause")
        sizePolicy5.setHeightForWidth(self.button_play_pause.sizePolicy().hasHeightForWidth())
        self.button_play_pause.setSizePolicy(sizePolicy5)
        self.button_play_pause.setMinimumSize(QSize(50, 50))
        self.button_play_pause.setMaximumSize(QSize(50, 50))
        self.button_play_pause.setCursor(QCursor(Qt.PointingHandCursor))
        self.button_play_pause.setStyleSheet(u"QPushButton {\n"
"	background-color: rgba(255, 255, 255, 0);\n"
"}")
        icon6 = QIcon()
        icon6.addFile(u":/icons/assets/play.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.button_play_pause.setIcon(icon6)
        self.button_play_pause.setIconSize(QSize(80, 80))

        self.gridLayout.addWidget(self.button_play_pause, 0, 1, 1, 1)

        self.button_next_song = QPushButton(self.widget_prev_play_next)
        self.button_next_song.setObjectName(u"button_next_song")
        sizePolicy5.setHeightForWidth(self.button_next_song.sizePolicy().hasHeightForWidth())
        self.button_next_song.setSizePolicy(sizePolicy5)
        self.button_next_song.setMinimumSize(QSize(40, 40))
        self.button_next_song.setMaximumSize(QSize(40, 40))
        self.button_next_song.setCursor(QCursor(Qt.PointingHandCursor))
        self.button_next_song.setStyleSheet(u"QPushButton {\n"
"	background-color: rgba(255, 255, 255, 0);\n"
"}")
        icon7 = QIcon()
        icon7.addFile(u":/icons/assets/forwad.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.button_next_song.setIcon(icon7)
        self.button_next_song.setIconSize(QSize(50, 50))

        self.gridLayout.addWidget(self.button_next_song, 0, 2, 1, 1)


        self.song_control_buttons_gridLayout.addWidget(self.widget_prev_play_next, 0, 0, 1, 2)


        self.widget_player_gridLayout.addWidget(self.song_control_buttons, 0, 1, 1, 1)

        self.widget_player_gridLayout.setColumnStretch(0, 1)
        self.widget_player_gridLayout.setColumnStretch(1, 1)
        self.widget_player_gridLayout.setColumnStretch(2, 1)

        self.centralwidget_gridLayout.addWidget(self.widget_player, 1, 0, 1, 1)


        self._centralwidget_grips_gridLayout.addWidget(self.centralwidget, 0, 0, 1, 1)


        self._central_widget_gridLayout.addWidget(self._centralwidget_grips, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self._centralwidget)
        self.statusBar = QStatusBar(MainWindow)
        self.statusBar.setObjectName(u"statusBar")
        sizePolicy.setHeightForWidth(self.statusBar.sizePolicy().hasHeightForWidth())
        self.statusBar.setSizePolicy(sizePolicy)
        self.statusBar.setMinimumSize(QSize(0, 5))
        self.statusBar.setMaximumSize(QSize(16777215, 5))
        self.statusBar.setSizeGripEnabled(False)
        MainWindow.setStatusBar(self.statusBar)

        self.retranslateUi(MainWindow)

        self.tabWidget_main.setCurrentIndex(0)
        self.tabWidget_song_parameters.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.action1.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.action2.setText(QCoreApplication.translate("MainWindow", u"2", None))
        self.button_menu.setText(QCoreApplication.translate("MainWindow", u"Menu", None))
        self.button_minimize.setText("")
        self.button_maximize.setText("")
        self.button_exit.setText("")
        self.button_all_songs.setText(QCoreApplication.translate("MainWindow", u"Songs", None))
        self.button_playlists.setText(QCoreApplication.translate("MainWindow", u"Playlists", None))
        ___qtablewidgetitem = self.tableWidget_all_songs.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"FileName", None));
        self.tabWidget_main.setTabText(self.tabWidget_main.indexOf(self.tab_all_songs), QCoreApplication.translate("MainWindow", u"Page", None))
        self.tabWidget_main.setTabText(self.tabWidget_main.indexOf(self.tab_all_playlists), QCoreApplication.translate("MainWindow", u"Page", None))
        self.label_currently_playing.setText(QCoreApplication.translate("MainWindow", u"CURRENT PLAYLIST", None))
        self.label_song_icon.setText("")
        self.label_song_name.setText("")
        self.label_volume_dial.setText(QCoreApplication.translate("MainWindow", u"Volume", None))
        self.label_speed_dial.setText(QCoreApplication.translate("MainWindow", u"Speed", None))
        self.tabWidget_song_parameters.setTabText(self.tabWidget_song_parameters.indexOf(self.tab_song_parameters_dials), QCoreApplication.translate("MainWindow", u"Tab 1", None))
        self.label_speed_slider.setText(QCoreApplication.translate("MainWindow", u"Speed", None))
        self.label_volume_slider.setText(QCoreApplication.translate("MainWindow", u"Volume", None))
        self.tabWidget_song_parameters.setTabText(self.tabWidget_song_parameters.indexOf(self.tab_song_parameters_sliders), QCoreApplication.translate("MainWindow", u"Tab 2", None))
        self.button_restore.setText("")
        self.button_repeat.setText("")
        self.button_shuffle.setText("")
        self.button_previous_song.setText("")
        self.button_play_pause.setText("")
        self.button_next_song.setText("")
    # retranslateUi

