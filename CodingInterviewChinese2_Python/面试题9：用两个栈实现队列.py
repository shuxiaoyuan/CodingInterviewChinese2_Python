#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class QueueWithTwoStacks:
    def __init__(self):
        self.stack1 = []    # 入队栈
        self.stack2 = []    # 出队栈
    
    def append_tail(self, val):
        self.stack1.append(val)
    
    def delete_head(self):
        if len(self.stack2) == 0:
            while len(self.stack1) > 0:
                self.stack2.append(self.stack1.pop())
                
        if len(self.stack2) == 0:
            raise ValueError("队列为空！")
            
        self.stack2.pop()
        
    def show(self):
        print("队列内的元素有（从头到尾）：", end="")
        for i in reversed(self.stack2):
            print(i, end=" ")
        for i in self.stack1:
            print(i, end=" ")
        print()
            
            
'''
测试

'''

queue = QueueWithTwoStacks()

#queue.delete_head()

queue.append_tail(1)
queue.append_tail(2)
queue.append_tail(3)
queue.append_tail(5)
queue.append_tail(8)
queue.show()

queue.delete_head()
queue.show()


