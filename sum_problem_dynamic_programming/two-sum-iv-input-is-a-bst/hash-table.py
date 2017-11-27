#!/usr/bin/python
# -*- coding: utf-8 -*-
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x, left = None, right = None):
        self.val = x
        self.left = left
        self.right = right


class Solution(object):
    """
    【思路】
    1. 这里我们使用hashtable，而python中的dict就是hashtable
    """
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        traveled = {}
        for n in self.yieldBreadthFirstSearch(root):
            if traveled.get(k-n):
                return True
            else:
                traveled[n] = True
        return False

    def yieldBreadthFirstSearch(self, root):
        que = [root]
        while que:
            cur = que.pop(0)
            if cur.left:
                que.append(cur.left)
            if cur.right:
                que.append(cur.right)
            yield cur.val

if "__main__" == __name__:
    s = Solution()
    print s.findTarget(TreeNode(2, None, TreeNode(7)), 9)
    print s.findTarget(TreeNode(7, TreeNode(2), TreeNode(2, TreeNode(7))), 9)

    print s.findTarget(TreeNode(5, TreeNode(3, TreeNode(2), TreeNode(4)), TreeNode(6, None, TreeNode(7))), 9)
    print s.findTarget(TreeNode(5, TreeNode(3, TreeNode(2), TreeNode(4)), TreeNode(6, None, TreeNode(7))), 13)
    print s.findTarget(TreeNode(5, TreeNode(3, TreeNode(2), TreeNode(4)), TreeNode(6, None, TreeNode(7))), 20)
