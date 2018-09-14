#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from collections import deque

class StackWithTwoQueues:
    def __init__(self):
        self.queue1 = deque()
        self.queue2 = deque()
    
    def push(self, val):
        if len(self.queue1) != 0:
            self.queue1.append(val)
        else:
            self.queue2.append(val)
            
    def pop(self):
        if len(self.queue1) != 0:
            while len(self.queue1) > 1:
                self.queue2.append(self.queue1.popleft())
            return self.queue1.pop()
        elif len(self.queue2) != 0:
            while len(self.queue2) > 1:
                self.queue1.append(self.queue2.popleft())
            return self.queue2.pop()
        else:
            return None
    
            
stack = StackWithTwoQueues()
stack.push(2)
stack.push(3)
stack.push(5)
stack.push(8)
print(stack.pop())
print(stack.pop())
print(stack.pop())
print(stack.pop())
print(stack.pop())
