import glob
import os

from PyQt5.QtWidgets import (QFileDialog)


def open_folder(parent=None, title="Open..."):
    folder = QFileDialog.getExistingDirectory(parent, title, os.getcwd())
    if folder == "":
        folder = os.getcwd()
    return folder


def scan_folder(path):
    im_formats = ['png', 'jpg', 'jpeg']
    files_paths = []
    [files_paths.extend(glob.glob(path + '\\**\\*.' + e, recursive=True)) for e in im_formats]
    return files_paths
