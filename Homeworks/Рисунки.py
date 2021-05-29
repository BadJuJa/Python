import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtGui import QPainter, QColor
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtGui import QPainterPath

class MyClass(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.action = 0
        self.setMouseTracking(True)

    def initUI(self):
        self.setGeometry(0, 0, 600, 600)
        self.setWindowTitle('Рисунки')


    def paintEvent(self, event):
        try:
            qp = QPainter()
            qp.begin(self)
            if self.action == 1:
                x = self.x
                y = self.y
                self.draw_rect(qp, x, y)
            elif self.action == 2:
                x = self.x
                y = self.y
                self.draw_cir(qp, x, y)
            elif self.action == 3:
                x = self.x
                y = self.y
                self.draw_tr(qp, x, y)                
            qp.end()
        except Exception as e:
            print(e)

    def draw_rect(self, qp, x, y):
        qp.setBrush(QColor(255, 0, 0))
        qp.drawRect(x, y, 120, 30)

    def draw_cir(self, qp, x, y):
        qp.setBrush(QColor(0, 0, 255))
        qp.drawEllipse(x, y, 120, 120)

    def draw_tr(self, qp, x, y):
        try:
            path = QPainterPath()
            qp.setBrush(QColor(0, 255, 0))
            path.moveTo(x, y)
            path.lineTo(x + 40, y)
            path.lineTo(x, y - 40)
            path.lineTo(x, y)
            qp.drawPath(path)
        except Exception as e:
            print(e)

    def mousePressEvent(self, event):
        try:
            but = event.button()
            if but == 2:
                event = QtGui.QMouseEvent(QtCore.QEvent.MouseButtonPress, event.pos(), QtCore.Qt.LeftButton, QtCore.Qt.LeftButton, QtCore.Qt.NoModifier)
                self.update()
                self.action = 2
            if but == 1:
                event = QtGui.QMouseEvent(QtCore.QEvent.MouseButtonPress, event.pos(), QtCore.Qt.LeftButton, QtCore.Qt.LeftButton, QtCore.Qt.NoModifier)
                self.update()
                self.action = 1
        except Exception as e:
            print(e)

    def mouseMoveEvent(self, event):
        self.x = event.x()
        self.y = event.y()
        self.pos = event.pos()

    def keyPressEvent(self, event):
        try:
            if event.key() == 32:
                self.action = 3
                self.update()
        except Exception as e:
            print(e)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyClass()
    ex.show()
    sys.exit(app.exec())
