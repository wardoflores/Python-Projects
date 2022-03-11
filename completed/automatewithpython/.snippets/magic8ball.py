#!/bin/zsh

import random

messages = ["It is certain",
    "it is decidedly so",
    "Yes definitely",
    "Reply hazy try again",
    "Ask again later",
    "Concentrate and ask again",
    "my reply is No.",
    "Outlook not so good",
    "Very doubtful"]

print(messages[random.randint(0, len(messages) - 1)])