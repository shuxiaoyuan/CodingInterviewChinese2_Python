#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Solution:
    # s 源字符串
    def replaceSpace(self, s):
        # write code here
        if not isinstance(s, str):
            return -1
        if not s:
            return -1
        
        return s.replace(" ", "%20")
    
'''
测试样例

'''

test_case1 = " we are happy"    # 开头有空格
test_case2 = "we are happy "    # 末尾有空格
test_case3 = "we  are  happy"   # 有连续空格
test_case4 = "wearehappy"       # 没有空格
test_case5 = " "                # 只有一个空格
test_case6 = ""                 # 空串
test_case7 = None               # 输入非字符串

print("test_case1:", Solution().replaceSpace(test_case1))
print("test_case2:", Solution().replaceSpace(test_case2))
print("test_case3:", Solution().replaceSpace(test_case3))
print("test_case4:", Solution().replaceSpace(test_case4))
print("test_case5:", Solution().replaceSpace(test_case5))
print("test_case6:", Solution().replaceSpace(test_case6))
print("test_case7:", Solution().replaceSpace(test_case7))
