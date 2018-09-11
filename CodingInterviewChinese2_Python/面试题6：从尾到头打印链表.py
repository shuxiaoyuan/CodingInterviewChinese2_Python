#!/usr/bin/env python3
# -*- coding: utf-8 -*-


'''
Python 的高级面向对象编程我不太熟悉
这里把对链表的各种操作都写在了外部
导致只能通过返回值的方式给外部 list 赋值，
以改变外部 list 引用的值

'''

# 链表节点类
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

        
# 往链表尾部添加新的节点
def add_to_tail(list, value):
    if list == None:
        return Node(value)
    if not isinstance(list, Node):
        raise TypeError("argument type is not a 'Node'")
    head = list
    while list.next != None:
        list = list.next
    list.next = Node(value)
    return head
    
    
# 删除第一个值为 value 的节点
def remove_node(list, value):
    if not isinstance(list, Node):
        raise TypeError("argument type is not a 'Node'")
    if list.value == value:
        return list.next
    head = list
    while list.next != None and list.next.value != value:
        list = list.next
    if list.next.value == value:
        list.next =  list.next.next
        return head
    if list.next == None:
        raise ValueError("can't find the value:", value)
    
    
# 顺序打印链表元素    
def print_list(list):
    if not isinstance(list, Node):
        raise TypeError("argument type is not a 'Node'")
    while list != None:
        print(list.value, end=" ")
        list = list.next
    print()
        

# 从尾部到头打印链表元素
def print_list_reversingly(list):
    if not isinstance(list, Node):
        raise TypeError("argument type is not a 'Node'")
    
    #by_iteratively(list)
    by_recursively(list)
    
    
# 用栈辅助结构
def by_iteratively(list):
    stack = []
    while list != None:
        stack.append(list.value)
        list = list.next
    while stack:
        print(stack.pop(), end=" ")
    print()
    

# 递归方式
def by_recursively(list):
    if list.next != None:
        by_recursively(list.next)
    print(list.value, end=" ")
    
    
'''
测试样例

'''

test_list = Node(0)
test_list = add_to_tail(test_list, 2)
test_list = add_to_tail(test_list, 5)
print_list(test_list)
print_list_reversingly(test_list)