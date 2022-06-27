# -*- coding: utf-8 -*-
"""
All my own work. Love recursion. Charles Thomas Wallace Truscott. Massachusetts Institute of Technology via edX for an xSeries Computational Thinking in Python certificate 2022

127 Broken Head Rd, Suffolk Park / Byron Bay 2481, NSW Australia
+6141533702
ctwtruscottwatters@gmail.com

"""
from sys import exit

def main(char, aStr):
    guesses = 0
    high = int(len(str(aStr)))
    low = 0
    guess = int((high + low) / 2.0)
    if aStr[guess] == char:
        print("Character {} was found at index {}".format(aStr[guess], guess))
        return True
    elif guesses > len(aStr) or guess == 0:
        print("No character was found.")
        return False
    print("high: {} low: {} guess: {} guessChar: {}".format(high, low, guess, aStr[guess]))
    if char > aStr[guess]:
        low = guess
    elif char < aStr[guess]:
        high = guess
    main(char, aStr[low:high])
    guesses += 1
    
    
if __name__ == "__main__": main('z', 'abfijmtvy')