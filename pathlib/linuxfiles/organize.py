#! python3
# Description: This Python script organizes files in a given path
# Usage: python organize.py <dir_path>
# Author: Gagan Deep Singh @GaganGulyani
# Github Repo: https://github.com/gagangulyani/File-Organizer
# Created Aug 26, 2020


from pathlib import Path
from sys import argv
from shutil import move


def get_dir(filename):
    """
        This function takes filename and returns name of the
        parent directory of the respective filename
        Returns Miscellaneous if Parent is not found
    """
    ext = filename.suffix[1:]
    return dirs.get(ext, "Miscellaneous")


'''
    pictures = dirs[jpeg, jpg, png, tiff, gif]
    videos = dirs[mp4, mkv, mov, webm, flv]
    music = dirs[mp3, ogg, wav, flac]
    documents = dirs[pdf, doc, docx, ppt, ods]
    ebooks = dirs[epub]
'''

dirs = {  
    # Pictures
    "jpeg": "/home/joey/Pictures/transfer/jpeg",
    "png": "/home/joey/Pictures/transfer/png",
    "jpg": "/home/joey/Pictures/transfer/jpg",
    "tiff": "/home/joey/Pictures/transfer/tiff",
    "gif": "/home/joey/Pictures/transfer/gif",

    # Videos
    "mp4": "/home/joey/Videos/Transfer",
    "mkv": "/home/joey/Videos/Transfer",
    "mov": "/home/joey/Videos/Transfer",
    "webm": "/home/joey/Videos/Transfer",
    "flv": "/home/joey/Videos/Transfer",

    # Music
    "mp3": "/home/joey/Music",
    "ogg": "/home/joey/Music",
    "wav": "/home/joey/Music",
    "flac": "/home/joey/Music",

    # Documents
    "pdf": "/home/joey/Documents/Transfer",
    "doc": "/home/joey/Documents/Transfer",
    "docx": "/home/joey/Documents/Transfer",
    "ppt": "/home/joey/Documents/Transfer",
    "ods": "/home/joey/Documents/Transfer",

    # Ebooks
    "epub": "/home/joey/Documents/Books"

}

if len(argv) != 2:
    print("=" * 35)
    print("[ERROR] Invalid number of arguments were given")
    print(f"[Usage] python {Path(__file__).name} <dir_path>")
    print("=" * 35)
    exit(1)

# Directory Path
PATH = Path(argv[1])

for filename in PATH.iterdir():

    path_to_file = filename.absolute()

    if path_to_file.is_file():
        destination = PATH / get_dir(filename)

        if not destination.exists():
            destination.mkdir()

        move(str(path_to_file), str(destination))