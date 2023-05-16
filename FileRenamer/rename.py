import os
import defs as df
from pathlib import Path
from os.path import join as J
from split_pile import get_range

def Rename(folder):
    temp_path = J(folder, "_temp_")

    if not os.path.exists(temp_path):
        os.mkdir(temp_path)

    files = df.scan_folder(folder)
    for _ in files:
        po = Path(_)
        po.rename(J(temp_path, po.name))

    files = df.scan_folder(temp_path)
    for i in range(len(files)):
        po = Path(files[i])
        suffix = po.suffix
        new_path = J(folder, str(i) + suffix)
        po.rename(new_path)
    os.rmdir(temp_path)


if __name__ == "__main__":
    folder = "C:\\Users\\user\\Documents\\check later\\Images\\all_images"
    Rename(folder)
    #get_range(15, 10000)
