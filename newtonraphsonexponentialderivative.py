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