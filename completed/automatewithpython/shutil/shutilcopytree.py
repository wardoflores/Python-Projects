# Code will copy a Folder.

import shutil, os

os.chdir("C:\\")
shutil.copytree("C:\\bacon", "C:\\bacon_backup") 
''' 
replace bacon (1st argument) with actual filename for backing it up on the backup folder (2nd argument).
'''