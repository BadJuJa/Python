import os
from os.path import join as J
from pathlib import Path
from defs import scan_folder as sf

def split(path, split_count, split_by_files_count):
    files = sf(path)
    file_count = len(files)
    splits_path = J(path, "splits")
    if not os.path.exists(splits_path):
            os.mkdir(splits_path)

    if split_by_files_count:
        for i in range(split_count):
             pass
    else:
        pass

def get_range(split_count, file_count):
     c = file_count//split_count
     print(c)