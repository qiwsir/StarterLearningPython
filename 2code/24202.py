#!/usr/bin/env python
# coding:utf-8

def parabola(a, b, c):
    def para(x):
        return a*x**2 + b*x + c
    return para

p = parabola(2, 3, 4)
print p(5)
