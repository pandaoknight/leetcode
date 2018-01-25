#-*- coding: utf-8 -*-

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        ret = []
        que = [(root, 0)]
        while que:
            cur, level = que.pop(0)
            if level >= len(ret):
                ret.append([])
            ret[level].append(cur.val)
            if cur.left:
                que.append((cur.left, level + 1))
            if cur.right:
                que.append((cur.right, level + 1))
        return ret

if "__main__" == __name__:
    s = Solution()
    print s.levelOrder(TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7))))