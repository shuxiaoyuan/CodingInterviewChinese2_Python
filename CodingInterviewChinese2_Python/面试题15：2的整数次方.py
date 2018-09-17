#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def is_2pow(num):
    return True if num & (num - 1) == 0 and \
                    num != 0 else False


print(is_2pow(-2147483648))
print(is_2pow(-0))
print(is_2pow(0))
print(is_2pow(1))
print(is_2pow(2))
print(is_2pow(2147483648))