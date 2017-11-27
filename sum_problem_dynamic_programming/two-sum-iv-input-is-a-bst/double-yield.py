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
    1. 我们现在知道了twoSum的解法有二，都是O(n)，第一个是我的"挤压法|夹逼定理（Squeeze Theorem）"
    2. 另一个就是使用Hash Table这个强大的数据结构。
    3. 因为，2Sum这个问题，就是需要Hash Table。不然二分查找多一个logn的倍数。
    4. 这里还是使用我的"输入集挤压法（Input Set Squeeze）"来做，那么，BST的InOrder遍历是具有顺序性的。
    5. 所以，我们使用两个yield，一个从左至右，一个从右至左来解这个问题。
    """
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        l = self.yieldInOrderLeft(root)
        left = l.next()
        r = self.yieldInOrderRight(root)
        right = r.next()
        print "================"
        while left != right:
            print left, right
            if left + right == k:
                return True
            if left + right > k:
                right = r.next()
            else:
                left = l.next()
        return False

    def yieldInOrderRight(self, root):
        if root.right:
            for x in self.yieldInOrderRight(root.right):
                yield x
        yield root.val
        if root.left:
            for x in self.yieldInOrderRight(root.left):
                yield x

    def yieldInOrderLeft(self, root):
        if root.left:
            for x in self.yieldInOrderLeft(root.left):
                yield x
        yield root.val
        if root.right:
            for x in self.yieldInOrderLeft(root.right):
                yield x

if "__main__" == __name__:
    s = Solution()
    print s.findTarget(TreeNode(2, None, TreeNode(7)), 9)
    print s.findTarget(TreeNode(7, TreeNode(2), TreeNode(2, TreeNode(7))), 9)

    print s.findTarget(TreeNode(5, TreeNode(3, TreeNode(2), TreeNode(4)), TreeNode(6, None, TreeNode(7))), 9)
    print s.findTarget(TreeNode(5, TreeNode(3, TreeNode(2), TreeNode(4)), TreeNode(6, None, TreeNode(7))), 13)
    print s.findTarget(TreeNode(5, TreeNode(3, TreeNode(2), TreeNode(4)), TreeNode(6, None, TreeNode(7))), 20)

    print s.findTarget(TreeNode(2, TreeNode(0, TreeNode(-4), TreeNode(1)), TreeNode(3)), -1)
