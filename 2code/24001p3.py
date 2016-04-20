#!/usr/bin/env python
# coding=utf-8

class Rectangle(object):

    def __init__(self):
        self.width = 0
        self.length = 0

    def setSize(self, size):
        self.width, self.length = size
    def getSize(self):
        return self.width, self.length

if __name__ == "__main__":
    r = Rectangle()
    r.width = 3
    r.length = 4
    print(r.getSize())
    r.setSize( (30, 40) )
    print(r.width)
    print(r.length)
