## ==> GUI FILE
from main import *

# Database
import sqlite3, requests, vk_api
from sqlite3 import Error


class UIFunctions(MainWindow):

    def toggleMenu(self, maxWidth, enable):
        if enable:

            # GET WIDTH
            width = self.ui.frame_left_menu.width()
            maxExtend = maxWidth
            standard = 64

            # SET MAX WIDTH
            if width == 64:
                widthExtended = maxExtend
            else:
                widthExtended = standard

            # PICTURE TO TEXT
            # sd

            # ANIMATION
            self.animation = QPropertyAnimation(self.ui.frame_left_menu, b"minimumWidth")
            self.animation.setDuration(400)
            self.animation.setStartValue(width)
            self.animation.setEndValue(widthExtended)
            self.animation.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
            self.animation.start()

    def updateDataBase(self):
        print("updating database")
        print(self.connectToDatabase('userData.db'))
        #con = self.connectToDatabase(self, 'userData.db')
        #cur = con.cursor()
        #user = cur.execute('''SELECT login, password, ID FROM userData''')
        #for i in user:
        #    print(i)

    def connectToDatabase(self, name):
        '''connection = None
        try:
            connection = sqlite3.connect(name)
            print("Connection to SQLite DB successful")
        except Error as e:
            print(f"The error '{e}' occurred")

        return connection'''
        return f"connecting to {name}"

    def nextDef(self):
        pass
