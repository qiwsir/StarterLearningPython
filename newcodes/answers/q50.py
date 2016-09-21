#!/usr/bin/env python
# coding=utf-8
import math

def sorted_sides(sides_lst):
    sides = sorted(sides_lst)
    x, y, z = sides[0], sides[1], sides[2]
    return float(x), float(y), float(z)

def is_triangle(sides_lst):
    x, y, z = sorted_sides(sides_lst)
    if x >=0:
        if (x + y > z):
            return True
        else:
            return False
    else:
        return False

def side_triangle(sides_lst):
    x, y, z = sorted_sides(sides_lst)
    if x == y or y == z:
        return "isosceles"
    elif x == z:
        return "equilateral"
    else:
        return "scalene"

def angle_triangle(sides_lst):
    x, y, z = sorted_sides(sides_lst)
    difference = z**2 - (x**2 + y**2)
    if difference == 0:
        return "right"
    elif difference > 0:
        return "obtuse"
    else:
        return "acute"

def area_triangle(sides_lst):
    x, y, z = sorted_sides(sides_lst)
    s = (x + y + z)/2
    a = math.sqrt(s*(s-x)*(s-y)*(s-z))
    return round(a, 3)

if __name__ == "__main__":
    triangle_sides = input("please input three sides of triangle, and split them by space:")
    sides_lst = triangle_sides.split()
    if is_triangle(sides_lst):
        result_side = side_triangle(sides_lst)
        result_angle = angle_triangle(sides_lst)
        area = area_triangle(sides_lst)
        print("The triangle is {0} and {1}. Its area is {2}".format(result_side, result_angle, area))
    else:
        print("Sorry, the sides cannot be the side of triangle.")
