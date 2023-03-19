import csv
import os


# �������� ������������ ��� �������� ������ ����������
def create_subfolders():
    p = os.path.join(os.getcwd(), "Playlists")
    if not os.path.exists(p):
        os.mkdir(p)
    i = os.path.join(p, "icons")
    if not os.path.exists(i):
        os.mkdir(i)


class CsvControl:
    # ������ �� csv �����
    @staticmethod
    def read_from_file(path_to_file):
        _list = []
        with open(path_to_file, 'r', newline="") as csvFile:
            reader = csv.reader(csvFile, delimiter='|', )
            for audio in reader:
                _list.append(audio[0])
        return _list

    # ������ � csv ����
    @staticmethod
    def write_to_file(_slist, location):
        path = location + ".csv"
        with open(path, 'w', newline='') as f:
            writer = csv.writer(f)
            for item in _slist:
                writer.writerow([item])

        return path
