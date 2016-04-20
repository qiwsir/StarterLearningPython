#!/usr/bin/env python
# coding=utf-8

"""
the interator as range()
"""
class MyRange(object):
    def __init__(self, n):
        self.i = 1
        self.n = n

    def __iter__(self):
        return self

    def __next__(self):
        if self.i <= self.n:
            i = self.i
            self.i += 1
            return i
        else:
            raise StopIteration()

if __name__ == "__main__":
    x = MyRange(7)
    print([i for i in x])
    #print list(x)
    #print "x.next()==>", x.next()
    #print "x.next()==>", x.next()
    #print "------for loop--------"
    #for i in x:
    #    print i
