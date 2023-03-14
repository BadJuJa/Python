import sqlite3
from sqlite3 import Error
import csv
import os


class CsvControl:
    @staticmethod
    def read_from_file(path_to_file):
        _list = []
        with open(path_to_file, 'r', newline='') as csvFile:
            reader = csv.reader(csvFile)
            for song in reader:
                _list.append(song[0])
        return _list

    @staticmethod
    def write_to_file(_slist, _path, _name):
        if _name == "":
            return

        list_to_write = _slist
        path = _path + _name + ".csv"
        with open(path, 'w', newline='') as f:
            writer = csv.writer(f)
            for item in list_to_write:
                writer.writerow([item])

        return path
