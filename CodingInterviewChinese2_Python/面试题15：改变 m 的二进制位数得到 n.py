#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def bits_mton(m, n):
    tmp = m ^ n
    count = 0
    while tmp != 0 and tmp >= -2147483648:
        count += 1
        tmp = tmp & (tmp - 1)
    
    return count
        
        
print(bits_mton(10, 13))
print(bits_mton(0, -1))