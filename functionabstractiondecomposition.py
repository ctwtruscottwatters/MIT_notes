# Charles Truscott
# I love MIT
# Thank you Eric Grimson, John Guttag, MIT 
import numpy
# THANK YOU MIT

def main():
    choice = float(input('Enter a value to find which x satisfies e ^ x = your input:\t'))
    answer = find_e_x(choice)
    print('e ^ {} = {}'.format(answer, choice))
    cube_root_of_answer = find_cube_root(answer)
    square_root_of_answer = find_square_root(answer)
    print('{} is the square root of {} and {} is the cube root of {}'.format(square_root_of_answer, answer, cube_root_of_answer, answer))
    print('e^({})^2 = {} e^({})^3 = {}'.format(square_root_of_answer, numpy.exp((2 * (square_root_of_answer))),cube_root_of_answer, numpy.exp((cube_root_of_answer **3)))) # e ^ x ^ 2 = e ^ 2 * x, etc
    print('e ^ {} = {}, once again'.format(answer, choice))
def find_e_x(input_y):
    epsilon = 0.0001
    y = input_y
    guess = y/2.0
    numGuesses = 0

    while (abs(numpy.exp(guess) - y) >= epsilon):
       # print('guess: {} number of guesses: {}'.format(guess, numGuesses))
        numGuesses += 1
        guess = abs((guess - (numpy.exp(guess) - y)/(numpy.exp(guess))))
    return guess
def find_square_root(input_sq):
    # Charles Truscott# Charles Thomas Wallace Truscott
    # MIT 6.001 Introduction to Computer Science and Programming Using Python

    square = input_sq
    high = square
    low = 0
    epsilon = 0.001
    guess = (high + low) / 2.0
    numGuesses = 0
    while(((guess ** 2) - square) >= epsilon):
       # print('high {} low {} guess {}'.format(high, low, guess))
        if ((((high + low) / 2.0 ) ** 2) > square):
            high = guess
        elif ((((high + low) / 2.0 ) ** 2) < square):
            low = guess
        guess = (((high + low) / 2.0))
        numGuesses += 1
    return guess
    #print('{} is apparently the square root of {}'.format(guess, square))
    #print('Finding the square root took {} guesses. '.format(numGuesses))


def find_cube_root(input_cube):
    cube = input_cube
    epsilon = 0.00001
    guess = 0
    num_guesses = 0
    while(not ((guess ** 3 - cube) >= epsilon)):
        guess += epsilon
        num_guesses += 1
    return guess

print('With love to MIT, Charles Truscott Byron Bay NSW 2481')

"""

Enter a value to find which x satisfies e ^ x = your input:	2
e ^ 0.6931475810597714 = 2.0
0.3465737905298857 is the square root of 0.6931475810597714 and 0.8850099999986071 is the cube root of 0.6931475810597714
e^(0.3465737905298857)^2 = 2.0000008009998127 e^(0.8850099999986071)^3 = 2.0000608838312566
e ^ 0.6931475810597714 = 2.0, once again

With love to MIT, Charles Truscott Byron Bay NSW 2481

Enter a value to find which x satisfies e ^ x = your input:	45
e ^ 3.806663453328388 = 45.0
1.903331726664194 is the square root of 3.806663453328388 and 1.5614100000017617 is the cube root of 3.806663453328388
e^(1.903331726664194)^2 = 45.000043360133965 e^(1.5614100000017617)^3 = 45.00256261388416
e ^ 3.806663453328388 = 45.0, once again


"""
if __name__ == "__main__": main()