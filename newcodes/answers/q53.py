#!/usr/bin/env python
# coding=utf-8

import math
import cmath

def solve_be(a, b, c):
    delta = b**2 - 4*a*c
    if delta == 0:
        #x = fractions.Fraction(-b, 2*a)
        x = -b / (2*a)
        return x
    elif delta > 0:
        sqrt_delata = math.sqrt(delta)
    else:
        sqrt_delata = cmath.sqrt(delta)
    #x1 = fractions.Fraction((-b + sqrt_delata), 2*a)
    #x2 = fractions.Fraction((-b - sqrt_delata), 2*a)
    x1 = (-b + sqrt_delata) / (2*a)
    x2 = (-b - sqrt_delata) / (2*a)
    return (x1, x2)

if __name__ == "__main__":
    print("The binary linear equation is x^2 + 2^x + 3 = 0")
    r = solve_be(1, 2, 3)
    if len(r) == 1:
        print("The equation only has one root. It is:")
        print(r)
    else:
        print("The equation have two root. They are:")
        print(r)
