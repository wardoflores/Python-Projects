#!/bin/zsh

baconfile = open(r'automatewithpython\file\practicetxts\baconfile.txt', 'w')
baconfile.write('Hello World!\n')
baconfile.close()

baconfile = open(r'automatewithpython\file\practicetxts\baconfile.txt', 'a')
baconfile.write('Bacon is not a vegetable')
baconfile.close()

baconfile = open(r'automatewithpython\file\practicetxts\baconfile.txt')
content = baconfile.read()
baconfile.close()

print(content)
