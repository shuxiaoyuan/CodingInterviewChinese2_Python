#!/usr/bin/env python3
# -*- coding: utf-8 -*-


'''
重建二叉树

'''

class BinaryTreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        
        
def construct(preorder, inorder):
    if not (isinstance(preorder, list) 
            and isinstance(inorder, list)
            and len(preorder) != len(inorder)):
        raise ValueError("输入的先序/中序遍历序列不正确！")
    
    return construct_core(preorder, 0, len(preorder)-1, 
        inorder, 0, len(inorder)-1)
    
    
def construct_core(preorder, start_preorder, end_preorder, 
        inorder, start_inorder, end_inorder):
    root_value = preorder[start_preorder]
    root = BinaryTreeNode(root_value)
    
    if start_preorder == end_preorder:
        if start_inorder == end_inorder:
            return root
        else:
            raise ValueError("输入的先序/中序遍历序列不正确！")
    
    # 在中序遍历序列中找到根结点的值
    root_inorder = start_inorder
    while root_inorder <= end_inorder and inorder[root_inorder] != root_value:
        root_inorder += 1
    # 感觉原书这里的判定有问题
    if root_inorder > end_inorder:
        raise ValueError("输入的先序/中序遍历序列不正确！")
    
    left_length = root_inorder - start_inorder
    left_preorder_end = start_preorder + left_length
    
    if left_length > 0:
        # 构建左子树
        root.left = construct_core(preorder, start_preorder+1, left_preorder_end,
            inorder, start_inorder, root_inorder-1)
    if left_length < end_preorder - start_preorder:
        # 构建右子树
        root.right = construct_core(preorder, left_preorder_end+1, end_preorder,
            inorder, root_inorder+1, end_inorder)
    
    return root
 
 
# 先序遍历    
def DLR(bt):
    if not isinstance(bt, BinaryTreeNode):
        return
    print(bt.val, end=" ")
    DLR(bt.left)
    DLR(bt.right)
    
    
def LDR(bt):
    if not isinstance(bt, BinaryTreeNode):
        return
    LDR(bt.left)
    print(bt.val, end=" ")
    LDR(bt.right)

    
'''
测试样例

'''
preorder = [1, 2, 4, 7, 3, 5, 6, 8]
inorder = [4, 7, 2, 1, 5, 3, 8, 6]
bt = construct(preorder, inorder)

print("先序遍历：", end="")
DLR(bt)
print("\n中序遍历：", end="")
LDR(bt)
print()

