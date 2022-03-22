# Charles Truscott
# I love MIT
# Thank you Eric Grimson, John Guttag, MIT 
epsilon = 0.0001
y = 24.0
guess = y/2.0
numGuesses = 0

while abs(((guess * guess) - y) >= epsilon):
    print('guess: {} number of guesses: {}'.format(guess, numGuesses))
    numGuesses += 1
    guess = guess - ((((guess ** 2 - y)/(2*guess)))) # root of the equation x^2 at x = 24 is x^2 - 24 / 2x the derivative of x^2, iterate until guess is found, the root of the equation x^2 at y = 24
print('The square root of {} is close to {}'.format(y, guess))
print('Guess squared is: {}'.format(guess * guess))

# Excited to plug in some derivatives, love Calculus, MIT OCW Single Variable Calculus such as derivatives, integrals, integration by substitution and integration by parts, partial fractions, conic sections, differentiation rules such as the chain rule, integration tables and integration by parts and integration by substitution and partial fractions, reverse chain rule for integration