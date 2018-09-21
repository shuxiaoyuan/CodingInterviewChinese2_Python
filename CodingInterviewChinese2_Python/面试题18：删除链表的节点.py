#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


def delete_node(head, node):
    if not (isinstance(head, Node) and isinstance(node, Node)):
        return
    # 链表有多个节点，且要删除的节点不是尾节点
    if node.next != None:
        next = node.next
        node.val = next.val
        node.next = next.next
    # 链表只有一个节点
    elif node == head:
        head = None
    # 链表有多个节点，删除尾节点
    else:
        tmp = head
        while tmp.next != node:
            tmp = tmp.next
        tmp.next = None
    return head
    
    
def show(head):
    while head != None:
        print(head.val, end=' ')
        head = head.next
    print()
    
    
head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head = delete_node(head, head.next)
show(head)

