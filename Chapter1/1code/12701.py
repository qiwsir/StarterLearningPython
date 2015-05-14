#!/usr/bin/env python
# coding=utf-8

f = open("you.md")

while True:
    line = f.readline()
    if not line:
        break
    print line ,

f.close()
