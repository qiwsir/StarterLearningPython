#!/usr/bin/env python
# coding=utf-8
"""
count the examine scores
"""
from __future__ import division

def average_score(scores):
    """
    count average score.
    """
    score_values = scores.values()
    sum_scores = sum(score_values)
    average = sum_scores/len(score_values)
    return average

def sorted_score(scores):
    """
    count the list for max to min.
    """
    score_lst = [(scores[k],k) for k in scores]
    sort_lst = sorted(score_lst, reverse=True)
    return [(i[1], i[0]) for i in sort_lst]

def max_score(scores):
    """
    the max scroe and the person's name.
    """
    lst = sorted_score(scores)
    max_score = lst[0][1]
    return [(i[0],i[1]) for i in lst if i[1]==max_score]

def min_score(scores):
    """
    the min score and the person's name.
    """
    lst = sorted_score(scores)
    min_score = lst[len(lst)-1][1]
    return [(i[0],i[1]) for i in lst if i[1]==min_score]

if __name__ == "__main__":
    examine_scores = {"google":98, "facebook":99, "baidu":52, "alibaba":80, "yahoo":49, "IBM":70, "android":76, "apple":99, "amazon":99}
    
    ave = average_score(examine_scores)
    print "the average score is: ",ave

    sor = sorted_score(examine_scores)
    print "list of the scores: ",sor

    xueba = max_score(examine_scores)
    print "Xueba is: ",xueba

    xuezha = min_score(examine_scores)
    print "Xuzha is: ",xuezha

