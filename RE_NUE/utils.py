import csv


class CsvControl:
    @staticmethod
    def read_from_file(path_to_file):
        _list = []
        with open(path_to_file, 'r', newline="") as csvFile:
            reader = csv.reader(csvFile, delimiter='|',)
            for song in reader:
                _list.append(song[0])
        return _list

    @staticmethod
    def write_to_file(_slist, location):
        path = location + ".csv"
        with open(path, 'w', newline='') as f:
            writer = csv.writer(f)
            for item in _slist:
                writer.writerow([item])

        return path
