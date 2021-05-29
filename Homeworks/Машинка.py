import sys
from random import randint
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton, QLabel, QFileDialog
from PyQt5.QtGui import QPainter, QColor, QPixmap
from PyQt5.QtCore import Qt



class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.setMouseTracking(True)
        self.initUI()

    def initUI(self):
        name = QFileDialog.getOpenFileName(self, 'Выбрать машину', 'фото машины')[0]
        self.pixmap = QPixmap(name)
        self.pixmap = self.pixmap.scaled(200, 150)

        self.l = QLabel(self)
        self.l.move(80, 60)
        self.l.resize(250, 250)
        self.l.setPixmap(self.pixmap)

        self.setGeometry(200, 200, 1900, 800)
        self.l.setGeometry(500, 500, 100, 100)

    def mouseMoveEvent(self, event):
        self.x = event.x()
        self.y = event.y()

        if event.x() > 1900:
            self.x = 1899
        
        if event.y() > 800:
            self.y = 799
        
        self.l.move(self.x, self.y)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec_())