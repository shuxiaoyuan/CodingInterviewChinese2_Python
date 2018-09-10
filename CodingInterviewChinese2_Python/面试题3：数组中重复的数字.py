#!/usr/bin/env python3
# -*- coding: utf-8 -*-


'''
 n 个元素，都在 0~n-1 之间，找出其中一个重复数字
 
''' 

# 哈希表方式，时间 O(n) 空间 O(n)，无需修改原数组
def by_hash(numbers):
    tmp = [False for i in range(len(numbers))]
    for n in numbers:
        if tmp[n] == True:
            return n
        else:
            tmp[n] = True
    return -1
    
    
# 对原数组进行排序然后顺序查找，时间 O(nlogn) 空间 O(1)
def by_sort(numbers):
    numbers.sort()
    for i in range(len(numbers)-1):
        if numbers[i] == numbers[i+1]:
            return numbers[i]
    return -1
    

# 交换原数组中的元素，时间 O(n) 空间 O(1)
def by_swap(numbers):
    for i in range(len(numbers)):
        while numbers[i] != i:
            if numbers[i] == numbers[numbers[i]]:
                return numbers[i]
            tmp = numbers[i]
            numbers[i] = numbers[tmp]
            numbers[tmp] = tmp
    return -1
                    

def get_duplication(numbers):
    # numbers 不为 list
    if not isinstance(numbers, list):
        return -1
    len_numbers = len(numbers)
    for i in range(len_numbers):
        # numbers[i] 不为 int
        if not isinstance(numbers[i], int):
            return -1
        # numbers[i] 范围不合法
        if numbers[i] < 0 or numbers[i] > len_numbers-1:
            return -1
            
    return by_swap(numbers)

    
'''
测试用例

'''  

# 长度为 n 的数组里包含一个或多个重复的数字
test_case1 = [2, 3, 1, 0, 2, 5, 3]

# 数组中不含重复的数字
test_case2 = [2, 3, 1, 0, 5, 4]

# 无效输入测试用例（输入 None；长度为 n 的数组中包含 0~n-1 之外的数字）
test_case3 = None
test_case4 = [2, 3, 1, 0, 2, 6]

print("test_case1:", get_duplication(test_case1))
print("test_case2:", get_duplication(test_case2))
print("test_case3:", get_duplication(test_case3))
print("test_case4:", get_duplication(test_case4))

