#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# 全局变量，用来标记返回值是否合法
g_InvalidInput = False
    
def power_core(base, abs_exponent):
    result = 1.0
    for i in range(abs_exponent):
        result *= base
    return result
    

def equal(a, b):
    if a - b > -0.0000001 and a - b < 0.0000001:
        return True
    return False
    
def power(base, exponent):
    global g_InvalidInput
    g_InvalidInput = False
    if equal(base, 0) and exponent <= 0:
        g_InvalidInput = True
        return 0.0
    abs_exponent = exponent if exponent >= 0 \
                            else -exponent
    result = power_core(base, abs_exponent)
    if exponent < 0:
        result = 1.0 / result
    return result
    
print(power(2, 3), g_InvalidInput)
print(power(2, 0), g_InvalidInput)
print(power(-2, 3), g_InvalidInput)
print(power(2, -3), g_InvalidInput)
print(power(-2, -3), g_InvalidInput)
print(power(0, 1), g_InvalidInput)
print(power(0, 0), g_InvalidInput)
print(power(0, -1), g_InvalidInput)

