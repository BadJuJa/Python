from PyQt5.QtCore import (QPoint, QSize, Qt)
from PyQt5.QtWidgets import (QWidget, QFileDialog, QTableWidgetItem, QHeaderView)

from gui.base.settings import Ui_MainWidget
from gui.custom_grips import CustomGrip


class SettingsWidget(QWidget, Ui_MainWidget):
    def __init__(self, parent):
        super().__init__()
        self.main_window_ref = parent
        self.setupUi(self)

        self.db = self.main_window_ref.db
        self.changes = {
            "paths": {
                "add": [],
                "remove": [],
                "change": []
            }
        }

        self.TABLE_ROWS_COUNT = 0

        # region WINDOW SETUP
        self.setWindowModality(Qt.WindowModality.ApplicationModal)
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setup_resizeGrips()
        # endregion

        # region TABLE SETUP
        self.tableWidget_music_paths.horizontalHeader().setMinimumSectionSize(20)
        self.tableWidget_music_paths.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.ResizeToContents)
        self.tableWidget_music_paths.verticalHeader().hide()
        # endregion

        self.connect_buttons()

        # region RESIZE EVENTS STUFF
        self.mouse_press_start = QPoint(0, 0)
        self.mouse_pressed = False
        self.grip_title_bar = False
        # endregion

        # region GET PATHS FROM DATABASE
        self.fill_paths()
        # endregion

    # region EVENT OVERRIDING
    def mousePressEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            if 5 < event.pos().y() < 20:
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
            if self.grip_title_bar:
                self.setGeometry(self.mapToGlobal(movement).x(),
                                 self.mapToGlobal(movement).y(),
                                 self.width(),
                                 self.height())
                self.mouse_press_start = end

    def mouseReleaseEvent(self, QMouseEvent):
        self.mouse_pressed = False

    def resizeEvent(self, event):
        self.resize_grips()
    # endregion

    # region CUSTOM METHODS
    def setup_resizeGrips(self):
        self.left_grip = CustomGrip(self, Qt.LeftEdge, 3)
        self.right_grip = CustomGrip(self, Qt.RightEdge, 3)
        self.top_grip = CustomGrip(self, Qt.TopEdge, 3)
        self.bottom_grip = CustomGrip(self, Qt.BottomEdge, 3)

    def resize_grips(self):
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

    def connect_buttons(self):
        self.button_cancel.clicked.connect(self.btn_cancel)
        self.button_ok.clicked.connect(self.btn_ok)
        self.button_apply.clicked.connect(self.btn_apply)

        self.button_add_path.clicked.connect(self.btn_add)
        self.button_edit_path.clicked.connect(self.btn_edit)
        self.button_delete_path.clicked.connect(self.btn_delete)

        self.button_radio_dials.toggled.connect(self.change_song_parameters_style)

    def discard_changes(self):
        add = self.changes['paths']['add']
        remove = self.changes['paths']['remove']
        change = self.changes['paths']['change']
        if len(change) > 0:
            for p in change:
                self.tableWidget_music_paths.findItems(p[1], Qt.MatchFlag.MatchExactly)[0].setText(p[0])
        if len(add) > 0:
            for p in add:
                item = self.tableWidget_music_paths.findItems(p, Qt.MatchFlag.MatchExactly)[0]
                self.tableWidget_music_paths.removeRow(item.row())
        if len(remove) > 0:
            for p in remove:
                self.add_path(p)

        self.clear_changelist()

    def clear_changelist(self):
        self.changes['paths']['add'].clear()
        self.changes['paths']['remove'].clear()
        self.changes['paths']['change'].clear()

    def fill_paths(self):
        paths = self.db.get_paths()
        for p in paths:
            self.add_path(p, False)

    # endregion

    # region BUTTON METHODS
    # region FOOTER
    def btn_cancel(self):
        self.hide()
        self.discard_changes()

    def btn_ok(self):
        self.btn_apply()
        self.hide()

    def btn_apply(self):
        add = self.changes['paths']['add']
        remove = self.changes['paths']['remove']
        change = self.changes['paths']['change']

        if len(change) > 0:
            for p in change:
                self.db.delete_path(p)
                self.db.add_path(p)
        if len(add) > 0:
            for p in add:
                self.db.add_path(p)
        if len(remove) > 0:
            for p in remove:
                self.db.delete_path(p)

        self.db.save_changes()
        self.clear_changelist()
    # endregion

    # region PATH LIST
    def add_path(self, path, with_discard=True):
        if self.tableWidget_music_paths.findItems(path, Qt.MatchFlag.MatchExactly):
            return

        self.tableWidget_music_paths.insertRow(self.TABLE_ROWS_COUNT)

        for col in range(2):
            if col % 2 == 0:
                item = QTableWidgetItem()
                item.setFlags(Qt.ItemFlag.ItemIsUserCheckable | Qt.ItemFlag.ItemIsEnabled)
                item.setCheckState(Qt.CheckState.Unchecked)
                item.setSizeHint(QSize(10, 10))
                self.tableWidget_music_paths.setItem(self.TABLE_ROWS_COUNT, col, item)
            else:
                self.tableWidget_music_paths.setItem(self.TABLE_ROWS_COUNT, col, QTableWidgetItem(path))
        self.TABLE_ROWS_COUNT += 1

        if with_discard:
            self.changes['paths']['add'].append(path)

    def btn_add(self):
        path = QFileDialog.getExistingDirectory(self, 'Get Path')
        self.add_path(path)

    def btn_delete(self):
        if len(self.tableWidget_music_paths.selectedItems()) == 0:
            return
        path = self.tableWidget_music_paths.currentItem().text()
        self.tableWidget_music_paths.removeRow(self.tableWidget_music_paths.currentRow())
        self.TABLE_ROWS_COUNT -= 1

        self.changes['paths']['remove'].append(path)

    def btn_edit(self):
        if len(self.tableWidget_music_paths.selectedItems()) == 0:
            return
        path = self.tableWidget_music_paths.currentItem().text()
        new_path = QFileDialog.getExistingDirectory(self, 'Edit Path')
        self.tableWidget_music_paths.currentItem().setText(new_path)
        self.changes['paths']['change'].append((path, new_path))
    # endregion
    # endregion

    # region CHANGE PARAMETERS
    # noinspection PyUnresolvedReferences
    def change_song_parameters_style(self):
        if self.button_radio_dials.isChecked():
            self.main_window_ref.tabWidget_song_parameters.setCurrentIndex(0)
        elif self.button_radio_sliders.isChecked():
            self.main_window_ref.tabWidget_song_parameters.setCurrentIndex(1)
    # endregion
