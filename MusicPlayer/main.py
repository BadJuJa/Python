# SYSTEM
import sys
import os
import platform

# DATABASE
import sqlite3
from sqlite3 import Error

# VK
import vk_api
from vk_api import audio

# REQUESTS
import requests

# PYQT
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject,
                          QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent)
from PyQt5.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence,
                         QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PyQt5.QtWidgets import *

# GUI FILE
from ui_main import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # CURRENT USER
        self.login = "_"
        self.password = "_"
        self.id = "_"

        self.buttons()

    def toggleMenu(self, maxWidth, enable):
        if enable:

            # GET WIDTH
            width = self.frame_left_menu.width()
            maxExtend = maxWidth
            standard = 64

            # SET MAX WIDTH
            if width == 64:
                widthExtended = maxExtend
            else:
                widthExtended = standard

            # PICTURE TO TEXT
            # Реализовать замену текста на иконку и обратно

            # ANIMATION
            self.animation = QPropertyAnimation(self.frame_left_menu, b"minimumWidth")
            self.animation.setDuration(400)
            self.animation.setStartValue(width)
            self.animation.setEndValue(widthExtended)
            self.animation.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
            self.animation.start()

    def buttons(self):
        # TOGGLE MENU
        self.btn_toggle.clicked.connect(lambda: self.toggleMenu(maxWidth=250, enable=True))

        # data
        self.btn_createPlaylist.clicked.connect(lambda: self.updateDataBase())

        # PAGES
        ########################################################################

        # PAGE SONGS
        self.btn_menu_songs.clicked.connect(lambda: self.pages_Widget.setCurrentWidget(self.page_songs))

        # PAGE PLAYLISTS
        self.btn_menu_playlists.clicked.connect(lambda: self.pages_Widget.setCurrentWidget(self.page_playlists))

        # PAGE DOWNLOADS
        self.btn_menu_downloads.clicked.connect(lambda: self.pages_Widget.setCurrentWidget(self.page_downloads))
        ########################################################################

    def updateDataBase(self):
        con = self.connectToDatabase('userData.db')
        cur = con.cursor()
        user = cur.execute('''SELECT login, password, ID FROM userData''').fetchall()  # возвращает кортеж
        LPI = ()
        for e in user:
            LPI = e
        self.login, self.password, self.id = LPI[0], LPI[1], LPI[2]

        vk_session = vk_api.VkApi(login=self.login, password=self.password)

        vk_session.auth()
        #vk = vk_session.get_api()
        #vk_audio = audio.VkAudio(vk_session)

        #request_status_code = 200
        #print(type(vk_audio.get(owner_id=self.id)))
        '''for i in vk_audio.get(owner_id=self.id):
            try:
                r = requests.get(i["url"])
                print(r.status_code)
                #if r.status_code == request_status_code:
                #    print(i["artist"] + '_' + i["title"])
                    #cur.execute('''''')
                    #with open(i["artist"] + '_' + i["title"] + '.mp3', 'wb') as output_file:
                    #    output_file.write(r.content)
            except OSError:
                print(i["artist"] + '_' + i["title"])'''

    def connectToDatabase(self, name):
        connection = None
        try:
            connection = sqlite3.connect(name)
        except Error as e:
            print(f"The error '{e}' occurred")

        return connection


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
