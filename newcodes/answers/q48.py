#! /usr/bin/env python
#coding:utf-8

def char_to_number(by_list, char):    #根据排序依据字母顺序，给另外一个字母编号
    try:
        return by_list.index(char)
    except:
        return 1000

def sort_by_list(by_list, input_list):
    result={}
    for word in input_list:
        number_list = [char_to_number(by_list,word[i]) for i in range(len(word))]
        result[word] = number_list
    return [v[0] for v in sorted(result.items(), key=lambda x:x[1])]

if __name__=="__main__":
    word = ["bed","dog","dear","eye"]
    by_string = ['d','g','e','c','f','b','o','a']
    print("the word list is:")
    print(word)
    print("\nwill sorted by:")
    print(by_string)
    print("\nthe result is:")
    print(sort_by_list(by_string,word))
