#!/usr/bin/python
#-*- coding:utf-8 -*-
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right

class Solution(object):
    def preOrder(self, root, res = []):
        """
        :type root: TreeNode
        :rtype: List[ * ]
        """
        if root:
            res.append(root.val)
            self.preOrder(root.left, res)
            self.preOrder(root.right, res)
        return res

    def inOrder(self, root, res = []):
        """
        :type root: TreeNode
        :rtype: List[ * ]
        """
        if root:
            self.preOrder(root.left, res)
            res.append(root.val)
            self.preOrder(root.right, res)
        return res

    def postOrder(self, root, res = []):
        """
        :type root: TreeNode
        :rtype: List[ * ]
        """
        if root:
            self.preOrder(root.left, res)
            self.preOrder(root.right, res)
            res.append(root.val)
        return res



if "__main__" == __name__:
    s = Solution()
    root = TreeNode(1, TreeNode(2, TreeNode(5), TreeNode(1)), TreeNode(3, None, TreeNode(9)))
    print s.preOrder(root)
    print s.inOrder(root)
    print s.postOrder(root)
