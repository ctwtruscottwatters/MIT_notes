# -*- coding: utf-8 -*-
import numpy
# Charles Thomas Wallace Truscott
# Very proud of this one, dy/dx = tan(x) Newton Raphson
# Third Revision

def main():
    epsilon = 0.00000000001
    number_of_guesses = 0
    shout_out_to_MIT = 30.0 * (numpy.pi / 180)
    y = numpy.tan(shout_out_to_MIT)
    guess = y/2.0
    while(abs(numpy.tan(guess)) != y):
        number_of_guesses += 1
        print('{} is the guess and it has taken {} iterations'.format(guess, number_of_guesses))
        guess = abs(guess - (((numpy.sin(guess)/numpy.cos(guess)) - y)/(1/((numpy.cos(guess)) ** 2))))
    print('tan({}) is the same as tan({})'.format(shout_out_to_MIT, guess))
    print('which are {} and {}'.format(y, numpy.tan(guess)))
    print('In degrees: {}, {}'.format(numpy.arctan(y) * (180 / numpy.pi), numpy.arctan(numpy.tan(guess)) * (180 / numpy.pi)))
    print('I love MIT. Charles Truscott Watters')
    print('All my own work, dy/dx tan(x) = 1/((cos(x))^2)')
    print('tan(x) = sin(x)/cos(x)')
    print('Lifelong dream of sitting a unit at MIT come true')
"""
runfile('C:/Users/user/Desktop/tannewtonraphson.py', wdir='C:/Users/user/Desktop')
0.49999999999999994 is the guess and it has taken 1 iterations
0.8494156605301215 is the guess and it has taken 2 iterations
0.7896655706082891 is the guess and it has taken 3 iterations
0.7854164258595169 is the guess and it has taken 4 iterations
0.7853981637309699 is the guess and it has taken 5 iterations
tan(0.7853981633974483) is the same as tan(0.7853981633974483)
which are 0.9999999999999999 and 0.9999999999999999
In degrees: 45.0, 45.0

runfile('C:/Users/user/Desktop/tannewtonraphson.py', wdir='C:/Users/user/Desktop')
0.28867513459481287 is the guess and it has taken 1 iterations
0.5463317714914422 is the guess and it has taken 2 iterations
0.5239049238315444 is the guess and it has taken 3 iterations
0.5235988297305857 is the guess and it has taken 4 iterations
0.5235987755983005 is the guess and it has taken 5 iterations
tan(0.5235987755982988) is the same as tan(0.5235987755982988)
which are 0.5773502691896257 and 0.5773502691896257
In degrees: 29.999999999999996, 29.999999999999996
I love MIT. Charles Truscott Watters
All my own work, dy/dx tan(x) = 1/((cos(x))^2)
tan(x) = sin(x)/cos(x)
Lifelong dream of sitting a unit at MIT come true


"""

if __name__ == "__main__": main()