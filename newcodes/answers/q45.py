#! /usr/bin/env python
#coding:utf-8

from __future__ import division
import random


def score(score_list, course_list, student_num):
    course_num = len(course_list)
    every_score = [[score_list[j][i] for j in range(course_num)] for i in range(student_num)]
    every_total = [sum(every_score[i]) for i in range(student_num)]
    ave_course = [sum(score_list[i])/len(score_list[i]) for i in range(len(score_list))]
    return (every_score, every_total, ave_course)

if __name__=="__main__":

    course_list = ["C++","Java","Servlet","JSP","EJB"]
    student_num = 20

    score_list = [[random.randint(0,100) for i in range(student_num)] for j in range(len(course_list))]
    for i in range(len(course_list)):
        print("score of every one in {0}:".format(course_list[i]))
        print(score_list[i])

    every_score, every_total, ave_one_course = score(score_list, course_list, student_num)
    print("\n")
    print("NEXT IS EVERY ONE SCORE IN EVERY COURSE:")
    for name in course_list:
        print(name, end=",")
    print("\t")
    print(every_score)
    print("\n")
    print("every one all score:\t{0}".format(every_total))
    print("every course of average score:\t{0}".format(ave_one_course))
