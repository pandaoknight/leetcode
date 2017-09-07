#!/usr/bin/python
#-*- coding:utf-8 -*-
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right

class Solution(object):
    res = []
    @classmethod
    def valCollector(cls, val):
        cls.res.append(val)
        return cls.res

    def __init__(self, funcitonObject = None):
        if None == funcitonObject:
            self.fo = Solution.valCollector
        else:
            self.fo = functionObject

    def setFunctionObject(self, funcitonObject):
        """
        :type funcitonObject: function
        :rtype: self # For Method Chaining.
        """
        return self

    def preOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[ * ]
        """
        res = None
        if root:
            res = self.fo(root.val)
            self.preOrder(root.left)
            self.preOrder(root.right)
        return res

    def inOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[ * ]
        """
        res = None
        if root:
            self.preOrder(root.left)
            res = self.fo(root.val)
            self.preOrder(root.right)
        return res

    def postOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[ * ]
        """
        res = None
        if root:
            self.preOrder(root.left)
            self.preOrder(root.right)
            res = self.fo(root.val)
        return res



if "__main__" == __name__:
    s = Solution()
    #print Solution.valCollector(1)
    #exit()

    root = TreeNode(1, TreeNode(2, TreeNode(5), TreeNode(1)), TreeNode(3, None, TreeNode(9)))
    print s.preOrder(root)
    print s.inOrder(root)
    print s.postOrder(root)
    #print s.setFunctionObject().preOrder(root)
    #print s.setFunctionObject().inOrder(root)
    #print s.setFunctionObject().postOrder(root)
