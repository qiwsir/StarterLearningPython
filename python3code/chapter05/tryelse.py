# coding:utf-8
'''
filename: tryelse.py
'''

while 1:
    try:
        x = input("the first number:")
        y = input("the second number:")

        r = float(x)/float(y)
        print(r)
    except Exception as e:
        print(e)
        print("try again.")
    else:
        break
