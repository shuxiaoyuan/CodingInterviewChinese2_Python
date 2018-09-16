#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def by_shift(n):
    count = 0
    flag = 1
    for i in range(32):
        # Python & 运算符比 != 优先级高
        if n & flag != 0:
            count += 1
        flag = flag << 1

    return count


def by_n_1(n):
    count = 0
    # Python 负数也支持大数，符号位用此种方式无法消除
    # 因此需要加上 n >= -2147483648
    while n != 0 and n >= -2147483648:
        count += 1
        n = n & (n - 1)
    return count
    
    
def nums_of1(n):
    #return by_shift(n)
    return by_n_1(n)
    
print(nums_of1(-1))

