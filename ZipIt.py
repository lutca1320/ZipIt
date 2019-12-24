import zipfile
import os, time
import threading
from datetime import datetime

def Timer():
    timer = threading.Timer(min * 60, ZipFile)
    timer.start()

def ZipFile():
    now = datetime.now()
    zip_file = zipfile.ZipFile("./ZipIt_" + foldername + "_" + now.strftime("%m%d%H%M%S") + ".zip", "w")

    for folder, subfolders, files in os.walk(folderpath):
        for file in files:
            if not file.startswith("ZipIt"):
                zip_file.write(os.path.join(folder, file),
                               os.path.relpath(os.path.join(folder, file), folderpath),
                               compress_type=zipfile.ZIP_DEFLATED)


    zip_file.close()

    print("Saved with " + now.strftime("%m%d%H%M%S"))
    Timer()

min = input("Interval Min: ")
min = int(min)

foldername = input("Folder name: ")
folderpath = "./" + foldername

Timer()