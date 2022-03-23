# -*- coding: utf-8 -*-
# Charles Thomas Wallace Truscott Watters Byron Bay NSW 2481
# Textbook arrived today, ready for June the 2nd to sit 6.001
# Plenty of paper notes, algorithms, data structures
# Hope I can pass 6.002 even if I do manage to pass 6.001
# Nice to review source code and find every operation to describe
# Eventually hope to learn optimisation, simulation and statistica; modelling in the second inaugural CSci unit from MIT
# Note taking and 5 hours of study a day for 6.001 and 6.002, should pass :-)
# Second Revision, Third and Sixth and Ninety-Ninth roots needed to reach the sine, cosine and tangent of 45 degrees (invoked in the function in radians)
# going to work on this one
import numpy as np
def find_root(x, power, epsilon):
    if x < 0 and power % 2 == 0:
        return None
    low = min(-1, x)
    high = max(1, x)
    ans = (high + low) / 2.0
    while (abs((ans ** power) - x) >= epsilon):
        if ans ** power < x:
            low = ans
        else:
            high = ans
        ans = (high + low) / 2.0
    return ans

def test_find_root(x_vals, powers, epsilons):
    for x in x_vals:
        for p in powers:
            for e in epsilons:
                result = find_root(x, p, e)
                if result == None:
                    val = 'No root exists'
                else:
                    val = 'Okay'
                    if abs(result ** p - x) > e:
                        val = 'Bad'
                if result != None:
                    if x == float(np.sin(45.0 * np.pi / 180.0)):
                        print('{} ^ {} = {} which is sin({}) {} {} {}'.format(result, p, x, '45.0', 'in radians or', (result ** p) * 180.0 / np.pi, ' degrees'))
                        print('arcsin({} ^ {}) = {} degrees'.format(result, p, np.arcsin(result ** p) * 180 / np.pi))
                    elif x == float(np.cos(45.0 * (np.pi / 180))):
                        print('{} ^ {} = {} which is cos({}) {} {} {}'.format(result, p, x, '45.0', 'in radians or', (result ** p) * 180.0 / np.pi, ' degrees'))
                        print('arccos({} ^ {}) = {} degrees'.format(result, p, np.arccos(result ** p) * 180 / np.pi))
                    elif x == float(np.tan(45.0 * (np.pi / 180.0))):
                        print('{} ^ {} = {} which is tan({}) {} {} {}'.format(result, p, x, '45.0', 'in radians or', (result ** p) * 180.0 / np.pi, ' degrees'))
                        print('arctan({} ^ {}) = {} degrees'.format(result, p, np.arctan(result ** p) * 180 / np.pi))
                    
def main():
    x_vals = (float(np.sin(45.0 * np.pi / 180.0)), float(np.cos(45.0 * (np.pi / 180))), float(np.tan(45.0 * (np.pi / 180.0))))
    powers = (3, 6, 99)
    epsilons = (0.001, 0.00001, 0.0000001)
    test_find_root(x_vals, powers, epsilons)
    print('Charles Truscott for an MIT certificate, page 70 Guttag et. alia')
    
if __name__ == "__main__": main()

