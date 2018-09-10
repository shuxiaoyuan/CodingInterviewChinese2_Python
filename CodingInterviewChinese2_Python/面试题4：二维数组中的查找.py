#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Solution:
    # array 二维列表
    def Find(self, target, array):
        # write code here
        if not isinstance(target, int):
            return False
        start_row = 0
        start_column = 0
        end_row = len(array) - 1
        end_column = len(array[0]) - 1
        while start_row <= end_row and end_column >= start_column:
            if array[start_row][end_column] < target:
                start_row += 1
            elif array[start_row][end_column] > target:
                end_column -= 1
            elif array[start_row][end_column] == target:
                return True
        return False
        
        
'''
测试样例

'''

arr = [
    [1, 2, 8, 9],
    [2, 4, 9, 12],
    [4, 7, 10, 13],
]

test_case1 = 1      # 最小值
test_case2 = 13     # 最大值
test_case3 = 7      # 介于最大值最小值之间
test_case4 = 0      # 小于最小值
test_case5 = 15     # 大于最大值
test_case6 = 11     # 介于最大值最小值之间，但没有这个数字
test_case7 = None   # 输入为 None（非整数）

print("test_case1:", Solution().Find(test_case1, arr))
print("test_case2:", Solution().Find(test_case2, arr))
print("test_case3:", Solution().Find(test_case3, arr))
print("test_case4:", Solution().Find(test_case4, arr))
print("test_case5:", Solution().Find(test_case5, arr))
print("test_case6:", Solution().Find(test_case6, arr))
print("test_case7:", Solution().Find(test_case7, arr))


