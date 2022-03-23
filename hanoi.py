# -*- coding: utf-8 -*-
"""
Created on Wed Mar 23 17:36:25 2022

@author: user
"""

def print_move(fr, to):
    print('Moving {} to {}'.format(fr, to))

def Towers(n, fr, to, spare):
    if n == 1:
        print_move(fr, to)
    else:
        Towers(n - 1, fr, spare, to)
        Towers(1, fr, to, spare)
        Towers(n - 1, spare, to, fr)
print(Towers(4, 'P1', 'P2', 'P3'))
