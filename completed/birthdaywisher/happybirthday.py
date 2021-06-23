#! python3
# This Python file uses the following encoding: utf-8
# Happy Birthday
# Bulls Eye: https://github.com/BullsEye0
# Created May, 20 2019
# Copyright (c) 2019 Jolanda de Koff, Bulls Eye.

import random
import time
import os


banner1 = """
\033[1;31m
 ▄ .▄ ▄▄▄·  ▄▄▄· ▄▄▄· ▄· ▄▌    ▄▄▄▄· ▪  ▄▄▄  ▄▄▄▄▄ ▄ .▄·▄▄▄▄   ▄▄▄·  ▄· ▄▌
██▪▐█▐█ ▀█ ▐█ ▄█▐█ ▄█▐█▪██▌    ▐█ ▀█▪██ ▀▄ █·•██  ██▪▐███▪ ██ ▐█ ▀█ ▐█▪██▌
██▀▐█▄█▀▀█  ██▀· ██▀·▐█▌▐█▪    ▐█▀▀█▄▐█·▐▀▀▄  ▐█.▪██▀▐█▐█· ▐█▌▄█▀▀█ ▐█▌▐█▪
██▌▐▀▐█ ▪▐▌▐█▪·•▐█▪·• ▐█▀·.    ██▄▪▐█▐█▌▐█•█▌ ▐█▌·██▌▐▀██. ██ ▐█ ▪▐▌ ▐█▀·.
▀▀▀ · ▀  ▀ .▀   .▀     ▀ •     ·▀▀▀▀ ▀▀▀.▀  ▀ ▀▀▀ ▀▀▀ ·▀▀▀▀▀•  ▀  ▀   ▀ •
\033[1;m
    ~Birthday song code~
    (Type name after intro :D)
        """

banner2 = """
\033[1;31m
 ▄  █ ██   █ ▄▄  █ ▄▄ ▀▄    ▄     ███   ▄█ █▄▄▄▄    ▄▄▄▄▀ ▄  █ ██▄   ██  ▀▄    ▄
█   █ █ █  █   █ █   █  █  █      █  █  ██ █  ▄▀ ▀▀▀ █   █   █ █  █  █ █   █  █
██▀▀█ █▄▄█ █▀▀▀  █▀▀▀    ▀█       █ ▀ ▄ ██ █▀▀▌      █   ██▀▀█ █   █ █▄▄█   ▀█
█   █ █  █ █     █       █        █  ▄▀ ▐█ █  █     █    █   █ █  █  █  █   █
   █     █  █     █    ▄▀         ███    ▐   █     ▀        █  ███▀     █ ▄▀
  ▀     █    ▀     ▀                        ▀              ▀           █
       ▀                                                              ▀
\033[1;m
    Happy Birthday! 
    (type name after intro :D)
        """

print(banner1.center(os.get_terminal_size().columns))
time.sleep(1)


def happy_birthday():

    first_name = input("[+] First name: ")
    print("\n")

    happy = "Happy Birthday to You..".center(os.get_terminal_size().columns)

    print("###########################################\n".center(os.get_terminal_size().columns))
    print("Happy Birthday ".center(os.get_terminal_size().columns) + (first_name.capitalize().center(os.get_terminal_size().columns)) + "\n")
    print("###########################################\n".center(os.get_terminal_size().columns))
    time.sleep(2)

    for x in range(2):
        x = print(happy)
        
        x
        time.sleep(2)
        x
        time.sleep(1.5)

        print("Happy Birthday".center(os.get_terminal_size().columns), first_name.capitalize().center(os.get_terminal_size().columns))
        time.sleep(1)
        print(happy + "\n".center(os.get_terminal_size().columns))
        time.sleep(1)

        for x in range(3):
            print("Hip Hip Hooray..!\n".center(os.get_terminal_size().columns))
            time.sleep(1)

    print("###########################################".center(os.get_terminal_size().columns))
    print("Happy Birthday".center(os.get_terminal_size().columns), first_name.capitalize().center(os.get_terminal_size().columns))
    print("Have some fun today :) ".center(os.get_terminal_size().columns))
    print("###########################################\n".center(os.get_terminal_size().columns))


happy_birthday()