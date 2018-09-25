#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
    
    
def delete_duplication(head):
    if not isinstance(head, Node):
        return None
    pre = None
    current = head
    while current != None:
        next = current.next
        if next == None or next.val != current.val:
            pre = current
        else:
            while next != None and next.val == current.val:
                next = next.next
            if pre == None:
                head = next
            else:
                pre.next = next
        current = next

    return head
    

def insert(vals):
    head = current = Node(vals[0])
    for i in range(1, len(vals)):
        current.next = Node(vals[i])
        current = current.next
    return head


def show(head):
    while head != None:
        print(head.val, end=' ')
        head = head.next
    print()
        
        
# vals = [1, 2, 3, 3, 4, 4, 5]
# vals = [1, 1, 3, 3, 4, 4, 5]
# vals = [1, 2, 3, 4, 4]
# vals = [1, 2, 3, 4, 5]
# vals = [1, 1]

# head = insert(vals)
head = None
show(head)
head = delete_duplication(head)
show(head)
