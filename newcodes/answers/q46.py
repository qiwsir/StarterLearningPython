#!/usr/bin/env python
#coding:utf-8

def ahead_one():
    a = [i for i in range(1,11)]
    b = a.pop(0)
    a.append(b)
    return a

if __name__ =="__main__":
    print(ahead_one())
