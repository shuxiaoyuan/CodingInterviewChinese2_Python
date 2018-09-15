#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# 递归方式
def by_recursive(n):
    if n <= 0:
        return 0
    if n == 1:
        return 1
    else:
        return by_recursive(n - 1) + by_recursive(n - 2)


# 迭代方式
def by_iterative(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    fibn_2 = 0
    fibn_1 = 1
    fibn = 0
    for i in range(2, n + 1):
        fibn = fibn_1 + fibn_2
        fibn_2 = fibn_1
        fibn_1 = fibn
    return fibn
        
        
def Fibonacci(n):
    #return by_recursive(n)
    return by_iterative(n)
    
    
print(Fibonacci(5))

    