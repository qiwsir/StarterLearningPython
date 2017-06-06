#!/usr/bin/env python
# utf-8

def fib(n):
    f = [0, 1]
    for i in range(n-2):
        f.append(f[-2] + f[-1])
    return f

if __name__ == "__main__":
    lst = fib(4)
    print(lst)
