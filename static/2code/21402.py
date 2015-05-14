#!/usr/bin/env python
# coding=utf-8
"""
compute Fibonacci by iterator
"""
__metaclass__ = type

class Fibs:
    def __init__(self, max):
        self.max = max
        self.a = 0
        self.b = 1

    def __iter__(self):
        return self

    def next(self):
        fib = self.a
        if fib > self.max:
            raise StopIteration
        self.a, self.b = self.b, self.a + self.b
        return fib

if __name__ == "__main__":
    fibs = Fibs(5)
    print list(fibs)


