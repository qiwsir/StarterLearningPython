#!/usr/bin/env python
# coding=utf-8

d = {}
with open("youraisemeup.txt") as f:
    for line in f:
        if bool(line):
            line_lst = line.split()
            for word in line_lst:
                word = word.lower()
                if word in d:
                    d[word] += 1
                else:
                    d[word] = 1
print(d)
