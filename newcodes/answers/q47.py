#!/usr/bin/env python
#coding:utf-8

def odd(x):return x%2==1
def even(x):return x%2==0

if __name__=="__main__":
    test_lst = [7,9,12,5,4,9,8,3,12,89]
    print(list(filter(even,test_lst)))
    print(list(filter(odd,test_lst)))
