#!/usr/bin/env python
# coding=utf-8

import math

def trail_sqrt(n):
    d = {}
    i = 0
    while n >= 2:
        n = math.sqrt(n)
        i += 1
        d[i] = n
    return d

if __name__ == "__main__":
    n = int(input("please input a interger, and it should more than 2."))
    if n < 2:
        print("sorry, your interger should more than 2.")

    else:
        d = trail_sqrt(n)
        for k,v in d.items():
            print("{0}--->{1}".format(k,v))
