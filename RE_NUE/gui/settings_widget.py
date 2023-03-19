# -*- coding: utf-8 -*-

from PyQt5.QtCore import QPoint, QSize, Qt
from PyQt5.QtWidgets import QWidget, QFileDialog, QTableWidgetItem, QHeaderView

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
        self.table_rows_count = 0

        # region Изменение параметров окна
        self.setWindowModality(Qt.WindowModality.ApplicationModal)
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.bottom_grip = CustomGrip(self, 3)
        # endregion

        # region Изменение параметров таблицы
        self.tableWidget_audio_paths.horizontalHeader().setMinimumSectionSize(20)
        self.tableWidget_audio_paths.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.ResizeToContents)
        self.tableWidget_audio_paths.verticalHeader().hide()
        # endregion

        # region Поля для событий масштабирования
        self.mouse_press_start = QPoint(0, 0)
        self.mouse_pressed = False
        self.grip_title_bar = False
        # endregion

        # Заполнение таблицы путями к папкам с аудио
        for p in self.db.get_paths():
            self.add_path(p, False)

        self.connect_signals()

    # region Перезапись событий для масштабирования окна
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
        self.bottom_grip.setGeometry(0, self.height() - self.bottom_grip.grip_width,
                                     self.width(), self.bottom_grip.grip_width)

    # endregion

    # Подписка методов на сигналы от элементов интерфейса
    def connect_signals(self):
        self.button_cancel.clicked.connect(self.cancel)
        self.button_ok.clicked.connect(self.ok)
        self.button_apply.clicked.connect(self.apply)

        self.button_add_path.clicked.connect(self.add)
        self.button_edit_path.clicked.connect(self.edit)
        self.button_delete_path.clicked.connect(self.delete)

    # Отмена внесённых, но не сохранённых изменений
    def discard_changes(self):
        add = self.changes['paths']['add']
        remove = self.changes['paths']['remove']
        change = self.changes['paths']['change']
        if len(change) > 0:
            for p in change:
                self.tableWidget_audio_paths.findItems(p[1], Qt.MatchFlag.MatchExactly)[0].setText(p[0])
        if len(add) > 0:
            for p in add:
                item = self.tableWidget_audio_paths.findItems(p, Qt.MatchFlag.MatchExactly)[0]
                self.tableWidget_audio_paths.removeRow(item.row())
        if len(remove) > 0:
            for p in remove:
                self.add_path(p)

        self.clear_changelist()

    # Очистка списка изменений после сохранения или отмены
    def clear_changelist(self):
        self.changes['paths']['add'].clear()
        self.changes['paths']['remove'].clear()
        self.changes['paths']['change'].clear()

    # Добавление пути в таблицу
    def add_path(self, path, with_discard=True):
        if self.tableWidget_audio_paths.findItems(path, Qt.MatchFlag.MatchExactly):
            return

        self.tableWidget_audio_paths.insertRow(self.table_rows_count)

        for col in range(2):
            if col % 2 == 0:
                item = QTableWidgetItem()
                item.setFlags(Qt.ItemFlag.ItemIsUserCheckable | Qt.ItemFlag.ItemIsEnabled)
                item.setCheckState(Qt.CheckState.Unchecked)
                item.setSizeHint(QSize(10, 10))
                self.tableWidget_audio_paths.setItem(self.table_rows_count, col, item)
            else:
                self.tableWidget_audio_paths.setItem(self.table_rows_count, col, QTableWidgetItem(path))
        self.table_rows_count += 1

        if with_discard:
            self.changes['paths']['add'].append(path)

    # Отмена изменений и закрытие окна
    def cancel(self):
        self.close()
        self.discard_changes()

    # Закрепление изменений и закрытие окна
    def ok(self):
        self.apply()
        self.close()

    # Закрепление внесённых изменений
    def apply(self):
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

    # Добавить новый путь к папке с аудио
    def add(self):
        path = QFileDialog.getExistingDirectory(self, 'Get Path')
        self.add_path(path)

    # Удалить путь к папке с аудио
    def delete(self):
        if len(self.tableWidget_audio_paths.selectedItems()) == 0:
            return
        path = self.tableWidget_audio_paths.currentItem().text()
        self.tableWidget_audio_paths.removeRow(self.tableWidget_audio_paths.currentRow())
        self.table_rows_count -= 1

        self.changes['paths']['remove'].append(path)

    # Изменить путь к папке с аудио
    def edit(self):
        if len(self.tableWidget_audio_paths.selectedItems()) == 0:
            return
        path = self.tableWidget_audio_paths.currentItem().text()
        new_path = QFileDialog.getExistingDirectory(self, 'Edit Path')
        self.tableWidget_audio_paths.currentItem().setText(new_path)
        self.changes['paths']['change'].append((path, new_path))



