# -*- coding: utf-8 -*-
import numpy
# Charles Thomas Wallace Truscott
# Very proud of this one, dy/dx = tan(x) Newton Raphson
# Second Revision

def main():
    epsilon = 0.00000000001
    number_of_guesses = 0
    shout_out_to_MIT = 45.0 * (numpy.pi / 180)
    y = numpy.tan(shout_out_to_MIT)
    guess = y/2.0
    while(abs(numpy.tan(guess)) != y):
        number_of_guesses += 1
        print('{} is the guess and it has taken {} iterations'.format(guess, number_of_guesses))
        guess = abs(guess - (((numpy.sin(guess)/numpy.cos(guess)) - y)/(1/((numpy.cos(guess)) ** 2))))
    print('tan({}) is the same as tan({})'.format(shout_out_to_MIT, guess))
    print('which are {} and {}'.format(y, numpy.tan(guess)))
    print('In degrees: {}, {}'.format(numpy.arctan(y) * (180 / numpy.pi), numpy.arctan(guess) * (180 / numpy.pi)))
    
"""
0.49999999999999994 is the guess and it has taken 1 iterations
0.8494156605301215 is the guess and it has taken 2 iterations
0.7896655706082891 is the guess and it has taken 3 iterations
0.7854164258595169 is the guess and it has taken 4 iterations
0.7853981637309699 is the guess and it has taken 5 iterations
tan(0.7853981633974483) is the same as tan(0.7853981633974483)
which are 0.9999999999999999 and 0.9999999999999999
In degrees: 45.0, 38.146025987222544

"""

if __name__ == "__main__": main()