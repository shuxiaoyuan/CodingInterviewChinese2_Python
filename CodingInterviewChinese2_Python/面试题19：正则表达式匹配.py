#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def match(str, pattern):
    if str == None or pattern == None:
        return False
    return matchCore(str, 0, pattern, 0)
    
def matchCore(str, str_pos, pattern, pat_pos):
    if str_pos >= len(str) and pat_pos >= len(pattern):
        return True
    if str_pos >= len(str) or pat_pos >= len(pattern):
        return False
    if pat_pos+1 < len(pattern) and pattern[pat_pos+1] == '*':
        if pattern[pat_pos] == str[str_pos] or pattern[pat_pos] == '.':
            return matchCore(str, str_pos+1, pattern, pat_pos+2) or \
                   matchCore(str, str_pos+1, pattern, pat_pos) or \
                   matchCore(str, str_pos, pattern, pat_pos+2)
        else:
            return matchCore(str, str_pos, pattern, pat_pos+2)
    if str[str_pos] == pattern[pat_pos] or \
            (pattern[pat_pos] == '.' and str_pos < len(str)):
        return matchCore(str, str_pos+1, pattern, pat_pos+1)
        

# str = "aaa"
str = None
# pattern = "a.a"
# pattern = "ab*ac*a"
# pattern = "aa.a"
# pattern = "ab*a"
# pattern = ""
pattern = None

print(match(str, pattern))
