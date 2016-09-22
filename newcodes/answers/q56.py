#!/usr/bin/env python
# coding=utf-8

def flod_paper(n, d):
    h = d*2**n
    return h

if __name__ == "__main__":
    d = 1/200
    n = 30
    h = flod_paper(n, d)
    h_meter = h / 100
    print('After {0} floding, its high is {1}m.'.format(n, h_meter))
