#!/usr/bin/env python
# coding=utf-8

def weight(g):
    def cal_mg(m):
        return m * g
    return cal_mg

w = weight(10)
mg = w(10)
print(mg)

g0 = 9.78046 #赤道海平面上的重力加速度
w0 = weight(g0)
mg0 = w0(10)
print(mg0)
