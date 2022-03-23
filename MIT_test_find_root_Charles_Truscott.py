# -*- coding: utf-8 -*-
# Charles Thomas Wallace Truscott Watters Byron Bay NSW 2481
# Textbook arrived today, ready for June the 2nd to sit 6.001
# Plenty of paper notes, algorithms, data structures
# Hope I can pass 6.002 even if I do manage to pass 6.001
# Nice to review source code and find every operation to describe
# Eventually hope to learn optimisation, simulation and statistica; modelling in the second inaugural CSci unit from MIT
# Note taking and 5 hours of study a day for 6.001 and 6.002, should pass :-)

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
                print('f\'x = {}, power = {}, epsilon = {}, val = {}, result = {}'.format(x, p, e, val, result))
                if result != None:
                    print('{} ^ {} = {}'.format(result, p, x))
def main():
    x_vals = (0.50, 0.333, -9)
    powers = (1, 2, 3)
    epsilons = (0.001, 0.00001, 0.0000001)
    test_find_root(x_vals, powers, epsilons)
    print('Charles Truscott for an MIT certificate, page 70 Guttag et. alia')
    
if __name__ == "__main__": main()


"""

runfile('C:/Users/user/Desktop/MIT_test_find_root_Charles_Truscott.py', wdir='C:/Users/user/Desktop')
f'x = 0.5, power = 1, epsilon = 0.001, val = Okay, result = 0.5
0.5 ^ 1 = 0.5
f'x = 0.5, power = 1, epsilon = 1e-05, val = Okay, result = 0.5
0.5 ^ 1 = 0.5
f'x = 0.5, power = 1, epsilon = 1e-07, val = Okay, result = 0.5
0.5 ^ 1 = 0.5
f'x = 0.5, power = 2, epsilon = 0.001, val = Okay, result = 0.70703125
0.70703125 ^ 2 = 0.5
f'x = 0.5, power = 2, epsilon = 1e-05, val = Okay, result = 0.7071075439453125
0.7071075439453125 ^ 2 = 0.5
f'x = 0.5, power = 2, epsilon = 1e-07, val = Okay, result = 0.7071068286895752
0.7071068286895752 ^ 2 = 0.5
f'x = 0.5, power = 3, epsilon = 0.001, val = Okay, result = 0.7939453125
0.7939453125 ^ 3 = 0.5
f'x = 0.5, power = 3, epsilon = 1e-05, val = Okay, result = 0.793701171875
0.793701171875 ^ 3 = 0.5
f'x = 0.5, power = 3, epsilon = 1e-07, val = Okay, result = 0.7937005758285522
0.7937005758285522 ^ 3 = 0.5
f'x = 0.333, power = 1, epsilon = 0.001, val = Okay, result = 0.33203125
0.33203125 ^ 1 = 0.333
f'x = 0.333, power = 1, epsilon = 1e-05, val = Okay, result = 0.3330078125
0.3330078125 ^ 1 = 0.333
f'x = 0.333, power = 1, epsilon = 1e-07, val = Okay, result = 0.33299994468688965
0.33299994468688965 ^ 1 = 0.333
f'x = 0.333, power = 2, epsilon = 0.001, val = Okay, result = 0.5771484375
0.5771484375 ^ 2 = 0.333
f'x = 0.333, power = 2, epsilon = 1e-05, val = Okay, result = 0.577056884765625
0.577056884765625 ^ 2 = 0.333
f'x = 0.333, power = 2, epsilon = 1e-07, val = Okay, result = 0.5770615339279175
0.5770615339279175 ^ 2 = 0.333
f'x = 0.333, power = 3, epsilon = 0.001, val = Okay, result = 0.693359375
0.693359375 ^ 3 = 0.333
f'x = 0.333, power = 3, epsilon = 1e-05, val = Okay, result = 0.6931304931640625
0.6931304931640625 ^ 3 = 0.333
f'x = 0.333, power = 3, epsilon = 1e-07, val = Okay, result = 0.6931300163269043
0.6931300163269043 ^ 3 = 0.333
f'x = -9, power = 1, epsilon = 0.001, val = Okay, result = -8.9993896484375
-8.9993896484375 ^ 1 = -9
f'x = -9, power = 1, epsilon = 1e-05, val = Okay, result = -8.999990463256836
-8.999990463256836 ^ 1 = -9
f'x = -9, power = 1, epsilon = 1e-07, val = Okay, result = -8.999999925494194
-8.999999925494194 ^ 1 = -9
f'x = -9, power = 2, epsilon = 0.001, val = No root exists, result = None
f'x = -9, power = 2, epsilon = 1e-05, val = No root exists, result = None
f'x = -9, power = 2, epsilon = 1e-07, val = No root exists, result = None
f'x = -9, power = 3, epsilon = 0.001, val = Okay, result = -2.08013916015625
-2.08013916015625 ^ 3 = -9
f'x = -9, power = 3, epsilon = 1e-05, val = Okay, result = -2.0800843238830566
-2.0800843238830566 ^ 3 = -9
f'x = -9, power = 3, epsilon = 1e-07, val = Okay, result = -2.0800838209688663
-2.0800838209688663 ^ 3 = -9
Charles Truscott for an MIT certificate, page 70 Guttag et. alia


"""