#!/usr/bin/env python3
# -*- coding: utf-8 -*-


'''
n+1 个元素，都在 1~n 之内，找出其中一个重复数字
不能修改原数组

'''

def get_duplication(numbers):
    if not isinstance(numbers, list):
        return -1
    start = 1
    end = len(numbers) - 1
    while start <= end:
        middle = (start + end) // 2
        n = get_count(numbers, start, middle)
        if n == -1:
            return -1
        if start == end:
            if n > 1:
                return start
            else:
                break
        if n > (middle - start + 1):
            end = middle
        else:
            start = middle + 1
            
    return -1
    
    
def get_count(numbers, start, end):
    n = 0
    len_numbers = len(numbers)
    for i in range(len_numbers):
        if not isinstance(numbers[i], int):
            return -1
        if numbers[i] < 1 or numbers[i] > len_numbers-1:
            return -1
        if numbers[i] >= start and numbers[i] <= end:
            n += 1
            
    return n
        
    
'''
测试用例

'''  

# 长度为 n+1 的数组里包含一个或多个重复的数字
test_case1 = [2, 3, 5, 4, 3, 2, 6, 7]

# 无效输入测试用例（输入 None；长度为 n+1 的数组中包含 1~n 之外的数字）
test_case2 = None
test_case3 = [2, 3, 5, 4, 3, 0, 6, 7]

print("test_case1:", get_duplication(test_case1))
print("test_case2:", get_duplication(test_case2))
print("test_case3:", get_duplication(test_case3))
