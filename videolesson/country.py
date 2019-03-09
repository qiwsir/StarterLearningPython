#coding:utf-8

'''
lesson 15-3
filename: country.py
'''

country = {"CHINA": "BEIJING", 'CANADA': "OTTAWA", 'GREECE': 'ATHENS', 'ITALY': 'ROME'}

name = input("input the name of country:")
capital = country[name]
print(name, "-->", capital)