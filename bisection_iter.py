# -*- coding: utf-8 -*-
"""
Charles Thomas Wallace Truscott

MIT OCW Bisection Search Alphabetically (numerically and pointer based ordered value) 

Ordering principles, like inequalities allow to halve the problem

Iterative Algorithm

6.0001 via edX.org

Thank you MIT, Grimson, Bell

8 days until mid-terms

due 9:30 A.M. GMT + 10 AEST Australian Eastern Standard Time

Authored 4:24 p.m. AEST Monday 27th of June in Spyder

Into a copy of Knuth's Art of Computer Programming, includes bisection search and binary trees ... Turing complete

"""

aStr = "hijklmnoqrstuxyz"
char = "a"
high = len(aStr)
low = 0
guess = int((high + low) / 2.0)
guessChar = ""
guesses = 1
found = False
while found != True:
    print("high: {} low: {} guesses: {} guesschar: {}".format(high, low, guesses, guessChar))
    if char > aStr[guess]:
        low = guess
        guessChar = aStr[guess]
    elif char < aStr[guess]:
        high = guess
        guessChar = aStr[guess]
    if guesses > len(aStr) + 1:
        found = False
        break
    if aStr[guess] == char:
        found = True
    guess = int((high + low) / 2.0)
    guesses += 1
    
if found == True:
    print("The guess was found at index {} and is the letter {}".format(guess, aStr[guess]))
elif found == False:
    print("The index was not found after {} guesses".format(guesses))
