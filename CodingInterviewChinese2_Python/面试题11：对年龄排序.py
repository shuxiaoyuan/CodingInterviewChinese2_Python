#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def sort_ages(ages):
    if not isinstance(ages, list):
        raise TypeError("ages 不是一个列表！")
    oldest = 99
    age_times = [0 for i in range(oldest+1)]
    for age in ages:
        if age <= 0 or age > oldest:
            raise ValueError("年龄错误！")
        age_times[age] += 1
    index = 0
    for i in range(oldest+1):
        for j in range(age_times[i]):
            ages[index] = i
            index += 1
    
    
ages1 = [20, 25, 35, 19]
ages2 = [20, 120, 50, 6]
ages3 = []
ages4 = None
sort_ages(ages1)
print("ages1:", ages1)
#sort_ages(ages2)
#print("ages2:", ages2)
sort_ages(ages3)
print("ages3:", ages3)
#sort_ages(ages4)
#print("ages4:", ages4)
