#!/usr/bin/env python
# coding=utf-8

def find_int(n):
    x = n ** 2
    if x>99 and x<1000:
        last_two = x % 100
        if last_two == n:
            return True
    else:
        return False

if __name__ == "__main__":
    numbers = []
    for i in range(10, 100):
        if find_int(i):
            numbers.append(i)
    print(numbers)

