#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def print_number(number):
    is_begin0 = True
    for i in range(len(number)):
        if is_begin0:
            if number[i] != '0':
                is_begin0 = False
            # number 全为 0 则直接返回
            elif i == len(number) - 1:
                return
        if not is_begin0:
            print(number[i], end='')
    print()
    

def increment(number):
    is_overflow = False
    takeover = 0
    for i in range(len(number) - 1, -1, -1):
        sum = ord(number[i]) - ord('0') + takeover
        if i == len(number) - 1:
            sum += 1
        if sum >= 10:
            if i == 0:
                is_overflow = True
            else:
                sum -= 10
                takeover = 1
                number[i] = chr(ord('0') + sum)
        else:
            number[i] = chr(ord('0') + sum)
            break
    return is_overflow


def by_add(n):
    if n <= 0:
        return
    number = ['0' for i in range(n)]
    while not increment(number):
        print_number(number)
        
        
def print_recursively(number, index):
    if index == len(number) - 1:
        print_number(number)
        return
    for i in range(10):
        number[index + 1] = chr(i + ord('0'))
        print_recursively(number, index + 1)
    
        
def by_recursively(n):
    if n <= 0:
        return
    number = ['0' for i in range(n)]
    for i in range(10):
        number[0] = chr(ord('0') + i)
        print_recursively(number, 0)
    
    
def print_to_max(n):
    #by_add(n)
    by_recursively(n)
        
        
print_to_max(2)

