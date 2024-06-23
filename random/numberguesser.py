#!/bin/zsh
# Automate the Boring Stuff with Python
# Fully modified 2024-06-24
import random

print("I am thinking of a number between 1 and 20, you have 6 attempts.")

def main():
    count=0
    secretnumber = random.randint(1,20)
    for guessestaken in range(1,7):
        count+=1
        print("Take a guess.")
        try:
            guess = int(input())

            if guess < secretnumber:
                print("Your guess is too low.")
                try:
                    if count == 6:
                        print("Nope. The number I was thinking of was " + str(secretnumber))
                except count <= 6:
                   continue 
            elif guess > secretnumber:
                print("Your guess is too high.")
                try:
                    if count == 6:
                        print("Nope. The number I was thinking of was " + str(secretnumber))
                except count <= 6:
                   continue 
            else:
                print("Good job! You guessed my number in " + str(guessestaken) + " guesses!")
                break
        except ValueError:
            print("Only 1 to 20!")
main()
