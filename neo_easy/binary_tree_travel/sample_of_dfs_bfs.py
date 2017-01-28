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

    def dfs(self, root, drl=None, rdl=None, rld=None):
        """
        Depth-first-search
        深度优先
        :type root: TreeNode
        :rtype: rtype of "fo"
        """
        if None != drl:
            drl(root.val)
        if None != root.left:
            self.dfs(root.left, drl, rdl, rld)
        if None != rdl:
            rdl(root.val)
        if None != root.right:
            self.dfs(root.right, drl, rdl, rld)
        if None != rld:
            rld(root.val)

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

def printVal(val, count=[0]):
    count[0] += 1
    print "count:%s val:%s" % (count[0], val)

if "__main__" == __name__:
    s = Solution()
    root = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3, TreeNode(6), TreeNode(7)))
    #print s.drl.__doc__
    s.drl(root, None)
    print "============================"
    s.dfs(root, drl=printVal)
    print "============================"
    s.dfs(root, rdl=printVal)
    print "============================"
    s.dfs(root, rld=printVal)
