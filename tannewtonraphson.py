# -*- coding: utf-8 -*-
import numpy
# Charles Thomas Wallace Truscott
# Very proud of this one, dy/dx = tan(x) Newton Raphson
# Github.com/ctwtruscottwatters
# MIT 6.001 through edX.org

def main():
    epsilon = 0.00001
    number_of_guesses = 0
    shout_out_to_MIT = 45.0 * (numpy.pi / 180)
    y = numpy.tan(shout_out_to_MIT)
    guess = y/2.0
    while(abs(numpy.tan(guess) - y) >= epsilon):
        number_of_guesses += 1
        print('{} is the guess and it has taken {} iterations'.format(guess, number_of_guesses))
        guess = abs(guess - (((numpy.tan(guess)) - y)/(1/((numpy.cos(guess)) ** 2))))
    print('tan({}) is the same as tan({})'.format(shout_out_to_MIT, guess))
    print('which are {} and {}'.format(y, numpy.tan(guess)))
    
"""
0.49999999999999994 is the guess and it has taken 1 iterations
0.8494156605301215 is the guess and it has taken 2 iterations
0.7896655706082891 is the guess and it has taken 3 iterations
0.785416425859517 is the guess and it has taken 4 iterations
tan(0.7853981633974483) is the same as tan(0.7853981637309698)
which are 0.9999999999999999 and 1.000000000667043
"""

if __name__ == "__main__": main()
