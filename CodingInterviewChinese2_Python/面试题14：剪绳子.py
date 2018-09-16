#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def by_dp(length):
    if length < 2:
        return 0
    if length == 2:
        return 1
    if length == 3:
        return 2
        
    products = [0 for i in range(length + 1)]
    products[0] = 0
    products[1] = 1
    products[2] = 2
    products[3] = 3
    
    max = 0
    
    for i in range(4, length + 1):
        max = 0
        for j in range(1, i // 2 + 1):
            product = products[j] * products[i - j]
            if max < product:
                max = product
        products[i] = max
    
    return products[length]
    
    
def by_greedy(length):
    if length < 2:
        return 0
    if length == 2:
        return 1
    if length == 3:
        return 2

    # 尽可能多地剪去长度为 3 的绳子段
    times_of3 = length // 3
    
    # 当绳子最后剩下的长度为 4 的时候，不能再剪去长度为 3 的绳子段
    # 此时更好的方法是把绳子剪成长度为 2 的两段，因为 2 * 2 > 3 * 1
    if length - times_of3 * 3 == 1:
        times_of3 -= 1
    
    times_of2 = (length - times_of3 * 3) // 2
    
    return (3**times_of3) * (2**times_of2)
    
    
def max_product(length):
    #return by_dp(length)
    return by_greedy(length)
    
    
print(max_product(8))
