#!/bin/zsh

with open("/home/joey/.config/waybar/config", "r", encoding="utf-8") as barconfig:
    customword = barconfig.readlines()

# print(customword)

prefix = "        \"format\": "



print(customword[25])
phrase = input("Write new phrase here (Reset Window Manager to display after): ")

customword[25] = (prefix + "\"" + phrase + "\"" + ",\n")

with open('/home/joey/.config/waybar/config', 'w', encoding='utf-8') as barconfig:
    barconfig.writelines(customword)
