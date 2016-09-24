#!/usr/bin/env python
# coding=utf-8

class ReverseRange:
    def __init__(self, n):
        self.n = n

    def __next__(self):
        if self.n == 0:
            raise StopIteration
        self.n -= 1
        return self.n

    def __iter__(self):
        return self

for i in ReverseRange(9):
    print(i)
