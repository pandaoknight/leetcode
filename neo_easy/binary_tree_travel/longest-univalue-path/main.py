#!/usr/bin/python
# -*- encoding: utf-8 -*-
# Definition for a binary tree node.
import copy

class TreeNode(object):
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right

class Solution(object):
    """
    【思路】
    之前读题完全读错，很少犯这种低级错误，下次千万不要再犯了。
    1. 这个题得用后续遍历。
    2. 其实这个长度的计算很复杂。
    3. 当一个节点的左右各贡献了2个长度，它自己是5个长度。但是它只能给它的父贡献3个长度。
    """
    def longestUnivaluePath(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return 0
        self.longest = 1
        self.recr(root)
        return self.longest - 1 # Accroding to requirement

    def recr(self, root):
        """
        :type root: TreeNode
        :rtype: (val, longest_side)
        """
        ## recursive
        if not root:
            return (None, 0)
        #

        # recursive-process
        left_val, left_longest_side = self.recr(root.left)
        right_val, right_longest_side = self.recr(root.right)

        if left_val == root.val and right_val == root.val:
            self.longest = max(self.longest, left_longest_side + 1 + right_longest_side)
            return root.val, max(left_longest_side + 1, 1 + right_longest_side)
        if left_val == root.val:
            self.longest = max(self.longest, left_longest_side + 1)
            return root.val, left_longest_side + 1
        if right_val == root.val:
            self.longest = max(self.longest, right_longest_side + 1)
            return root.val, right_longest_side + 1
        return root.val, 1

if "__main__" == __name__:
    s = Solution()
    root = TreeNode(1, None, None)
    print s.longestUnivaluePath(root)

    root = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3, TreeNode(6), TreeNode(7)))
    print s.longestUnivaluePath(root)

    root = TreeNode(1, None, None)
    print s.longestUnivaluePath(root)

    root = TreeNode(1, TreeNode(4, TreeNode(4), TreeNode(1)), TreeNode(5, None, TreeNode(5)))
    print s.longestUnivaluePath(root)

    root = TreeNode(4, TreeNode(4, TreeNode(4, TreeNode(4), None), TreeNode(4, TreeNode(4), TreeNode(4, None, TreeNode(4))) ), TreeNode(4, None, TreeNode(1)))
    print s.longestUnivaluePath(root) # expect: 6
