#!/usr/bin/env python
# coding=utf-8

def power_seq(func, seq):
    return [func(i) for i in seq]

def pingfang(x):
    return x ** 2

if __name__ == "__main__":
    num_seq = [111, 3.14, 2.91]
    r = power_seq(pingfang, num_seq)
    print(num_seq)
    print(r)
