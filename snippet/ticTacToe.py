#!/bin/zsh
# Automate the Boring Stuff with Python

theBoard = {'top-L': ' ', 'top-m': ' ', 'top-R': ' ',
 'mid-L': ' ', 'mid-m': ' ', 'mid-R': ' ',
 'low-L': ' ', 'low-m': ' ', 'low-R': ' '}

def printBoard(board):
    print(board['top-L'] + '|' + board['top-m'] + '|' + board['top-R'])
    print('-+-+-')
    print(board['mid-L'] + '|' + board['mid-m'] + '|' + board['mid-R'])
    print('-+-+-')
    print(board['low-L'] + '|' + board['low-m'] + '|' + board['low-R'])

turn = 'X'

for i in range(9):
    printBoard(theBoard)
    print('Turn for '  + turn +    '. move on which space?')
    move = input()
    theBoard[move] = turn
    if turn == 'X':
        turn = 'O'
    else:
        turn = 'X'

printBoard(theBoard)     
