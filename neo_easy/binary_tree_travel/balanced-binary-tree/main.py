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

    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        # 后续遍历，因为这个节点的信息只能在我的LR子树都遍历后才能知晓
        
        return True

if "__main__" == __name__:
    s = Solution()
    root = TreeNode(1, None, None)
    print s.isBalanced(root)

    root = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3, TreeNode(6), TreeNode(7)))
    print s.isBalanced(root)

    root = TreeNode(1, None, None)
    print s.isBalanced(root)
