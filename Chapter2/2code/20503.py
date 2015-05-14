#!/usr/bin/env python
# coding=utf-8

"""
find the prime
"""

import math

def is_prime(n):
    """
    a integer is prime or not
    """
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n) + 1)):
        if n % i == 0:
            return False
    return True

if __name__ == "__main__":
    primes = [i for i in range(2,100) if is_prime(i)]
    print primes
