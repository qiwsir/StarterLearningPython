#!/usr/bin/env python
# coding=utf-8

"""
the better Fibonacci
"""

meno = {0:0, 1:1}

def fib(n):
    if not n in meno:
        meno[n] = fib(n-1) + fib(n-2)
    return meno[n]

if __name__ == "__main__":
    f = fib(10)
    print f
