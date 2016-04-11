#! /usr/bin/env python
# coding:utf-8

def convert(func, seq):
    return [func(i) for i in seq]

if __name__ == "__main__":
    myseq = (111, 3.14, -9.21)
    r = convert(str, myseq)
    print r
