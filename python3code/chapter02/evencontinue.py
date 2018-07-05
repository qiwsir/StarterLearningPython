#coding:utf-8
'''
filename: evencontinue.py
'''

a = 9
while a:
    if a%2 == 0:
        a -=1
        continue    #如果是偶数，就返回循环的开始
    else:
        print("{} is odd number".format(a))    #如果是奇数，就打印出来
        a -=1
