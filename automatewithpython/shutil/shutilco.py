#!/bin/zsh

# Code will copy a single file.

import shutil, os

os.chdir("C:\\")
shutil.copy("C:\\spam.txt",  "C:\\delicious") # Source, Destination

shutil.copy("eggst.txt", "C:\\delicious\\eggs2.txt")

