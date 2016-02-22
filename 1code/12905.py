#!/usr/bin/env python
# coding=utf-8

n = int(raw_input("Enter an interger >=0: "))

fact = 1

for i in range(2, n + 1):
    fact = fact * i

print str(n) + " factorial is " + str(fact)
