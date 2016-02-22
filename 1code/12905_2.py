#!/usr/bin/env python
# coding=utf-8

n = int(raw_input('Enter an integer >= 0: '))

fact = 1
i = 2
while i<=n:
    fact = fact * i
    i += 1

print str(n) + " factorial is " + str(fact)
