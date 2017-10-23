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
    1. 肯定是要用先序遍历的。
    2. 然后，例如我们得到了一个：1-4-4-5的序列，我们可能要用最长子序列来解这个问题。
    3. 但实际上不用。因为当我们要得到1-4-4-5这个过程中，我们必定已经得到过了1，1-4，1-4-4，1-4-4-5。所以每次都算一遍，写起来要简单一些。
    4. 但是！只在叶节点上做一次"最长子序列"的计算，是要比每次都算来得省。
    本次，用第3步的方法来做。
    *5. 如果随调用栈传递Path的时候，这里是可能减少重复计算的。其思想来自于LCS（最常子序列）

    A1. 传递Path的时候要用
    """
    def longestUnivaluePath(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        self.longest = 0
        self.recr(root)
        return self.longest

    def recr(self, root, path=[]):
        ## recursive
        if not root:
            return root
        #

        ## Way1:
        # path stack append
        path.append(root.val)

        # calc longtest
        s, longest = {}, 0
        for i in path[::-1]:
            if s.get(i, None):
                break
            longest += 1
            s[i] = 1
        self.longest = max(self.longest, longest)

        ## Way1:
        # recursive-process
        #self.recr(root.left, path)
        #self.recr(root.right, path)
        # path stack pop
        #path.pop()

        ## Way2:
        # recursive-process with deep-copy
        self.recr(root.left, copy.copy(path))
        self.recr(root.right, copy.copy(path))
        return root

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
