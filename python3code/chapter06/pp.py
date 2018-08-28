# coding:utf-8
'''
filename: pp.py
'''
__all__ = ['_private_variable', 'public_teacher']

public_variable = "Hello, I am a public variable."
_private_variable = "Hi, I am a private variable."

def public_teacher():
    print("I am a public teacher, I am from JP.")

def _private_teacher():
    print("I am a private teacher, I am from CN.")
