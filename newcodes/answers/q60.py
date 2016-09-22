#!/usr/bin/env python
# coding=utf-8

def gcd(m, n):
    return m if n == 0 else gcd(n, m % n)

def lcm(m, n):
    return m * n // gcd(m, n)

if __name__ == "__main__":
    m = int(input("input m:"))
    n = int(input("input n:"))
    print("GCD", gcd(m, n))
    print("LCM", lcm(m, n))
