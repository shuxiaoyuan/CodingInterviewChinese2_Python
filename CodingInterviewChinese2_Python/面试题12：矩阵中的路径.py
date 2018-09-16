#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def has_path(matrix, rows, cols, str):

    if rows <= 0 or cols <= 0 or len(matrix) == 0 \
            or len(str) == 0:
        return False
    
    visited = [False for i in range(rows * cols)]
    for i in range(rows):
        for j in range(cols):
            if has_path_core(matrix, rows, cols, i, j,
                                str, 0, visited):
                return True
    return False
    
def has_path_core(matrix, rows, cols, row, col,
                    str, len_path, visited):
    if len_path == len(str):
        return True
    has_path = False
    if row >= 0 and row < rows and col >= 0 and col < cols \
            and matrix[row * cols + col] == str[len_path] \
            and (not visited[row * cols + col]):

        len_path += 1
        visited[row * cols + col] = True
        
        has_path = has_path_core(matrix, rows, cols, row, col-1,
                                    str, len_path, visited) or \
                   has_path_core(matrix, rows, cols, row-1, col,
                                    str, len_path, visited) or \
                   has_path_core(matrix, rows, cols, row, col+1,
                                    str, len_path, visited) or \
                   has_path_core(matrix, rows, cols, row+1, col,
                                    str, len_path, visited)
        if not has_path:
            len_path -= 1
            visited[row * cols + col] = False
    return has_path
    
    
matrix = [
    'a', 'b', 't', 'g',
    'c', 'f', 'c', 's',
    'j', 'd', 'e', 'h'
]
print(has_path(matrix, 3, 4, 'bfce'))
