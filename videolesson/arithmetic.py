#coding:utf-8

'''
lesson 07-6
filename: arithmetic.py
'''

print('Please input two int:')
a = input('a number:')
b = input('another number:')
a = int(a)
b = int(b)

add_result = a + b
sub_result = a - b
mul_result = a * b
div_result = a / b

print(a, " + ", b, ' = ', add_result)
print(a, " - ", b, ' = ', sub_result)
print(a, " * ", b, ' = ', mul_result)
print(a, " / ", b, ' = ', div_result)