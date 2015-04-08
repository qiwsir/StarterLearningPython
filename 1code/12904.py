#!/usr/bin/env python
# coding=utf-8

a, b = 0, 1

for i in range(4):
    a, b = b, a+b

print a
