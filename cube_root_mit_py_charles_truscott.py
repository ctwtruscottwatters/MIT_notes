# cube_root_mit_py_charles_truscott.py
# -*- coding: utf-8 -*-
"""
Charles Thomas Wallace Truscott
I love MIT :-)
Thank you MIT
I had always wanted to study at MIT and get the chance with edX :-)
Byron Bay NSW 2481
Re-form of iteration in cube root example
Need to think out algorithms for numerics
Saw two interesting examples in the lectures of definitions
of the Peano arithmetic reaching to a set a variable to increment
itself by itself until another number was reached, as the 
definition of multiplication as repeated addition
e.g. 5 x 3 = 3 + 3 + 3 + 3 + 3
e.g.
if you want to solve five times three
set a variable to 0 and increment itself by 3 5 times
print('{} x {} = {}'.format(5, 3, 3 + 3 + 3 + 3 + 3))
"""

cube = 2481
epsilon = 0.00001
guess = 0
num_guesses = 0
while(not ((guess ** 3 - cube) >= epsilon)):
    guess += epsilon
    num_guesses += 1
print('The cube root of {} is apparently {}'.format(cube, guess))
print('guess cubed equals: {}\n'.format(guess ** 3))

    
