#!/usr/bin/env python
# coding=utf-8

def average(lst):
    total = 0
    for i in lst:
        total = total + i
    ave = total / len(lst)
    return ave

def max_student(dct):
    max = 0
    for k,v in dct.items():
        if v > max:
            max = v
            name = k
    return (name, max)

if __name__ == "__main__":
    d = {}
    score_lst = []
    while True:
        name = input("input name:('q'-exit)")
        if name == "q":
            break
        else:
            score = int(input("input score:"))
            d[name] = score
            score_lst.append(score)
    
    ave = average(score_lst)
    print("the average scroe is:{}".format(round(ave, 2)))
    name, score = max_student(d)
    print("xueba is {0}, his/her score is {1}".format(name, score))


