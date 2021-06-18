import datetime
import sys
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog
from design import Ui_MainWindow
from imutils import paths
import numpy as np
import cv2
import os


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.open_folder_button.clicked.connect(self.browse_folder)
        self.ui.next_button.clicked.connect(self.open_next_image)
        self.ui.back_button.clicked.connect(self.open_prev_image)
        self.ui.delete_button_2.clicked.connect(self.delete_double_image)
        self.directory = None
        self.imageList = None
        self.hashes = []
        self.hash_idx = 0
        self.originals = []
        self.pairs = []
        self.pathsImage = []
        self.double_count = 0

    def dhash(self, image, hashSize=8):
        # пробразовываем изображение в оттенки серого и изменяем
        # его размер, затем добавляем столбец ширины, чтобы
        # можно было вычислить горизонтальный градиет
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        resized = cv2.resize(gray, (hashSize + 1, hashSize))

        # вычисляем относительный горизонтальный градиент
        # между пикселями соседних столбцов
        diff = resized[:, 1:] > resized[:, :-1]

        # преобразуем разностное изображение в хэш и возвращаем его
        return sum([2 ** i for (i, v) in enumerate(diff.flatten()) if v])

    def pars_image(self):
        print("[INFO] вычисляем хэш изображений")

        images_count = len(self.imageList)  # общее количество картинок в папке(для счетчика)
        image_number = 0  # количество картинок пропарсено
        one_percent = images_count // 100 if images_count >= 100 else 1

        # проходим по списку изображений
        for imagePath in self.imageList:
            # загружаем входное изображение и вычисляем хэш
            image = cv2.imdecode(np.fromfile(str(imagePath), dtype=np.uint8), cv2.IMREAD_COLOR)
            h = self.dhash(image)

            # добавляем в список хэш изображения
            self.hashes.append(h)
            # и в новый список путь к изображению
            self.pathsImage.append(imagePath)
            image_number += 1
            # вычисляем процент для прогресс бара
            if image_number % one_percent == 0 or image_number == images_count:
                self.ui.progressBar.setValue((image_number/images_count)*100)

        for ind, h in enumerate(self.hashes):
            if h in self.originals: continue
            for ind2, h2 in enumerate(self.hashes[ind + 1:]):
                ind2 += ind + 1
                if h == h2:
                    self.pairs.append((ind, ind2))
            self.originals.append(h)

    # отправляем изображения в гуи
    def show_image(self):
        idxs = self.pairs[self.hash_idx]
        original_pixmap = QPixmap(f'{self.imageList[idxs[0]]}')
        double_pixmap = QPixmap(f'{self.imageList[idxs[1]]}')

        # вычисляем нужный размер изображения из размера лейбла и самого изображения
        height = original_pixmap.height() / original_pixmap.width() * self.ui.original.width()
        if height > self.ui.original.height():
            height = self.ui.original.height()
            width = original_pixmap.width() / original_pixmap.height() * height
        else:
            width = self.ui.original.width()

        self.double_count = len([None for i in self.pairs if i[0] == self.pairs[self.hash_idx][0] and self.pathsImage[i[1]].split('\\')[-1] in os.listdir(self.directory)])
        self.ui.duble_count.setText(f'Число копий: {self.double_count}')
        self.ui.original.setPixmap(original_pixmap.scaled(width, height))
        self.ui.duble.setPixmap(double_pixmap.scaled(width, height))

    # логика кнопки "Далее"
    def open_next_image(self):
        if self.pairs:
            self.hash_idx += 1
            if self.hash_idx >= len(self.pairs):
                self.hash_idx = 0
            while_counter = 0
            while self.pathsImage[self.pairs[self.hash_idx][1]].split('\\')[-1] not in os.listdir(self.directory):
                while_counter += 1
                self.hash_idx += 1
                if self.hash_idx >= len(self.pairs):
                    self.hash_idx = 0
                if while_counter > len(self.pairs):
                    self.ui.original.setText('Дублей больше нет')
                    self.ui.duble.setText('Дублей больше нет')
                    return
            self.show_image()

    # логика кнопки "Назад"
    def open_prev_image(self):
        if self.pairs:
            self.hash_idx -= 1
            if self.hash_idx < 0:
                self.hash_idx = len(self.pairs) - 1
            while_counter = 0
            while self.pathsImage[self.pairs[self.hash_idx][1]].split('\\')[-1] not in os.listdir(self.directory):
                while_counter += 1
                self.hash_idx -= 1
                if self.hash_idx < 0:
                    self.hash_idx = len(self.pairs) - 1
                if while_counter > len(self.pairs):
                    self.ui.original.setText('Дублей больше нет')
                    self.ui.duble.setText('Дублей больше нет')
                    return
            self.show_image()

    # логика кнопки "Удалить"
    def delete_double_image(self):
        if self.pairs:
            if self.pathsImage[self.pairs[self.hash_idx][1]].split('\\')[-1] in os.listdir(self.directory):
                os.remove(self.pathsImage[self.pairs[self.hash_idx][1]])
                with open('history.txt', 'a', encoding='utf-8') as file:
                    file.write(f'Файл {self.pathsImage[self.pairs[self.hash_idx][1]]} был удален в '
                               f'{datetime.datetime.now()}\n')
            self.open_next_image()

    # логика кнопки выбора пути до папки с изображениями
    def browse_folder(self):
        self.ui.folder_line_edit.clear()
        self.directory = QFileDialog.getExistingDirectory(self, "Выберите папку")
        # открыть диалог выбора директории и установить значение переменной
        # равной пути к выбранной директории

        if self.directory:  # не продолжать выполнение, если пользователь не выбрал директорию
            self.hash_idx = 0
            self.pairs = []
            self.originals = []
            self.hashes = []
            self.pathsImage = []
            self.imageList = list(paths.list_images(self.directory))
            if not self.imageList:
                self.ui.original.setText('В папке нет картинок')
                self.ui.duble.setText('В папке нет картинок')
                return
            self.ui.folder_line_edit.setText(self.directory)
            self.ui.original.setText('Подождите, идет поиск')
            self.ui.duble.setText('Подождите, идет поиск')
            self.pars_image()
            if not self.pairs:
                self.ui.original.setText('Дублей не найдено')
                self.ui.duble.setText('Дублей не найдено')
                return
            self.show_image()


def main():
    app = QApplication(sys.argv)  # Новый экземпляр QApplication
    window = MainWindow()  # Создаём объект класса ExampleApp
    window.show()  # Показываем окно
    app.exec()  # и запускаем приложение


if __name__ == '__main__':  # Если мы запускаем файл напрямую, а не импортируем
    main()  # то запускаем функцию main()
