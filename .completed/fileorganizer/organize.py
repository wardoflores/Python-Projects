#! python3
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
    # TODO: make the Directories more compact in ext.
    for key,val in dirs.items():

    for filename in ext:
        if filename == :
            ext = dirs[jpeg, jpg, png, tiff, gif]

    '''
    pictures = dirs[jpeg, jpg, png, tiff, gif]
    videos = dirs[mp4, mkv, mov, webm, flv]
    music = dirs[mp3, ogg, wav, flac]
    documents = dirs[pdf, doc, docx, ppt, ods]
    ebooks = dirs[epub]
    '''

    return dirs.get(ext, "Miscellaneous")


dirs = {  
    # Pictures
    "jpeg": r"D:\Pictures\Transfer\jpeg",
    "png": r"D:\Pictures\Transfer\png",
    "jpg": r"D:\Pictures\Transfer\jpg",
    "tiff": r"D:\Pictures\Transfer\tiff",
    "gif": r"D:\Pictures\Transfer\gif",

    # Videos
    "mp4": r"C:\Users\Flores\Videos\Transfer",
    "mkv": r"C:\Users\Flores\Videos\Transfer",
    "mov": r"C:\Users\Flores\Videos\Transfer",
    "webm": r"C:\Users\Flores\Videos\Transfer",
    "flv": r"C:\Users\Flores\Videos\Transfer",

    # Music
    "mp3": r"D:\Music",
    "ogg": r"D:\Music",
    "wav": r"D:\Music",
    "flac": r"D:\Music",

    # Documents
    "pdf": r"C:\Users\Flores\Documents\Transfer",
    "doc": r"C:\Users\Flores\Documents\Transfer",
    "docx": r"C:\Users\Flores\Documents\Transfer",
    "ppt": r"C:\Users\Flores\Documents\Transfer",
    "ods": r"C:\Users\Flores\Documents\Transfer",

    # Ebooks
    "epub": r"C:\Users\Flores\Documents\.E books\temp"

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