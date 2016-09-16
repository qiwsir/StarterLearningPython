#!/usr/bin/env python
# coding=utf-8

import calendar

years = range(1840, 2016)
leap_years = []
for year in years:
    if calendar.isleap(year):
        leap_years.append(year)

print(leap_years)
