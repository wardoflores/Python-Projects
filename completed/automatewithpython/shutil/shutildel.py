import os
import shutil

os.unlink(path)
''' 
Will delete file at path
'''

os.rmdir(path) 
'''
Will delete folder path, foldder must be empty of any files or folders.
'''

shutil.rmtree(path)
''' 
Will remove the folder at path, 
and all fil and folders itcontains will also be deleted.
'''