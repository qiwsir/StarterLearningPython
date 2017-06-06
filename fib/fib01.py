#!/usr/bin/env python
# coding=utf-8

def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)

if __name__=="__main__":
    n = fib(4)
    print(n)
