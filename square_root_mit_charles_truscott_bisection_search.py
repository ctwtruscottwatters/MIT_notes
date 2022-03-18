# Charles Thomas Wallace Truscott
# MIT 6.001 Introduction to Computer Science and Programming Using Python
# Square Root Bisection Search
# edX.org
# written from scratch, nice to see how operators and operands use bisection search for other problems
# data structures and algorithms, e.g. what is the fastest way to search a list of values, e.g. by numerical key and not indexed from 0 to len(values) incrementing by indices



square = 2481
high = square
low = 0
guesses = 0
guess = (high + low) / 2.0
epsilon = 0.001

while(((guess ** 2) - square) >= epsilon):
    if ((guess ** 2) > square):
        high = guess
    else:
        low = guess
    guess = ((high + low) / 2.0)

    
print('{} is apparently the square root of {}'.format(guess, square))
