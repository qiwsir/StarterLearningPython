# coding:utf-8
'''
filename: fibsiterator.py
'''

class Fibs:
    def __init__(self, max):
        self.max = max
        self.a = 0
        self.b = 1

    def __iter__(self):
        return self

    def __next__(self):       
        fib = self.a
        if fib > self.max:
            raise StopIteration
        self.a, self.b = self.b, self.a + self.b
        return fib

fibs = Fibs(10000)
lst = [fibs.__next__() for i in range(10)]
print(lst)