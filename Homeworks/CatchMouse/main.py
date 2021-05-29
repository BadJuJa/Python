import sys
import random
from PyQt5.QtWidgets import QPushButton
from PyQt5 import QtWidgets
from PyQt5.QtCore import pyqtSignal
import form


class Button(QPushButton):
    mouseMoved = pyqtSignal()

    def mouseMoveEvent(self, event):
        self.mouseMoved.emit()


class ExampleApp(QtWidgets.QMainWindow, form.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

    def moveButton(self):
        self.coords[0] = random.randint(0, self.w - self.btn_size[0])
        self.coords[1] = random.randint(0, self.h - self.btn_size[1])
        self.btn.move(*self.coords)

def main():
    app = QtWidgets.QApplication(sys.argv)
    window = ExampleApp()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()