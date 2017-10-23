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
    【已知】
        For this problem, a height-balanced binary tree is defined as
        a binary tree in which the depth of the two subtrees of every
        node never differ by more than 1.
    【思路】
        1. 后续遍历
        2. 每次返回LR子树的Height
        3. 按题设比较其差值即可
        *3. 注意：空子树的Height算0
    """
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        is_balanced, height = self.recr(root)
        return is_balanced

    def recr(self, root):
        """
        :type root: TreeNode
        :rtype: (bool, int)
        """
        # termination situation
        if not root:
            return True, 0

        # interuption situation
        left_flag, left_height = self.recr(root.left)
        if True != left_flag:
            return False, None
        right_flag, right_height = self.recr(root.right)
        if True != right_flag:
            return False, None
        if abs(left_height - right_height) > 1:
            return False, None

        return True, 1 + max(left_height, right_height)

if "__main__" == __name__:
    s = Solution()
    root = TreeNode(1, None, None)
    print s.isBalanced(root)

    root = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3, TreeNode(6), TreeNode(7)))
    print s.isBalanced(root)

    root = TreeNode(1, TreeNode(2), None)
    print s.isBalanced(root)

    root = TreeNode(1, TreeNode(2, TreeNode(3)), None)
    print s.isBalanced(root)
