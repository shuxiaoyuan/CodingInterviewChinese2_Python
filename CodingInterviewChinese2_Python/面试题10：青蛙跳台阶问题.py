#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# 只用了迭代方式
def jump_floor(n):
    if n <= 0:
        return 0
    if n == 1:
        return 1
    if n == 2:
        return 2
    fibn = 0
    fibn_1 = 2
    fibn_2 = 1
    for i in range(3, n+1):
        fibn = fibn_1 + fibn_2
        fibn_2 = fibn_1
        fibn_1 = fibn
    return fibn    
    
print(jump_floor(5))