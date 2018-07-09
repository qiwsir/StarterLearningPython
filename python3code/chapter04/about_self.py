# coding:utf-8

class Person:
    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def breast(self, n):
        self.breast = n

    def color(self, color):
        print("{0} is {1}".format(self.name, color))

    def how(self):
        print("{0} breast is {1}".format(self.name, self.breast))

girl = Person('canglaoshi')
girl.breast(90)

girl.color("white")
girl.how()
