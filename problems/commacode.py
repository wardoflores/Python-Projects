#!/bin/zsh
# Automate the Boring Stuff with Python

'''
Comma Code

Say you have a list like this:

spam = ["apples", "bananas", "tofu", "cats"]

Write a function that takes a list value as an argument and returns a
string with all the items separated by a comma and a space, with an and
inserted before the last item. For example, passing the previous spam 
list to function would return "apples, bananas, tofu, and cats".

But your function should be able to work with any list value passed
to it.
'''

lstwtrds = ['one', 'two', 'three']

for word in lstwtrds:
    print(word, end=', ')
    # TODO: make algorithm for last word.

    
