#!/usr/bin/env python
# coding=utf-8

def salary(base_salary, work_days, off_days, add_days):
    salary = base_salary
    if off_days == 0:
        salary = salary + salary*0.2
    elif off_days > 0 and off_days <= 2:
        salary = salary
    elif off_days > 2 and off_days <=7:
        salary = salary * 0.9
    elif off_days > 7 and off_days <= 14:
        salary = salary * 0.5
    else:
        return 0

    if add_days > 0:
        more_salary = add_days * base_salary / work_days
        salary = salary + more_salary
    
    return salary

if __name__ == "__main__":
    base_salary = 5000.00
    work_days = 21
    off_days = 0
    add_days = 5
    s = salary(base_salary, work_days, off_days, add_days)
    print(round(s, 2))
