# coding:utf-8
'''
filename: tryexceptccb.py
'''

while 1:
    print("this is a division program.")
    c = input("input 'c' continue, otherwise logout:")
    if c == 'c':
        a = input("first number:")
        b = input("second number:")
        try:
            print(float(a)/float(b))
            print("*************************")
        except ZeroDivisionError:
            print("The second number can't be zero!")
            print("*************************")
    else:
        break
