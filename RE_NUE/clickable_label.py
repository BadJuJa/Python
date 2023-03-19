from PyQt5.QtCore import pyqtSignal as Signal
from PyQt5.QtWidgets import QLabel


class ClickableLabel(QLabel):
    clicked = Signal()

    def __init__(self, parent=None):
        super().__init__(parent)

    # ���������� ������� ������� ������ ����
    def mouseReleaseEvent(self, event):
        self.clicked.emit()
