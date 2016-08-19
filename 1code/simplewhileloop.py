#!/usr/bin/env python
# coding=utf-8

a = 1 
while a:
    if a%2 == 0:
        break
    else:
        print("{} is odd number".format(a))
        a -= 1 
print("{} is even number".format(a))

