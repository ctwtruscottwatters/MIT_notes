# Charles Truscott
# I love MIT
# Thank you Eric Grimson, John Guttag, MIT 
import numpy

epsilon = 0.01
y = 93.0
guess = y/2.0
numGuesses = 0

while (abs(numpy.exp(guess) - y) >= epsilon):
    print('guess: {} number of guesses: {}'.format(guess, numGuesses))
    numGuesses += 1
    guess = +(guess - (numpy.exp(guess) - y)/((numpy.exp(guess))))
print('{} = e ^ {}'.format(y, guess))
print('Charles Thomas Wallace Truscott. I love MIT. All my own work')

#dy/dx e^x = 93.0 
#guess = guess - ((numpy.sin(guess) - y)/-((numpy.cos(guess))
"""
93.0 4.5326114282570416

runfile('C:/Users/user/Desktop/newtonraphsonexponentialderivative.py', wdir='C:/Users/user/Desktop')
guess: 46.5 number of guesses: 0
guess: 45.5 number of guesses: 1
guess: 44.5 number of guesses: 2
guess: 43.5 number of guesses: 3
guess: 42.5 number of guesses: 4
guess: 41.5 number of guesses: 5
guess: 40.5 number of guesses: 6
guess: 39.5 number of guesses: 7
guess: 38.5 number of guesses: 8
guess: 37.5 number of guesses: 9
guess: 36.50000000000001 number of guesses: 10
guess: 35.50000000000002 number of guesses: 11
guess: 34.50000000000006 number of guesses: 12
guess: 33.500000000000156 number of guesses: 13
guess: 32.50000000000042 number of guesses: 14
guess: 31.500000000001133 number of guesses: 15
guess: 30.500000000003077 number of guesses: 16
guess: 29.500000000008356 number of guesses: 17
guess: 28.500000000022705 number of guesses: 18
guess: 27.500000000061707 number of guesses: 19
guess: 26.500000000167727 number of guesses: 20
guess: 25.500000000455916 number of guesses: 21
guess: 24.500000001239297 number of guesses: 22
guess: 23.50000000336875 number of guesses: 23
guess: 22.500000009157205 number of guesses: 24
guess: 21.500000024891854 number of guesses: 25
guess: 20.500000067663066 number of guesses: 26
guess: 19.500000183927273 number of guesses: 27
guess: 18.500000499966124 number of guesses: 28
guess: 17.50000135904851 number of guesses: 29
guess: 16.500003694274554 number of guesses: 30
guess: 15.500010042062243 number of guesses: 31
guess: 14.50002729702864 number of guesses: 32
guess: 13.500074200080928 number of guesses: 33
guess: 12.500201689815862 number of guesses: 34
guess: 11.500548198666511 number of guesses: 35
guess: 10.501489781055465 number of guesses: 36
guess: 9.504046858520368 number of guesses: 37
guess: 8.510979964552087 number of guesses: 38
guess: 7.529695890335421 number of guesses: 39
guess: 6.579627730653698 number of guesses: 40
guess: 5.708745772816824 number of guesses: 41
guess: 5.017210962398645 number of guesses: 42
guess: 4.633147422937058 number of guesses: 43
guess: 4.537489189405706 number of guesses: 44
93.0 = e ^ 4.5326114282570416
Charles Thomas Wallace Truscott. I love MIT. All my own work
"""
