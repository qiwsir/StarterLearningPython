#coding:utf-8
'''
    path: ./mypackage/A/abasic.py
    filename: abasic.py
'''

from . import apython    
from ..B import brust    

basic = "BASIC-" + apython.python() + "-" + brust.rust

#it will be Error!
if __name__ == "__main__":
    print(basic) 
