# coding:utf-8
'''
filename: nameage.py
'''

name = input("What is your name?")
age = input("How old are you?")

print("Your name is: ",  name)
print("You are " + age + " years old.")

after_ten = int(age) + 10
print("You will be " + str(after_ten) + " years old after ten years.")