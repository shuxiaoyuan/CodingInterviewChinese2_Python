#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# 给出一个正整数，计算其各个位之和
def get_digit_sum(num):
    sum = 0
    while num > 0:
        sum += num % 10
        num //= 10
    return sum


def check(threshold, rows, cols, row, col, visited):
    if row >= 0 and row < rows and col >= 0 and col < cols \
            and (get_digit_sum(row) + get_digit_sum(col) <= threshold) \
                and (not visited[row * cols + col]):
        return True
    return False
    
    
def moving_count_core(threshold, rows, cols, row, col, visited):
    count = 0
    if check(threshold, rows, cols, row, col, visited):
        visited[row * cols + col] = True
        count = 1 + moving_count_core(threshold, rows, cols, 
                                        row-1, col, visited) \
                  + moving_count_core(threshold, rows, cols,
                                        row, col-1, visited) \
                  + moving_count_core(threshold, rows, cols,
                                        row+1, col, visited) \
                  + moving_count_core(threshold, rows, cols,
                                        row, col+1, visited)
    return count


def moving_count(threshold, rows, cols):
    if threshold < 0 or rows <= 0 or cols <= 0:
        return 0
    
    visited = [False for i in range(rows * cols)]
    count = moving_count_core(threshold, rows, cols, 0, 0, visited)
    
    return count


print(moving_count(18, 10, 10))
