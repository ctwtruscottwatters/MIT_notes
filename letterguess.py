# -*- coding: utf-8 -*-
"""
Created on Wed Mar 23 21:17:17 2022

@author: user
"""

def isIn():
    '''
    char: a single character
    aStr: an alphabetized string
    
    returns: True if char is in aStr; False otherwise
    '''
    aStr = 'abcdefghijklmnopqrstuvwxyz'
    char = 'w'
    length_of_string = len(aStr)
    high = length_of_string
    low = 0
    guess = int((high + low) / 2)
    numGuesses = 0
    while(aStr[guess] != char):
        print('{} {} {} {}'.format(aStr[guess], guess, high, low))
        if (str(aStr[guess]) > str(char)):
            high = guess
        elif (str(aStr[guess]) < str(char)):
            low = guess
        guess = int((((high + low) / 2)))
        numGuesses += 1
    print('Guess: {} Letter retrieved: {}'.format(guess, aStr[guess]))
    
isIn()