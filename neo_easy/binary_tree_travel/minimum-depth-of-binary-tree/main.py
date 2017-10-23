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
    1. 其实应该使用层级遍历。
    2. 判断这个节点是不是leaf，是，则程序interupt。
    """
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        q = [(root, 1)]
        while q:
            cur, height = q.pop()
            # termination situation
            if None == cur.left and None == cur.right:
                return height
            if cur.left:
                q.append((cur.left, height + 1))
            if cur.right:
                q.append((cur.right, height + 1))

if "__main__" == __name__:
    s = Solution()
    root = TreeNode(1, None, None)
    print s.minDepth(root)

    root = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3, TreeNode(6), TreeNode(7)))
    print s.minDepth(root)

    root = TreeNode(1, TreeNode(2), None)
    print s.minDepth(root)

    root = TreeNode(1, TreeNode(2, TreeNode(3)), None)
    print s.minDepth(root)

    root = TreeNode(1, None, TreeNode(2))
    print s.minDepth(root)
