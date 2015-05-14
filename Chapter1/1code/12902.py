#!/usr/bin/env python
# coding=utf-8

from __future__ import division
import random

score = [random.randint(0,100) for i in range(40)]
print score

num = len(score)
sum_score = sum(score)
ave_num = sum_score/num
less_ave = len([i for i in score if i<ave_num])
print "the average score is:%.1f" % ave_num
print "There are %d students less than average."%less_ave

sorted_score = sorted(score, reverse=True)
print sorted_score
