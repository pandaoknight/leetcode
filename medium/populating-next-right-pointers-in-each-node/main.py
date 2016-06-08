#!/usr/bin/python
#-*- coding: utf-8 -*-
# description: 合并两个排过序的链表，要求不能重新生成一个崭新的列表
# Definition for binary tree with next pointer.
class TreeLinkNode(object):
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right
        self.next = None

class Solution(object):
    def connect(self, root):
        """
        :type root: TreeLinkNode
        :rtype: nothing
        """

    def printTreeLinkNode(self, root):
        q = [root]
        while q:
            cur = q.pop(0)
            lv = None
            if cur.left:
                lv = cur.left.val
                q.append(cur.left)
            rv = None
            if cur.right:
                rv = cur.right.val
                q.append(cur.right)
            nv = None
            if cur.next:
                nv = cur.next.val
            print (cur.val, lv, rv, nv)

if "__main__" == __name__:
    s = Solution()
    root = TreeLinkNode(1, TreeLinkNode(2, TreeLinkNode(4), TreeLinkNode(5)), TreeLinkNode(3, TreeLinkNode(6), TreeLinkNode(7)))
    s.printTreeLinkNode(root)
