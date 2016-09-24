#!/usr/bin/env python
# coding=utf-8

from datetime import date

class DateDiff:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        
    def diff_days(self):
        return (self.end - self.start).days

    def diff_months(self):
        delta_years = self.end.year - self.start.year
        delta_months = delta_years * 12 + (self.end.month - self.start.month)
        return delta_months

    def diff_years(self):
        delta_years = self.end.year - self.start.year
        return delta_years

if __name__ == "__main__":
    start = date(2015,1,1)
    end = date(2016,9,3)
    print(start, "-->", end)
    di = DateDiff(start, end)
    print("the days is:{0}".format(di.diff_days()))
    print("the months is:{0}".format(di.diff_months()))
    print("the years is:{0}".format(di.diff_years()))
