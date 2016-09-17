#!/usr/bin/env python
# coding=utf-8

def f_and_c(value):
    unite = value[-1]
    v = int(value[:-1])
    try:
        if unite == "F":
            c = (5*v - 32)/9
            return round(c, 2)
        elif unite == "C":
            f = 9*v/5 + 32
            return round(f, 2)
        else:
            return False
    except:
        return False

if __name__ == "__main__":
    while True:
        print("you should input the tempreture like: 23C or 65F, NOTE: F and C is upper.")
        t = input("input the tempreture:('q'-exit)")
        if t == "q":
            break
        else:
            result = f_and_c(t)
            if result:
                print("the tempreture is {}".format(result))
            else:
                print("your value is not right")
