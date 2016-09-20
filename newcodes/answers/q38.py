#!/usr/bin/env python
# coding=utf-8

import re

def validate_email(email):
    if len(email) > 4:
        if re.match("^[a-zA-Z0-9._%-]+@[a-zA-Z0-9._%-]+\.[a-zA-Z]{2,6}$", email) != None:
            return True
    else:
        return False

if __name__ == "__main__":
    while True:
        e = input("Input your email('q'-exit):")
        if e == "q":
            print("Bye!")
            break
        else:
            r = validate_email(e)
            if r:
                print("The email is right.")
            else:
                print("sorry, the email is not right.")
