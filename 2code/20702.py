#! /usr/bin/env python
# coding:utf-8

def convert(func, seq):
    return [func(i) for i in seq]

def num(n):
    if n%2 == 0:
        return n**n
    else:
        return n*n
    
if __name__ == "__main__":
    myseq = (3, 4, 5)
    r = convert(num, myseq)
    print r    #Python 3: print(r)
