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
    """
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.max_depth = 0
        self.recr(root, 0)
        return self.max_depth

    def recr(self, root, height):
        """
        :type root: TreeNode
        :type height: int
        :rtype: None
        """
        # termination situation
        if not root:
            return None

        height += 1
        self.max_depth = max(height, self.max_depth)
        self.recr(root.left, height)
        self.recr(root.right, height)

        return None

if "__main__" == __name__:
    s = Solution()
    root = TreeNode(1, None, None)
    print s.maxDepth(root)

    root = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3, TreeNode(6), TreeNode(7)))
    print s.maxDepth(root)

    root = TreeNode(1, TreeNode(2), None)
    print s.maxDepth(root)

    root = TreeNode(1, TreeNode(2, TreeNode(3)), None)
    print s.maxDepth(root)
