# -*- coding: utf-8 -*-
"""
All my own work. Love recursion. Charles Thomas Wallace Truscott. Massachusetts Institute of Technology via edX for an xSeries Computational Thinking in Python certificate 2022

127 Broken Head Rd, Suffolk Park / Byron Bay 2481, NSW Australia
+6141533702
ctwtruscottwatters@gmail.com

"""

def main(char, aStr):
    guesses = 0
    high = len(aStr)
    low = 0
    guess = int((high + low) / 2.0)
    print("high: {} low: {} guess: {} guessChar: {}".format(high, low, guess, aStr[guess]))
    if high == 0 or guess == 0 or guess == len(aStr):
        return False
    if guesses >= len(aStr):
        return False
    if char > aStr[guess]:
        low = guess
        main(char, main(char, aStr[low:high]))
    elif char < aStr[guess]:
        high = guess
        main(char, main(char, aStr[low:high]))
    if aStr[guess] == char:
        print("Character {} was found at index {}".format(aStr[guess], guess))
        return True
    guesses += 1
    
    
if __name__ == "__main__": main("k", "bcdefghijk")