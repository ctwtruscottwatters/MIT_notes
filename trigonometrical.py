# -*- coding: utf-8 -*-
# Charles Thomas Wallace Truscott Watters Byron Bay NSW 2481
# Textbook arrived today, ready for June the 2nd to sit 6.001
# Plenty of paper notes, algorithms, data structures
# Hope I can pass 6.002 even if I do manage to pass 6.001

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

def test_find_root(x_vals, powers, epsilons, input_sine, input_cosine, input_tangent):
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
                    if (result ** p - float(np.sin(input_sine * np.pi / 180.0)) <= e):
                        print('The {}th root of sin({}) is {}'.format(p, input_sine * np.pi / 180.0, result))
                        print('and arcsin({} ^ {}) = {}'.format(result, p, np.arcsin((result ** p)) * 180 / np.pi))
                        print('and sin({} degrees) = {}'.format(np.arcsin(x) * 180.0 / np.pi, x))
                        print('and sin({} degrees) = {}'.format(input_sine, np.sin(input_sine * np.pi / 180.0)))
                    elif (result ** p - float(np.cos(input_cosine * np.pi / 180.0)) <= e):
                        print('The {}th root of cos({}) is '.format(p, input_cosine * np.pi / 180.0, result))
                        print('and arccos({} ^ {}) = {}'.format(result, p, np.arccos((result ** p)) * 180 / np.pi))
                        print('and cos({} degrees) = {}'.format(np.arccos(x) * 180.0 / np.pi, x))
                        print('and cos({} degrees) = {}'.format(input_cosine, np.cos(input_cosine * np.pi / 180.0)))
                    elif (result ** p - float(np.tan(input_tangent * np.pi / 180.0)) <= e):
                        print('The {}th root of tan({}) is {}'.format(p, input_tangent * np.pi / 180.0, result))
                        print('and arctan({} ^ {}) = {}'.format(result, p, np.arctan((result ** p)) * 180 / np.pi))
                        print('and tan({} degrees) = {}'.format(np.arctan(x) * 180.0 / np.pi, x))
                        print('and tan({} degrees) = {}'.format(input_tangent, np.tan(input_tangent * np.pi / 180.0)))
                    
def main():
    input_sine = float(input('Input a value (in degrees) for the sine:\t'))
    input_cosine = float(input('Input a value (in degrees) for the cosine:\t'))
    input_tangent = float(input('Input a value (in degrees) for the tangent:\t'))
    print('\n')
    x_vals = (float(np.sin(input_sine * np.pi / 180.0)), float(np.cos(input_cosine * (np.pi / 180))), float(np.tan(input_tangent * (np.pi / 180.0))))
    powers = (40, 60, 99)
    epsilons = (0.001, 0.00001, 0.0000001)
    test_find_root(x_vals, powers, epsilons, input_sine, input_cosine, input_tangent)
    print('Charles Truscott for an MIT certificate, page 70 Guttag et. alia')
    
if __name__ == "__main__": main()

"""

Input a value (in degrees) for the sine:	45

Input a value (in degrees) for the cosine:	45

Input a value (in degrees) for the tangent:	45


The 40th root of sin(0.7853981633974483) is 0.99139404296875
and arcsin(0.99139404296875 ^ 40) = 45.04848490175129
and sin(45.00000000000001 degrees) = 0.7071067811865476
and sin(45.0 degrees) = 0.7071067811865476
The 40th root of sin(0.7853981633974483) is 0.9913730621337891
and arcsin(0.9913730621337891 ^ 40) = 44.9999414454123
and sin(45.00000000000001 degrees) = 0.7071067811865476
and sin(45.0 degrees) = 0.7071067811865476
The 40th root of sin(0.7853981633974483) is 0.9913730844855309
and arcsin(0.9913730844855309 ^ 40) = 44.999993117544264
and sin(45.00000000000001 degrees) = 0.7071067811865476
and sin(45.0 degrees) = 0.7071067811865476
The 60th root of sin(0.7853981633974483) is 0.9942626953125
and arcsin(0.9942626953125 ^ 60) = 45.07711011046793
and sin(45.00000000000001 degrees) = 0.7071067811865476
and sin(45.0 degrees) = 0.7071067811865476
The 60th root of sin(0.7853981633974483) is 0.9942402839660645
and arcsin(0.9942402839660645 ^ 60) = 44.99951644496803
and sin(45.00000000000001 degrees) = 0.7071067811865476
and sin(45.0 degrees) = 0.7071067811865476
The 60th root of sin(0.7853981633974483) is 0.9942404255270958
and arcsin(0.9942404255270958 ^ 60) = 45.000005911040404
and sin(45.00000000000001 degrees) = 0.7071067811865476
and sin(45.0 degrees) = 0.7071067811865476
The 99th root of sin(0.7853981633974483) is 0.9965057373046875
and arcsin(0.9965057373046875 ^ 99) = 45.002050297535995
and sin(45.00000000000001 degrees) = 0.7071067811865476
and sin(45.0 degrees) = 0.7071067811865476
The 99th root of sin(0.7853981633974483) is 0.9965052604675293
and arcsin(0.9965052604675293 ^ 99) = 44.999335992038915
and sin(45.00000000000001 degrees) = 0.7071067811865476
and sin(45.0 degrees) = 0.7071067811865476
The 99th root of sin(0.7853981633974483) is 0.9965053759515285
and arcsin(0.9965053759515285 ^ 99) = 44.99999333942125
and sin(45.00000000000001 degrees) = 0.7071067811865476
and sin(45.0 degrees) = 0.7071067811865476
The 40th root of sin(0.7853981633974483) is 0.99139404296875
and arcsin(0.99139404296875 ^ 40) = 45.04848490175129
and sin(45.00000000000001 degrees) = 0.7071067811865476
and sin(45.0 degrees) = 0.7071067811865476
The 40th root of sin(0.7853981633974483) is 0.9913730621337891
and arcsin(0.9913730621337891 ^ 40) = 44.9999414454123
and sin(45.00000000000001 degrees) = 0.7071067811865476
and sin(45.0 degrees) = 0.7071067811865476
The 40th root of sin(0.7853981633974483) is 0.9913730844855309
and arcsin(0.9913730844855309 ^ 40) = 44.999993117544264
and sin(45.00000000000001 degrees) = 0.7071067811865476
and sin(45.0 degrees) = 0.7071067811865476
The 60th root of sin(0.7853981633974483) is 0.9942626953125
and arcsin(0.9942626953125 ^ 60) = 45.07711011046793
and sin(45.00000000000001 degrees) = 0.7071067811865476
and sin(45.0 degrees) = 0.7071067811865476
The 60th root of sin(0.7853981633974483) is 0.9942402839660645
and arcsin(0.9942402839660645 ^ 60) = 44.99951644496803
and sin(45.00000000000001 degrees) = 0.7071067811865476
and sin(45.0 degrees) = 0.7071067811865476
The 60th root of sin(0.7853981633974483) is 0.9942404255270958
and arcsin(0.9942404255270958 ^ 60) = 45.000005911040404
and sin(45.00000000000001 degrees) = 0.7071067811865476
and sin(45.0 degrees) = 0.7071067811865476
The 99th root of sin(0.7853981633974483) is 0.9965057373046875
and arcsin(0.9965057373046875 ^ 99) = 45.002050297535995
and sin(45.00000000000001 degrees) = 0.7071067811865476
and sin(45.0 degrees) = 0.7071067811865476
The 99th root of sin(0.7853981633974483) is 0.9965052604675293
and arcsin(0.9965052604675293 ^ 99) = 44.999335992038915
and sin(45.00000000000001 degrees) = 0.7071067811865476
and sin(45.0 degrees) = 0.7071067811865476
The 99th root of sin(0.7853981633974483) is 0.9965053759515285
and arcsin(0.9965053759515285 ^ 99) = 44.99999333942125
and sin(45.00000000000001 degrees) = 0.7071067811865476
and sin(45.0 degrees) = 0.7071067811865476
The 40th root of tan(0.7853981633974483) is 0.9999847412109375
and arctan(0.9999847412109375 ^ 40) = 44.98251458340694
and tan(45.0 degrees) = 0.9999999999999999
and tan(45.0 degrees) = 0.9999999999999999
The 40th root of tan(0.7853981633974483) is 0.9999997615814209
and arctan(0.9999997615814209 ^ 40) = 44.999726792400644
and tan(45.0 degrees) = 0.9999999999999999
and tan(45.0 degrees) = 0.9999999999999999
The 40th root of tan(0.7853981633974483) is 0.9999999981373549
and arctan(0.9999999981373549 ^ 40) = 44.99999786556589
and tan(45.0 degrees) = 0.9999999999999999
and tan(45.0 degrees) = 0.9999999999999999
The 60th root of tan(0.7853981633974483) is 0.9999847412109375
and arctan(0.9999847412109375 ^ 60) = 44.973771877146
and tan(45.0 degrees) = 0.9999999999999999
and tan(45.0 degrees) = 0.9999999999999999
The 60th root of tan(0.7853981633974483) is 0.9999998807907104
and arctan(0.9999998807907104 ^ 60) = 44.99979509431269
and tan(45.0 degrees) = 0.9999999999999999
and tan(45.0 degrees) = 0.9999999999999999
The 60th root of tan(0.7853981633974483) is 0.9999999990686774
and arctan(0.9999999990686774 ^ 60) = 44.999998399174416
and tan(45.0 degrees) = 0.9999999999999999
and tan(45.0 degrees) = 0.9999999999999999
The 99th root of tan(0.7853981633974483) is 0.9999923706054688
and arctan(0.9999923706054688 ^ 99) = 44.97836188022383
and tan(45.0 degrees) = 0.9999999999999999
and tan(45.0 degrees) = 0.9999999999999999
The 99th root of tan(0.7853981633974483) is 0.9999999403953552
and arctan(0.9999999403953552 ^ 99) = 44.999830952813014
and tan(45.0 degrees) = 0.9999999999999999
and tan(45.0 degrees) = 0.9999999999999999
The 99th root of tan(0.7853981633974483) is 0.9999999990686774
and arctan(0.9999999990686774 ^ 99) = 44.999997358637785
and tan(45.0 degrees) = 0.9999999999999999
and tan(45.0 degrees) = 0.9999999999999999
Charles Truscott for an MIT certificate, page 70 Guttag et. alia

"""