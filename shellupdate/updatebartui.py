#!/bin/zsh

with open("/home/joey/.config/waybar/config", "r", encoding="utf-8") as barconfig:
    customword = barconfig.readlines()

# print(customword)

prefix = "        \"format-alt\": "

phrase = input("Write new phrase here (Reset Window Manager to display after): ")

customword[26] = (prefix + "\"" + phrase + "\"" + ",\n")

with open('/home/joey/.config/waybar/config', 'w', encoding='utf-8') as barconfig:
    barconfig.writelines(customword)
