#!/usr/bin/python
#-*- coding:utf-8 -*-
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right

class Solution(object):
    def largestValues(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        que = [(root, 1),]
        maxArr = []
        curLevel = 0
        while que:
            print maxArr
            cur = que.pop(0)
            level = cur[1]
            if curLevel < level:
                curLevel = level
                maxArr.append(cur[0].val)
            elif maxArr[-1] < cur[0].val:
                maxArr[-1] = cur[0].val
            print cur[0].val
            print level
            left = cur[0].left
            if left:
                que.append((left, level+1))
            right = cur[0].right
            if right:
                que.append((right, level+1))
        return maxArr



if "__main__" == __name__:
    print "中文"
    s = Solution()
    print s.largestValues(TreeNode(1, TreeNode(2, TreeNode(5), TreeNode(1)), TreeNode(3, None, TreeNode(9))))
