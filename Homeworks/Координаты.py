import sys
from PyQt5.QtWidgets import QWidget, QApplication, QLabel


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 300, 300)
        self.setWindowTitle('Координаты')

        self.coords = QLabel(self)
        self.coords.setText("Координаты:None, None")
        self.coords.move(30, 30)
        self.show()

    def mouseMoveEvent(self, event):
        self.coords.setText("Координаты:{}, {}".format(
            event.x(), event.y()))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())