# -*- coding: utf-8 -*-
"""
Extra-curricular study to complement my MIT units via edX
10:55 P.M. 23/03/2022 AEST

CHARLES THOMAS WALLACE TRUSCOTT

WOOOOOHOOOOOOOO

I'm sitting a unit from MIT and as part of my extra-curricular study just calculated an approximation to sine by using the Taylor polynomial

ALL MY OWN WORK

Byron Bay NSW 2481

"""
import math
import numpy
def find_sine(find_answer):
    x = []
    for n in range(0, 100):
        if n % 2 == 0:
            continue
        else:
                x.append(n)
    dummy_val = float(find_answer) * math.pi / 180
    num = dummy_val
    adding = False
    subtracting = False
    index = 0
    for n in x:
        print('guess: {} index: {} n: {} index == even (hence add?): {}'.format(num, index, n, 'True' if index % 2 == 0 else 'False'))
        if index % 2 == 0:
                num -= ((dummy_val ** n))/((math.factorial(n)))
        else:
                num += ((dummy_val ** n))/((math.factorial(n)))
        index += 1
    print('Final Step, subtracting {} degrees: {} = {} - {}'.format(find_answer, dummy_val - num, dummy_val, num))
    num = dummy_val - num
    print('{} is the sine of {} evaluated with a Taylor polynomial, to compare: {} is the computer\'s inbuilt sine for {}'.format(num, dummy_val * 180 / math.pi, numpy.sin(dummy_val), dummy_val * 180 / math.pi))
    print('All my own work. Charles Thomas Wallace Truscott Watters')
    
# ALL MY OWN WORK, CHARLES TRUSCOTT, NUMERICAL INFINITE SERIES FOR SINE

            
#        x = n - (n ** (2 * n + 1))/(math.factorial(2 * n + 1))
#def find_pi():
    
def main():
    print('Welcome to the program. Authored by Charles Truscott from the Taylor Approximation of the sine from Single Variable Calculus')
    find_answer = input('Enter a value, in degrees for which to calculate the sine:\t')
    find_sine(find_answer)

if __name__ == "__main__":main()


"""
Next Ramanujan's Infinite Series for Pi
runfile('C:/Users/user/Desktop/excurr_pi_MIT_infiniteseries.py', wdir='C:/Users/user/Desktop')
Welcome to the program. Authored by Charles Truscott from the Taylor Approximation of the sine from Single Variable Calculus

Enter a value, in degrees for which to calculate the sine:	93.125
guess: 1.6253378659197195 index: 0 n: 1 index == even (hence add?): True
guess: 0.0 index: 1 n: 3 index == even (hence add?): False
guess: 0.715615452186512 index: 2 n: 5 index == even (hence add?): True
guess: 0.6210925558436662 index: 3 n: 7 index == even (hence add?): False
guess: 0.6270378731331349 index: 4 n: 9 index == even (hence add?): True
guess: 0.6268197358763781 index: 5 n: 11 index == even (hence add?): False
guess: 0.6268249745877167 index: 6 n: 13 index == even (hence add?): True
guess: 0.6268248858747348 index: 7 n: 15 index == even (hence add?): False
guess: 0.6268248869907117 index: 8 n: 17 index == even (hence add?): True
guess: 0.626824886979873 index: 9 n: 19 index == even (hence add?): False
guess: 0.6268248869799568 index: 10 n: 21 index == even (hence add?): True
guess: 0.6268248869799562 index: 11 n: 23 index == even (hence add?): False
guess: 0.6268248869799562 index: 12 n: 25 index == even (hence add?): True
guess: 0.6268248869799562 index: 13 n: 27 index == even (hence add?): False
guess: 0.6268248869799562 index: 14 n: 29 index == even (hence add?): True
guess: 0.6268248869799562 index: 15 n: 31 index == even (hence add?): False
guess: 0.6268248869799562 index: 16 n: 33 index == even (hence add?): True
guess: 0.6268248869799562 index: 17 n: 35 index == even (hence add?): False
guess: 0.6268248869799562 index: 18 n: 37 index == even (hence add?): True
guess: 0.6268248869799562 index: 19 n: 39 index == even (hence add?): False
guess: 0.6268248869799562 index: 20 n: 41 index == even (hence add?): True
guess: 0.6268248869799562 index: 21 n: 43 index == even (hence add?): False
guess: 0.6268248869799562 index: 22 n: 45 index == even (hence add?): True
guess: 0.6268248869799562 index: 23 n: 47 index == even (hence add?): False
guess: 0.6268248869799562 index: 24 n: 49 index == even (hence add?): True
guess: 0.6268248869799562 index: 25 n: 51 index == even (hence add?): False
guess: 0.6268248869799562 index: 26 n: 53 index == even (hence add?): True
guess: 0.6268248869799562 index: 27 n: 55 index == even (hence add?): False
guess: 0.6268248869799562 index: 28 n: 57 index == even (hence add?): True
guess: 0.6268248869799562 index: 29 n: 59 index == even (hence add?): False
guess: 0.6268248869799562 index: 30 n: 61 index == even (hence add?): True
guess: 0.6268248869799562 index: 31 n: 63 index == even (hence add?): False
guess: 0.6268248869799562 index: 32 n: 65 index == even (hence add?): True
guess: 0.6268248869799562 index: 33 n: 67 index == even (hence add?): False
guess: 0.6268248869799562 index: 34 n: 69 index == even (hence add?): True
guess: 0.6268248869799562 index: 35 n: 71 index == even (hence add?): False
guess: 0.6268248869799562 index: 36 n: 73 index == even (hence add?): True
guess: 0.6268248869799562 index: 37 n: 75 index == even (hence add?): False
guess: 0.6268248869799562 index: 38 n: 77 index == even (hence add?): True
guess: 0.6268248869799562 index: 39 n: 79 index == even (hence add?): False
guess: 0.6268248869799562 index: 40 n: 81 index == even (hence add?): True
guess: 0.6268248869799562 index: 41 n: 83 index == even (hence add?): False
guess: 0.6268248869799562 index: 42 n: 85 index == even (hence add?): True
guess: 0.6268248869799562 index: 43 n: 87 index == even (hence add?): False
guess: 0.6268248869799562 index: 44 n: 89 index == even (hence add?): True
guess: 0.6268248869799562 index: 45 n: 91 index == even (hence add?): False
guess: 0.6268248869799562 index: 46 n: 93 index == even (hence add?): True
guess: 0.6268248869799562 index: 47 n: 95 index == even (hence add?): False
guess: 0.6268248869799562 index: 48 n: 97 index == even (hence add?): True
guess: 0.6268248869799562 index: 49 n: 99 index == even (hence add?): False
Final Step, subtracting 93.125 degrees: 0.9985129789397633 = 1.6253378659197195 - 0.6268248869799562
0.9985129789397633 is the sine of 93.125 evaluated with a Taylor polynomial, to compare: 0.9985129789397631 is the computer's inbuilt sine for 93.125
All my own work. Charles Thomas Wallace Truscott Watters

"""