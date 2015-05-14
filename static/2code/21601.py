#!/usr/bin/env python
# coding=utf-8

"""
try... except
"""

while 1:
    print "this is a division program."
    c = raw_input("input 'c' continue, otherwise logout:")
    if c == 'c':
        a = raw_input("first number:")
        b = raw_input("second number:")
        try:
            print float(a)/float(b)
            print "*************************"
        except ZeroDivisionError:
            print "The second number can't be zero!"
            print "*************************"
    else:
        break
    
