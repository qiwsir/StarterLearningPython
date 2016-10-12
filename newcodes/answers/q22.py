#!/usr/bin/env python
# coding=utf-8

def add(x, y):
    return x + y

if __name__ == "__main__":
    while True:
        print("please input two number and then the program will add them.'q'-exit.")
        v_1 = input("input a number:")
        if v_1 == "q":
            break
        else:
            v_2 = input("input another number:")
            result = add(v_1, v_2)
            print("{0} + {1} = {2}".format(v_1, v_2, result))
