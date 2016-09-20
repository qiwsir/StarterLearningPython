#! /usr/bin/env python
# encoding:utf-8

def divided(m,r,out):
    if(r==0):
        return True
    tm=r
    while tm>0:
        if(tm<=m):
            out.append(tm)
            if(divided(tm, r-tm, out)):
                print(out)
            out.pop()
        tm = tm-1
    return False


n=6
output=[]
divided(n-1, n, output)
