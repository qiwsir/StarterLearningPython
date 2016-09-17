#!/usr/bin/env python
# coding=utf-8

the_num = input("Please enter a number to check:")
the_num = int(the_num)

divisor = 1
sum_of_divisors = 0
while divisor < the_num:
    if the_num % divisor == 0:
        sum_of_divisors = sum_of_divisors + divisor
    divisor = divisor + 1

if the_num == sum_of_divisors:
    print(the_num, "is perfect")
else:
    print(the_num, "is not perfect")
