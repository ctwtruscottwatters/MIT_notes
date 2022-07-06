# -*- coding: utf-8 -*-
"""
oneHalf = Fraction(1, 2)

twoThirds = Fraction(2, 3)

print(oneHalf)
1/2

print(twoThirds)
2/3

Charles Truscott

runfile('C:/Users/17/Downloads/ProblemSet4/Frac_Class.py', wdir='C:/Users/17/Downloads/ProblemSet4')
One half plus two thirds is 1.1666666666666667 in decimal
One half squared is: 1/4
Two thirds squared is: 4/9
1/2 squared + 2/3 squared is 49/36 or 1.3611111111111112
1.1666666666666667 x 1.1666666666666667 = 1.3611111111111114

Charles Thomas Wallace Truscott Watters

MIT 6.00.1x Week 9 

"""

class Fraction(object):
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator
    def __str__(self):
        return str(self.numerator) + '/' + str(self.denominator)
    def getNumerator(self):
        return self.numerator
    def getDenominator(self):
        return self.denominator
    
    def __add__(self, other):
        new_Numerator = self.getNumerator() * other.getDenominator() + self.getDenominator() * other.getNumerator()
        new_Denominator = self.getDenominator() * other.getDenominator()
        return Fraction(new_Numerator, new_Denominator)
    def __sub__(self, other):
        new_Numerator = self.getNumerator() * other.getDenominator() - self.getNumerator() - other.getDenominator()
        new_Denominator = self.getDenominator() * other.getDenominator()
        return Fraction(new_Numerator, new_Denominator)
    def convert_to_floating_point(self):
        return float((self.getNumerator() / self.getDenominator()))
    def square(self):
        return Fraction(self.getNumerator() * self.getNumerator(), self.getDenominator() * self.getDenominator())
oneHalf = Fraction(1, 2)
twoThirds = Fraction(2, 3)
added_fractions = oneHalf + twoThirds
print("One half plus two thirds is {} in decimal".format(added_fractions.convert_to_floating_point()))
print("One half squared is: ", end='')
print(oneHalf.square())
print("Two thirds squared is: ", end='')
print(twoThirds.square())
print("{} squared + {} squared is {} or {}".format(oneHalf, twoThirds, added_fractions.square(), added_fractions.square().convert_to_floating_point()))
print("{} x {} = {}".format(added_fractions.convert_to_floating_point(), added_fractions.convert_to_floating_point(), added_fractions.convert_to_floating_point() * added_fractions.convert_to_floating_point()))


