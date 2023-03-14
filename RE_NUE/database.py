import sqlite3
from sqlite3 import Error
import os


class Database:
    def __init__(self, existing_db=None):
        self.connection = None
        self.cursor = None

        if existing_db is not None and os.path.exists(existing_db):
            self.connection_create(existing_db)
        else:
            self.create_database()

    def create_database(self):
        self.connection_create()
        c = self.connection.cursor()
        c.execute("""CREATE TABLE Settings  (SettingName  TEXT PRIMARY KEY, SettingValue TEXT);""")
        c.execute("""CREATE TABLE ScanPaths (Path         TEXT PRIMARY KEY);""")
        c.execute("""CREATE TABLE AllSongs  (FileName     TEXT,Path TEXT REFERENCES ScanPaths (Path));""")
        self.save_changes()

    # region CONNECTION
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

    def connection_close(self):
        self.connection.close()

    def save_changes(self):
        self.connection.commit()

    # endregion

    # region PATHS
    def add_path(self, path):
        self.cursor.execute(f'''INSERT INTO ScanPaths (Path) VALUES("{path}")''')

    def delete_path(self, path):
        self.cursor.execute(f'''DELETE FROM AllSongs WHERE Path LIKE "%{path}%"''')
        self.cursor.execute(f'''DELETE FROM ScanPaths WHERE Path == "{path}"''')
    # endregion

    # region SONG TABLE
    def add_song(self, file_name, file_path):
        self.cursor.execute(f'''INSERT INTO AllSongs (FileName, Path) VALUES ("{file_name}","{file_path}")''')

    def clear_songs_table(self):
        self.cursor.execute('''DELETE FROM AllSongs''')
        self.save_changes()
        self.cursor.execute('''VACUUM''')
        self.save_changes()
    # endregion

    # region GETTERS
    def get_paths(self):
        paths = self.cursor.execute('''SELECT * FROM ScanPaths''').fetchall()
        paths = [x[0] for x in paths]
        return paths

    def get_songs(self):
        songs = self.cursor.execute('''SELECT FileName, path FROM AllSongs''').fetchall()
        return songs
    # endregion
