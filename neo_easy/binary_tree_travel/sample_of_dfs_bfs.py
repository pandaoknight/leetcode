#!/usr/bin/python
# -*- encoding: utf-8 -*-
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right

class Solution(object):
    stack = []

    def drl(self, root, fo):
        """
        Depth-first-search Preorder
        深度优先 先序遍历
        :type fo: Function Object
        :rtype: rtype of "fo"
        """
        leftResult = None
        #print root.val
        if None != root.left:
            leftResult = self.drl(root.left, fo)
        #print root.val
        if None != root.right:
            rightResult = self.drl(root.right, fo)
        print root.val
        return 1


if "__main__" == __name__:
    s = Solution()
    root = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3, TreeNode(6), TreeNode(7)))
    #print s.drl.__doc__
    s.drl(root, None)
