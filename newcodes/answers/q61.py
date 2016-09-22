#!/usr/bin/env python
# coding=utf-8

class SchoolKid:
    def __init__(self, name, years):
        self.name = name
        self.years = years

    def get_name(self):
        return self.name

    def get_years(self):
        return self.years

    def change_name(self, new_name):
        self.name = new_name
        return self.name

    def change_years(self, new_years):
        self.years = new_years
        return self.years


class ExaggeratingKid(SchoolKid):
    def get_years(self):
        return self.years + 2


if __name__ == "__main__":
    tom = SchoolKid("Tom", 12)
    print(tom.get_name())
    print(tom.get_years())
    tom.change_years(28)
    print(tom.get_years())

    john = ExaggeratingKid("John", 13)
    print(john.get_name())
    print(john.get_years())
