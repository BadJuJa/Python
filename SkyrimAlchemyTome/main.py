import sqlite3
import sys
from PyQt5 import QtWidgets

from GUI_Module import GUIClass


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = GUIClass()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()