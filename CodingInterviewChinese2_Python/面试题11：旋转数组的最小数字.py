#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def min_number(numbers):
    if not isinstance(numbers, list):
        raise TypeError("numbers is not a list!")
    if len(numbers) == 0:
        raise ValueError("numbers is empty!")
    
    index1 = 0
    index2 = len(numbers) - 1
    indexm = index1     # 0 个旋转数字
    
    while numbers[index1] >= numbers[index2]:
        if index2 - index1 == 1:
            indexm = index2
            break
        indexm = (index1 + index2) // 2
        
        # 如果 index1、index2 和 indexm 指向的三个数字相等，
        # 则只能顺序查找
        if numbers[index1] == numbers[index2] and \
                numbers[index1] == numbers[indexm]:
            return sequential_search(numbers, index1, index2)
        
        if numbers[indexm] >= numbers[index1]:
            index1 = indexm
        elif numbers[indexm] <= numbers[index2]:
            index2 = indexm
    return numbers[indexm]
    
    
def sequential_search(numbers, index1, index2):        
    result = numbers[index1]
    for i in range(index1+1, index2+1):
        if result > numbers[i]:
            result = numbers[i]
    return result
    
    
print(min_number([4, 5, 6, 1, 2, 3]))
print(min_number([1, 1, 1, 0, 1]))
#print(min_number([]))
#print(min_number(None))
