#!/usr/bin/env python3
# -*- coding: utf-8 -*-


'''
没有给测试样例，去 Java 版实现看吧

'''


# 二叉树节点类
class BinaryTreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
    
def get_next(node):
    if not isinstance(node, BinaryTreeNode):
        return None
    
    # 如果当前节点有右子树，则返回其右子树的最左节点
    if node.right != None:
        next = node.right
        while next.left != None:
            next = next.left
        return next
        
    # 当前节点有父结点
    if node.parent != None:
        next = node.parent
        
        # 当前节点为父亲结点的左子树
        if node == next.left:
            return next
            
        # 当前节点为父亲结点的右子树
        while next.parent != None and next == next.parent.right:
            next = next.parent
        
        # 包括 next 为 None 的情况（当 node 是中序遍历最后一个结点时）
        return next
    
    # node 是没有右子树的根结点
    return None