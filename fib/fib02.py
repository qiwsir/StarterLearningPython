#!/usr/bin/env python
# utf-8

from math import sqrt

def fib(n):
    return ((1+sqrt(5))**n - (1-sqrt(5))**n)/(2**n*sqrt(5))

if __name__=="__main__":
    f = fib(4)
    print(f)
