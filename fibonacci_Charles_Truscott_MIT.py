# -*- coding: utf-8 -*-
"""
Charles Thomas Wallace Truscott
Fibonacci Numbers
MIT 6.001
"""

def fib(x):
    if x == 0 or x == 1:
        return 1
    else:
        print('{} + {}'.format(fib(x - 1), fib(x - 2)))
        return fib(x - 1) + fib(x - 2)

def fib_two(x):
    a = 0
    b = 1
    for n in range(1, x):
        a, b = b, a + b
        print('{} + {}'.format(a, b))
    return a + b
        
q = fib(12)
r = fib_two(12)

print('The same algorithm reaches the same conclusion: {} = {}'.format(q, r) if q == r else 'The same algorithm does not reach the same conclusion')