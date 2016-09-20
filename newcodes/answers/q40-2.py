#!/usr/bin/env python
# coding=utf-8

from functools import reduce

def addx(x):
    numbers = range((x+1))
    r = reduce(lambda x,y: x+y, numbers)
    return r

if __name__ == "__main__":
    x = int(input("please input a interger:"))
    print("0+1+2...+{0}".format(x))
    print(addx(x))
