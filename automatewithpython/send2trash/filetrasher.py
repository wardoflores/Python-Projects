#!/bin/zsh

import os
import send2trash

baconfile = open("bacon.txt", 'a')

baconfile.write("Bacon is not a vegetable")

baconfile.close()

send2trash.send2trash('bacon.txt')
