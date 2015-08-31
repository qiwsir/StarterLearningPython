#!/usr/bin/env python
# coding=utf-8

class ContextManagerOpenDemo(object):
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode

    def __enter__(self):
        print "Starting the Manager."
        self.open_file = open(self.filename, self.mode)
        return self.open_file

    #def __exit__(self, *others):
    #    self.open_file.close()
    #    print "Exiting the Manager."
    
    def __exit__(self, exc_type, exc_value, exc_traceback):
        #return SyntaxError != exc_type
        return False

with ContextManagerOpenDemo("23501.txt", 'r') as reader:
    print "In the Manager."
    for line in reader:
        print lines

