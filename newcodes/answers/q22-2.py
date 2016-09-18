#!/usr/bin/env python
# coding=utf-8

def split_number(num):
    w = len(str(num))
    w_lst = [10**i for i in range(w)]
    num_lst = []
    for n in w_lst:
        a = (num // n) % 10
        num_lst.append(a)
    return num_lst

if __name__ == "__main__":
    n = 2016
    r = split_number(n)
    r.reverse()
    print(r)
