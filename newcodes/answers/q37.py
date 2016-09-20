#!/usr/bin/env python
# coding=utf-8

def interest(p,r,n):
    a = p*pow((1+r),n)
    return a

if __name__ == "__main__":
    p = 1000
    r = 0.05
    n = 2
    total = interest(p,r,n)
    print(round(total, 2))
