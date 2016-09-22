#!/usr/bin/env python
# coding=utf-8

def split_int(a):
    for i in range(2, 100, 1):
        if a % i == 0:
            return i
    return 0

if __name__ == '__main__':
    a = int(input('input a number, please.'))
    val = split_int(a)
    while val > 1:
        print(val)
        a = a / val
        val = split_int(a)
