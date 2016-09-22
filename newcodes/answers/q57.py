#!/usr/bin/env python
# coding=utf-8

def palindrome(word):
    word_lst = [ i for i in word ]
    word_lst.reverse()
    new_word = "".join(word_lst)
    if word == new_word:
        return True
    else:
        return False

if __name__ == "__main__":
    while True:
        word = input("input a word:('q'-exit)")
        if word == "q":
            break
        else:
            if palindrome(word):
                print("{0} is a palindrome".format(word))
            else:
                print("The word is not palindrome")

