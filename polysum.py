# -*- coding: utf-8 -*-
"""
Created on Wed Mar 23 21:43:44 2022

@author: user
"""

import math
def polysum(n, s):
    area = (0.25 * n * (s * s))/(math.tan(math.pi/n))
    perimeter = s * n
    summation = area + (perimeter * perimeter)
    return round(summation, 4)