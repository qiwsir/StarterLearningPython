# coding:utf-8
"""
the better Fibonacci
filename: fibsbetter.py
"""

m = {0:0, 1:1}    

def fib(n):
    if not n in m:    
        m [n] = fib(n-1) + fib(n-2)
    return m[n]

f = fib(10)
print(f)
