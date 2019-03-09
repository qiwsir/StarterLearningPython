#coding: utf-8
'''
    calculate the square root by Newton's method.
    lesson 22-1
    filename: newton.py
'''
value = 23 #f(x) = x^2 - 23 
epsilon = 0.001
result = value / 2
while abs(result*result - value) >= epsilon:
    result = result - ((result*result - value) / (2 * result))
print("The square root of {0} is about {1}".format(value, result))