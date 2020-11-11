# coding:utf-8
'''
filename: forelse.py
'''

from math import sqrt
"""
math is module/ library under python which  can perform simple math operations.
"""

for n in range(99, 1, -1): # we are iterating the for loop starting from 99 with a diffrence of 1 and ends at 10 (including).
    root = sqrt(n) # this will calculate the square root of n 
    if root == int(root):# we are checking data type
        print(n)
        break # if condition not satisfy it will move out of loop

else:
    print("Nothing.") # when above execution  condition fails.
