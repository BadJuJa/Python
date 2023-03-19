# -*- coding: utf-8 -*-

import os
import sqlite3
from sqlite3 import Error


class Database:
    def __init__(self, existing_db=None):
        self.connection = None
        self.cursor = None

        if existing_db is not None and os.path.exists(existing_db):
            self.connection_create(existing_db)
        else:
            self.create_database()

        self.scan_playlists()

    # Создание базы данных и её таблиц
    def create_database(self):
        self.connection_create()
        c = self.connection.cursor()
        c.execute("""CREATE TABLE Settings  (SettingName  TEXT PRIMARY KEY, SettingValue TEXT);""")
        c.execute("""CREATE TABLE ScanPaths (Path         TEXT PRIMARY KEY);""")
        c.execute("""CREATE TABLE AllSongs  (FileName     TEXT,Path TEXT REFERENCES ScanPaths (Path));""")
        c.execute("""CREATE TABLE Playlists (path         TEXT PRIMARY KEY, name TEXT, icon TEXT)""")
        self.save_changes()

    # Подключение к базе
    def connection_create(self, existing_db=None):
        db_file_name = 'data.db'
        if existing_db is not None:
            db_file_name = existing_db
        connection = None
        try:
            connection = sqlite3.connect(db_file_name)
        except Error as e:
            print(f"The error '{e}' occurred")

        self.connection = connection
        self.cursor = connection.cursor()

    # Разрыв соединения с базой
    def connection_close(self):
        if self.connection:
            self.connection.close()

    # Сохранение внесённых изменений
    def save_changes(self):
        self.connection.commit()

    # Добавление в базу пути к аудио
    def add_path(self, path):
        self.cursor.execute(f'''INSERT INTO ScanPaths (Path) VALUES("{path}")''')

    # Удаление из базы пути к аудио
    def delete_path(self, path):
        self.cursor.execute(f'''DELETE FROM AllSongs WHERE Path LIKE "%{path}%"''')
        self.cursor.execute(f'''DELETE FROM ScanPaths WHERE Path == "{path}"''')

    # Добавление аудио
    def add_audio(self, file_name, file_path):
        self.cursor.execute(f'''INSERT INTO AllSongs (FileName, Path) VALUES ("{file_name}","{file_path}")''')

    # Добавление плейлиста в базу
    def add_playlist(self, name, file_path, icon_path):
        query = f"""
            INSERT INTO Playlists (path, name, icon) 
            VALUES (?,?,?) 
            ON CONFLICT (path) 
            DO UPDATE SET path=?, name=?, icon=?
        """
        self.cursor.execute(query, (file_path, name, icon_path, file_path, name, icon_path))

    # Очистка таблицы с аудио
    def clear_audio_table(self):
        self.cursor.execute('''DELETE FROM AllSongs''')
        self.save_changes()
        self.cursor.execute('''VACUUM''')
        self.save_changes()

    # Удаление плейлиста из базы
    def remove_playlist(self, name):
        query = f"""
        DELETE FROM Playlists
        WHERE name LIKE ?
        """
        self.cursor.execute(query, (name,))

    # Получение путей к папкам с аудио
    def get_paths(self):
        paths = self.cursor.execute('''SELECT * FROM ScanPaths''').fetchall()
        paths = [x[0] for x in paths]
        return paths

    # Получение списка аудио и их путей
    def get_all_audio(self):
        audio = self.cursor.execute('''SELECT FileName, path FROM AllSongs''').fetchall()
        return audio

    # Получение пути к аудио по его имени
    def get_audio(self, name):
        query = f'''SELECT path FROM AllSongs WHERE FileName == "{name}"'''
        audio = self.cursor.execute(query).fetchone()[0]
        return audio

    # Получение имени аудио по его пути
    def get_audio_name(self, path):
        query = f'''SELECT FileName from AllSongs WHERE path LIKE "%{path}%"'''
        name = self.cursor.execute(query).fetchone()[0]
        return name

    # Получение списка плейлистов
    def get_playlists(self):
        _ = self.cursor.execute('''SELECT name FROM Playlists''').fetchall()
        _ = [_[x][0] for x in range(len(_))]
        return _

    # Получение плейлиста по его имени
    def get_playlist(self, name):
        playlist = self.cursor.execute(f'''SELECT path, name, icon FROM Playlists WHERE name == "{name}"''').fetchone()
        return playlist

    # Сканирование на наличие файлов плейлистов из базы, очистка от несуществующий плейлистов
    def scan_playlists(self):
        for ps in self.get_playlists():
            path = self.get_playlist(ps)[0]
            if not os.path.exists(path):
                self.remove_playlist(path)

    # Обновление данных плейлиста
    def update_playlist(self, old_name, new_name, csv_path, icon_path):
        query = """
        UPDATE Playlists
        SET (path, name, icon) = (?,?,?)
        WHERE name == ?
        """
        self.cursor.execute(query, (csv_path, new_name, icon_path, old_name,))
