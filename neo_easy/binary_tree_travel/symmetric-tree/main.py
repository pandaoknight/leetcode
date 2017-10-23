#!/usr/bin/python
# -*- encoding: utf-8 -*-
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right

class Solution(object):
    """
    【思路】
    1. 这个直接对两侧进行对称深度遍历即可
    2. 这又是一个带中断的recursive算法
    3. 主要退出条件的优先级，先判断是否相等，再判断是否为Null。
    """
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        is_symmetric = self.recr(root.left, root.right)
        return is_symmetric

    def recr(self, left, right):
        """
        :type root: TreeNode
        :rtype: (val, longest_side)
        """
        ## recursive
        if not left and right:
            return False
        if left and not right:
            return False
        if not left and not right:
            return True
        if left.val != right.val:
            return False
        #

        # recursive-process
        outer = self.recr(left.left, right.right)
        if not outer:
            return False
        inner = self.recr(left.right, right.left)
        if not inner:
            return False
        return True


if "__main__" == __name__:
    s = Solution()
    root = TreeNode(1, None, None)
    print s.isSymmetric(root)

    root = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3, TreeNode(6), TreeNode(7)))
    print s.isSymmetric(root)

    root = TreeNode(1, None, None)
    print s.isSymmetric(root)

    root = TreeNode(1, TreeNode(4, TreeNode(4), TreeNode(1)), TreeNode(5, None, TreeNode(5)))
    print s.isSymmetric(root)

    root = TreeNode(4, TreeNode(4, TreeNode(4, TreeNode(4), None), TreeNode(4, TreeNode(4), TreeNode(4, None, TreeNode(4))) ), TreeNode(4, None, TreeNode(1)))
    print s.isSymmetric(root)

    root = TreeNode(1, TreeNode(5, TreeNode(5), TreeNode(1)), TreeNode(5, TreeNode(1), TreeNode(5)))
    print s.isSymmetric(root)

    root = TreeNode(1, TreeNode(5, TreeNode(5), None), TreeNode(5, None, TreeNode(5)))
    print s.isSymmetric(root)
