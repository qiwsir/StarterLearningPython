#!/usr/bin/env python
# coding=utf-8

def exact_division(interger):
    if interger % 17 == 0:
        return interger

if __name__ == "__main__":
    nlst = range(100, 1000)
    inter_lst = []
    for i in nlst:
        a = exact_division(i)
        if a:
            inter_lst.append(a)
    print(inter_lst)
