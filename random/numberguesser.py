#!/bin/zsh
# Automate the Boring Stuff with Python
import random

print("I am thinking of a number between 1 and 20")

def main():
    count=0
    for guessestaken in range(1,7):
        count+=1
        secretnumber = random.randint(1,20)
        print("Take a guess.")
        guess = int(input())

        if guess < secretnumber:
            print("Your guess is too low.")
            if count == 6:
                print("Nope. The number I was thinking of was " + str(secretnumber))
        elif guess > secretnumber:
            print("Your guess is too high.")
            if count == 6:
                print("Nope. The number I was thinking of was " + str(secretnumber))
        elif guess == secretnumber:
            print("Good job! You guessed my number in " + str(guessestaken) + " guesses!")
            break
        else:
            print("Nope. The number I was thinking of was " + str(secretnumber))
main()
