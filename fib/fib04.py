#!/usr/bin/env python
#utf-8

def fib(n):
    a, b = 0, 1
    while n > 0:
        a, b = b, a + b
        n -= 1
    return a

if __name__ == "__main__":
    print(fib(4))
