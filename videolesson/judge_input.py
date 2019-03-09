#coding:utf-8
'''
    lesson 19-03
    filename: judge_input.py
'''
input_char = input("Input something: ")
if input_char.isdigit(): 
    result = int(input_char) * 10
    print("You input {0}. Output is {1}".format(input_char, result))
elif input_char.isalpha(): 
    print(input_char + "@python")
else: 
    print(input_char)